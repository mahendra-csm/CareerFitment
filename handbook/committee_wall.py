"""The full-page photo wall of the scientific committee (used at the start and in Part 8)."""
import json, os
from lib import *

CM = json.load(open(os.path.join(os.path.dirname(__file__), "committee.json")))
INTL = sorted([o for o in CM if o["country"] not in ("India", "")], key=lambda o: (o["country"], o["name"]))
HOME = sorted([o for o in CM if o["country"] in ("India", "")], key=lambda o: o["name"])
NC = len({o["country"] for o in INTL}) + 1


def nm(n):
    return n.replace("Dr. ", "Dr ").replace("Prof. ", "Prof ").strip()


LEAD = ["Dr Manjunath G N", "Dr Rudrarup Gupta", "Dr Rohan Singh", "Dr G. Vikram", "Dr Bishnu Pada Bose"]


def ordered():
    lead = [o for n in LEAD for o in CM if o["name"] == n]
    rest_in = [o for o in HOME if o not in lead]
    rest_out = [o for o in INTL if o not in lead]
    return lead + rest_in + rest_out


def wall_page(kicker, section):
    add(head(kicker, "OneGrasp's International", "Scientific Committee Members",
             f"{len(CM)} featured members from {NC} countries review abstracts, chair sessions and deliver keynotes across 11 disciplines.", center=True)
        + '<div class="wall">' + "".join(f'<div class="wm{" wi" if o["country"] not in ("India", "") else ""}"><img src="assets/committee/{o["img"]}"><b>{nm(o["name"])}</b><span>{o["country"] or "&nbsp;"}</span></div>' for o in ordered()) + "</div>"
        + band(" · ".join(["India"] + sorted({o["country"] for o in INTL})), f"{NC} countries:", "globe", "push"),
        section=section)
