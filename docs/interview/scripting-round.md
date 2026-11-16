---
title: "Scripting round: shell and Python exercises"
status: draft
form: guide
commands: container
---

# Scripting round: shell and Python exercises

> **Status: AI draft, 2026-11-16.** Not yet verified by me. Every solution was run in a throwaway Debian 13 container (the `ruby:3.3` image, chosen because it has bash 5.2, GNU findutils, mawk and Python 3.13); the output shown is real. Sample data uses documentation IP ranges.

## In one line

Scripting rounds test whether you can turn a small operations task into a correct, readable script: read the input carefully, start with the simplest pipeline that works, handle the obvious edge cases (empty input, spaces, failures), and say what you would add for production. Try each task before opening the solution.

## How to approach a task

1. Restate the input and the expected output; ask about edge cases.
2. Pick the tool: a shell pipeline for line-oriented text; Python for JSON, CSV, arithmetic and anything with more than a few branches ([Bash scripting](../linux/bash-scripting.md), [Text tools](../linux/text-tools.md)).
3. Write it, run it on a tiny sample, then mention `set -euo pipefail`, quoting, and error handling.

## 1. Top client IPs from an access log

Print the three IP addresses with the most requests in `access.log` (combined log format; the client IP is the first field).

<details markdown="1">
<summary>Solution</summary>

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -3
```

```text
      4 203.0.113.10
      3 198.51.100.7
      2 203.0.113.11
```

`uniq -c` only counts adjacent lines, so `sort` must come first. In Python:

```python
from collections import Counter
with open("access.log") as f:
    counts = Counter(line.split()[0] for line in f if line.strip())
for ip, n in counts.most_common(3):
    print(n, ip)
```

```text
4 203.0.113.10
3 198.51.100.7
2 203.0.113.11
```

</details>

## 2. Find files larger than a size

List files under `data/` larger than 10 MB, with sizes.

<details markdown="1">
<summary>Solution</summary>

```bash
find data -type f -size +10M -exec ls -lh {} + | awk '{print $5, $9}'
```

```text
15M data/big.bin
120M data/huge.iso
```

`-size +10M` means more than 10 MiB (find rounds up to whole units). For a whole disk, `du -xh --max-depth=1 / | sort -h` finds the heavy directories first ([Disks and filesystems](../linux/disks-and-filesystems.md)).

</details>

## 3. Check a list of URLs and report status codes

`urls.txt` holds one URL per line. Print the HTTP status for each; unreachable URLs should not stop the loop.

<details markdown="1">
<summary>Solution</summary>

```bash
while read -r url; do
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 5 "$url")
  echo "$code $url"
done < urls.txt
```

```text
200 http://127.0.0.1:8000/
404 http://127.0.0.1:8000/missing
000 http://127.0.0.1:8001/
```

`000` means no HTTP response at all (connection refused, DNS failure, timeout). The test server was `python3 -m http.server 8000` in the same container. Add `-L` to follow redirects, and run checks in parallel with `xargs -P` for long lists ([curl -v line by line](../networking/curl-v-annotated.md)).

</details>

## 4. Remove files older than N days

Delete `*.log` files in `logs/` older than 7 days, printing what is deleted.

<details markdown="1">
<summary>Solution</summary>

```bash
find logs -name '*.log' -mtime +7 -print -delete
ls logs
```

```text
logs/app-20.log
logs/app-40.log
logs/app-10.log
app-1.log
app-5.log
```

Run it once with `-print` alone (no `-delete`) to see what matches. To compress instead of delete: `find logs -name '*.log' -mtime +7 -exec gzip {} +`. On real servers, `logrotate` already does this ([Logs](../linux/logs.md)).

</details>

## 5. Parse JSON from an API response

From `response.json`, print the items whose status is not `running`, and the total number of replicas.

```json
{"items":[{"name":"web","status":"running","replicas":3},{"name":"worker","status":"degraded","replicas":1},{"name":"db","status":"running","replicas":2}]}
```

<details markdown="1">
<summary>Solution</summary>

```python
import json
with open("response.json") as f:
    data = json.load(f)
for item in data["items"]:
    if item["status"] != "running":
        print(f'{item["name"]}: {item["status"]} ({item["replicas"]} replicas)')
print("total replicas:", sum(i["replicas"] for i in data["items"]))
```

```text
worker: degraded (1 replicas)
total replicas: 6
```

With `jq` (not in this image): `jq -r '.items[] | select(.status != "running") | .name' response.json` and `jq '[.items[].replicas] | add' response.json` ([jq and yq](../linux/jq-and-yq.md)).

</details>

## 6. Retry a command with exponential backoff

Write a `retry` function: run a command up to N times, doubling the wait after each failure, and return failure if every attempt fails.

<details markdown="1">
<summary>Solution</summary>

```bash
retry() {
  local max=$1; shift
  local delay=1
  for ((i = 1; i <= max; i++)); do
    "$@" && return 0
    if ((i < max)); then
      echo "attempt $i failed; retrying in ${delay}s" >&2
      sleep "$delay"
      delay=$((delay * 2))
    fi
  done
  echo "attempt $max failed; giving up" >&2
  return 1
}
retry 3 curl -sf --max-time 2 http://127.0.0.1:8001/; echo "exit status: $?"
```

```text
attempt 1 failed; retrying in 1s
attempt 2 failed; retrying in 2s
attempt 3 failed; giving up
exit status: 1
```

`"$@"` keeps the command's arguments intact, spaces included. In production add jitter (a random extra delay) so many clients do not retry in lockstep, and a cap on the delay.

</details>

## 7. Compare two lists

`expected.txt` lists hosts that should be running; `running.txt` lists hosts that are. Print what is missing and what is unexpected.

<details markdown="1">
<summary>Solution</summary>

```bash
echo "missing (expected, not running):"
comm -23 <(sort expected.txt) <(sort running.txt)
echo "unexpected (running, not expected):"
comm -13 <(sort expected.txt) <(sort running.txt)
```

```text
missing (expected, not running):
web-2
unexpected (running, not expected):
cache-1
```

`comm` needs sorted input; `-23` hides lines only in file 2 and lines in both. In Python: `set(expected) - set(running)` and the reverse.

</details>

## 8. Read a CSV and sum a column

`costs.csv` has `service,month,cost`. Print the total per service and the overall total.

<details markdown="1">
<summary>Solution</summary>

```bash
awk -F, 'NR > 1 { sum[$1] += $3 } END { for (s in sum) printf "%s %.2f\n", s, sum[s] }' costs.csv | sort
awk -F, 'NR > 1 { total += $3 } END { printf "total %.2f\n", total }' costs.csv
```

```text
cache 45.25
db 310.00
web 220.00
total 575.25
```

`awk -F,` breaks on quoted fields that contain commas; for real CSV use Python's `csv` module:

```python
import csv
from collections import defaultdict
totals = defaultdict(float)
with open("costs.csv", newline="") as f:
    for row in csv.DictReader(f):
        totals[row["service"]] += float(row["cost"])
for service, cost in sorted(totals.items()):
    print(f"{service} {cost:.2f}")
print(f"total {sum(totals.values()):.2f}")
```

```text
cache 45.25
db 310.00
web 220.00
total 575.25
```

For money, Python's `decimal.Decimal` avoids floating-point rounding.

</details>

## 9. Count words

Print the three most common words in `words.txt`, ignoring case.

<details markdown="1">
<summary>Solution</summary>

```bash
tr -s '[:space:]' '\n' < words.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -rn | head -3
```

```text
      3 the
      2 dog
      1 sleeps
```

Ties (every word with count 1) come out in whatever order `sort` leaves them; add `-k2` to the last sort to make it stable. Python: `Counter(open("words.txt").read().lower().split()).most_common(3)`.

</details>

## 10. Find and stop a process by name

Two stray `sleep 300` and `sleep 301` processes are running. List them and stop them with SIGTERM.

<details markdown="1">
<summary>Solution</summary>

```bash
pgrep -af 'sleep 30[01]'
pkill -TERM -f 'sleep 30[01]'
sleep 1
pgrep -f 'sleep 30[01]' >/dev/null && echo "still running" || echo "none left"
```

```text
28 sleep 300
29 sleep 301
none left
```

`-f` matches the full command line; check the list before killing, because a loose pattern can match more than you meant (including your own shell). Send SIGTERM first and SIGKILL only if the process ignores it ([Processes and signals](../linux/processes-and-signals.md)).

</details>

## 11. Validate an IP address

Report whether each input is a valid IP address (or network).

<details markdown="1">
<summary>Solution</summary>

Python's standard library does it properly, IPv6 included:

```python
import ipaddress
for value in ["10.0.1.25", "256.1.1.1", "10.0.0.0/16", "2001:db8::1", "abc"]:
    try:
        ip = ipaddress.ip_address(value)
        print(f"{value}: valid IPv{ip.version}, private={ip.is_private}")
    except ValueError:
        try:
            net = ipaddress.ip_network(value)
            print(f"{value}: a network with {net.num_addresses} addresses")
        except ValueError:
            print(f"{value}: not valid")
```

```text
10.0.1.25: valid IPv4, private=True
256.1.1.1: not valid
10.0.0.0/16: a network with 65536 addresses
2001:db8::1: valid IPv6, private=True
abc: not valid
```

In bash, IPv4 only:

```bash
valid_ipv4() {
  local ip=$1 IFS=.
  [[ $ip =~ ^[0-9]{1,3}(\.[0-9]{1,3}){3}$ ]] || return 1
  for octet in $ip; do ((octet <= 255)) || return 1; done
}
for v in 10.0.1.25 256.1.1.1 1.2.3; do valid_ipv4 "$v" && echo "$v valid" || echo "$v invalid"; done
```

```text
10.0.1.25 valid
256.1.1.1 invalid
1.2.3 invalid
```

A regex alone accepts `999.1.1.1`; the octet check is what makes it correct ([IP addresses and subnetting](../networking/ip-and-subnetting.md)).

</details>

## What interviewers listen for

- Quoting (`"$var"`, `"$@"`) and `read -r`.
- Failure handling: exit codes, `set -euo pipefail` and when it surprises you, timeouts on network calls.
- Knowing when to switch from shell to Python.
- Testing on a small sample before running against production data, and a dry run before deleting anything.
