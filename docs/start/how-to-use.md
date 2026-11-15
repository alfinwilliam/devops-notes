---
title: "How to use these notes"
status: draft
form: guide
commands: none
---

# How to use these notes

> **Status: AI draft, 2026-11-15.** Not yet verified by me.

## In one line

Each page explains one concept, lets you try it for free, and tests you with hidden-answer questions. Read one page per study session, do its exercise, then answer from memory.

## What a page looks like

Every concept page has the same sections in the same order, so you always know where to look.

| Section | What it is for |
|---|---|
| Status line | Whether anyone has checked the page yet. See the next table. |
| In one line | The 20-second answer for an interview. |
| The plain idea | Everyday words first, then the proper term. |
| How it works | The mechanism, built up step by step, with a diagram. |
| A concrete example | One scenario from start to finish. |
| Why not just...? | The tempting shortcuts and why they fail. |
| Commands to know | The commands, what they show, and every flag used. |
| How it breaks | Symptom, layer, check, likely cause. |
| Interview questions | Six to eight questions. Each answer is hidden until you click. |
| Try it | A hands-on exercise of ten minutes or less that costs nothing. |
| Zoom out | Where the concept fits, and the principle to keep. |
| Sources | The official documentation behind the page. |

Short pages keep only the one-line answer, the mechanism, the questions and the sources.

## How far to trust a page

These notes were drafted with an AI assistant. A draft can be wrong in ways that sound right, so every page says how far it has been checked.

| Status | Meaning | How to treat it |
|---|---|---|
| Not written yet | A placeholder listing what the page will cover. | Use the official documentation. |
| AI draft | Written by an AI. Nobody has checked it. | Read it to get the shape. Check anything you would repeat in an interview. |
| AI draft, fact-checked by a second AI pass | A second pass compared each claim with a source. | Better, and still not checked by a person. |
| Verified by me | The owner compared every claim with its source and did the exercise. | Trust it as you would your own notes. |

Each fact-checked page has a claims ledger in the repository's [review folder](https://github.com/alfinwilliam/devops-notes/tree/main/review): a table of every checkable claim on the page with its source. Verifying a page means working down that table.

## One study session

Reading alone does not count. Something has to be run, or written from memory.

1. **Predict.** Read the page title and the first interview question. Write your answer before you read anything else.
2. **Read.** About 25 minutes. Follow the diagram with your finger. Stop at every command and say what each flag does.
3. **Do.** Run the "Try it". Type the commands yourself. Predict each result before you press Enter, and break one thing on purpose.
4. **Explain.** Close the page. Write the concept in your own words in fifteen lines or fewer, then compare and correct.
5. **Score.** Answer the interview questions aloud. Open each hidden answer and score yourself: 2 for every point, 1 for some, 0 for none or wrong. Seventy per cent is a pass.
6. **Come back.** Tomorrow, answer yesterday's questions again before you start a new page.

## Where to start

Work through the sections in the order of the tabs. Each one leans on the ones before it.

1. **Foundations:** [Linux](../linux/README.md), then [Networking](../networking/README.md), then [Git](../git/README.md).
2. **AWS identity and network:** [who may call what, and which subnet can reach which](../aws-core/README.md).
3. **Containers and Kubernetes:** [Containers](../containers/README.md), [Kubernetes](../kubernetes/README.md), then [EKS](../eks/README.md) and [Helm](../helm/README.md).
4. **Delivery:** [Infrastructure as code](../iac/README.md), [CI/CD](../cicd/README.md), [GitOps](../gitops/README.md).
5. **Operate:** [Observability](../observability/README.md), [Security](../security/README.md), [Operations](../operations/README.md).
6. **The rest of AWS** and the deeper topics as you need them: [AWS services](../aws-services/README.md), [Serverless](../serverless/README.md), [Service mesh](../mesh/README.md), [Data stores](../data/README.md).

Two pages tie everything together, and are worth reading first and again later: [One request, end to end](request-path.md) and [The debugging walk](debugging-walk.md).

When an interview is close, use the [Interview kit](../interview/README.md). Its [question index](../interview/question-index.md) lists every question in these notes on one page.
