---
title: "Architecture and the reconcile loop"
status: stub
form: full
commands: kind
---

# Architecture and the reconcile loop

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Desired state vs actual state
- Control plane: API server, etcd, scheduler, controller manager, cloud controller manager
- Node: kubelet, container runtime, kube-proxy, CNI plugin (diagram)
- What happens after kubectl apply for a Deployment, step by step (sequence diagram)
- spec vs status
- Everything talks through the API server
