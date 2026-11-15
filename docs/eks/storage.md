---
title: "EBS and EFS CSI drivers"
status: stub
form: full
commands: docs
---

# EBS and EFS CSI drivers

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- EBS: block storage, one AZ, RWO, a gp3 StorageClass, WaitForFirstConsumer and AZ pinning
- EFS: NFS, multi-AZ, RWX, access points for per-app directories and a fixed uid and gid
- When to choose which (table)
- The IAM permissions the drivers need
- Common failures: volume in another AZ, mount timeout from a security group, permission denied on EFS
