"""Poster-grade 'sales edition' pages (built in sales.py) placed inside the full book."""
import lib
import sales

NAMES = ["cover", "hook", "traps", "elements", "report", "views", "dashboard", "jobready", "trust", "cta"]
B = {n: sales.BODIES[i] for i, n in enumerate(NAMES)}


def v5page(name, section=""):
    cls, body = B[name]
    lib.add(f'<div class="v5"><div class="{cls}" style="position:absolute;inset:0">{body}</div></div>', section=section, kind="full")
