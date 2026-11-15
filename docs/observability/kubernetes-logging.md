---
title: "How Kubernetes logging works"
status: stub
form: full
commands: kind
---

# How Kubernetes logging works

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Container stdout and stderr go to the runtime, then to files on the node under /var/log/pods
- What kubectl logs actually reads
- Rotation by the kubelet
- A node-level agent as a DaemonSet shipping to a backend (diagram)
- The sidecar pattern
- What is lost when a pod is deleted
- Multiline logs
- Structured logging
- look at the files inside the kind node container
