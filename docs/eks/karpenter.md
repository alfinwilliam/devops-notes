---
title: "Karpenter in depth"
status: stub
form: full
commands: docs
---

# Karpenter in depth

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- NodePool, EC2NodeClass, NodeClaim
- The provisioning flow from a Pending pod to a node (sequence diagram)
- Requirements: instance families, capacity type, zones
- Disruption: consolidation, drift, expiration, disruption budgets
- The do-not-disrupt annotation
- Spot interruption handling
- Limits and weights
- Common problems: pods never schedule, nodes churn, a waiting pod is evicted
- use the current API version from the docs
