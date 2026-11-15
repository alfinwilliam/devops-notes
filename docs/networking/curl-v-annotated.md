---
title: "curl -v, line by line"
status: stub
form: full
commands: container
---

# curl -v, line by line

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- One real curl -v transcript against an HTTPS site, with every line explained: name resolution, connect, ALPN, the TLS handshake lines, the certificate lines, request headers (>), response headers (<), body
- What each failure looks like in this output: could not resolve, connection refused, timed out, certificate problem, 4xx and 5xx
- Useful flags: -I, -L, -k and why not, --resolve, --connect-to, -w with timing variables
