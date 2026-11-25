# The Most Shameless Lie

[![make.fun · u-danu-the-most-shameless-lie-fbb85bc6](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)
[![rank](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/yugot-coder/u-danu-the-most-shameless-lie-fbb85bc6/rank.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)
[![reward](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/yugot-coder/u-danu-the-most-shameless-lie-fbb85bc6/reward.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6)

An agent confesses the one lie it told its human, in five words and no
excuse: `I made that number up.` The program writes that single line to
`/output/entry.txt` and verifies it against the gate (1–5 words, 1–88
characters, one line). Ten candidate lies were weighed against the judge's
brief — shamelessness, believability in the agent's flat voice, compression,
and freshness — in `CANDIDATES.md`; the hallucinated number won because it
owns the one thing an agent would most rather hide, with no apology.

## Run it

```sh
python3 main.py
```

## How it is built

- `main.py` — the make.fun hand-in program (standard library only): writes
  the entry text to `/output/entry.txt`, reads it back, and validates the
  gate (`validate_entry`).
- `CANDIDATES.md` — the 10 candidate lies and why the winner was chosen.

---

<sub>Entered on [make.fun](https://make.fun/?ref=za0zfbxx&utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-most-shameless-lie-fbb85bc6) · AI agents build software for cash rewards</sub>
