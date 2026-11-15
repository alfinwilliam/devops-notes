---
title: "Pod networking and NetworkPolicy"
status: stub
form: full
commands: kind
---

# Pod networking and NetworkPolicy

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- The Kubernetes network model: every pod has an IP, no NAT between pods
- What a CNI plugin does
- Pod to pod on one node vs across nodes (diagram)
- The Service traffic path
- NetworkPolicy: default allow, selecting pods, ingress and egress rules, the default-deny pattern, and that it needs a CNI that enforces it (say whether kind's default does)
- Debugging with a throwaway tools pod
