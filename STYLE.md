# How pages are written

Every page under `docs/` follows this file, whoever writes it: you, or an AI you hand it to.

- The blank form is `templates/page.md`.
- The model page is `docs/networking/dns.md`. Match its depth and tone.
- `python3 tools/check_page.py --mermaid <file>` checks most of the rules below.

## The reader

A DevOps engineer with about six years in IT who is preparing for interviews. They have used most of these tools in production and are rebuilding the fundamentals underneath, so a term is not understood merely because the tool is familiar. They read one page in about 25 minutes, do its "Try it", then answer its questions from memory.

## Voice

1. **Plain idea first, then the name.** Describe what happens in everyday words, then attach the term in bold. Not "it uses a readiness probe", but "Kubernetes keeps asking the container 'ready for traffic yet?'; that check is a **readiness probe**."
2. **Build from primitives.** The first time a page leans on a term, define it in one line or link to the page that owns it.
3. **Show the chain.** For a sequence or a decision, say why each step follows from the one before.
4. **Real names and mechanics.** Name the actual component, file, field or flag. Never "the system handles it".
5. **Short sentences, no filler.** No "simply", "just", "basically", "it is important to note". No hype, no emojis. British spelling.
6. **Say "you".** No first-person experience claims such as "in my project" or "we used".
7. **General knowledge only.** Never name an employer, an internal product, a customer or a person.
8. **Depth beats brevity in the explanation.** A page that is correct but too thin to learn from has failed.

## Front matter

```yaml
---
title: "DNS"
status: draft        # stub | draft | reviewed | verified
form: full           # full | short | guide
commands: container  # container | kind | cli | docs | none
---
```

| `status` | Meaning |
|---|---|
| `stub` | Not written yet. Lists what the page will cover. |
| `draft` | Written by an AI. Nobody has checked it. |
| `reviewed` | Fact-checked by a second AI pass. The claims are listed in `review/`. |
| `verified` | Checked by the site owner against the sources. |

| `commands` | How the commands on the page were checked |
|---|---|
| `container` | Run in a throwaway container. The output shown is real. |
| `kind` | Run on a local `kind` cluster. The output shown is real. |
| `cli` | Run with the tool's own CLI in an empty temporary directory. |
| `docs` | Taken from official documentation and not run. Output is illustrative. |
| `none` | The page has no commands. |

## The first two lines of every page

The title, then the status line. Use these exact wordings and fill in the date.

```markdown
# DNS

> **Status: AI draft, 2026-11-15.** Not yet verified by me. Commands and output were run in a throwaway container; addresses are rewritten to example ranges.
```

- After review, the first sentence becomes `**Status: AI draft, fact-checked by a second AI pass on 2026-11-15.**`
- After the owner verifies it: `**Status: verified by me on YYYY-MM-DD.**`
- Second sentence by `commands` value:
    - `container`: Commands and output were run in a throwaway container; addresses are rewritten to example ranges.
    - `kind`: Commands and output were run on a local kind cluster; addresses are rewritten to example ranges.
    - `cli`: Commands and output were run locally with the tool's own CLI.
    - `docs`: Commands are from the official documentation and were not run; output is illustrative.
    - `none`: leave the sentence out.

## Sections

### Form `full` (1,200 to 2,200 words outside code blocks)

Use these `##` headings, in this order, spelled exactly. Use `###` for anything inside them.

| Heading | What goes in it |
|---|---|
| `## In one line` | The answer you would say aloud in 20 seconds. 40 words at most. |
| `## The plain idea` | One to three short paragraphs in everyday words. An analogy is fine if it is accurate; say where it stops being true. |
| `## How it works` | The core of the page. Build the mechanism from primitives, step by step. At least one diagram. Tables for comparisons. |
| `## A concrete example` | One worked scenario from start to finish, with example values. |
| `## Why not just...?` | Two or three tempting simpler alternatives, and why each one fails. |
| `## Commands to know` | Each command, what it shows, and every flag used explained. Real output where the page's `commands` value allows. |
| `## How it breaks` | A table with the columns `Symptom`, `Layer`, `Check`, `Likely cause`. Four to seven rows. |
| `## Interview questions` | Six to eight questions with hidden answers. See below. |
| `## Try it` | A hands-on exercise of at most 10 minutes that costs nothing. See below. |
| `## Zoom out` | Two to four sentences: where this sits in the bigger path, what breaks without it, the principle to carry to the next problem. |
| `## Sources` | A bullet list of links. See "Links and sources". |

When `commands` is `none`, `## Commands to know` may be left out, and `## Try it` may be a paper exercise or left out.

### Form `short` (500 to 900 words)

`## In one line`, `## How it works` (with a diagram), `## Interview questions` (four to six), `## Sources`.

### Form `guide`

For pages that are not about one concept (playbooks, comparison tables, interview technique). `## In one line` first, then whatever headings serve the reader. If it has an `## Interview questions` section, that section follows the format below.

### Interview questions

Order them from recall to diagnosis: two that ask "what is", two that ask "how" or "why", at least two scenarios ("users report X; what do you check?"), and optionally one trade-off or design question. Write the questions an interviewer for an AWS and Kubernetes DevOps role would ask.

Each answer is a rubric: three to six bullets naming what a strong answer contains. The reader scores 2 for every point, 1 for some, 0 for none.

Write each one exactly like this, including the blank lines:

```markdown
**1. What does a 404 tell you that a connection timeout does not?**

<details markdown="1">
<summary>Answer</summary>

- The request reached a server: DNS, routing, the TCP connection and TLS all worked.
- The server understood the request and says the path does not exist.
- A timeout proves none of that: the packet may never have arrived.

</details>
```

### Try it

- Local and free: Docker, `kind`, network namespaces. For AWS pages, only read-only calls (`describe`, `list`, `get`) or free resources with their teardown commands. Nothing that bills.
- Steps that take at most 10 minutes in total. Write each one as a paragraph that starts `**Step 1.**`, with its code fence below it. Do not use a numbered list here: a fence at the left margin ends the list, and the numbering restarts on the site.
- Start from a clean, public starting point such as `docker run --rm -it ubuntu:24.04 bash`, and include the install line for any tool the image lacks.
- Ask the reader to predict the result before the step that matters, then show the expected output.
- End with cleanup.
- If you did not run it yourself, make the first line `*Untested: written from documentation.*`

## Markdown dialect

The same file must render on the site and on github.com.

- A blank line before and after every list, table, code fence and `<details>` block.
- Nested list items are indented by 4 spaces.
- Code fences start at the left margin, never inside a list. Give every fence a language: `bash`, `console`, `yaml`, `json`, `hcl`, `text`, `ini`, `dockerfile`, `groovy`, `python`, `sql`.
- In `console` blocks, show a command with a `$` prompt (or `#` for root) and its output below it. Use `bash` blocks for commands meant to be copied.
- Not allowed: admonitions (`!!!`, `???`), content tabs (`===`), footnotes, attribute lists, raw HTML other than `<details>`, `<summary>` and `<br/>`, emojis, bare URLs, a pipe character inside a table cell.
- For a note or warning, use a blockquote with a bold lead-in: `> **Gotcha:** ...`

## Diagrams

- Full and short pages have at least one diagram. Use one where there is a flow, a sequence or a structure to see; three at most.
- Mermaid only, in a fence with the language `mermaid`. The first line is `flowchart LR`, `flowchart TD` or `sequenceDiagram`.
- Node ids are plain letters and digits. Every node label is in double quotes: `A["Recursive resolver"]`. Edge labels too: `A -->|"asks"| B`.
- Inside a label: no double quotes, no backticks, no `{{` or `}}`, no `#`, no `;`.
- At most 12 nodes, or 6 participants. No styling (`classDef`, `style`, `linkStyle`), no `click`, at most one level of `subgraph`.
- The diagram must agree with the text: same names, same order.

## Links and sources

- Link to other pages with a relative path to the `.md` file: `[TLS](tls.md)`, `[VPC basics](../aws-core/vpc-basics.md)`. Every page that exists is listed in `mkdocs.yml`.
- Link to the page, never to a heading inside it.
- **One home per concept.** If another page owns a concept, give one sentence and a link. Do not explain it again. The owners:

| Concept | Home |
|---|---|
| DNS, TCP, TLS, HTTP status codes, L4 vs L7 | `networking/` |
| Permissions, processes and signals, memory and cgroups | `linux/` |
| Namespaces and cgroups as the basis of containers | `containers/what-is-a-container.md` |
| OAuth 2.0, OIDC, JWTs | `security/oauth-oidc-jwt.md` |
| IAM policy evaluation | `aws-core/iam-policies.md` |
| Roles, trust policies, STS | `aws-core/iam-roles-and-sts.md` |
| IRSA and EKS Pod Identity | `eks/access-and-pod-identity.md` |
| OIDC from a CI pipeline to AWS | `cicd/oidc-to-aws.md` |
| Security groups vs NACLs | `aws-core/security-groups-and-nacls.md` |
| Deployment strategies | `cicd/deployment-strategies.md` |
| Probes | `kubernetes/probes-and-graceful-shutdown.md` |
| Finalizers | `kubernetes/finalizers-and-deletion.md` |
| Argo CD deletion behaviour | `gitops/deletion-and-finalizers.md` |
| Karpenter | `eks/karpenter.md` |
| The Kubernetes Secret object | `kubernetes/configmaps-and-secrets.md` |
| AWS secret stores | `aws-services/kms-and-secrets.md` |
| Getting AWS secrets into pods | `eks/secrets.md` |
| Secrets practice in general | `security/secrets-management.md` |

- External links go in `## Sources`, or right beside the number they support. Always `https`, always written as `[text](https://...)`.
- A source is a page you opened while writing. Official documentation first: the project's own docs, man pages, RFCs. No blog you did not open, no link from memory.
- Use hosts from this list. If you need another official site, use it and say so when you hand the page over.

```text
kubernetes.io  k8s.io  kind.sigs.k8s.io  gateway-api.sigs.k8s.io  helm.sh  istio.io  www.envoyproxy.io
docs.aws.amazon.com  aws.amazon.com  karpenter.sh  kubernetes-sigs.github.io  aws.github.io
developer.hashicorp.com  terragrunt.gruntwork.io  opentofu.org  docs.ansible.com
docs.github.com  github.com  support.atlassian.com  www.jenkins.io  argo-cd.readthedocs.io  argoproj.github.io  opengitops.dev
prometheus.io  grafana.com  docs.fluentbit.io  opensearch.org  docs.opensearch.org  opentelemetry.io
docs.docker.com  containerd.io  opencontainers.org  git-scm.com  nginx.org  www.postgresql.org  redis.io  valkey.io
man7.org  manpages.ubuntu.com  www.kernel.org  docs.kernel.org  www.gnu.org  www.freedesktop.org  systemd.io
www.rfc-editor.org  datatracker.ietf.org  developer.mozilla.org  www.iana.org  curl.se  docs.openssl.org  www.openssh.com  man.openbsd.org
letsencrypt.org  openid.net  oauth.net  jwt.io  semver.org  sre.google  www.brendangregg.com  trivy.dev  docs.sonarsource.com
maven.apache.org  docs.gradle.org  docs.npmjs.com  jqlang.org  mikefarah.gitbook.io  www.shellcheck.net  www.cisecurity.org  www.first.org
```

## Facts, numbers and versions

- If you cannot confirm a flag, default, limit or behaviour from a man page, `--help` or official documentation, leave it out or tag it `(unverified)`. Never guess.
- Numbers that change (quotas, prices, support windows, per-instance limits) are linked, not quoted: "see the quotas page". Stable protocol facts (port numbers, status codes) are stated, with a source.
- Say what a statement depends on: "as of Kubernetes 1.34", or "as of November 2026".
- Things that changed recently are where memory is most often wrong. Open the current documentation for them.

## Commands and output

- **Never paste output from the machine you are working on.** No hostname, username, home path, kernel build string, hardware detail or public address. Output comes only from throwaway containers, the lab cluster, or an empty temporary directory.
- A container leaks a little of its host. Its `/etc/resolv.conf` and the `SERVER` line of `dig` show the laptop's real resolver: rewrite that address to `10.0.0.2`. `uname` shows the host's kernel build: leave it out. Memory, CPU and disk sizes are harmless.
- Show only what the page created. Do not list other images, containers or files that happen to be on the machine.
- Output may be trimmed with a `...` line. It may not be invented on a page whose `commands` value says it was run.
- If real output contains an address outside the example ranges below, rewrite the address and keep everything else.

## Example values

These are the only values allowed. An automatic scan rejects anything else.

| Kind | Allowed |
|---|---|
| Private IPv4 | Anything inside `10.0.0.0/16` or `192.168.0.0/16`. As whole ranges only: `10.0.0.0/8`, `172.16.0.0/12`, `100.64.0.0/10`, `169.254.0.0/16`. |
| Public IPv4 | Anything inside `203.0.113.0/24`, `198.51.100.0/24` or `192.0.2.0/24`. Also `8.8.8.8`, `8.8.4.4`, `1.1.1.1`, `0.0.0.0`, `0.0.0.0/0`, `127.0.0.x`, `169.254.169.254`. |
| IPv6 | Anything inside `2001:db8::/32`, and `::1` |
| Docker's default bridge | `172.17.0.0/16`, with `172.17.0.1`, `172.17.0.2`, `172.17.0.3` (also written with `/16`), and `172.17.255.255` |
| A `kind` node | `172.18.0.0/16`, with `172.18.0.2`, `172.18.0.3` |
| Kubernetes Service addresses | `10.96.0.0/12`, with `10.96.0.1`, `10.96.0.10`, `10.96.100.10`, `10.96.100.20` |
| Kubernetes pod addresses | `10.244.0.0/16`, with `10.244.0.5` to `10.244.0.9` and `10.244.1.5` to `10.244.1.9` |
| AWS account id | `123456789012`, and `111122223333` for a second account |
| AWS region | `ap-south-1` |
| AWS resource ids | Only `vpc-0123456789abcdef0`, `subnet-0123456789abcdef0`, `sg-0123456789abcdef0`, `i-1234567890abcdef0`, `ami-0123456789abcdef0`, `vol-0123456789abcdef0`. Anything else is a placeholder such as `<nat-gateway-id>`. |
| Domain | `example.com` and names under it. Inside a cluster: `sample-app.demo.svc.cluster.local`. |
| Names | App `sample-app`; namespaces `demo`, `team-a`; users `app`, `ci`, `deploy`; email `user@example.com` |
| Secrets | Never realistic. `changeme`, `example-password`, `<your-token>`. The only AWS key is `AKIAIOSFODNN7EXAMPLE`. |
| Placeholders | Lowercase in angle brackets: `<account-id>`, `<cluster-name>` |

Also:

- Show a token or JWT as decoded JSON, never as the encoded string. Do not paste PEM blocks; describe them.
- No UUIDs: write `<uuid>`. No number of nine or more digits: use units (`1Gi`) or a placeholder (`<unix-time>`).
- Hashes and digests in lowercase hex, shortened to 12 characters unless the full length is the point.
- Nothing shaped like a ticket id: capital letters, a hyphen, then digits.

## Before a page is done

1. `python3 tools/check_page.py --mermaid docs/<section>/<page>.md` prints no problems.
2. The identifier scan is clean (see `RUNBOOK.md`, "Confidentiality scan").
3. Every `Try it` step was run, or the section is marked untested.
4. Read the page once as the reader: could you answer the interview questions from this page alone?
