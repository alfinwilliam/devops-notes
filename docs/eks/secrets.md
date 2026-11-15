---
title: "Secrets from AWS into pods"
status: stub
form: full
commands: docs
---

# Secrets from AWS into pods

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Options compared: External Secrets Operator (syncs into Kubernetes Secrets), Secrets Store CSI driver with the AWS provider (mounts files), direct SDK calls
- How each authenticates (IRSA or Pod Identity)
- Rotation, and whether running pods see the new value
- Envelope encryption of Kubernetes Secrets with KMS
- Choosing one
