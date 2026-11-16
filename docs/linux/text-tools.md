---
title: "Text tools: grep, sed, awk, find"
status: draft
form: full
commands: container
---

# Text tools: grep, sed, awk, find

> **Status: AI draft, 2026-11-16.** Not yet verified by me. Commands and output were run in a throwaway container; addresses are rewritten to example ranges.

## In one line

`grep` picks lines, `cut` and `awk` pick fields, `sort` and `uniq -c` count, `sed` edits text as it streams past, and `find` picks files. Chained with pipes, they answer most "what is in this log?" questions in one line.

## The plain idea

Logs, configs and command output are just lines of text. Most questions about them are one of a few shapes: "which lines mention X?", "how many of each?", "what is in column 9?", "what are the slowest?". Each shape has a small tool, and you join the tools with pipes ([Streams, pipes and redirection](streams-and-redirection.md)).

The habit that makes this work is building a pipeline one step at a time. Run the first command, look at the output, add the next stage, look again. You never write the whole thing in one go.

## How it works

```mermaid
flowchart LR
    A["access.log"] --> B["grep: keep matching lines"]
    B --> C["awk or cut: keep one field"]
    C --> D["sort: group equal values together"]
    D --> E["uniq -c: count each group"]
    E --> F["sort -rn: biggest first"]
    F --> G["head: top N"]
```

### The tools and their one job

| Tool | Job | Works on |
|---|---|---|
| `grep` | Keep lines that match a pattern (or, with `-v`, that do not) | Lines |
| `cut` | Keep fields split by one fixed delimiter | Fields |
| `awk` | Split each line into fields, test conditions, print, sum, count | Fields, with logic |
| `sed` | Edit the stream: substitute, delete or print lines | Lines |
| `sort` | Order lines; `-n` numeric, `-r` reverse, `-k` by field | Whole input |
| `uniq` | Collapse repeated **adjacent** lines; `-c` counts them | Sorted input |
| `wc -l` | Count lines | Whole input |
| `head`, `tail` | First or last N lines; `tail -f` follows a growing file | Lines |
| `find` | Find files by name, age, size or type, and act on them | The filesystem |

`uniq` only merges lines that are next to each other, which is why `sort` almost always comes before it.

### grep and regular expressions

`grep` matches a **regular expression**, a small pattern language. With `-E` (extended), the common pieces are:

| Pattern | Matches |
|---|---|
| `.` | Any one character |
| `^` and `$` | Start and end of the line |
| `[0-9]`, `[a-z]` | One character from a set |
| `x*`, `x+`, `x?` | Zero or more, one or more, zero or one of `x` |
| `\.` | A literal dot |

A vertical bar separates alternatives: `(500|502)` matches either code.

### awk in one paragraph

`awk` reads a line, splits it on whitespace into `$1`, `$2` and so on (`$0` is the whole line, `NF` the number of fields, `NR` the line number), then runs your program on it. A program is `condition { action }`. Either part may be left out. `END { ... }` runs after the last line, which is where totals are printed. Variables need no declaring and start at zero.

### sed in one paragraph

`sed` applies an edit to each line as it passes. The one you will use most is substitute, `s/old/new/`, where `old` is a regular expression; add `g` to replace every match on the line, not just the first. `sed -n '3,4p'` prints only lines 3 to 4. `sed -i` edits a file in place, so try the command without `-i` first.

## A concrete example

Users report errors on the orders API. You have the access log. Each line looks like this; field 1 is the client address, field 9 the status code, and the last field (11) the response time in seconds:

```text
203.0.113.10 - - [16/Nov/2026:09:00:02 +0000] "POST /api/orders HTTP/1.1" 500 87 1.204
```

1. How many 5xx responses? `grep -c " 50[0-9] " access.log` prints `4`.
2. Which status codes, and how many of each? `awk '{print $9}' access.log | sort | uniq -c | sort -rn`.
3. What share are errors? `awk '$9 >= 500 {e++} END {printf "errors %d of %d\n", e, NR}' access.log`.
4. Which requests were slowest? `sort -k11 -rn access.log | head -3`. One took 30 seconds and returned 502: a sign of a timeout behind a proxy ([Load balancers and proxies](../networking/load-balancers-and-proxies.md)).
5. Who is sending the errors? `grep -E " (500|502|503) " access.log | cut -d" " -f1,9`.

Five commands, and you have the error rate, the slowest calls and the clients affected, before opening any dashboard.

## Why not just...?

- **...open the log in an editor?** A production log can be gigabytes. Editors load it into memory; `grep` and `awk` stream it and use almost none.
- **...use `cut` for everything?** `cut` splits on exactly one delimiter character, so two spaces in a row create an empty field. `awk` splits on any run of whitespace, which suits most logs.
- **...use `sed -i` straight away?** It changes the file with no undo. Run the same `sed` without `-i` first and read the output, or use `-i.bak` to keep a copy.

## Commands to know

Count, invert and number:

```console
# grep -c " 50[0-9] " access.log
4
# grep -v "/health" access.log | wc -l
8
# grep -n "POST" access.log
3:203.0.113.10 - - [16/Nov/2026:09:00:02 +0000] "POST /api/orders HTTP/1.1" 500 87 1.204
7:203.0.113.11 - - [16/Nov/2026:09:00:06 +0000] "POST /api/orders HTTP/1.1" 201 77 0.233
```

`-c` counts matching lines, `-v` inverts the match, `-n` adds line numbers. Also: `-i` ignores case, `-r` searches a directory tree, `-E` uses extended patterns, and `-A 2`, `-B 2`, `-C 2` show 2 lines after, before, or around each match.

Top talkers and a status-code histogram:

```console
# awk '{print $1}' access.log | sort | uniq -c | sort -rn
      4 203.0.113.10
      2 203.0.113.11
      2 198.51.100.7
      1 203.0.113.13
      1 203.0.113.12
# awk '{print $9}' access.log | sort | uniq -c | sort -rn
      5 200
      1 503
      1 502
      1 500
      1 404
      1 201
```

A rate and the slowest requests:

```console
# awk '$9 >= 500 {e++} END {printf "errors %d of %d (%.0f%%)\n", e, NR, 100*e/NR}' access.log
errors 3 of 10 (30%)
# sort -k11 -rn access.log | head -3 | awk '{print $11, $7, $9}'
30.001 /api/orders 502
1.204 /api/orders 500
0.233 /api/orders 201
```

`sort -k11 -rn` sorts by field 11, numerically, largest first.

Pick fields and lines, and edit:

```console
# grep -E " (500|502|503) " access.log | cut -d" " -f1,9
203.0.113.10 500
203.0.113.10 502
203.0.113.13 503
# sed -n "3,4p" access.log
203.0.113.10 - - [16/Nov/2026:09:00:02 +0000] "POST /api/orders HTTP/1.1" 500 87 1.204
198.51.100.7 - - [16/Nov/2026:09:00:03 +0000] "GET /health HTTP/1.1" 200 2 0.001
# echo "level=INFO user=alice" | sed -E "s/user=[a-z]+/user=REDACTED/"
level=INFO user=REDACTED
```

Find old files, look first, then act:

```console
# find /var/log/app -name "*.log" -mtime +7
/var/log/app/old.log
# find /var/log/app -name "*.log" -mtime +7 -exec rm -v {} \;
removed '/var/log/app/old.log'
```

`-mtime +7` means modified more than 7 days ago. `-exec ... {} \;` runs the command once per file, with `{}` replaced by the name. Other useful tests: `-type f` (files only), `-size +100M`, `-user app`, `-maxdepth 1`.

## How it breaks

| Symptom | Layer | Check | Likely cause |
|---|---|---|---|
| `uniq -c` shows the same value several times | Input order | Was the input sorted? | `uniq` only merges adjacent lines |
| `sort` puts 10 before 9 | Sort type | Add `-n` | Text sort compares character by character |
| `cut` gives empty or wrong fields | Delimiter | `cat -A` shows tabs as `^I` and line ends as `$` | Several spaces in a row, or tabs; use `awk` |
| `grep` misses lines you can see | Pattern | Try `-F` for a fixed string, or `-i` | Special characters such as `.` or `[` treated as pattern syntax, or case differences |
| `sed -i` damaged a config file | In-place edit | Compare with a backup | The pattern matched more than intended; test without `-i` first |
| `find -exec rm` deleted the wrong files | Selection | Run the same `find` without `-exec` | The test was too broad, for example a missing `-name` or `-type f` |

## Interview questions

**1. How do you find the 5 IP addresses that made the most requests in an access log?**

<details markdown="1">
<summary>Answer</summary>

- Extract the field: `awk '{print $1}' access.log`.
- Sort so equal values are adjacent, then count: `sort` and then `uniq -c`.
- Sort the counts numerically, largest first, and take the top: `sort -rn` and then `head -5`.

</details>

**2. Why does `uniq` need sorted input?**

<details markdown="1">
<summary>Answer</summary>

- `uniq` only compares each line with the one before it.
- Equal values that are not next to each other are counted separately.
- Sorting first brings equal lines together; `sort -u` is an alternative when you only need distinct values.

</details>

**3. When would you use `awk` instead of `cut`?**

<details markdown="1">
<summary>Answer</summary>

- `cut` splits on one fixed character, so runs of spaces break it.
- `awk` splits on any whitespace by default and can test conditions, compute and sum.
- Use `cut` for simple, consistently delimited data such as CSV without quotes; `awk` for logs and anything with logic.

</details>

**4. How do you show 3 lines of context around every "Exception" in a log, case-insensitively?**

<details markdown="1">
<summary>Answer</summary>

- `grep -i -C 3 exception app.log`.
- `-A` and `-B` give lines after or before only.
- Add `-n` for line numbers.

</details>

**5. How do you replace a value in a config file safely with `sed`?**

<details markdown="1">
<summary>Answer</summary>

- Run the substitution without `-i` first and read the result.
- Anchor the pattern so it only matches the intended line, for example `s/^port=.*/port=8080/`.
- Use `-i.bak` to keep a copy, then compare with `diff`.

</details>

**6. A disk is filling with old logs. How do you find and delete logs older than 14 days under `/var/log/app` safely?**

<details markdown="1">
<summary>Answer</summary>

- List first: `find /var/log/app -type f -name "*.log" -mtime +14`.
- Check the list, then add `-delete` or `-exec rm {} \;`.
- Check that no process still holds them open; deleted open files keep using space ([Disks and filesystems](disks-and-filesystems.md)).
- The lasting fix is log rotation, not manual deletion.

</details>

**7. Using only the access log, how would you work out whether a spike of 502s came from one client or from everyone?**

<details markdown="1">
<summary>Answer</summary>

- Filter the 502 lines: `awk '$9 == 502'`.
- Count by client: print field 1, then `sort` and `uniq -c`.
- Count by path the same way, and by minute (part of field 4).
- One client points at that client; all clients on one path at one time points at the backend.

</details>

## Try it

**Step 1.** Start a throwaway container and make a small log.

```bash
docker run --rm -it ubuntu:24.04 bash
cd /tmp
printf '%s\n' \
 '203.0.113.10 GET /api/orders 200 0.041' \
 '203.0.113.11 GET /api/orders 500 1.204' \
 '203.0.113.10 GET /health 200 0.001' \
 '203.0.113.12 POST /api/orders 502 30.001' \
 '203.0.113.10 GET /api/orders 200 0.044' > app.log
```

**Step 2.** Before running each line, predict its output.

```bash
grep -c " 5[0-9][0-9] " app.log
awk '{print $1}' app.log | sort | uniq -c | sort -rn
awk '$4 >= 500 {e++} END {print e, "of", NR}' app.log
sort -k5 -rn app.log | head -1
```

**Step 3.** Type `exit`. The container is deleted.

## Zoom out

These tools are the first pass in almost every investigation, before metrics and dashboards: [Logs](logs.md) tells you where the text lives, and [jq and yq](jq-and-yq.md) do the same job for JSON and YAML. Without them you are scrolling. The principle to carry: build a pipeline one stage at a time, and look at the output after every stage.

## Sources

- [GNU grep manual](https://www.gnu.org/software/grep/manual/grep.html)
- [GNU sed manual](https://www.gnu.org/software/sed/manual/sed.html)
- [GNU awk (gawk) manual](https://www.gnu.org/software/gawk/manual/gawk.html)
- [GNU coreutils manual: sort, uniq, cut, wc, head, tail](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [GNU findutils manual](https://www.gnu.org/software/findutils/manual/html_mono/find.html)
- [regex(7) manual page](https://man7.org/linux/man-pages/man7/regex.7.html)
