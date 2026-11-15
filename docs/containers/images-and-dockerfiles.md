---
title: "Images and Dockerfiles"
status: stub
form: full
commands: container
---

# Images and Dockerfiles

> **Status: not written yet.** This page is a placeholder that lists what it will cover.

## Planned coverage

- An image is layers plus config
- The Dockerfile instructions that matter: FROM, RUN, COPY, WORKDIR, ENV, EXPOSE, USER, ENTRYPOINT, CMD
- Layer caching and why instruction order matters
- Multi-stage builds
- Base images: distroless, alpine, slim
- ENTRYPOINT vs CMD
- exec form vs shell form and signals reaching PID 1
- .dockerignore
- Tags vs digests
- docker history and docker inspect
- build one small image for real
