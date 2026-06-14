# plexus-site

The open Plexus developer website → **plexuslabs.dev**. Built with MkDocs Material
(Markdown source → static HTML/CSS/JS, served by GitHub Pages).

## Run locally

```bash
pip install -r requirements.txt
mkdocs serve            # http://127.0.0.1:8000
```

## Build

```bash
mkdocs build            # → site/
```

## Structure

- `docs/` — the pages (Markdown; compiled to HTML at build).
- `docs/assets/` — logos + generated hero art (SVG + PNG).
- `docs/stylesheets/extra.css` — the brand palette + hero/card styling.
- `brand/` — `BRAND.md` + `gen_image.py` (Gemini hero generation).
- `.github/workflows/deploy.yml` — build + deploy to Pages on push.

The full protocol spec (`PROTOCOL.md`) is pulled from `plexus-protocol` at build time
(Phase 2 docs aggregation). Deep API reference is generated per open repo into `/reference/`.
