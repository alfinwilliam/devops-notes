# Runbook: maintaining these notes with no AI

Everything needed to preview, edit, check and publish the site by hand. If a step here turns out to be wrong, fix this file in the same commit as the fix.

- **Site:** `https://alfinwilliam.github.io/devops-notes/`
- **Repo on the laptop:** `~/Documents/Git/devops-notes`
- **Needs:** git, Docker, python3, and the GitHub CLI (`gh`) for the few commands that use it. Nothing else is installed.

## 1. What is where

| Path | What it is |
|---|---|
| `docs/<section>/<page>.md` | The pages. One concept each. |
| `docs/<section>/README.md` | The section's index page: a list of links. |
| `mkdocs.yml` | Site settings, and the `nav:` list at the bottom. A page only appears on the site if it is listed there. |
| `STYLE.md` | How a page is written. `templates/page.md` is the blank form. |
| `REVIEW.md` | How a page is fact-checked and verified. |
| `review/<section>/<page>.md` | The claims ledger for a page: your verification checklist. |
| `preview.sh` | Runs the site generator from a pinned Docker image. |
| `tools/check.sh` | Every local check in one command. |
| `.github/workflows/pages.yml` | Builds and publishes the site on every push to `main`. |

## 2. Preview on the laptop

```bash
cd ~/Documents/Git/devops-notes
./preview.sh
```

Open `http://localhost:8000/devops-notes/`. The page reloads when you save a file. Press Ctrl+C to stop.

- The first run downloads the generator image (about 300 MB).
- Diagrams are drawn by a script the page loads from the internet, so they need a connection even in the local preview.
- No Docker? You can still read every page on github.com, which renders the diagrams too.

## 3. Edit a page

1. Edit the `.md` file. Follow `STYLE.md`.
2. Check it: `python3 tools/check_page.py --mermaid docs/<section>/<page>.md`
3. Commit and push (section 7).

For a typo, the pencil icon at the top of every page on the site opens the file in GitHub's editor. Commit there and the site rebuilds itself.

## 4. Add a page

1. Copy the template: `cp templates/page.md docs/<section>/<new-page>.md`
2. Fill it in. Set `title`, `status`, `form` and `commands` at the top (the allowed values are in `STYLE.md`).
3. Register it in `mkdocs.yml`: find the section under `nav:`, copy a neighbouring line and change the title and path.

```yaml
          - "My new page": linux/my-new-page.md
```

4. Add the same link to the section's `docs/<section>/README.md`.
5. Run `./tools/check.sh`. A page that is missing from `nav:` fails the build with "not included in the nav".

To add a whole section, make the folder with a `README.md` in it and copy an existing section's block in `nav:`.

## 5. Verify a page

A page is `draft` or `reviewed` until you have checked it yourself. To make it `verified`:

1. Open its ledger, `review/<section>/<page>.md`. For each row, open the source and find the sentence that supports the claim. A page with no ledger yet has only been drafted: check each fact against the page's own Sources.
2. Do the page's "Try it". Answer its questions from memory.
3. Fix anything that is wrong.
4. In the page, set `status: verified` in the front matter and change the first sentence of the status line to `**Status: verified by me on YYYY-MM-DD.**`
5. Commit: `git commit -m "verify: <page>"`

How many pages are in each state:

```bash
grep -rh '^status:' docs --include='*.md' | sort | uniq -c
```

## 6. Run the checks

```bash
./tools/check.sh           # structure, Markdown lint, diagrams, strict build
./tools/check.sh --links   # the same, then every external link (slow, needs internet)
```

| Failure | What it means | Fix |
|---|---|---|
| `missing section '## ...'` | A required heading is absent or misspelled. | Use the exact heading from `STYLE.md`. |
| `each question needs one hidden answer` | A question lacks its `<details>` block, or the blank lines are missing. | Copy the question pattern from `templates/page.md`. |
| `a Mermaid diagram does not parse` | Diagram syntax error. | Section 8. |
| `diagram is ...px wide` | The diagram would be shrunk to fit the column, making its text too small. | Use `flowchart TD`, shorter labels, or `<br/>` to wrap a long label (STYLE.md, Diagrams). |
| `link target does not exist` | A relative link points at a file that is not there. | Fix the path. Links are relative to the page's own folder. |
| Lint: `MD031` or `MD032` | No blank line before or after a code fence or a list. | Add the blank line. |
| Lint: `MD007` | A nested list item is not indented by 4 spaces. | Indent it by 4. |
| Build: `not included in the "nav"` | The page is not registered. | Section 4, step 3. |
| Build: `contains a link ... not found` | A broken link between pages. | Fix the path. |
| Links: a 404 | The page moved. | Find its new address, or remove the link. |
| `AWS documentation links that silently redirect` lists a link | That AWS page does not exist; AWS redirects missing pages to the guide's index instead of showing a 404. | Search the AWS documentation for the page's new address. |

Only the strict build runs in GitHub Actions. The other checks are for you.

## 7. Publish

```bash
git add <files>
git commit -m "linux: fix the umask example"
git push
```

Two hooks run automatically (section 9). After the push, GitHub Actions builds the site and publishes it, usually within two minutes.

```bash
gh run list --limit 3      # the latest runs and whether they passed
gh run view --log-failed   # the log of the failed step
gh run rerun <run-id>      # run it again, for a failure that was not your change
```

The same information is in the repository's **Actions** tab on github.com.

- **Build step failed:** the strict build found a warning. Run `./preview.sh build` on the laptop, fix what it prints, push again.
- **Deploy step failed:** usually GitHub's side. Run it again.
- **A warning that an action version is deprecated:** open `.github/workflows/pages.yml` and raise the number after `@` to the version the warning names. Dependabot opens a pull request for this once a month; merging it is enough.

## 8. Diagrams

Diagrams are text, in a code fence marked `mermaid`. The rules in `STYLE.md` keep them working both on the site and on github.com:

- First line: `flowchart LR`, `flowchart TD` or `sequenceDiagram`.
- Every label in double quotes: `A["Recursive resolver"] -->|"asks"| B["Root server"]`
- No quotes, backticks, `#` or `;` inside a label.

To fix a broken one, paste it into `https://mermaid.live`, which shows the error as you type. Then run `python3 tools/check_page.py --mermaid <file>`.

On the site, every diagram can be clicked (or focused and opened with Enter) to view it full screen, with zoom and drag. That viewer is two small files, `docs/assets/javascripts/diagram-zoom.js` and `docs/assets/stylesheets/diagram-zoom.css`, registered under `extra_javascript` and `extra_css` in `mkdocs.yml`. It re-draws the diagram from its source text with the same Mermaid library the page already loads, so it needs no maintenance of its own. If a theme upgrade ever breaks it, remove those two lines from `mkdocs.yml`: the diagrams still show, just without the enlarge feature.

## 9. Confidentiality scan

This repo is public. Nothing in it may identify a former employer, its products, customers or people, and nothing may look like a real account id, address, hostname or secret. Write from general knowledge, with the example values in `STYLE.md`.

Two git hooks enforce this. Turn them on once per clone:

```bash
git config core.hooksPath tools/githooks
```

- **pre-commit** runs the identifier scanner from the prep KB (`~/Documents/prep-context/tools/sanitize.py`) over what you are committing.
- **pre-push** runs it over every tracked file, then runs gitleaks (through Docker) over the commits being pushed.

Both fail closed: if the scanner or Docker is missing, the commit or push is blocked.

| The scanner says | Do this |
|---|---|
| `ip-or-cidr`, `12-digit-number`, `aws-resource-id`, `uuid`, `long-id`, `email` | Replace the value with an example value from `STYLE.md`. |
| `secret-assignment`, `high-entropy`, `jwt`, `token` | Replace it with `changeme` or a placeholder such as `<your-token>`. |
| `high-entropy` on a documentation link (for example an S3 user guide page whose name is one long CamelCase word) | A false positive: the path mixes upper case, lower case and a digit (the `AmazonS3` part) with one segment longer than 14 characters. Link an equivalent page whose last segment is short or hyphenated (`notification-how-to-event-types-and-destinations.html`), or the product page. |
| `domain`, for a public documentation site | Add the exact hostname as a new line in `~/Documents/Prep/denylist/allow.txt`. |
| `deny:...` | The line contains a term that must not be published. Reword it in general terms. Never add it to `allow.txt`. |

To scan by hand:

```bash
python3 ~/Documents/prep-context/tools/sanitize.py scan docs review *.md mkdocs.yml tools
```

Do not use `git push --no-verify` on this repo while it is public.

## 10. Rebuild the question index

`docs/interview/question-index.md` is generated from every page's interview questions. After adding or changing questions:

```bash
python3 tools/build-question-index.py
```

## 11. Make the repo private, and public again

On a free GitHub account, Pages only works for public repositories. **Switching this repo to private takes the site offline automatically.** The notes stay readable through `./preview.sh` and in the file view on github.com.

```bash
gh repo edit alfinwilliam/devops-notes --visibility private --accept-visibility-change-consequences
```

Or on github.com: Settings, General, Danger Zone, Change visibility.

To go public again, change the visibility back, then check Settings, Pages. If "Source" is not "GitHub Actions", select it. Then publish:

```bash
gh workflow run "Publish site"
```

GitHub's documentation does not say whether Pages comes back by itself, so check that page.

## 12. A new machine

1. Install git, Docker, python3 and `gh`. Run `gh auth login`.
2. Clone into the usual place and turn the hooks on:

```bash
git clone https://github.com/alfinwilliam/devops-notes.git ~/Documents/Git/devops-notes
cd ~/Documents/Git/devops-notes
git config core.hooksPath tools/githooks
```

3. Set the commit identity for this repo, with your GitHub no-reply address, so your personal email stays out of a public history:

```bash
git config user.name "Your Name"
git config user.email "<id>+<username>@users.noreply.github.com"
```

4. The hooks need the prep KB's scanner and its local lists (`~/Documents/prep-context/tools/sanitize.py` and `~/Documents/Prep/denylist/`). Restore those first. If the scanner lives somewhere else, set `NOTES_SANITIZER=/path/to/sanitize.py`.
5. Run `./preview.sh build` to confirm everything works.

## 13. The toolchain

Every tool runs from a Docker image pinned by digest, so nothing changes until you change it.

| Tool | Pinned in |
|---|---|
| Site generator: Material for MkDocs 9.8.1 | `preview.sh` |
| Mermaid checker | `tools/check_page.py` |
| Markdown linter, link checker | `tools/check.sh` |
| gitleaks | `tools/githooks/pre-push` |

**You do not need to upgrade.** A pinned image keeps building the same site. Material for MkDocs reaches end of life on 2027-05-05; after that it gets no fixes, and this site still builds.

To move to another version, change the `IMAGE=` line in `preview.sh` to the new tag, run `./preview.sh build`, and look at the site before pushing.

**If the generator ever has to be replaced:** its successor, Zensical, reads the same `mkdocs.yml`. The pages are plain Markdown with Mermaid fences and `<details>` blocks, and use no generator-specific syntax, so they will move to any tool. Try it without changing anything else:

```bash
docker run --rm -v "$PWD:/docs" zensical/zensical build
```

That command was not tested when this runbook was written. Read Zensical's own documentation at `https://zensical.org` first.
