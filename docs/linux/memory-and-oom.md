---
title: "Memory and the OOM killer"
status: stub
form: full
commands: container
---

# Memory and the OOM killer

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Virtual vs resident memory: VSZ and RSS
- Reading free -h: used, buff/cache, available
- Page cache
- swap and swappiness
- overcommit
- The OOM killer, oom_score, and how to see a kill in dmesg or the journal
- cgroups v2 memory.max, and why a container is killed with exit code 137 while the host still has free memory (demonstrate with docker run -m)
- top and ps sorted by memory
