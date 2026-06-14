#!/usr/bin/env python3
"""Generate brand imagery via the Gemini image API.

Reads GEMINI_API_KEY from the environment (kept in the workspace .env, never committed).
Uses the Gemini *-image models (generateContent + IMAGE modality). No extra deps.

Usage:
    python gen_image.py --model gemini-3.1-flash-image \
        --out ../docs/assets/octopus-hero.png "a prompt..."
"""
import argparse
import base64
import json
import os
import sys
import urllib.request

API = "https://generativelanguage.googleapis.com/v1beta/models"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt")
    ap.add_argument("--model", default="gemini-3.1-flash-image")
    ap.add_argument("--out", default="out.png")
    a = ap.parse_args()

    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("GEMINI_API_KEY not set (source the workspace .env)")

    body = {
        "contents": [{"parts": [{"text": a.prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }
    req = urllib.request.Request(
        f"{API}/{a.model}:generateContent?key={key}",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            resp = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:600]}")

    for part in resp.get("candidates", [{}])[0].get("content", {}).get("parts", []):
        data = part.get("inlineData") or part.get("inline_data")
        if data and data.get("data"):
            with open(a.out, "wb") as f:
                f.write(base64.b64decode(data["data"]))
            print(f"wrote {a.out}")
            return
    sys.exit("no image in response: " + json.dumps(resp)[:600])


if __name__ == "__main__":
    main()
