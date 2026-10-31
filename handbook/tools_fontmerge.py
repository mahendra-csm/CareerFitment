"""Add the few symbols the book uses (₹ → ← ☐ ✓ ▾ ✎ ✂) to Inter and Poppins so every glyph is embedded as TrueType.
Glyph outlines come from DejaVu Sans (free licence), scaled to each font's units-per-em.  Run once: python3 tools_fontmerge.py"""
import glob
from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen

CODES = [0x20B9, 0x2190, 0x2191, 0x2192, 0x2193, 0x2610, 0x2611, 0x2713, 0x2714, 0x25BE, 0x270E, 0x2702]
SRC = TTFont("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
scmap, sgs = SRC.getBestCmap(), SRC.getGlyphSet()
for path in sorted(glob.glob("assets/fonts/poppins-*.woff2")) + sorted(glob.glob("assets/fonts/Inter-*.ttf")):
    f = TTFont(path)
    k = f["head"].unitsPerEm / SRC["head"].unitsPerEm
    glyf, hmtx = f["glyf"], f["hmtx"]
    added = 0
    for cp in CODES:
        if cp not in scmap or cp in f.getBestCmap():
            continue
        gname = f"sym{cp:04X}"
        pen = TTGlyphPen(None)
        sgs[scmap[cp]].draw(TransformPen(pen, (k, 0, 0, k, 0, 0)))
        glyf[gname] = pen.glyph()
        hmtx[gname] = (round(SRC["hmtx"][scmap[cp]][0] * k), glyf[gname].xMin if hasattr(glyf[gname], "xMin") else 0)
        for t in f["cmap"].tables:
            if t.isUnicode():
                t.cmap[cp] = gname
        added += 1
    f["maxp"].numGlyphs = len(f.getGlyphOrder())
    if "post" in f and f["post"].formatType == 2.0:
        f["post"].extraNames = []
        f["post"].mapping = {}
    f.save(path)
    print(path, "added", added)
