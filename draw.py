# draw.py — draws entry.png for news-image-20261118.
# One image summing up the world news of Wednesday 18 November 2026.
# Flat vector style, drawn procedurally with PIL. Deterministic: no random
# numbers, no timestamps, no network. Output is 1024x1024.
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (20, 33, 61)
PAPER = (247, 242, 231)
RED = (178, 34, 34)
DARK = (30, 30, 30)
SKY = (127, 178, 229)

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(d, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def center_text(d, cx, y, text, fnt, fill):
    d.text((cx, y), text, font=fnt, fill=fill, anchor="ma")

def gradient(d, box, top, bottom):
    x0, y0, x1, y1 = box
    for y in range(y0, y1):
        t = (y - y0) / max(1, y1 - y0)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(x0, y), (x1, y)], fill=c)

def star(d, cx, cy, r, fill):
    import math
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=fill)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- outer border ----
d.rectangle([4, 4, W - 5, H - 5], outline=NAVY, width=6)

# ---- masthead ----
d.rectangle([16, 16, W - 17, 104], fill=NAVY)
d.text((32, 30), "THE WORLD TODAY", font=font(BOLD, 58), fill=(255, 255, 255))
d.text((W - 32, 34), "18 NOV 2026", font=font(BOLD, 44), fill=(255, 214, 90), anchor="ra")

# ---- date band ----
d.rectangle([16, 104, W - 17, 140], fill=RED)
center_text(d, W // 2, 110, "WEDNESDAY, 18 NOVEMBER 2026", font(BOLD, 26), (255, 255, 255))

# ================= HERO: Trump lands in Manila =================
hx0, hy0, hx1, hy1 = 16, 152, W - 17, 440
gradient(d, (hx0, hy0, hx1, hy1), (232, 131, 58), (249, 232, 201))
# sun
d.ellipse([hx1 - 190, hy0 + 26, hx1 - 90, hy0 + 126], fill=(255, 240, 180))
# skyline silhouettes
buildings = [(30, 120), (90, 180), (150, 100), (220, 160), (300, 90),
             (370, 150), (450, 110), (520, 170), (600, 95), (680, 150),
             (750, 105), (830, 165), (900, 120)]
bx = hx0 + 8
for bw, bh in buildings:
    d.rectangle([bx, hy1 - bh, bx + bw - 12, hy1], fill=(38, 52, 86))
    bx += bw
# airplane silhouette (dark navy jet, nose to the right), clean side profile
d.polygon([(280, 246), (600, 240), (644, 248), (600, 256), (280, 254)], fill=NAVY)
d.polygon([(380, 252), (470, 252), (512, 302), (428, 302)], fill=NAVY)
d.polygon([(298, 246), (330, 198), (362, 198), (350, 246)], fill=NAVY)
d.polygon([(288, 250), (322, 274), (342, 274), (320, 250)], fill=NAVY)
# location chip, sized to its text
chip_text = "MANILA, PHILIPPINES"
chip_w = int(d.textlength(chip_text, font=font(BOLD, 22))) + 28
d.rectangle([hx0 + 16, hy1 - 52, hx0 + 16 + chip_w, hy1 - 14], fill=NAVY)
d.text((hx0 + 30, hy1 - 46), chip_text, font=font(BOLD, 22), fill=(255, 255, 255))

# hero headline block
d.text((32, 452), "TRUMP LANDS IN MANILA", font=font(BOLD, 52), fill=NAVY)
d.text((32, 512), "Quad talks open as Asia's summits begin",
       font=font(REG, 28), fill=DARK)
# Quad flags row (right of subline): four small flags
fx, fy = 700, 505
def flag_us(x, y, w=52, h=34):
    for i in range(7):
        d.rectangle([x, y + i * (h // 7), x + w, y + (i + 1) * (h // 7)],
                    fill=(178, 34, 52) if i % 2 == 0 else (255, 255, 255))
    d.rectangle([x, y, x + w * 2 // 5, y + h * 4 // 7], fill=(20, 40, 90))
def flag_jp(x, y, w=52, h=34):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255), outline=DARK, width=1)
    d.ellipse([x + w // 2 - 9, y + h // 2 - 9, x + w // 2 + 9, y + h // 2 + 9],
              fill=(188, 0, 45))
def flag_in(x, y, w=52, h=34):
    d.rectangle([x, y, x + w, y + h // 3], fill=(255, 153, 51))
    d.rectangle([x, y + h // 3, x + w, y + 2 * h // 3], fill=(255, 255, 255))
    d.rectangle([x, y + 2 * h // 3, x + w, y + h], fill=(19, 136, 8))
    d.ellipse([x + w // 2 - 6, y + h // 2 - 6, x + w // 2 + 6, y + h // 2 + 6],
              outline=(0, 0, 128), width=2)
def flag_au(x, y, w=52, h=34):
    d.rectangle([x, y, x + w, y + h], fill=(0, 40, 104))
    star(d, x + w - 12, y + 10, 5, (255, 255, 255))
    star(d, x + w - 26, y + 22, 4, (255, 255, 255))
    star(d, x + 12, y + 24, 4, (255, 255, 255))
flag_us(fx, fy)
flag_jp(fx + 64, fy)
flag_in(fx + 128, fy)
flag_au(fx + 192, fy)
d.text((fx, fy + 42), "THE QUAD", font=font(BOLD, 18), fill=DARK)

# divider
d.line([(16, 572), (W - 17, 572)], fill=NAVY, width=3)

# ================= THREE PANELS =================
panels = [
    (16, "bridge"),
    (352, "radar"),
    (688, "trade"),
]
for px0, kind in panels:
    px1 = px0 + 320
    # picture area
    if kind == "bridge":
        gradient(d, (px0, 584, px1, 750), (188, 216, 240), (220, 235, 245))
        # sea
        d.rectangle([px0, 700, px1, 750], fill=(46, 109, 164))
        # bridge towers and deck
        d.line([(px0, 712), (px1, 712)], fill=(60, 60, 60), width=6)
        for tx in (px0 + 70, px0 + 230):
            d.rectangle([tx - 6, 640, tx + 6, 712], fill=(60, 60, 60))
            d.line([(tx, 640), (px0 + 10, 712)], fill=(90, 90, 90), width=2)
            d.line([(tx, 640), (px1 - 10, 712)], fill=(90, 90, 90), width=2)
        # explosion burst on the deck
        star(d, px0 + 160, 690, 46, (255, 170, 0))
        star(d, px0 + 160, 690, 28, (255, 220, 80))
        d.ellipse([px0 + 120, 640, px0 + 160, 676], fill=(120, 120, 120))
        d.ellipse([px0 + 168, 632, px0 + 204, 668], fill=(150, 150, 150))
        # caption
        d.text((px0 + 8, 762), "UKRAINE HITS", font=font(BOLD, 30), fill=NAVY)
        d.text((px0 + 8, 796), "CRIMEA BRIDGE", font=font(BOLD, 30), fill=NAVY)
        d.text((px0 + 8, 836), "Second strike in two days",
               font=font(REG, 21), fill=DARK)
    elif kind == "radar":
        d.rectangle([px0, 584, px1, 750], fill=(28, 43, 74))
        for sx, sy in [(40, 40), (120, 26), (200, 48), (270, 30)]:
            star(d, px0 + sx, 584 + sy, 3, (255, 255, 255))
        # radar dish on a mast: upper half-ellipse arc, feed arm, mast
        d.ellipse([px0 + 95, 612, px0 + 225, 702], outline=(220, 220, 220), width=5)
        d.rectangle([px0 + 85, 656, px0 + 235, 752], fill=(28, 43, 74))
        d.rectangle([px0 + 152, 656, px0 + 168, 750], fill=(200, 200, 200))
        d.line([(px0 + 160, 656), (px0 + 238, 606)], fill=(255, 214, 90), width=4)
        # drone silhouette, top right
        d.rectangle([px0 + 238, 612, px0 + 292, 628], fill=(10, 10, 10))
        for rx in (238, 292):
            d.line([(px0 + rx - 16, 606), (px0 + rx + 16, 606)], fill=(10, 10, 10), width=4)
        d.line([(px0 + 252, 628), (px0 + 246, 640)], fill=(10, 10, 10), width=3)
        d.line([(px0 + 278, 628), (px0 + 284, 640)], fill=(10, 10, 10), width=3)
        d.text((px0 + 8, 762), "IRAN DRONES HIT", font=font(BOLD, 30), fill=NAVY)
        d.text((px0 + 8, 796), "US RADAR", font=font(BOLD, 30), fill=NAVY)
        d.text((px0 + 8, 836), "Strike on base in Bahrain",
               font=font(REG, 21), fill=DARK)
    else:  # trade
        d.rectangle([px0, 584, px1, 750], fill=(240, 230, 210))
        # Canada flag
        d.rectangle([px0 + 30, 610, px0 + 58, 664], fill=(255, 0, 0))
        d.rectangle([px0 + 58, 610, px0 + 114, 664], fill=(255, 255, 255))
        d.rectangle([px0 + 114, 610, px0 + 142, 664], fill=(255, 0, 0))
        d.polygon([(px0 + 86, 622), (px0 + 96, 640), (px0 + 92, 640),
                   (px0 + 98, 652), (px0 + 86, 646), (px0 + 74, 652),
                   (px0 + 80, 640), (px0 + 76, 640)], fill=(255, 0, 0))
        # China flag
        d.rectangle([px0 + 178, 610, px0 + 290, 664], fill=(222, 41, 16))
        star(d, px0 + 198, 628, 10, (255, 222, 0))
        star(d, px0 + 226, 620, 5, (255, 222, 0))
        star(d, px0 + 236, 634, 5, (255, 222, 0))
        # rising arrow
        d.line([(px0 + 40, 730), (px0 + 140, 690), (px0 + 210, 706),
                (px0 + 290, 660)], fill=(19, 136, 8), width=8)
        d.polygon([(px0 + 290, 660), (px0 + 262, 660), (px0 + 290, 688)],
                  fill=(19, 136, 8))
        d.text((px0 + 8, 762), "XI MEETS CARNEY", font=font(BOLD, 30), fill=NAVY)
        d.text((px0 + 8, 796), "TRADE DEALS", font=font(BOLD, 30), fill=NAVY)
        d.text((px0 + 8, 836), "Canada-China deals extended",
               font=font(REG, 21), fill=DARK)

# ---- footer: also today ----
d.line([(16, 892), (W - 17, 892)], fill=NAVY, width=3)
d.text((32, 906), "ALSO TODAY", font=font(BOLD, 22), fill=RED)
foot = ("UK sanctions Israeli settlement firms  •  Cyclone Akvan "
        "strengthens over the Bay of Bengal  •  Dhoni retires from the IPL")
for i, line in enumerate(wrap(d, foot, font(REG, 21), W - 64)):
    d.text((32, 936 + i * 28), line, font=font(REG, 21), fill=DARK)
center_text(d, W // 2, 988, "THE WORLD TODAY  •  18 NOVEMBER 2026",
            font(BOLD, 18), (120, 120, 120))

img.save("entry.png", "PNG")
print("saved entry.png", img.size)
