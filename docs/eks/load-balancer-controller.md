---
title: "AWS Load Balancer Controller"
status: stub
form: full
commands: docs
---

# AWS Load Balancer Controller

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- What the controller does: watches Ingress and Service objects and creates ALBs and NLBs
- Ingress to ALB, target type ip vs instance
- Service type LoadBalancer to NLB
- The annotations that matter
- IngressGroup to share one ALB
- TargetGroupBinding
- Health checks and pod readiness gates
- Why an Ingress has no address: IAM, subnet tags, controller logs
