#!/usr/bin/env python3
"""Rebuild docs/interview/question-index.md from the 'Interview questions' section of every page.

  python3 tools/build-question-index.py

Pages are listed in the order of the nav in mkdocs.yml. Stubs are skipped. Standard library only.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = DOCS / "interview" / "question-index.md"
RE_NAV = re.compile(r"^\s*-\s+(?:\"((?:[^\"\\]|\\.)*)\":\s+)?([A-Za-z0-9_./-]+\.md)\s*$")
RE_Q = re.compile(r"^\*\*\d+\. (.+)\*\*\s*$")


def front(path):
    meta = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
            if m:
                meta[m.group(1)] = m.group(2).strip().strip('"')
    return meta, lines


def questions(lines):
    out, inside, fence = [], False, False
    for line in lines:
        if line.startswith("```"):
            fence = not fence
        if fence:
            continue
        if line.startswith("## "):
            inside = line[3:].strip() == "Interview questions"
            continue
        m = RE_Q.match(line) if inside else None
        if m:
            out.append(m.group(1))
    return out


def main():
    nav = []
    for line in (ROOT / "mkdocs.yml").read_text(encoding="utf-8").splitlines():
        m = RE_NAV.match(line)
        if m:
            nav.append(m.group(2))
    body, total, pages = [], 0, 0
    current = None
    for rel in nav:
        path = DOCS / rel
        if path.name == "README.md" or path == OUT or not path.is_file():
            continue
        meta, lines = front(path)
        if meta.get("status") == "stub":
            continue
        qs = questions(lines)
        if not qs:
            continue
        section = rel.split("/")[0]
        if section != current:
            current = section
            smeta, _ = front(DOCS / section / "README.md")
            body.append(f"\n## {smeta.get('title', section)}\n")
        body.append(f"\n**[{meta.get('title', rel)}](../{rel})**\n")
        body += [f"{i}. {q}" for i, q in enumerate(qs, 1)]
        total += len(qs)
        pages += 1
    head = [
        "---", 'title: "Question index"', "status: draft", "form: guide", "commands: none", "---", "",
        "# Question index", "",
        "> **Status: generated.** Built by `tools/build-question-index.py` from every page's interview questions. Do not edit by hand.",
        "", "## In one line", "",
        f"Every interview question in these notes, {total} of them across {pages} pages, grouped by section. "
        "Answer from memory, then open the page and compare with the hidden answer.", "",
        "## How to drill with this page", "",
        "1. Pick one section and set a timer.",
        "2. Answer each question aloud or on paper before opening anything.",
        "3. Open the page, expand the answer, and score yourself: 2 for every point, 1 for some, 0 for none or wrong.",
        "4. A section passes at 70%. Anything scored 0 goes on your list for the next loop.",
    ]
    OUT.write_text("\n".join(head + body) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {total} questions from {pages} pages")


if __name__ == "__main__":
    main()
