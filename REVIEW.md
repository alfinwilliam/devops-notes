# How pages are fact-checked

A page moves from `draft` to `reviewed` when a second reader has tried to prove it wrong, and to `verified` when the site owner has done the same. This file is the procedure for both.

The job is to find errors, not to confirm the page. Assume it contains at least three.

## Procedure

1. Read `STYLE.md`, then the page.
2. **List every checkable claim**: numbers, defaults, limits, port numbers, what a flag does, the order of steps in a sequence, "X does Y" statements about a mechanism, statements about versions, and every point in the hidden answers. A full page has at least 12.
3. **Check each claim against a primary source you open now**: the official documentation, a man page, an RFC, or by running the command in a throwaway container. Memory does not count as a source.
4. Give each claim a verdict:
    - `confirmed`: the source says the same.
    - `corrected`: the page was wrong; fix the page and note what changed.
    - `unverified`: no primary source found in reasonable time. Tag the sentence `(unverified)` on the page, or remove it if it is not needed.
5. **Check the diagram** against the text and the source: same names, same order, arrows in the right direction.
6. **Check the commands**: every flag exists and does what the page says. On pages whose `commands` value is `container`, `kind` or `cli`, run anything that looks wrong.
7. **Check the recent-changes list below** for anything the page touches.
8. Write the claims ledger (format below).
9. Change facts only. Do not restyle or rewrite sentences that are correct.
10. Set `status: reviewed` in the front matter and change the status line as `STYLE.md` describes (or `verified`, if you are the owner).
11. Run `python3 tools/check_page.py --mermaid <page>` and the identifier scan on the page and its ledger.

## Claims ledger

One file per page at `review/<section>/<page>.md`:

```markdown
# Claims ledger: DNS

Page: `docs/networking/dns.md` · Checked 2026-11-15 by a second AI pass · 14 claims: 12 confirmed, 1 corrected, 1 unverified

| # | Claim | Source | Verdict | Note |
|---|---|---|---|---|
| 1 | DNS queries use UDP port 53 and fall back to TCP | [RFC 7766](https://www.rfc-editor.org/rfc/rfc7766) | confirmed | |
| 2 | ... | `man 5 resolv.conf` | corrected | Page said the default for ndots is 5; it is 1. |
```

- The claim is written as the page states it, in a few words.
- The source is a link, a man page reference, or `ran in ubuntu:24.04`.
- Quote nothing longer than a short phrase from a source.

## Verifying a page yourself

The ledger is your checklist. For each row, open the source and find the sentence that supports the claim. Do the page's "Try it". Answer its questions from memory. When every row holds, change the status as in step 10 and commit.

## Things that changed recently

An AI's memory is most often wrong about these. Open the current documentation before accepting any statement about them.

| Area | What to check |
|---|---|
| Kubernetes ingress | The community ingress-nginx controller was retired. Check the Kubernetes site for its current status and for what replaces it (Gateway API). |
| Terraform S3 backend | State locking with `use_lockfile`; DynamoDB-based locking is deprecated. |
| EKS access | Access entries and access policies vs the `aws-auth` ConfigMap. |
| EKS pod permissions | EKS Pod Identity next to IRSA. |
| Karpenter | Current API version and kinds: NodePool, EC2NodeClass, NodeClaim; disruption settings. |
| Amazon Linux | Amazon Linux 2 end of life; current EKS node images. |
| Kubernetes sidecars | Native sidecar containers (init containers with `restartPolicy: Always`). |
| Docker Compose | `docker compose` (v2) vs the old `docker-compose` binary. |
| Helm | Helm 4 flag and behaviour changes. |
| Istio | Ambient mode status; Gateway API support. |
| Terragrunt | CLI command renames (`run --all`), root configuration file name. |
| GitHub Actions | Current major versions of actions; `pull_request_target` behaviour. |
| MkDocs | Material for MkDocs is in maintenance mode; Zensical is its successor. |
| AWS | Any quota, price or per-instance limit: link to the page instead of quoting a number. |
