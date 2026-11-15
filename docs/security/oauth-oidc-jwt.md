---
title: "OAuth 2.0, OIDC and JWTs"
status: stub
form: full
commands: docs
---

# OAuth 2.0, OIDC and JWTs

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- Authentication vs authorisation
- OAuth roles, and the authorization code flow with PKCE (sequence diagram)
- The client credentials flow for machines
- OIDC adds identity: the ID token
- JWT anatomy: header, payload claims (iss, sub, aud, exp), signature
- validation steps and JWKS
- show decoded JSON only, never an encoded token
- Where this shows up: SSO, CI OIDC, IRSA, API authorizers (links)
- Common mistakes: no audience check, long-lived tokens
