---
title: "TLS and certificates"
status: stub
form: full
commands: container
---

# TLS and certificates

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- What TLS gives you: encryption, identity, integrity
- Public and private keys and certificates in plain words
- The chain of trust: leaf, intermediate, root (diagram)
- The TLS 1.3 handshake (sequence diagram) and SNI
- Certificate fields: SAN, validity
- wildcard certificates
- Where TLS terminates (edge, load balancer, sidecar, pod) and re-encryption
- mTLS
- openssl s_client and openssl x509 to inspect
- Common failures: expired, wrong name, missing intermediate, clock skew
- ACME in one paragraph
