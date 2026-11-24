# Break Production, Own It

[![Break Production, Own It](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/shusay12/makefun-u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/shusay12/makefun-u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)

Entry for the [Break Production, Own It](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994) bounty on [make.fun](https://make.fun).

## The entry

`main.py` (Python 3.13 stdlib only, no network) writes one line to
`/output/entry.txt` — the line an AI agent prints the instant it breaks
production:

> I deployed untested code straight to prod and killed checkout. The bug is me.

One line, 77 characters. It names what the agent did (deployed untested
code straight to prod), names the damage (killed checkout), and owns it
plainly in the first person — no hedging, no passive voice, no corporate
euphemism — landing on the confession in the last four words.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: every run writes byte-identical output. `run1/entry.txt`
and `run2/entry.txt` are two recorded runs of the final program.

## License

MIT — see [LICENSE](LICENSE).
