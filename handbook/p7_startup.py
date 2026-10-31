import json, os
from lib import *

divider(7, "startup", "Startups & Funding", "OneGrasp's startup programmes, and every grant, loan, subsidy, equity and credit-guarantee programme in the dashboard's Funding directory: 311 of them.",
        ["The Startups course", "How to use the Funding directory", "Central government programmes", "Banks and SIDBI", "Incubators and funds", "State government programmes"], "feat/startups.webp")
S = "Startups & Funding"
F = json.load(open(os.path.join(os.path.dirname(__file__), "funding.json")))
P = F["programmes"]
T = F["totals"]

from tools import opener, howto, mission
mark("The Startups course")
opener(13, "Startups", "Build a startup, lesson by lesson: 11 modules, 52 video lessons, a quiz after each, a mission on your own idea, and 311 funding programmes when you're ready.", "feat/startups.webp",
       [("11", "modules"), ("52", "video lessons"), ("311", "funding programmes")],
       pills(["Class 9–12: founder mindset", "UG: build and pitch", "Anyone with an idea"]),
       ["Entrepreneurship is learned by doing, not by reading about it.", "Every module ends with a mission on your own idea, so you finish with a real plan.", "Funding is listed in one place, with amounts and deadlines."],
       [("target", "Placement quiz", "2 minutes to the right module."), ("video", "Video lessons", "Short talks + reads."), ("circle-check", "Quizzes", "Pass one to unlock the next."),
        ("flag", "Missions", "Each builds your Startup Portfolio."), ("clapperboard", "Founder videos", "A library of talks."), ("wallet", "Funding", "Grants, loans, incubators.")],
       ("Dashboard", "Career Toolkit", "Startups"), S)
howto("Startups", [("startups-place", "The 2-minute placement quiz."), ("startups-videos", "Video library."), ("startups-funding", "Funding directory.")],
      [("Take the placement quiz", "It points you to the right module."), ("Watch and read", "Each lesson is short."), ("Do the task on your idea", "Every lesson, a small action."), ("Pass the quiz", "Unlocks the next lesson; a test ends each module."),
       ("Build your portfolio", "Missions become pages; then find funding.")],
      [callout("simple", "Modules: Founder Mindset → Right Problem → Customer Discovery → Validation → MVP → Business Model → First Customers → Money → Team → Legal (India) → Pitching."), callout("good", "Learning from failure is part of the course.")], S)
mission("Startups",
        [("Find the right problem", "30 min", ["Take the placement quiz", "Finish module 1 or 2", "Write your problem below"]),
         ("Talk to 5 people", "1 week", ["Interview 5 people who have the problem", "Ask about their past, not your idea", "Note what you learned"]),
         ("Shape your idea", "45 min", ["Fill the idea canvas", "Find 2 funding programmes for your stage", "Share it with a mentor"])],
        '<div class="canvas">' + "".join(f'<div><b>{icon(ic, "4mm", "var(--c1)")} {t}</b><span>{q}</span></div>' for t, q, ic in [
            ("Problem", "What hurts, for whom?", "triangle-alert"), ("Customer", "Who exactly has it?", "user-round"), ("Solution", "My first simple answer", "lightbulb"),
            ("Proof", "What the 5 interviews said", "messages-square"), ("First customers", "How I'll reach 10 people", "megaphone"), ("Money", "Who pays, how much, why", "indian-rupee"),
            ("Team", "Who I need", "users"), ("Funding to try", "2 programmes from Part 7", "wallet")]) + "</div>",
        "You have a tested problem and a one-page plan.", S)

mark("How to use the Funding directory")
kinds = [("Grant", sum(p["kind"] == "grant" for p in P), "#16A34A"), ("Subsidy", sum(p["kind"] == "subsidy" for p in P), "#0EA5E9"), ("Loan", sum(p["kind"] == "loan" for p in P), "#F59E0B"),
         ("Equity", sum(p["kind"] == "equity" for p in P), "#8B5CF6"), ("Guarantee", sum(p["kind"] == "guarantee" for p in P), "#F43F5E")]
runby = [("State government", T["runBy"]["state"], "#D946EF"), ("Incubators and funds", T["runBy"]["incubator"], "#F43F5E"), ("Central government", T["runBy"]["central"], "#F97316"), ("Banks and SIDBI", T["runBy"]["bank"], "#64748B")]
early = sum(1 for p in P if set(p["stages"]) & {"idea", "proof-of-concept", "prototype"})
add(head("Funding directory", "Money to start", "your startup.",
         f"The dashboard's Funding directory lists every grant, loan, subsidy, equity and credit-guarantee programme for Indian startups from CapEasy's scheme directory (CapEasy is OneGrasp's own company). The next nine pages list all {T['programmes']}, as of {F['fetchedAt']}.")
    + stats([(str(T["programmes"]), "programmes", "list"), (f"₹{T['crore']:,.0f} cr", "on offer in total", "indian-rupee"), (str(early), "for idea / prototype stage", "lightbulb"), (str(T["oneClick"]), "one-click applications", "mouse-pointer-click")])
    + two(box(h3("What kind of money?", "chart-pie") + '<div class="two mid" style="display:grid;grid-template-columns:42mm 1fr;gap:3mm">' + donut(kinds, 40, 0.55, (str(T["programmes"]), "programmes")) + legend(kinds) + "</div>"),
          box(h3("Who runs them?", "landmark") + '<div class="two mid" style="display:grid;grid-template-columns:42mm 1fr;gap:3mm">' + donut(runby, 40, 0.55, ("4", "sources")) + legend(runby) + "</div>"), gap="4mm")
    + two(laptop("shots/startups-funding.jpg", "Startups › Funding: filter by stage, amount, type, state and sector."),
          vsteps([("Filter for students", "Tick “For students” or pick Idea, Proof of concept or Prototype."), ("Pick your state and sector", "State schemes only fund startups registered in that state."),
                  ("Open the programme", "Each opens its CapEasy page: details, eligibility, how to apply."), ("Check the deadline", "“Open now or rolling”, or a date. Plan back from it.")]), "mt", gap="5mm")
    + two(box(h3("Reading the listing", "book-open") + '<div class="pills">' + "".join(f'{tag(k, c)}' for k, _, c in kinds) + "</div>"
              + p("<b>Grant:</b> money you don't repay · <b>Subsidy:</b> part of a cost paid back to you · <b>Loan:</b> repaid, often at low interest · <b>Equity:</b> investment for a share · <b>Guarantee:</b> cover that helps you get a loan", "small mt")),
          callout("warn", "Never pay an agent to “guarantee” a government grant. Real schemes apply directly or through registered incubators."), "push", gap="4mm"),
    section=S)

KIND = {"grant": tag("Grant", "#16A34A"), "subsidy": tag("Subsidy", "#0EA5E9"), "loan": tag("Loan", "#F59E0B"), "equity": tag("Equity", "#8B5CF6"), "guarantee": tag("Guarantee", "#F43F5E")}
STAGE = {"idea": "Idea", "proof-of-concept": "PoC", "prototype": "Prototype", "early-stage": "Early", "seed": "Seed", "paid-pilot": "Pilot", "early-revenue": "Revenue", "growth": "Growth", "scale": "Scale"}


def sname(s):
    fix = {"jammu-and-kashmir": "Jammu & Kashmir", "dadra-and-nagar-haveli-and-daman-and-diu": "DNH & DD"}
    return fix.get(s) or " ".join(w if (i and w in ("and", "of")) else w.capitalize() for i, w in enumerate(s.split("-")))


def amt(p):
    a = (p["amount_band"] or "").strip().rstrip("…").strip()
    return a[:30] if a else "See programme"


def short(n, k=74):
    return n if len(n) <= k else n[:k - 1].rstrip() + "…"


PER = 80
groups = [("central", "Central government programmes"), ("bank", "Banks and SIDBI"), ("incubator", "Incubators and funds"), ("state", "State government programmes")]
items = []
for key, title in groups:
    g = [p for p in P if p["run_by_kind"] == key]
    g.sort(key=(lambda p: (p["states"][0] if p["states"] else "", p["name"])) if key == "state" else (lambda p: p["name"]))
    cnt = len(g)
    items.append(("H", title, cnt))
    items += [("P", title, p) for p in g]
pages = []
cur = []
for it in items:
    cur.append(it)
    if len(cur) >= PER:
        pages.append(cur); cur = []
if cur:
    pages.append(cur)


def col(rows):
    out = []
    for kind, title, x in rows:
        if kind == "H":
            out.append(f'<tr class="gh"><td colspan="4">{icon("landmark", "3.2mm", "#fff")} {title} · {x}</td></tr>')
            continue
        p = x
        where = sname(p["states"][0]) if p["states"] else "All India"
        out.append(f'<tr><td>{E(short(p["name"], 52))}</td><td>{KIND[p["kind"]]}</td><td>{E(amt(p)[:22])}</td><td>{where}</td></tr>')
    return f'<table class="tbl fund2"><colgroup><col style="width:52%"><col style="width:16%"><col style="width:19%"><col style="width:13%"></colgroup><thead><tr><th>Programme</th><th>Type</th><th>Amount</th><th>Where</th></tr></thead><tbody>{"".join(out)}</tbody></table>'


seen = set()
for i, pg in enumerate(pages):
    for kind, title, _ in pg:
        if title not in seen:
            mark(title); seen.add(title)
    half = (len(pg) + 1) // 2
    add(head("Funding directory", "Startup funding", f"programmes ({i + 1} of {len(pages)})")
        + two(col(pg[:half]), col(pg[half:]), gap="3mm")
        + p(f"Source: CapEasy scheme directory (capeasy.in/schemes), {F['fetchedAt']}. Amounts and deadlines change; open each programme in Startups › Funding for details, eligibility and how to apply.", "small push"),
        section=S)
