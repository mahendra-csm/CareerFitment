"""Prints the print and digital editions from out/handbook.html.

Chromium re-encodes PNG/WebP pictures losslessly, which makes the PDF huge, but it
embeds JPEG files as they are. So every picture without transparency is converted
to JPEG first (print: 1800 px, q88; digital: 1100 px, q74) and the page HTML is
pointed at those copies.

    python3 editions.py      -> out/OneGrasp-Career-Fitment-Handbook-print.pdf, -digital.pdf
"""
import os, re, subprocess, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
CACHE = os.path.join(OUT, ".edition-assets")
EDITIONS = {"print": (1800, 88, 900), "digital": (1100, 74, 600)}


def prepare(src, ed):
    maxpx, q, alpha_max = EDITIONS[ed]
    full = os.path.join(HERE, "assets", src)
    im = Image.open(full)
    has_alpha = im.mode in ("RGBA", "LA", "P") and (im.mode != "P" or "transparency" in im.info)
    if has_alpha:
        a = im.convert("RGBA").getchannel("A").getextrema()
        has_alpha = a[0] < 250
    base = os.path.splitext(src)[0]
    if has_alpha:
        dst = os.path.join(CACHE, ed, base + ".png")
        if not os.path.exists(dst):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            im = im.convert("RGBA")
            lim = 360 if "logo" in src and ed == "digital" else alpha_max
            im.thumbnail((lim, lim), Image.LANCZOS)
            im.save(dst, optimize=True)
    else:
        dst = os.path.join(CACHE, ed, base + ".jpg")
        if not os.path.exists(dst):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            im = im.convert("RGB")
            im.thumbnail((maxpx, maxpx), Image.LANCZOS)
            im.save(dst, quality=q, optimize=True, progressive=False)
    return dst


def main():
    html = open(os.path.join(OUT, "handbook.html")).read()
    for ed in EDITIONS:
        srcs = sorted(set(re.findall(r'src="assets/([^"]+\.(?:png|jpg|jpeg|webp))"', html)))
        h = html
        for s in srcs:
            h = h.replace(f'src="assets/{s}"', f'src="{prepare(s, ed)}"')
        h = h.replace("url(assets/", f"url({HERE}/assets/")
        tmp = os.path.join(OUT, f"handbook-{ed}.html")
        open(tmp, "w").write(h)
        pdf = os.path.join(OUT, f"OneGrasp-Career-Fitment-Handbook-{ed}.pdf")
        subprocess.run(["node", os.path.join(HERE, "print.js"), tmp, pdf], check=True)
        os.remove(tmp)
        print(ed, round(os.path.getsize(pdf) / 1e6, 1), "MB")


if __name__ == "__main__":
    main()
