---
title: "\"Walk me through your project\": a skeleton"
status: draft
form: guide
commands: none
---

# "Walk me through your project": a skeleton

> **Status: AI draft, 2026-11-16.** Not yet verified by me. A blank structure to fill in privately; it deliberately contains no project details.

## In one line

Answer in five parts, in this order: context, architecture, your part, a hard problem, and the result. Keep it to about three minutes, then let the interviewer pick what to dig into, and have the follow-ups ready.

## The order to speak in

| Part | Time | Say |
|---|---|---|
| 1. Context | 20 seconds | What the business does, what the platform is for, its scale in numbers you can trace |
| 2. Architecture | 60 seconds | The request path and the delivery path, as you would draw them |
| 3. Your part | 40 seconds | What you owned, built or changed, separately from what the team did |
| 4. A hard problem | 40 seconds | One problem, how you found the cause, what you changed |
| 5. Result | 20 seconds | What improved, with a number you can back up, and what you would do differently |

## The fill-in template

Copy this into private notes and replace each placeholder. Keep the filled version out of anything public: it will contain details about a former employer.

```text
CONTEXT
The company does <one-line business description>.
I worked on <platform role, e.g. "the platform that runs customer workflows">,
used by <who> at about <scale, with a source>.

ARCHITECTURE (request path)
Users reach it through <DNS / CDN / load balancer>,
which sends traffic to <compute: EKS / ECS / Lambda / EC2>
in <how many> zones. State lives in <databases, caches, queues, object storage>.

ARCHITECTURE (delivery path)
Code goes from <repository> through <CI tool> (<tests, scans, build>)
to <registry>, and is deployed by <CD tool / GitOps> to <environments>.
Infrastructure is defined in <IaC tool>.
We observe it with <metrics, logs, traces tools>.

MY PART
I was responsible for <area>.
I built / changed <specific thing>, which involved <two or three concrete steps>.
The team handled <what others did>, and I <how you worked with them>.

A HARD PROBLEM
<Symptom users or the team saw>.
I narrowed it down by <steps and tools>.
The cause was <root cause>.
I fixed it by <change>, and prevented recurrence with <alert / test / guardrail>.

RESULT
<Metric> went from <before> to <after>, measured by <where the number comes from>.
If I did it again, I would <one improvement>.
```

## A typical day, if they ask

```text
Mornings: <alerts and on-call review, pull request reviews>.
Most of the day: <project work, e.g. infrastructure changes through IaC and pull requests>.
Regularly: <supporting developers with deploys, debugging, access requests>.
On-call: <rotation, what pages you, how incidents are run>.
```

## Follow-up questions to prepare for

Write a two-sentence answer for each, from your own notes:

- Why was it designed that way? What were the alternatives?
- What would you change if you rebuilt it today?
- What broke most often, and why?
- How did you deploy changes safely? How did you roll back?
- How was access controlled? Where did secrets live?
- How did you know it was healthy? Which alerts woke people up?
- What did it cost, and what drove the cost?
- What did you personally build, versus inherit?
- What was the biggest incident, and what changed afterwards?
- Draw the request path from the user to the database.

## Rules that keep the answer honest and safe

- **"I" for your work, "we" for the team's.** Interviewers listen for the difference ([STAR stories](star-stories.md)).
- **Numbers you can trace.** If you cannot say where a number came from, say "roughly" or leave it out.
- **Describe by role, not by name.** "A workflow platform for enterprise customers", not product, customer or colleague names, hostnames, account IDs or real network ranges.
- **Implemented versus designed.** Say "designed" only for decisions you made.
- **Short first.** Three minutes, then stop and invite questions: "Which part would you like me to go deeper on?"

## Practise

Say it aloud with a timer, record it once, and listen for "we" where you meant "I", vague numbers, and jargon you did not explain. Then answer three follow-ups from the list without notes ([How to answer technical questions](how-to-answer.md), [System design on a whiteboard](system-design.md)).
