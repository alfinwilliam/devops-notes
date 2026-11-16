#!/usr/bin/env python3
"""Check that pages follow STYLE.md.

  python3 tools/check_page.py docs                      every page (a stub only gets its front matter checked)
  python3 tools/check_page.py docs/networking/dns.md    one page
  python3 tools/check_page.py --mermaid FILE...         also parse every Mermaid diagram (needs Docker)
  python3 tools/check_page.py --mermaid-only docs       only the diagram check

Prints one line per problem as file:line: message. Exit code 1 if any page has an error.
Standard library only, so it runs on any machine with python3.
"""
import fcntl
import re
import subprocess
import sys
import tempfile
from pathlib import Path

MERMAID_IMAGE = "minlag/mermaid-cli@sha256:18938e53497376d524e04b1fc0bf7b6d61a491ce9ff7032bb2855d57155acb10"
LOCK_FILE = Path(tempfile.gettempdir()) / "devops-notes-mermaid.lock"
MAX_DIAGRAM_WIDTH = 800   # px. The content column is about 760px on a desktop screen; up to 800 keeps text at 95% or more.

STATUSES = {"stub", "draft", "reviewed", "verified"}
FORMS = {"full", "short", "guide"}
COMMANDS = {"container", "kind", "cli", "docs", "none"}

SECTIONS = {
    "full": ["In one line", "The plain idea", "How it works", "A concrete example", "Why not just...?",
             "Commands to know", "How it breaks", "Interview questions", "Try it", "Zoom out", "Sources"],
    "short": ["In one line", "How it works", "Interview questions", "Sources"],
    "guide": ["In one line"],
}
OPTIONAL_WITHOUT_COMMANDS = {"Commands to know", "Try it"}   # may be left out when commands: none
MIN_WORDS = {"full": 900, "short": 350, "guide": 300}
QUESTIONS = {"full": (6, 8), "short": (4, 6)}
MIN_SOURCES = {"full": 2, "short": 1, "guide": 0}

RE_FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([A-Za-z0-9_+-]*)")
RE_QUESTION = re.compile(r"^\*\*(\d+)\. .+\*\*\s*$")
RE_LINK = re.compile(r"(!?)\[[^\]\n]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
RE_BANNED = [
    (re.compile(r"^\s*(!!!|\?\?\?\+?)\s"), "admonition syntax (!!! or ???) is not portable; use a blockquote"),
    (re.compile(r"^===\s+\""), "content tabs (===) are not portable"),
    (re.compile(r"\[\^[^\]]+\]"), "footnotes are not portable"),
    (re.compile(r"^\[TOC\]\s*$"), "[TOC] is not portable"),
    (re.compile(r"\{:\s|\{\s*[.#][A-Za-z]"), "attribute lists ({: } or { .class }) are not portable"),
    (re.compile(r"\b(TODO|TBD|FIXME)\b"), "unfinished marker (TODO/TBD/FIXME)"),
]


class Page:
    def __init__(self, path: Path):
        self.path = path
        self.errors = []
        self.meta = {}
        self.lines = path.read_text(encoding="utf-8").splitlines()
        self.body_start = 0
        self.mermaid = []        # (line number, text)

    def err(self, line, msg):
        self.errors.append((line, msg))

    def parse_front_matter(self):
        if not self.lines or self.lines[0].strip() != "---":
            self.err(1, "missing front matter (the file must start with ---)")
            return
        for i in range(1, len(self.lines)):
            if self.lines[i].strip() == "---":
                self.body_start = i + 1
                break
            m = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*(#.*)?$", self.lines[i])
            if m:
                self.meta[m.group(1)] = m.group(2).strip().strip('"').strip("'")
        else:
            self.err(1, "front matter is not closed with ---")
            return
        for key, allowed in (("status", STATUSES), ("form", FORMS), ("commands", COMMANDS)):
            v = self.meta.get(key)
            if v is None:
                self.err(1, f"front matter is missing '{key}'")
            elif v not in allowed:
                self.err(1, f"front matter {key}: '{v}' is not one of {sorted(allowed)}")
        if not self.meta.get("title"):
            self.err(1, "front matter is missing 'title'")

    def check_body(self):
        form, commands = self.meta.get("form"), self.meta.get("commands")
        if form not in FORMS:
            return
        in_fence, fence_mark, fence_lang, fence_line, block = False, "", "", 0, []
        h1 = []
        h2 = []                  # (line number, title)
        prose = []               # (line number, text) outside fences
        for n, raw in enumerate(self.lines[self.body_start:], start=self.body_start + 1):
            m = RE_FENCE.match(raw)
            if m and not in_fence:
                if m.group(1):
                    self.err(n, "code fence is indented; fences start at the left margin (not inside a list)")
                in_fence, fence_mark, fence_lang, fence_line, block = True, m.group(2)[0] * 3, m.group(3), n, []
                continue
            if in_fence:
                if raw.strip().startswith(fence_mark) and raw.strip().strip(fence_mark[0]) == "":
                    if fence_lang == "mermaid":
                        self.mermaid.append((fence_line, "\n".join(block)))
                    in_fence = False
                else:
                    block.append(raw)
                continue
            prose.append((n, raw))
            if raw.startswith("# "):
                h1.append(n)
            elif raw.startswith("## "):
                h2.append((n, raw[3:].strip()))
        if in_fence:
            self.err(fence_line, "code fence is never closed")

        # one H1, then the status line
        if len(h1) != 1:
            self.err(h1[1] if len(h1) > 1 else self.body_start + 1, f"expected exactly one '# ' title, found {len(h1)}")
        else:
            after = [(n, t) for n, t in prose if n > h1[0] and t.strip()]
            if not after or not after[0][1].startswith("> **Status:"):
                self.err(h1[0] + 1, "the first line after the title must be the status line: > **Status: ...**")

        # required sections, in order
        want = [s for s in SECTIONS[form] if not (commands == "none" and s in OPTIONAL_WITHOUT_COMMANDS)]
        titles = [t for _, t in h2]
        pos = -1
        for s in SECTIONS[form]:
            if s in titles:
                i = titles.index(s)
                if i < pos:
                    self.err(h2[i][0], f"section '## {s}' is out of order")
                pos = max(pos, i)
            elif s in want:
                self.err(self.body_start + 1, f"missing section '## {s}'")
        if form in ("full", "short"):
            for n, t in h2:
                if t not in SECTIONS[form]:
                    self.err(n, f"unexpected section '## {t}' (use ### inside a standard section)")

        def section(name):
            idx = [i for i, (_, t) in enumerate(h2) if t == name]
            if not idx:
                return []
            start = h2[idx[0]][0]
            end = h2[idx[0] + 1][0] if idx[0] + 1 < len(h2) else 10 ** 9
            return [(n, t) for n, t in prose if start < n < end]

        def words(rows):
            text = " ".join(re.sub(r"<[^>]+>", " ", t) for _, t in rows)
            return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'/.-]*", text))

        total = words(prose)
        if total < MIN_WORDS[form]:
            self.err(self.body_start + 1, f"page is too thin: {total} words outside code blocks (minimum {MIN_WORDS[form]} for form '{form}')")
        one = section("In one line")
        if one and words(one) > 60:
            self.err(one[0][0], f"'In one line' is {words(one)} words; keep it to about 40")

        # diagrams
        if form in ("full", "short") and not self.mermaid:
            self.err(self.body_start + 1, "no Mermaid diagram (at least one is required)")
        for n, text in self.mermaid:
            first = next((l.strip() for l in text.splitlines() if l.strip()), "")
            if not (first.startswith("flowchart ") or first == "sequenceDiagram"):
                self.err(n, "diagram must start with 'flowchart LR', 'flowchart TD' or 'sequenceDiagram'")
            if "{{" in text or "}}" in text:
                self.err(n, "diagram contains {{ or }}, which Mermaid reads as a shape")
            if re.search(r"^\s*(classDef|style|linkStyle|click)\b", text, re.M):
                self.err(n, "diagram uses styling or click directives; keep diagrams plain")

        # interview questions
        qs = section("Interview questions")
        if form in QUESTIONS:
            self.check_questions(qs, *QUESTIONS[form])
        elif qs:
            self.check_questions(qs, 1, 99)
        for n, t in prose:
            if "<details" in t and t.strip() != '<details markdown="1">':
                self.err(n, 'write the opening tag exactly as <details markdown="1"> on its own line')

        # banned syntax, links
        external_in_sources = 0
        src_lines = {n for n, _ in section("Sources")}
        for n, t in prose:
            if t.lstrip().startswith("|") and ("\\|" in t or any("|" in s for s in re.findall(r"`[^`]*`", t))):
                self.err(n, "a pipe character inside a table cell (even in code) breaks the table; reword the cell")
            bare = re.sub(r"`[^`]*`", "", t)
            for rx, msg in RE_BANNED:
                if rx.search(bare):
                    self.err(n, msg)
            for m in RE_LINK.finditer(bare):
                target = m.group(2)
                if target.startswith("https://"):
                    if n in src_lines:
                        external_in_sources += 1
                elif target.startswith("http://"):
                    self.err(n, f"link uses http://, use https:// ({target})")
                elif target.startswith("mailto:"):
                    self.err(n, "no mailto links")
                elif target.startswith("#"):
                    self.err(n, "link to a page, not to a heading (heading anchors differ between the site and github.com)")
                else:
                    path, _, anchor = target.partition("#")
                    if anchor:
                        self.err(n, f"link to the page, not to a heading: drop '#{anchor}'")
                    dest = (self.path.parent / path).resolve()
                    if not path.endswith(".md"):
                        self.err(n, f"relative link must point at a .md file: {target}")
                    elif not dest.is_file():
                        self.err(n, f"link target does not exist: {target}")
            stripped = RE_LINK.sub("", bare)
            stripped = re.sub(r"<https://[^>\s]+>", "", stripped)
            if re.search(r"https?://", stripped):
                self.err(n, "bare URL; write it as [text](https://...)")
        if external_in_sources < MIN_SOURCES[form]:
            self.err(self.body_start + 1, f"'Sources' has {external_in_sources} https link(s); at least {MIN_SOURCES[form]} needed")

    def check_questions(self, rows, lo, hi):
        qlines = [n for n, t in rows if RE_QUESTION.match(t)]
        if not lo <= len(qlines) <= hi:
            where = rows[0][0] if rows else self.body_start + 1
            self.err(where, f"found {len(qlines)} interview questions; expected {lo} to {hi}, each written as **1. Question?**")
        opens = sum(1 for _, t in rows if t.strip() == '<details markdown="1">')
        closes = sum(1 for _, t in rows if t.strip() == "</details>")
        summaries = sum(1 for _, t in rows if t.strip() == "<summary>Answer</summary>")
        if not (opens == closes == summaries == len(qlines)):
            where = rows[0][0] if rows else self.body_start + 1
            self.err(where, f"each question needs one hidden answer: {len(qlines)} questions, {opens} <details markdown=\"1\">, "
                            f"{summaries} <summary>Answer</summary>, {closes} </details>")
        nonblank = [(n, t.strip()) for n, t in rows if t.strip()]
        for i, (n, t) in enumerate(nonblank):
            if RE_QUESTION.match(t):
                nxt = [x[1] for x in nonblank[i + 1:i + 3]]
                if nxt[:2] != ['<details markdown="1">', "<summary>Answer</summary>"]:
                    self.err(n, "a question must be followed by <details markdown=\"1\"> and then <summary>Answer</summary>")

    def check_mermaid(self):
        """Parse every diagram with mermaid-cli in Docker. One run at a time across all callers."""
        if not self.mermaid:
            return
        with tempfile.TemporaryDirectory(prefix="notes-mmd-") as td:
            Path(td).chmod(0o777)
            src = Path(td) / "page.md"
            src.write_text("\n\n".join(f"```mermaid\n{t}\n```" for _, t in self.mermaid) + "\n", encoding="utf-8")
            src.chmod(0o666)
            with open(LOCK_FILE, "w") as lock:
                fcntl.flock(lock, fcntl.LOCK_EX)
                try:
                    r = subprocess.run(["docker", "run", "--rm", "--network", "none", "-v", f"{td}:/data", MERMAID_IMAGE,
                                        "-i", "/data/page.md", "-o", "/data/out.md", "-q"],
                                       capture_output=True, text=True, timeout=300)
                except (subprocess.TimeoutExpired, FileNotFoundError) as e:
                    self.err(self.mermaid[0][0], f"could not run the Mermaid check: {e}")
                    return
            if r.returncode != 0:
                detail = next((l.strip() for l in (r.stderr + r.stdout).splitlines()
                               if "error" in l.lower() or "Expecting" in l), "syntax error")
                lines = ", ".join(str(n) for n, _ in self.mermaid)
                self.err(self.mermaid[0][0], f"a Mermaid diagram does not parse (diagrams start at lines {lines}): {detail[:200]}")
                return
            # Width check: a diagram wider than the content column is shrunk until its text is hard to read.
            for i, (n, _) in enumerate(self.mermaid, start=1):
                svg = Path(td) / f"out-{i}.svg"
                if not svg.is_file():
                    continue
                m = re.search(r'viewBox="[-\d.]+ [-\d.]+ ([\d.]+) ([\d.]+)"', svg.read_text(encoding="utf-8", errors="ignore"))
                if m and float(m.group(1)) > MAX_DIAGRAM_WIDTH:
                    self.err(n, f"diagram is {float(m.group(1)):.0f}px wide; the limit is {MAX_DIAGRAM_WIDTH}px (the page column is about 760px), so its text "
                                f"would shrink to {100 * 760 / float(m.group(1)):.0f}%. Use flowchart TD, fewer or shorter "
                                f"labels, or <br/> to wrap long sequence messages")


def collect(args):
    files = []
    for a in args:
        p = Path(a)
        if p.is_dir():
            files += sorted(f for f in p.rglob("*.md") if f.name != "README.md")
        elif p.name != "README.md":
            files.append(p)
    return files


def main():
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not paths or flags - {"--mermaid", "--mermaid-only"}:
        print(__doc__)
        return 2
    bad = stubs = 0
    files = collect(paths)
    for f in files:
        if not f.is_file():
            print(f"{f}:1: file not found")
            bad += 1
            continue
        page = Page(f)
        page.parse_front_matter()
        if page.meta.get("status") == "stub":
            stubs += 1
        else:
            if not page.errors:
                page.check_body()
            if flags and not [e for e in page.errors if "fence" in e[1]]:
                if "--mermaid-only" in flags:
                    page.errors = []
                page.check_mermaid()
        for line, msg in sorted(page.errors):
            print(f"{f}:{line}: {msg}")
        bad += bool(page.errors)
    print(f"checked {len(files)} page(s): {len(files) - bad - stubs} ok, {bad} with problems, {stubs} still stubs")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
