"""Copies app screenshots into assets/shots as compressed JPEGs (python3 import_shots.py SRC_DIR)."""
import glob, os, sys
from PIL import Image
src, dst = sys.argv[1], os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "shots")
os.makedirs(dst, exist_ok=True)
for f in glob.glob(os.path.join(src, "*.png")):
    out = os.path.join(dst, os.path.basename(f)[:-4] + ".jpg")
    if os.path.exists(out) and os.path.getmtime(out) > os.path.getmtime(f):
        continue
    im = Image.open(f).convert("RGB")
    if im.width > 1800:
        im = im.resize((1800, round(im.height * 1800 / im.width)), Image.LANCZOS)
    im.save(out, quality=86)
print(len(os.listdir(dst)))
