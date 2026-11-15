---
title: "OIDC from pipelines to AWS"
status: stub
form: full
commands: docs
---

# OIDC from pipelines to AWS

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- The problem with long-lived access keys in CI
- How OIDC federation works: the CI provider issues a signed token, AWS trusts the provider, AssumeRoleWithWebIdentity returns temporary credentials (sequence diagram)
- Trust policy conditions on aud and sub, and why sub must be pinned
- GitHub Actions setup: id-token: write and the configure-aws-credentials action
- Bitbucket differences
- Debugging 'not authorized to perform sts:AssumeRoleWithWebIdentity'
