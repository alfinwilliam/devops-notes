---
title: "Probes and graceful shutdown"
status: stub
form: full
commands: kind
---

# Probes and graceful shutdown

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Startup vs readiness vs liveness: what each controls and what a failure does
- Probe types and timing fields
- Common mistakes: a liveness probe that kills a slow start, a readiness probe that depends on a downstream service
- The termination sequence: SIGTERM, preStop, terminationGracePeriodSeconds, and the endpoint-removal race (sequence diagram)
- A zero-downtime checklist
