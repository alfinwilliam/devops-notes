---
title: "Nginx as a reverse proxy"
status: stub
form: full
commands: container
---

# Nginx as a reverse proxy

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Master and worker processes
- Config structure: http, server, location
- how a request picks a server block and a location
- proxy_pass and upstream blocks
- Passing Host and X-Forwarded-* headers
- proxy_connect_timeout, proxy_read_timeout, and the 502 and 504 they cause (reproduce both)
- TLS termination config in outline
- Access and error logs, a log format with upstream timings
- nginx -t, reload vs restart
