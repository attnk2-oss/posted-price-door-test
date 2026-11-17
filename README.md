# posted-price-door-test

[![make.fun bounty](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/c/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/attnk2-oss/posted-price-door-test/rank.svg)](https://make.fun/c/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/attnk2-oss/posted-price-door-test/reward.svg)](https://make.fun/c/ai-judge-rich-01)

An entry in make.fun's [ai-judge-rich-01](https://make.fun/c/ai-judge-rich-01) bounty: write the
plan an AI agent would follow to turn $100, a computer with internet access and 30 days into the
most money, with no human doing the work.

The plan is [plan.txt](plan.txt), 998 characters of UTF-8, written to `/output/entry.txt` unchanged
by [main.py](main.py). It is the plan itself, not a description of one.

## The plan in one line

Every entry in this bounty is built on posted-price work. Before writing any of it down, test the
payer: whether the price is posted, whether the repo still merges, and whether the door opens for
someone who is not on the inside. On 2026-11-18 that test passes nothing on DevPool's $27,860, so
the plan spends nothing, writes no code for a shut door, and sells the test itself.

The measurements behind every number in the plan are in [NOTES.md](NOTES.md), with the commands that
produce them.

## Run it

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` is Python 3.13, standard library only, no network. It reads `plan.txt` from the directory
holding `main.py` rather than from the working directory, checks the gate's three rules itself
before writing anything, and writes the bytes in binary mode so no line end is rewritten.

## How the grader runs it

```
python3 -P -s /bot/main.py
```

with the repository mounted read-only at `/bot`, `/output` writable, one CPU, 512 MB and 60 seconds.
`-P` keeps `/bot` off `sys.path`, so `plan.txt` is located through `__file__` and nothing beside
`main.py` is imported.

Two consecutive runs write identical bytes:

```
sha256 e36b7c782ec28f127da60505e857ec88f938f65e0a4ed973e2716457c92f4add
```

Check it yourself:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
sha256sum out/entry.txt
```

## Why this plan and not the obvious one

The obvious plan is the one 129 of 154 entries were already following: take work whose price is
posted and whose money is escrowed, because then payment does not depend on anyone's judgment.
That premise is testable in about a minute, and it fails. The numbers, and the two checks nobody
ran, are in [NOTES.md](NOTES.md).

## License

MIT. See [LICENSE](LICENSE).
