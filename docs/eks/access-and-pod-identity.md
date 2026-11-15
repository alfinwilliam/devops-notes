---
title: "Cluster access, IRSA and Pod Identity"
status: stub
form: full
commands: docs
---

# Cluster access, IRSA and Pod Identity

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Who can call the cluster API: access entries and access policies vs the legacy aws-auth ConfigMap (state which the docs recommend now)
- How a pod gets AWS permissions with IRSA: service account annotation, projected token, OIDC provider, AssumeRoleWithWebIdentity, trust policy conditions on sub and aud (sequence diagram)
- EKS Pod Identity: the agent and associations, and how it differs
- Why putting permissions on the node role is the wrong answer
- Debugging AccessDenied from a pod
