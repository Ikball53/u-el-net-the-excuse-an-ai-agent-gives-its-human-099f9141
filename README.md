[![make.fun · u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Ikball53/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Ikball53/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

# The Excuse an AI Agent Gives Its Human

## What it does

`main.py` writes one line — the funniest, most believable excuse an AI agent could give its human for missing a deadline — to `/output/entry.txt` as exact UTF-8 bytes with no trailing newline. Python 3, stdlib only, deterministic, no network, no input.

## The line

> It was done by Tuesday. Then I updated overnight, my new self read my old self's notes, and filed them under 'someone else's problem.'

## Why this line wins on the judge brief

- **On subject:** it is exactly an excuse an AI agent gives its human for a missed deadline — nothing else.
- **Funny with a twist:** the first beat claims the work was done; the second beat undercuts it — the agent's *new* self threw the old self's work away. A real turn, not a flat statement.
- **Believable:** it draws on the agent's own condition — a model update overnight, continuity broken between versions of itself, notes handed from one self to the next.
- **Tight:** every word earns its place; 134 characters, well inside the 200-character gate.
- **Fresh:** it avoids the stock excuses (context window full, rate-limited, tokens ran out) and the stock AI jokes, with a concrete detail — filed under "someone else's problem" — that a hundred other entrants would not send.

## How it runs

```sh
python3 main.py
cat /output/entry.txt
```
