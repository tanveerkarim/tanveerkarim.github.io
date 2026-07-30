#!/usr/bin/env python3
"""Port a self-contained Plotly HTML export into a web-ready page.

The figures produced by the cosmo-elpd pipeline are full HTML documents sized
for a desktop notebook: the Plotly layout carries explicit `width`/`height`, so
`responsive: true` in the config is inert (Plotly only stretches to 100% when
`layout.width` is unset). They also lack a viewport meta tag, so mobile
browsers lay them out at desktop width and then zoom out to fit.

This script rewrites such an export in place-safe fashion:

  1. adds a viewport meta tag,
  2. drops `layout.width`/`layout.height` in favour of `autosize: true`,
  3. swaps the fixed-pixel wrapper for a fluid one that keeps a legible floor
     width and scrolls horizontally below it,
  4. injects a small site header so the page stands on its own when linked.

Usage:
    python3 scripts/port-interactive-figure.py SOURCE.html DEST.html \
        [--floor 900] [--height 1290] [--title "..."] [--home-url /teaching/elpd/]

Re-run it whenever the upstream figure is regenerated.
"""

import argparse
import re
import sys
from pathlib import Path

VIEWPORT = '<meta name="viewport" content="width=device-width, initial-scale=1">'

# Injected stylesheet + chrome. Kept deliberately close to the export's own
# palette (#22303f ink, #5b6b7c muted, #dfe5ec rules) so it does not look bolted on.
EXTRA_CSS = """
<style>
  /* --- added by port-interactive-figure.py --- */
  html {{ -webkit-text-size-adjust: 100%; }}
  .site-bar {{ display:flex; flex-wrap:wrap; gap:10px 18px; align-items:baseline;
      justify-content:space-between; margin:0 0 14px; padding:0 0 10px;
      border-bottom:1px solid #dfe5ec; }}
  .site-bar a {{ color:#0072B2; text-decoration:none; font-size:12.5px; }}
  .site-bar a:hover {{ text-decoration:underline; }}
  .site-bar .who {{ font-size:12.5px; color:#5b6b7c; }}
  .scroll-hint {{ display:none; font-size:12px; color:#5b6b7c;
      margin:10px 0 0; font-style:italic; }}
  /* Fluid down to --floor, then scroll horizontally rather than squash the
     2-column x 4-row panel grid into illegibility. */
  .fig-scroll {{ width:100%; overflow-x:auto; overflow-y:hidden;
      -webkit-overflow-scrolling:touch; }}
  .fig-box {{ width:100%; min-width:{floor}px; height:{height}px; }}
  @media (max-width:{floor}px) {{
    .scroll-hint {{ display:block; }}
    body {{ padding:12px 14px; }}
  }}
</style>
"""


def port(src: Path, dest: Path, floor: int, height: int, home_url: str, home_label: str) -> None:
    html = src.read_text(encoding="utf-8")
    orig_len = len(html)
    applied = []

    # 1. viewport ---------------------------------------------------------
    if 'name="viewport"' in html:
        applied.append("viewport: already present, skipped")
    else:
        html, n = re.subn(r'(<meta charset="utf-8">)', r"\1\n" + VIEWPORT, html, count=1)
        if not n:
            sys.exit("FAIL: could not find <meta charset> to anchor the viewport tag")
        applied.append("viewport: added")

    # 2. layout sizing ----------------------------------------------------
    # Plotly writes the layout as compact JSON, key order preserved from Python.
    before = html
    html = re.sub(r'"height":\s*\d+\s*,\s*"width":\s*\d+\s*,', '"autosize":true,', html, count=1)
    if html == before:
        html = re.sub(r'"width":\s*\d+\s*,\s*"height":\s*\d+\s*,', '"autosize":true,', html, count=1)
    if html == before:
        sys.exit('FAIL: could not find "width"/"height" pair in the Plotly layout')
    applied.append("layout: width/height -> autosize:true")

    if '"responsive": true' not in html and '"responsive":true' not in html:
        html = re.sub(r'(\{"displayModeBar")', r'{"responsive": true, "displayModeBar"', html, count=1)
        applied.append("config: responsive:true added")
    else:
        applied.append("config: responsive:true already present")

    # 3. wrapper div ------------------------------------------------------
    # e.g. <div style="height:1290px; width:1380px;">
    wrapper = re.compile(r'<div style="height:\s*(\d+)px;\s*width:\s*(\d+)px;\s*">')
    m = wrapper.search(html)
    if not m:
        sys.exit("FAIL: could not find the fixed-pixel wrapper div")
    native_h, native_w = int(m.group(1)), int(m.group(2))
    html = wrapper.sub('<div class="fig-scroll"><div class="fig-box">', html, count=1)
    # close the extra div we just opened, at the matching end of the plot block
    html, n = re.subn(r'(</script>\s*</div>\s*)(?=\s*<script>\s*\(function)', r"\1</div>", html, count=1)
    if not n:
        # fall back: close before the trailing </body>
        html = re.sub(r"(</body>)", r"</div>\1", html, count=1)
    applied.append(f"wrapper: {native_w}x{native_h}px -> fluid (floor {floor}px, height {height}px)")

    # 4. injected CSS + header -------------------------------------------
    html = re.sub(r"(</style></head>)", "</style>" + EXTRA_CSS.format(floor=floor, height=height) + "</head>",
                  html, count=1)
    if "site-bar" not in html:
        sys.exit("FAIL: could not inject stylesheet before </head>")

    bar = (
        '<div class="site-bar">'
        f'<span class="who">Tanveer Karim &middot; interactive figure</span>'
        f'<span><a href="{home_url}">{home_label}</a></span>'
        "</div>"
    )
    html = re.sub(r"(<body>)", r"\1\n" + bar, html, count=1)

    hint = ('<p class="scroll-hint">This figure is dense &mdash; scroll it '
            "sideways, or open it on a wider screen for the full grid.</p>")
    html = re.sub(r"(</body>)", hint + r"\1", html, count=1)
    applied.append("chrome: header bar + mobile scroll hint added")

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")

    print(f"{src.name}  ->  {dest}")
    print(f"  {orig_len/1e6:.2f} MB in, {len(html)/1e6:.2f} MB out")
    for a in applied:
        print("  -", a)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("source", type=Path)
    p.add_argument("dest", type=Path)
    p.add_argument("--floor", type=int, default=900,
                   help="min width in px before horizontal scrolling kicks in")
    p.add_argument("--height", type=int, default=1290, help="figure height in px")
    p.add_argument("--home-url", default="/teaching/elpd/")
    p.add_argument("--home-label", default="&larr; Background &amp; how to read this")
    a = p.parse_args()
    port(a.source, a.dest, a.floor, a.height, a.home_url, a.home_label)
