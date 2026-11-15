---
title: "Finalizers and deletion"
status: stub
form: full
commands: kind
---

# Finalizers and deletion

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- What delete really does: deletionTimestamp, then finalizers, then removal (sequence diagram)
- ownerReferences and garbage collection
- Cascading deletion: background, foreground, orphan
- Why a namespace or resource is stuck Terminating and how to find the blocker
- The danger of removing a finalizer by hand
- The risk of deleting by label selector
