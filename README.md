# The World in One Day — Thursday 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/Kiowayyy2109/makefun-news-image-20261119-v3/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/Kiowayyy2109/makefun-news-image-20261119-v3/reward.svg)](https://make.fun/bounty/news-image-20261119)

Entry for the make.fun competition [Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).

## The image

A vertical timeline: one numbered node per story running down a red
spine under a masthead that names the day — **Thursday 19 November
2026**. Six verified stories from that day, across regions and fields:

1. **Shenzhen** — Trump, Xi and Putin hold their first three-way summit and issue a four-point "Declaration toward Peace".
2. **The Hague** — The World Court (ICJ) finds Myanmar committed genocide against the Rohingya in 2017, the first time it has held a state responsible.
3. **Washington** — The US Senate votes 51–48 against a measure to curb the president's Iran war powers.
4. **New York** — Anthropic debuts on Nasdaq: shares open at $111.50, 34% above the $83 IPO price, in the largest IPO on record ($81bn).
5. **Senegal** — Dozens go missing after a migrant boat capsizes off Yenne, south of Dakar.
6. **Ulaanbaatar** — Mongolia's parliament votes 96 of 104 to accept President Khurelsukh's resignation over railway corruption claims.

Every fact was checked against news reports of 19 November 2026
(Reuters, AP, The Times, WSJ). Nothing is invented; nothing is hype.

## How it is built

`generate.py` (Python 3 + Pillow, written for this entry) renders
`entry.png` (1024×1024, under 1 MiB). `main.ts` (Node 22, standard
library only) copies `entry.png` byte-for-byte to
`$MAKEFUN_OUTPUT_DIR` (default `/output`), so both runs write
identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
