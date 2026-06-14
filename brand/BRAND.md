# Plexus Brand Kit

The visual identity for the open developer site (plexuslabs.dev). Anchored to the existing
PRISM operator-console palette so the website and the product feel like one system.

## The metaphor — an octopus 🐙

Distributed intelligence: not one head, but a living network reaching every arm.

| Name | Meaning | Visual |
|---|---|---|
| **Plexus** | the nervous system / network | node mesh; the hex + spokes mark |
| **PRISM** | the brain — refracts raw market light into a clear decision | prism / spectrum |
| **Axon** | the engine — carries the impulse out, fires the trade | a firing arm / signal |
| **Ammonite** | the earlier engine (retiring) | spiral fossil |

Two layers: the **hex + spokes mark** (technical / favicon / in-product) and the
**octopus** (marketing hero / story).

## Palette (from the console `:root`)

| Token | Hex | Use |
|---|---|---|
| bg | `#0f141b` | base background |
| panel | `#161d27` | surfaces / cards |
| line | `#263243` | borders |
| text | `#c9d4e3` | body |
| muted | `#7f8ea3` | secondary |
| **Plexus blue** | `#2f6dd0` | brand primary (network) |
| cyan | `#4a90e2` | accent |
| **Axon green** | `#3fb96b` | signal / "go" |
| **Ammonite amber** | `#d6a14a` | warm accent |
| **Rust red** | `#e0492b` | core spark |

Signature gradient (the "prism"): `#e0492b → #d6a14a → #3fb96b → #4a90e2 → #7c5cff`.

## Assets

- `docs/assets/plexus-mark.svg` — hex + spokes mark (logo + favicon).
- `docs/assets/octopus-mark.svg` — geometric octopus (concept / fallback).
- `docs/assets/octopus-hero.png` — generated hero art (Gemini; see `gen_image.py`).

## Generating imagery

```bash
set -a; . ../../.env; set +a          # GEMINI_API_KEY (never committed)
python gen_image.py --model gemini-3.1-flash-image \
  --out ../docs/assets/octopus-hero.png "<prompt>"
```

Use Gemini for raster hero/marketing art; keep logos/icons as hand-authored SVG.
