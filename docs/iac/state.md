---
title: "Terraform state"
status: stub
form: full
commands: cli
---

# Terraform state

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Why state exists: it maps configuration to real resource IDs
- What is inside
- Remote backends (S3) and locking: check the current S3 backend docs for use_lockfile and the status of DynamoDB locking
- State commands: list, show, mv, rm
- Sensitive values in state
- Drift and refresh
- Splitting state by blast radius
- Recovering from a stuck lock
