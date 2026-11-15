#!/usr/bin/env bash
# Build or preview the site with Docker, so nothing has to be installed on the laptop.
#
#   ./preview.sh          serve at http://localhost:8000/devops-notes/, rebuild on save, Ctrl+C to stop
#   ./preview.sh build    build once into site/ in strict mode; any warning fails the build
#
# The image is pinned by digest, so the laptop and GitHub Actions run the same generator.
# The first run downloads the image (about 300 MB); later runs start in seconds.

set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"

IMAGE="squidfunk/mkdocs-material:9.8.1@sha256:f797da217ff01b20b298d2185eb9d88fb81f5a322c439eba854f2e4de8a48e65"

mode="${1:-serve}"

# Run as the current user so the files in site/ are not owned by root.
common=(--rm --user "$(id -u):$(id -g)" -e HOME=/tmp -e NO_MKDOCS_2_WARNING=1 -v "$PWD:/docs")

case "$mode" in
  serve)
    tty_args=()
    if [ -t 0 ] && [ -t 1 ]; then
      tty_args=(-it)
    fi
    exec docker run "${common[@]}" "${tty_args[@]}" -p 127.0.0.1:8000:8000 "$IMAGE" serve --dev-addr=0.0.0.0:8000
    ;;
  build)
    exec docker run "${common[@]}" "$IMAGE" build --strict --clean
    ;;
  *)
    echo "Usage: $0 [serve|build]" >&2
    exit 2
    ;;
esac
