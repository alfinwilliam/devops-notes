---
title: "Boot, systemd and services"
status: stub
form: full
commands: docs
---

# Boot, systemd and services

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Boot in brief: firmware, bootloader, kernel, PID 1
- What systemd is and what a unit is
- Unit types: service, timer, socket, target
- Unit file anatomy: ExecStart, Restart, User, Environment, After, Wants, WantedBy
- systemctl start, stop, restart, enable, status, cat, daemon-reload
- Write a minimal service unit
- restart policies
- Find out why a service failed
- supervisord compared with systemd in a short table
- systemd does not run in a plain container, so say how the commands were checked
