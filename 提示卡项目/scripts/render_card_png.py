#!/usr/bin/env python3
"""Render a standalone card SVG through the project-local Kami pipeline.

The SVG remains the editable source. Kami is used only for deterministic
HTML-to-PDF rendering; the PDF is an intermediate and the script emits PNG.
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a card SVG to PNG with Kami")
    parser.add_argument("svg", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    svg = args.svg.resolve()
    output = args.output.resolve()
    if not svg.is_file():
        parser.error(f"SVG not found: {svg}")

    kami_scripts = (Path(__file__).resolve().parents[1] / ".agents/skills/kami/scripts").resolve()
    sys.path.insert(0, str(kami_scripts))
    try:
        try:
            import pymupdf as fitz  # type: ignore
        except ImportError:
            import fitz  # type: ignore
        from render import render_pdf  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "Kami dependencies are missing; run this script with the project .kami-venv Python"
        ) from exc

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="pic-helper-kami-") as temp_name:
        temp = Path(temp_name)
        html = temp / "card.html"
        pdf = temp / "card.pdf"
        html.write_text(
            """<!doctype html>
<html><head><meta charset="utf-8"><title>pic-helper card</title>
<style>
@page { size: 2520px 5472px; margin: 0; }
html, body { margin: 0; padding: 0; width: 2520px; height: 5472px; }
img { display: block; width: 2520px; height: 5472px; }
</style></head><body>
<img src="SVG_URI" alt="pic-helper card">
</body></html>
""".replace("SVG_URI", svg.as_uri()),
            encoding="utf-8",
        )
        pages = render_pdf(html, pdf)
        if pages != 1:
            raise SystemExit(f"expected one page, got {pages}")

        document = fitz.open(pdf)
        page = document[0]
        pixmap = page.get_pixmap(matrix=fitz.Matrix(96 / 72, 96 / 72), alpha=False)
        pixmap.save(output)
        document.close()

    with fitz.open(output) as rendered:
        page = rendered[0]
        width, height = page.rect.width, page.rect.height
    print(f"rendered {output} ({pixmap.width}x{pixmap.height}, source page {width:g}x{height:g}pt)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
