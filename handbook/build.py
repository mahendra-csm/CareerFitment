"""Builds the OneGrasp Career Fitment Handbook.

    python3 build.py            -> out/handbook.html and out/handbook.pdf (+ out/canva-inserts.json)

Pages marked as Canva placeholders are left out of the PDF but keep their
page number; out/canva-inserts.json lists where the original Canva pages
(logos, partners, campus photos, scientific committee) are merged back in.
"""
import json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(__file__))
import lib
import content  # noqa: F401  (fills lib.PAGES)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

CSS = open(os.path.join(HERE, "style.css")).read()
FONTS = open(os.path.join(HERE, "fonts.css")).read()

total = len(lib.PAGES)


def toc_html(entries):
    out = []
    for kind, no, title, idx in entries:
        if kind == "part":
            out.append(f'<div class="toc-part"><span class="tn">{no:02d}</span><b>{title}</b><span class="tp">{idx + 1}</span></div>')
        else:
            out.append(f'<div class="toc-sub"><span></span><span>{title}</span><span class="tp">{idx + 1}</span></div>')
    return "".join(out)


# split the contents across the two contents pages at a part boundary near the middle
parts_at = [i for i, e in enumerate(lib.TOC) if e[0] == "part"]
cut = min(parts_at, key=lambda i: abs(i - len(lib.TOC) / 2)) if parts_at else len(lib.TOC)
TOC1, TOC2 = toc_html(lib.TOC[:cut]), toc_html(lib.TOC[cut:])
sheets, inserts = [], []
for i, pg in enumerate(lib.PAGES):
    n = i + 1
    if pg["kind"] == "canva":
        inserts.append({"page": n, "source": pg["section"]})
        continue
    body = pg["body"].replace("{{TOTAL}}", str(total)).replace("{{TOC1}}", TOC1).replace("{{TOC2}}", TOC2)
    # contents pages resolve their own page numbers
    body = re.sub(r"\{\{PAGE:(\d+)\}\}", lambda m: f"{int(m.group(1)) + 1:02d}", body)
    cls = f'page {pg["kind"]}' + (" dark" if pg["dark"] else "")
    if pg["kind"] in ("cover", "back", "divider", "full"):
        chrome = ""
    else:
        chrome = (f'<header class="ph"><img src="assets/art/logo.png" class="plogo"><span class="psec">{pg["section"]}</span></header>'
                  f'<footer class="pf"><span>OneGrasp · Career Fitment Handbook · 2026–27</span><span class="pn">{n:02d}</span></footer>')
    if pg["kind"] == "divider":
        chrome = f'<footer class="pf light"><span>OneGrasp · Career Fitment Handbook</span><span class="pn">{n:02d}</span></footer>'
    sheets.append(f'<section class="{cls}" data-n="{n}">{chrome}<div class="pc">{body}</div></section>')

doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><base href="../"><title>OneGrasp Career Fitment Handbook</title>
<style>{FONTS}{CSS}</style></head><body>{''.join(sheets)}</body></html>"""
open(os.path.join(OUT, "handbook.html"), "w").write(doc)
json.dump({"total_pages": total, "pdf_pages": len(sheets), "inserts": inserts}, open(os.path.join(OUT, "canva-inserts.json"), "w"), indent=2)
print(f"book pages: {total}  (pdf {len(sheets)} + canva {len(inserts)})")

if "--html" not in sys.argv:
    subprocess.run(["node", os.path.join(HERE, "print.js"), os.path.join(OUT, "handbook.html"), os.path.join(OUT, "handbook.pdf")], check=True)
