---
title: "How to answer technical questions"
status: draft
form: guide
commands: none
---

# How to answer technical questions

> **Status: AI draft, 2026-11-16.** Not yet verified by me. Advice page; no commands.

## In one line

Lead with a one-sentence answer, then explain how it works from the parts up, name one trade-off, and give a concrete example. On scenarios, think aloud in a fixed order. Say "I don't know" with what you would check. Draw when there is more than one moving part, and be ready to go three "whys" deeper.

## A structure for "what is X?" and "how does X work?"

Use the same four beats every time, out loud:

1. **The one-line answer.** The sentence you would write under the title. Every page here starts with one (the "In one line" section). It shows you know the thing before you start explaining it.
2. **How it works.** Build it from parts the listener already knows: "A Service is a stable virtual IP plus a list of pod IPs that kube-proxy turns into forwarding rules on every node."
3. **A trade-off or limit.** "...which means it balances connections, not requests, so long-lived gRPC connections stick to one pod."
4. **An example.** From practice if you have one ("we saw that when..."), or a concrete scenario if you do not.

Stop after the four beats and let the interviewer steer. Two minutes is usually enough; they will ask for more if they want it.

## Thinking aloud on scenario questions

"The site is slow, what do you do?" is a test of method, not of guessing the answer.

- **Ask one clarifying question first**: since when, for whom, what changed? ([Scenario walk-throughs](scenario-walkthroughs.md))
- **Say the order you will check things in**, then walk it: the user's path from DNS to the database, one layer at a time ([The debugging walk](../start/debugging-walk.md)).
- **Name the command for each step**, and what a good and a bad result look like.
- **State your hypothesis** as you narrow down: "Latency is only on writes, so I'd look at the database next."
- **Mention the fix and the follow-up**: mitigate first (roll back, scale out), then root cause, then prevent recurrence.

## Saying "I don't know" well

Pretending is the expensive mistake: interviewers usually know the answer and will dig. A good "I don't know" has three parts:

1. Say it plainly: "I haven't used X directly."
2. Connect it to what you do know: "I'd expect it to work like Y, because..."
3. Say how you would find out: "I'd check the docs for the default, then test it in a kind cluster."

That answer shows reasoning and honesty, which is most of what the question was testing.

## Drawing while talking

When there are three or more moving parts (a request path, a pipeline, a failover), draw. Boxes for components, arrows for requests with their direction, labels for ports or protocols. Narrate as you draw, left to right in request order. Leave space: the follow-up is often "where would you put the cache?" ([System design on a whiteboard](system-design.md)).

## Depth ladders: three "whys" down

Interviewers probe until you run out. For each topic you list on your CV, prepare three levels:

| Level | Example question | Example answer depth |
|---|---|---|
| What | What does a readiness probe do? | Removes the pod from Service endpoints when it fails |
| How | How does that reach traffic? | The EndpointSlice controller marks the endpoint not ready; kube-proxy stops sending to it |
| Why or what if | What if readiness depends on the database? | One database blip removes every pod at once; check dependencies carefully |

The pages in these notes are written as these ladders: "In one line", then "How it works", then "How it breaks".

## Common traps

- **Answering a different question.** Repeat the question in your own words if unsure.
- **Listing tools instead of explaining.** "We used Prometheus, Grafana and Loki" says nothing about how you debug.
- **"We" for everything.** Say what you did yourself ([STAR stories](star-stories.md)).
- **Numbers you cannot back up.** Use only numbers you can trace to a source; say "roughly" or leave them out otherwise.
- **Going silent while thinking.** Say what you are considering, even if you then discard it.
- **Arguing with the premise.** If you disagree with a design, say why and offer the alternative, briefly.

## Practise

Pick three pages. For each, say the one-line answer out loud without looking, then the four beats, then answer its interview questions and score yourself 2, 1 or 0 against the hidden answers ([How to use these notes](../start/how-to-use.md)).
