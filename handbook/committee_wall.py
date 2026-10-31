"""The full-page photo wall of the scientific committee (used at the start and in Part 8)."""
import json, os
from lib import *

CM = json.load(open(os.path.join(os.path.dirname(__file__), "committee.json")))
INTL = sorted([o for o in CM if o["country"] not in ("India", "")], key=lambda o: (o["country"], o["name"]))
HOME = sorted([o for o in CM if o["country"] in ("India", "")], key=lambda o: o["name"])
NC = len({o["country"] for o in INTL}) + 1


def nm(n):
    return n.replace("Dr. ", "Dr ").replace("Prof. ", "Prof ").strip()


def wall_page(kicker, section):
    add(head(kicker, "The OneGrasp", "Scientific Committee.",
             f"{len(CM)} featured members of our 50-member international committee, from {NC} countries. They review abstracts, chair sessions and deliver keynotes across 11 disciplines.", center=True)
        + '<div class="wall">' + "".join(f'<div class="wm{" wi" if o["country"] not in ("India", "") else ""}"><img src="assets/committee/{o["img"]}"><b>{nm(o["name"])}</b><span>{o["country"] or "&nbsp;"}</span></div>' for o in INTL + HOME) + "</div>"
        + band(" · ".join(["India"] + sorted({o["country"] for o in INTL})), f"{NC} countries:", "globe", "push"),
        section=section)
