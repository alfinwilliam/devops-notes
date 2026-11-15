---
title: "Sidecars and traffic flow"
status: stub
form: full
commands: docs
---

# Sidecars and traffic flow

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Sidecar injection through a mutating webhook: namespace label, revision
- How traffic is redirected into the proxy (init container or CNI, iptables)
- The path of one request: app, local Envoy, remote Envoy, app (diagram)
- Protocol detection from port names and appProtocol
- Startup and shutdown ordering issues
- Resource overhead
