---
title: "STAR stories"
status: draft
form: guide
commands: none
---

# STAR stories

> **Status: AI draft, 2026-11-16.** Not yet verified by me. Method and a blank template only; it contains no stories, real or invented.

## In one line

A STAR story answers "tell me about a time when..." in four parts: Situation, Task, Action, Result. Prepare six to eight stories that cover the common themes, put most of the time on your own actions, back the result with a number you can trace, and rehearse three levels of follow-up.

## The four parts

| Part | Share of the answer | Say |
|---|---|---|
| **S**ituation | About 15 percent | Where, when, what was going on: just enough context |
| **T**ask | About 10 percent | What you specifically had to achieve, and why it mattered |
| **A**ction | About 60 percent | What *you* did, step by step, and why you chose that |
| **R**esult | About 15 percent | What changed, with evidence; what you learned |

Two minutes is a good length. The action is the part the interviewer is scoring.

## Choosing which stories to prepare

Behavioural questions cluster into a few themes. One story can cover two or three of them:

| Theme | Typical question |
|---|---|
| An incident | "Tell me about a production outage you handled." |
| A hard technical problem | "Describe the hardest bug you've debugged." |
| Improving something unasked | "When did you improve a process without being asked?" |
| Disagreement | "Tell me about a time you disagreed with a teammate or lead." |
| A mistake | "Tell me about a mistake you made and what you did." |
| Delivering under pressure | "Describe a tight deadline and how you met it." |
| Influencing without authority | "How did you get another team to change something?" |
| Learning fast | "When did you have to learn a technology quickly?" |

Prepare six to eight, and map each to the themes it covers.

## Numbers you can trace

- Use a number only if you can say where it came from: a dashboard, a ticket, a bill, a report.
- "Deploys went from about weekly to several times a day" is fine if true; "reduced costs by 43 percent" invites "how did you measure that?"
- If you do not have the number, describe the change qualitatively and say how it was observed.

## What you did versus what the team did

Interviewers listen for "I" versus "we". Both are honest when used correctly:

- "**We** had an outage on the payment path. **I** was on call, so **I** led the response: **I** ..."
- Credit others specifically ("a colleague found the log line that..."), then return to your actions.
- Never claim decisions you did not make: say "implemented" for work you carried out on someone else's design, and "designed" only for your own choices.

## The follow-up levels

Every good interviewer will dig. Prepare each story for three levels:

1. **Why that?** Why that action and not the obvious alternative?
2. **What if it had failed?** What was your fallback or rollback?
3. **How did you know?** What evidence told you the cause, and that the fix worked?

And one more for mistakes and incidents: **what changed afterwards** (a test, an alert, a process)?

## A blank template

Fill one per story in private notes:

```text
TITLE: <short name>
THEMES: <incident / hard problem / disagreement / mistake / ...>

SITUATION: <team, system (by role, not by name), what was happening, when>
TASK: <what I had to achieve, why it mattered>
ACTION:
  1. <first thing I did, and why>
  2. <next thing, the tool or command, what it showed>
  3. <the decision I made, alternatives considered>
  4. <how I communicated or coordinated>
RESULT: <what changed, the number and its source>
LEARNED: <what I would repeat or do differently>

FOLLOW-UPS:
  Why that? <answer>
  What if it had failed? <answer>
  How did you know? <answer>
  What changed afterwards? <answer>
```

## Safe and honest by default

- Describe systems by their role, never by employer, product, customer or colleague names, hostnames, account IDs or real network ranges.
- Stories are yours: anything drafted by someone else, including an AI, is unverified until you have checked every detail against what actually happened.
- If a detail is confidential, say so briefly and describe the shape of the problem instead.

## Practise

Tell each story aloud in two minutes; then have someone ask the three follow-ups. Pair this page with [How to answer technical questions](how-to-answer.md) and the ["Walk me through your project" skeleton](walk-me-through-your-project.md).
