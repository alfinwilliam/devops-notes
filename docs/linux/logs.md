---
title: "Logs"
status: stub
form: full
commands: container
---

# Logs

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Where logs live: /var/log, the journal, application files, container stdout
- journalctl -u -f --since -p -k -b
- syslog facilities and severity levels
- logrotate: copytruncate vs asking the process to reopen
- Reading logs under pressure: time window, first error, a request id
- Logs filling a disk
- Structured (JSON) logs and why they help
