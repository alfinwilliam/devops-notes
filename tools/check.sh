#!/usr/bin/env bash
# Every local check, in one command. Run it before pushing.
#
#   ./tools/check.sh           structure, Markdown lint, diagrams, strict build
#   ./tools/check.sh --links   the same, then test every external link (slow; needs internet)
#
# Only the strict build runs in GitHub Actions. The rest is for you, so a moved link on someone
# else's site can never block a typo fix.

set -uo pipefail
cd "$(dirname "$(readlink -f "$0")")/.."
repo="$(pwd)"

LINT_IMAGE="davidanson/markdownlint-cli2@sha256:caf0698eaea0268bcf35b5e2d7ba946b5899d323e765bc2862054405658cd948"
LINK_IMAGE="lycheeverse/lychee@sha256:eaff3e0a13603c9a701accfcc84f44158bb77bf36ecfa4622b626056c3463892"

fail=0
step() { printf '\n== %s\n' "$1"; }

step "1/4 page structure (tools/check_page.py)"
python3 tools/check_page.py docs || fail=1

step "2/4 Markdown lint (blank lines round lists and fences, 4-space nesting)"
docker run --rm --user "$(id -u):$(id -g)" -v "$repo:/workdir" "$LINT_IMAGE" || fail=1

step "3/4 Mermaid diagrams parse"
python3 tools/check_page.py --mermaid-only docs || fail=1

step "4/4 strict site build"
./preview.sh build || fail=1

if [ "${1:-}" = "--links" ]; then
  step "extra: external links"
  # 403 and 429 mean the site refused an automated request, not that the page is gone. Check those by hand.
  docker run --rm --user "$(id -u):$(id -g)" -v "$repo:/input:ro" "$LINK_IMAGE" \
    --no-progress --max-concurrency 6 --max-retries 2 --timeout 30 \
    --accept '200..=299,403,429' --exclude 'localhost' --exclude 'example\.(com|org|net)' \
    /input/docs /input/review || fail=1

  step "extra: AWS documentation links that silently redirect"
  # docs.aws.amazon.com answers a page that does not exist with a redirect to the guide's index,
  # which a normal link checker counts as a success. A real page answers 200 directly.
  bad=0
  while read -r url; do
    code=$(curl -s -o /dev/null -m 25 -w "%{http_code}" "$url")
    if [ "$code" != "200" ]; then echo "  $code $url"; bad=1; fi
  done < <(grep -rhoE '\]\(https://docs\.aws\.amazon\.com/[^) ]+\)' docs --include='*.md' | sed -E 's/^\]\(//; s/\)$//' | sort -u)
  [ "$bad" -eq 0 ] && echo "  all AWS documentation links load directly" || fail=1
fi

echo
if [ "$fail" -eq 0 ]; then echo "All checks passed."; else echo "Some checks FAILED. Fix the lines listed above and run this again."; fi
exit "$fail"
