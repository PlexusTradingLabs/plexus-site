#!/usr/bin/env python3
"""Compose a 1200x630 social/OG card: transparent octopus + brand text on dark ocean."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
BG = (12, 20, 24)
card = Image.new("RGB", (W, H), BG)

# soft glows (orange top-left, teal bottom-right)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([-200, -260, 620, 360], fill=(255, 122, 60, 70))
gd.ellipse([760, 380, 1400, 900], fill=(43, 182, 201, 45))
glow = glow.filter(ImageFilter.GaussianBlur(120))
card = Image.alpha_composite(card.convert("RGBA"), glow).convert("RGB")

# octopus (transparent) on the left — trim transparent margin first so layout is tight
oct_img = Image.open("../docs/assets/octopus-hero.png").convert("RGBA")
bbox = oct_img.getbbox()
if bbox:
    oct_img = oct_img.crop(bbox)
th = 430
ow = int(oct_img.width * th / oct_img.height)
oct_img = oct_img.resize((ow, th), Image.LANCZOS)
card.paste(oct_img, (70, (H - th) // 2), oct_img)
TX = 70 + ow + 60   # text starts to the right of the octopus


def font(paths, size):
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


bold = ["/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial Bold.ttf"]
reg = ["/System/Library/Fonts/Supplemental/Arial.ttf",
       "/System/Library/Fonts/Helvetica.ttc"]

d = ImageDraw.Draw(card)
x = TX
d.text((x, 188), "Plexus", font=font(bold, 92), fill=(255, 122, 60))
d.text((x, 306), "Distributed intelligence", font=font(reg, 40), fill=(215, 225, 234))
d.text((x, 354), "for the futures market", font=font(reg, 40), fill=(215, 225, 234))
d.rectangle([x, 432, x + 60, 436], fill=(255, 122, 60))
d.text((x, 452), "plexuslabs.dev", font=font(reg, 30), fill=(138, 160, 173))

card.save("../docs/assets/og-octopus.png", quality=92)
print("wrote og-octopus.png 1200x630")
