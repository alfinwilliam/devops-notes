---
title: "Deletion, finalizers and safe cleanup"
status: stub
form: full
commands: docs
---

# Deletion, finalizers and safe cleanup

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- What deleting an Application does with and without the resources finalizer
- Cascading (foreground, background) vs non-cascading delete
- ApplicationSet deletion and preserveResourcesOnDeletion
- Prune safety: the Prune=false and Delete=false options
- How one delete can remove many workloads, and the guardrails that prevent it
