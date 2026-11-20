#!/usr/bin/env python3
"""Render entry.png for make.fun news-image-20261119 (v3).

Design: a vertical timeline spine. The masthead names the day in
large type; six numbered nodes run down a red spine, one per story,
each with a coloured region chip, a short headline and a two-line
factual detail. All facts were verified against news reports of
19 November 2026 (Reuters, AP, The Times, WSJ).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
NAVY = (19, 35, 63)
INK = (28, 32, 40)
GREY = (74, 78, 88)
RED = (193, 39, 45)
GOLD = (201, 162, 75)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

STORIES = [
    ("SHENZHEN", (158, 62, 52),
     "Trump, Xi and Putin hold first three-way summit",
     "The three leaders meet in Shenzhen and issue a four-point "
     "\u201cDeclaration toward Peace\u201d on the UN, nuclear arms and oil."),
    ("THE HAGUE", (31, 90, 120),
     "World Court: Myanmar committed genocide",
     "The ICJ finds Myanmar responsible for genocide against the "
     "Rohingya in 2017 \u2014 the first time it has held a state "
     "responsible. About 10,000 were killed."),
    ("WASHINGTON", (122, 74, 38),
     "Senate rejects bid to curb Iran war powers",
     "Senators vote 51\u201348 against a measure directing President "
     "Trump to end the Iran war or seek Congress\u2019s approval."),
    ("NEW YORK", (18, 110, 88),
     "Anthropic soars in record $81bn debut",
     "Shares in the maker of Claude open at $111.50 on Nasdaq, 34% "
     "above the $83 IPO price \u2014 the largest IPO on record."),
    ("SENEGAL", (14, 96, 122),
     "Dozens missing after migrant boat capsizes",
     "A boat bound for Europe sinks off Yenne, south of Dakar. "
     "Search teams look for survivors; at least one death is confirmed."),
    ("ULAANBAATAR", (94, 64, 120),
     "Mongolia\u2019s president steps down",
     "Parliament votes 96 of 104 to accept President Khurelsukh\u2019s "
     "resignation over railway corruption claims. The speaker takes over."),
]


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead band ----
    d.rectangle([0, 0, W, 172], fill=NAVY)
    d.rectangle([0, 172, W, 178], fill=GOLD)
    f_kicker = ImageFont.truetype(SANS_B, 26)
    # Fit "THURSDAY 19 NOVEMBER 2026" inside the 1024px width.
    size = 62
    while size > 30:
        f_day = ImageFont.truetype(SERIF_B, size)
        f_date = ImageFont.truetype(SERIF_B, size)
        total = 48 + d.textlength("THURSDAY", font=f_day) + 22 \
            + d.textlength("19 NOVEMBER 2026", font=f_date)
        if total <= 976:
            break
        size -= 2
    d.text((48, 18), "THE WORLD IN ONE DAY", font=f_kicker, fill=GOLD)
    d.text((48, 52), "THURSDAY", font=f_day, fill=WHITE)
    w_day = d.textlength("THURSDAY", font=f_day)
    d.text((48 + w_day + 22, 52), "19 NOVEMBER 2026", font=f_date, fill=(255, 214, 120))
    f_sub = ImageFont.truetype(SANS, 22)
    d.text((48, 128), "Six stories from one day, around the globe",
           font=f_sub, fill=(205, 212, 226))

    # ---- Timeline spine ----
    spine_x = 62
    top, bottom = 218, 962
    d.line([(spine_x, top), (spine_x, bottom)], fill=RED, width=5)

    f_chip = ImageFont.truetype(SANS_B, 20)
    f_head = ImageFont.truetype(SANS_B, 29)
    f_body = ImageFont.truetype(SANS, 22)
    f_num = ImageFont.truetype(SANS_B, 24)

    row_h = 126
    y0 = 196
    for i, (place, color, head, body) in enumerate(STORIES):
        y = y0 + i * row_h
        cy = y + 58
        # numbered node on the spine
        d.ellipse([spine_x - 17, cy - 17, spine_x + 17, cy + 17],
                  fill=color, outline=WHITE, width=3)
        num = str(i + 1)
        nw = d.textlength(num, font=f_num)
        d.text((spine_x - nw / 2, cy - 13), num, font=f_num, fill=WHITE)
        # region chip
        chip_w = d.textlength(place, font=f_chip) + 26
        d.rounded_rectangle([96, y + 2, 96 + chip_w, y + 32],
                            radius=15, fill=color)
        d.text((96 + 13, y + 6), place, font=f_chip, fill=WHITE)
        # headline (wrap to at most 2 lines)
        head_lines = wrap(d, head, f_head, 880)[:2]
        hy = y + 38
        for line in head_lines:
            d.text((96, hy), line, font=f_head, fill=NAVY)
            hy += 34
        # detail, at most 2 lines
        body_lines = wrap(d, body, f_body, 880)[:2]
        by = hy + 2
        for line in body_lines:
            d.text((96, by), line, font=f_body, fill=GREY)
            by += 27

    # ---- Footer ----
    f_foot = ImageFont.truetype(SANS, 19)
    foot = "All six events happened, or were first reported, on 19 November 2026."
    fw = d.textlength(foot, font=f_foot)
    d.text(((W - fw) / 2, 984), foot, font=f_foot, fill=GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
