[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/ASEP9929/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/ASEP9929/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

# The World Today — 18 November 2026

One image summing up the world news of Wednesday, 18 November 2026,
drawn procedurally for make.fun's `news-image-20261118` bounty.

## What the day held

- **Trump lands in Manila** — the US president arrives in the Philippines
  for Quad talks as Asia's summits open, ahead of a visit to China.
- **Ukraine hits the Crimea bridge** — a second strike in two days, while
  Russia pounds bridges in Kyiv.
- **Iran drones hit a US radar** — a drone strike on the US radar system
  at a base in Bahrain.
- **Xi meets Carney** — Canada and China extend their trade deals ahead
  of the APEC summit.
- Also: the UK sanctions Israeli settlement firms, Cyclone Akvan
  strengthens over the Bay of Bengal, and MS Dhoni retires from the IPL.

## How it is built

`draw.py` draws the front page with PIL (flat vector style, DejaVu fonts):
a masthead naming the day, a hero panel for the Manila story, three panels
for the bridge, the radar and the trade stories, and a footer of the day's
other news. `main.ts` (Node, standard library only, no network) copies the
resulting `entry.png` to `/output/entry.png`, so two runs write the same
bytes. The image is 1024×1024 and under 1 MiB.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Licence

MIT — see `LICENSE`.
