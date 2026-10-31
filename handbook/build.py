"""Builds the OneGrasp Career Fitment Handbook.

    python3 build.py            -> out/handbook.html and out/handbook.pdf
    python3 build.py --html     -> HTML only
"""
import os, subprocess, sys

sys.path.insert(0, os.path.dirname(__file__))
import lib
import content  # noqa: F401  (fills lib.PAGES)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
CSS = open(os.path.join(HERE, "fonts.css")).read() + open(os.path.join(HERE, "style.css")).read() + open(os.path.join(HERE, "editorial.css")).read()


def tvars(key):
    _, c1, c2, soft, deep = lib.THEMES[key]
    return f"--c1:{c1};--c2:{c2};--soft:{soft};--deep:{deep}"


def toc_html():
    parts = []
    for kind, no, title, idx, key in lib.TOC:
        if kind == "part":
            parts.append({"no": no, "title": title, "idx": idx, "key": key, "subs": []})
        elif parts:
            parts[-1]["subs"].append((title, idx))
        else:
            parts.append({"no": 0, "title": "Getting started", "idx": idx, "key": "brand", "subs": [(title, idx)]})
    out = []
    for pt in parts:
        c1 = lib.THEMES[pt["key"]][1]
        subs = "".join(f'<div class="ts2"><span>{t}</span><i></i><b>{i + 1}</b></div>' for t, i in pt["subs"])
        num = f'{pt["no"]:02d}' if pt["no"] else "★"
        out.append(f'<div class="tp2" style="--tc:{c1}"><div class="tp2h"><span>{num}</span><b>{pt["title"]}</b><em>{pt["idx"] + 1}</em></div>{subs}</div>')
    return '<div class="toc2">' + "".join(out) + "</div>"


total = len(lib.PAGES)
import re
REFS = {t: i + 1 for k, _, t, i, _ in lib.TOC}


def ref(m):
    if m.group(1) not in REFS:
        print("WARNING unknown page reference:", m.group(1)); return "??"
    return str(REFS[m.group(1)])
TOC = toc_html()
sheets = []
for i, pg in enumerate(lib.PAGES):
    n = i + 1
    body = re.sub(r"\{\{REF:([^}]+)\}\}", ref, pg["body"].replace("{{TOC}}", TOC).replace("{{TOTAL}}", str(total)))
    sec = pg["section"] or lib.THEMES[pg["theme"]][0]
    if pg["kind"] in ("cover", "back", "divider", "full"):
        chrome = ""
    else:
        part = lib.THEMES[pg["theme"]][0]
        side = "r" if n % 2 else "l"
        chrome = (f'<div class="rh {side}"><span class="rh-book">Career Fitment Handbook</span><span class="rh-sec">{sec}</span></div>'
                  f'<div class="tab {side}"></div>'
                  f'<div class="folio {side}"><b>{n}</b><span>OneGrasp</span></div>')
    sheets.append(f'<section class="page {pg["kind"]}" data-n="{n}" style="{tvars(pg["theme"])}">{chrome}<div class="pc">{body}</div></section>')

doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><base href="../"><title>OneGrasp Career Fitment Handbook</title>'
       f'<style>{CSS}</style></head><body>{"".join(sheets)}</body></html>')
open(os.path.join(OUT, "handbook.html"), "w").write(doc)
print(f"book pages: {total}")

if "--html" not in sys.argv:
    subprocess.run(["node", os.path.join(HERE, "print.js"), os.path.join(OUT, "handbook.html"), os.path.join(OUT, "handbook.pdf")], check=True)
