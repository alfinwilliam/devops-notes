---
title: "DevOps Notes"
---

# DevOps Notes

General interview-prep notes for a DevOps engineer: the fundamentals first, then every tool built on them. One concept per page, each with a diagram, a free hands-on exercise and hidden-answer questions.

New here? Read [How to use these notes](start/how-to-use.md) first.

> **How far to trust this.** These notes were drafted with an AI assistant. Every page says in its first line whether it is still an AI draft, has been fact-checked by a second AI pass, or has been verified by me. Check anything important against the sources at the bottom of the page.

## The two maps

- [One request, end to end](start/request-path.md): a request's whole journey from a browser to a container, and what can break at each hop.
- [The debugging walk](start/debugging-walk.md): a fixed order for finding out why something does not work.

## Sections, in study order

| Section | The question it answers |
|---|---|
| [Linux](linux/README.md) | What is this process doing, and what is it allowed to do? |
| [Networking](networking/README.md) | How does a packet get there, and where can it die? |
| [Git](git/README.md) | What does Git store, and how do you get out of trouble? |
| [AWS identity and network](aws-core/README.md) | Who may call what, and which subnet can reach which? |
| [Containers](containers/README.md) | What is a container really, and how do you debug one? |
| [Kubernetes](kubernetes/README.md) | How does a container get scheduled, wired up and kept alive? |
| [EKS](eks/README.md) | What does AWS change about Kubernetes? |
| [Helm](helm/README.md) | How are manifests packaged, and what goes wrong on upgrade? |
| [Infrastructure as code](iac/README.md) | How do you write infrastructure down and change it safely? |
| [CI/CD](cicd/README.md) | How does a commit become a running change, and how do you undo it? |
| [GitOps and Argo CD](gitops/README.md) | What happens when Git is the source of truth for the cluster? |
| [Observability](observability/README.md) | How do you see what the system is doing? |
| [AWS services](aws-services/README.md) | Compute, storage, data, and the services that watch them. |
| [Service mesh](mesh/README.md) | What does Istio do to traffic between services? |
| [Serverless and Fargate](serverless/README.md) | How do you run code and containers without managing servers? |
| [Security](security/README.md) | Identity protocols, secrets, vulnerabilities and guardrails. |
| [Operations](operations/README.md) | Keeping it up, getting it back, paying for it, changing it safely. |
| [Data stores](data/README.md) | What an operator needs to know about the databases behind the services. |
| [Interview kit](interview/README.md) | Turning what you know into answers. |

## Find something

Use the search box at the top, or the [Glossary](start/glossary.md). Every interview question in these notes is listed in the [question index](interview/question-index.md).
