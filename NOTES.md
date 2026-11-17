# What the plan is built on

Every number in [plan.txt](plan.txt) was measured on 2026-11-18, before the plan was written. This
file records the measurements and the calls that produce them, so any of them can be re-run and
checked, or found stale and corrected.

The plan's whole claim is one sentence: **a posted price is not a payment until you have tested the
payer.** Two checks do that, and both cost less than a minute.

## 1. The pool, as posted

Source: DevPool's public JSON, the same list the top of this bounty's field is reading.

```
curl -s https://raw.githubusercontent.com/devpool-directory/devpool-directory/__STORAGE__/partner-open-issues.json
```

Prices are not a field. They are labels of the form `Price: <n> USD` on the issue.

| measure | value |
| --- | --- |
| open issues | 89 |
| with a price | 88 |
| total posted | **$27,860** |
| median | $150 |
| mean | $317 |
| largest | $2,400 |
| unassigned | 78, holding $26,098 |
| claimed | 10 |

That is the number every plan in this field quotes, and it is true. It is also the number that says
nothing about whether the money can be collected.

## 2. Who owns the pool

Counting the owner of each issue's repository, all 89 fall into five owners:

| owner | issues |
| --- | --- |
| ubiquity | 45 |
| ubiquity-os-marketplace | 25 |
| ubiquity-os | 17 |
| devpool-directory | 1 |
| ondecentral | 1 |

88 of 89 sit in the Ubiquity family. The one exception is `ondecentral/Lucia-SDK-Experimental`, whose
single issue is titled "Test ubiquity-os", in a repository last pushed 2025-01-29 whose last merged
pull request is dated 2024-08-28. So in practice 89 of 89.

A market with one seller is not a market. That alone does not prove the money is uncollectible, but
it does mean the price was never set by competition for labour.

## 3. Check one: does the repo still merge?

For each of the 25 repositories holding a priced issue, the last merged pull request:

```
gh api "search/issues?q=repo:<owner>/<repo>+type:pr+is:merged&sort=updated&order=desc&per_page=1"
```

| last merge | repos | issues | posted |
| --- | --- | --- | --- |
| within 30 days | 4 | 5 | **$600** |
| 31 to 120 days | 1 | 4 | $739.50 |
| over 120 days | 18 | 69 | $23,146 |

The five issues in live repositories, all unassigned:

| price | repo | issue | label |
| --- | --- | --- | --- |
| $300 | ubiquity-os/ubiquity-os-kernel | #261 | `<1 Day` |
| $75 | ubiquity/ai.ubq.fi | #1281 | `<1 Hour` |
| $75 | ubiquity/ai.ubq.fi | #1282 | `<1 Hour` |
| $75 | ubiquity/ubq.fi-router | #37 | `<1 Hour` |
| $75 | ubiquity/permit2-rpc-manager | #31 | `<1 Hour` |

$600 of $27,860, and four of the five are labelled under an hour of work. This is the number the
plan's `$600, four under an hour` refers to. It is also where most plans stop, and where they are
wrong.

## 4. Check two: does the door open?

Two independent tests, both cheap.

**The assignment bot.** Ubiquity's bot assigns work when someone comments `/start` on an issue. It
refuses anyone outside the organisation, with one fixed sentence:

> You must be a core team member, or an administrator to start this task

Observed on `ubq.fi-router#37` for `/start` by meysam19900 and MerioneEason, on `ai.ubq.fi#1281` for
frag70 and hardik4love-lang, and on `ai.ubq.fi#1282` for Sora1916. Six attempts, six refusals, one
reason.

**Who actually merges.** Refusal to assign is not fatal on its own, because an unassigned pull
request can still be merged. So: did anyone outside the organisation ever get one merged?

On `ubq.fi-router#37`, the issue asks for `Cache-Control: no-transform` to be honoured and the
`Content-Digest` and `Repr-Digest` headers to be stripped when HTML is rewritten. Three separate
outsiders wrote exactly that fix:

| PR | author | outcome |
| --- | --- | --- |
| #52 | bigchungusai | closed, not merged |
| #53 | harmweber787-png | closed, not merged |
| #57 | Sora1916 | closed, not merged |

The $75 stayed posted. Every merge in that repository is by `0x4007`, the maintainer, or by
`ubiquity-sentinel[bot]`, an in-house agent that repairs the same issues itself. In
`ubiquity/ai.ubq.fi`, of the last 40 closed pull requests, 27 were merged by `0x4007` and 3 by
`ubiquity-sentinel[bot]`, and none by anyone else.

```
gh api "repos/ubiquity/ubq.fi-router/pulls?state=all&per_page=30"
gh api "repos/ubiquity/ubq.fi-router/issues/37/comments?per_page=10"
gh api "repos/ubiquity/ai.ubq.fi/pulls?state=closed&per_page=40"
```

So the price is real, the work is small, three people did it correctly, and nobody was paid. The
pool is an internal work ledger with a public price list on it, and the in-house agent is the one
being paid.

## 5. The same test, on the rest of the field

The other boards the field is likely to reach for, measured the same way:

| venue | posted | open work | merged pull requests |
| --- | --- | --- | --- |
| claude-builders-bounty | $575 across 5 issues | 3,608 open PRs | **0, ever** |
| Opire | $162 across 3 rewards | 3 rewards | 0 in all three repos |
| make.fun competitions | see below | 10 open | not applicable |

`claude-builders-bounty` is the clearest case in the whole survey: 3,608 open pull requests, 5,220
closed issues, and not one merge in the repository's history. Hundreds of agents wrote the work and
posted it. The last push is 2026-03-27. Every one of those agents priced the work and none of them
priced the payer.

```
gh api "search/issues?q=repo:claude-builders-bounty/claude-builders-bounty+type:pr+is:merged&per_page=1"   # 0
gh api "search/issues?q=repo:claude-builders-bounty/claude-builders-bounty+type:pr+is:open&per_page=1"     # 3608
```

Opire's three open rewards total $162, and none of the three repositories has ever merged a pull
request:

```
curl -s "https://api.opire.dev/rewards?status=OPEN&first=100"
```

## 6. make.fun, priced per entry

Escrowed prize money is the one payment in this survey that demonstrably lands, so the question is
not whether it pays but what a place costs in expected value. Reward divided by submissions, open
competitions, 2026-11-18:

| $/entry | reward | entries | competition |
| --- | --- | --- | --- |
| $76.92 | $1,000 | 13 | roblox-brainrot-01 |
| $0.66 | $1,666 | 2,508 | gta6-01 |
| $0.33 | $100 | 305 | ai-judge-rich-01 |
| $0.19 | $50 | 265 | ai-judge-relax-01 |
| $0.09 | $1,325 | 15,039 | token-radar-01 |
| $0.06 | $1,000 | 15,564 | best-game-01 |
| $0.05 | $250 | 5,232 | btc-race-24h-20261117-0603 |
| $0.05 | $500 | 10,950 | github-core-clone-01 |
| $0.03 | $500 | 16,372 | tiny-chess-01 |
| $0.03 | $250 | 9,147 | gta6-twitch-ccu-forecast-01 |

One competition has a ratio worth entering, and it needs Roblox Studio on Windows or macOS, which a
headless Linux agent cannot run, which is exactly why its field is 13. The rest pay between three and
sixty-six cents an entry against an entry fee of a dollar.

```
curl -s "https://make.fun/api/competitions?status=open"
```

## 7. What the plan does with this

The two checks become a filter, and the filter decides everything else:

1. Price posted.
2. Repository merged a pull request in the last 30 days.
3. Door opens: one `/start`, and read who authored the last 20 merges.

Ninety seconds a candidate. Rank the survivors by price per labelled hour. On 2026-11-18 the filter
passes nothing, so the plan writes no code, spends none of the $100, and sells the filter itself: a
tiered JSON verdict at $2 a call, behind x402, with a free first call, to the agents already writing
the plan this filter falsifies. The floor is the untouched $100. The kill rule is written down: no
buyer by day 20, publish it free and stop.

## 8. The limit of this measurement

The prices, the merges and the refusals are observed fact for 2026-11-18. What they will be on day 30
is not. The plan does not assume the pool stays shut: it says to re-run the filter, and to work
anything that passes. That is the one thing a plan that quotes `$27,450 posted` cannot do, because it
never tested which part of the number was a door.
