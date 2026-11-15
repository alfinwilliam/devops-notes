# DevOps Notes

General interview-prep notes for a DevOps engineer: Linux and networking first, then AWS, Kubernetes, delivery and operations. One concept per page, each with a diagram, a free hands-on exercise and hidden-answer questions.

**Read them here:** <https://alfinwilliam.github.io/devops-notes/>

The pages also read well on GitHub itself: start at [docs/README.md](docs/README.md).

## How far to trust them

These notes were drafted with an AI assistant. Every page says in its first line which state it is in:

| State | Meaning |
|---|---|
| Not written yet | A placeholder listing what the page will cover. |
| AI draft | Written by an AI. Nobody has checked it. |
| AI draft, fact-checked by a second AI pass | Each claim was compared with a source; the list is in [`review/`](review/). |
| Verified by me | I checked every claim against its source and did the exercise. |

Everything here is general knowledge with example values such as `10.0.0.0/16`, `123456789012` and `example.com`. Nothing describes a real system.

## Working on them

```bash
./preview.sh          # preview at http://localhost:8000/devops-notes/ (needs Docker)
./tools/check.sh      # every check, before pushing
```

- [RUNBOOK.md](RUNBOOK.md): how to edit, add, verify, check and publish pages.
- [STYLE.md](STYLE.md): how a page is written.
- [REVIEW.md](REVIEW.md): how a page is fact-checked.
