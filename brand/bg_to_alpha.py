#!/usr/bin/env python3
"""Bake a dark/near-black background into the alpha channel → true transparent PNG.

For a bright subject on a dark background (our glowing octopus), alpha is derived
from per-pixel brightness: dark bg → transparent, bright subject + glow → opaque.
Keeps the soft glow so it blends on any background.

Usage: python bg_to_alpha.py in.png out.png [lo] [hi]
"""
import sys
import numpy as np
from PIL import Image

src = sys.argv[1]
dst = sys.argv[2]
lo = float(sys.argv[3]) if len(sys.argv) > 3 else 24.0
hi = float(sys.argv[4]) if len(sys.argv) > 4 else 82.0

rgb = np.asarray(Image.open(src).convert("RGB")).astype(np.float32)
m = rgb.max(axis=2)                                  # brightest channel per pixel
alpha = np.clip((m - lo) / (hi - lo), 0.0, 1.0) ** 0.85
out = np.dstack([rgb, alpha * 255.0]).astype(np.uint8)
Image.fromarray(out, "RGBA").save(dst)

print(f"wrote {dst} — {(alpha < 0.04).mean()*100:.0f}% transparent, "
      f"{(alpha > 0.96).mean()*100:.0f}% opaque")
