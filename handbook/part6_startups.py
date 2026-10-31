import json, os
from lib import *

S = "Startups & Funding"
F = json.load(open(os.path.join(os.path.dirname(__file__), "funding.json")))
P = F["programmes"]

divider(6, "Startups & Funding", "OneGrasp's startup programmes, and every grant, loan, subsidy, equity and credit-guarantee programme in the dashboard's Funding directory.",
        ["Spot, Build, Pitch: OneGrasp startup programmes", "How to use the Funding directory", "Central government programmes", "Banks and SIDBI", "Incubators and funds", "State government programmes"],
        image="shots/startups-funding.jpg")

mark("Spot, Build, Pitch: OneGrasp startup programmes")
add(head("Entrepreneurship", "Entrepreneurship is best", "learned by doing.",
         "Most students meet entrepreneurship as a subject: a chapter, a guest lecture, a case study. OneGrasp's startup programmes give them a structured occasion to take one real problem, build a first answer and defend it in front of people who ask hard questions.")
    + '<div class="grid g3">' + "".join(f'<div class="card"><div class="cnum">{n}</div><h4 style="font-size:16pt">{t}</h4><p>{x}</p></div>' for n, t, x in [
        ("01", "SPOT", "Observe, investigate and define a real problem."), ("02", "BUILD", "Develop a prototype or a structured business solution."), ("03", "PITCH", "Present the idea, answer questions and plan the next steps.")]) + "</div>"
    + h3("From problem to pitch: what students actually do")
    + '<div class="flow">' + "".join(f"<div><b>{i}</b>{t}</div>" for i, t in enumerate(["Meet a real-world problem", "Find out who lives with it", "Build and test a first solution", "Shape a simple business model", "Present it and answer questions"], 1)) + "</div>"
    + two(box(h3("In the lecture hall") + p("<b>Learning about business:</b> a chapter on business models, a guest lecture, a case study.")),
          box(h3("In the programme") + p("<b>Building and testing an idea:</b> a real problem chosen by the team, a first solution people can handle, a panel that asks hard questions."), "tint"), "mt")
    + band("For universities", "OneGrasp designs the cohort with the institution and delivers it on campus. A short, well-run programme gives an institution a repeatable way to offer this experience. Talk to us at support@onegrasp.com.", "navy push"),
    section=S)

mark("How to use the Funding directory")
tot = F["totals"]
add(head("Funding directory", "Money to start", "your startup.",
         f"The dashboard's Funding directory lists every grant, loan, subsidy, equity and credit-guarantee programme for Indian startups from CapEasy's scheme directory (CapEasy is OneGrasp's own company). The next pages list all {tot['programmes']} programmes as of {F['fetchedAt']}.")
    + shot("shots/startups-funding.jpg", "Startups › Funding: filter by stage, amount, type, state and sector; sort by deadline or amount.")
    + stats([(str(tot["programmes"]), "programmes"), (f"₹{tot['crore']:,.0f} cr", "on offer in total"), (str(tot["runBy"]["central"]), "central government"), (str(tot["runBy"]["state"]), "state government"), (str(tot["runBy"]["incubator"]), "incubators and funds"), (str(tot["runBy"]["bank"]), "banks and SIDBI")])
    + two(steps([("Filter for students", "Tick “For students” or pick the Idea, Proof of concept or Prototype stage."), ("Pick your state and sector", "State schemes only fund startups registered in that state."),
                 ("Open the programme", "Each one opens its CapEasy page with details, eligibility and how to apply."), ("Check the deadline", "“Open now or rolling” or a date. Plan back from it.")]),
          box(h3("Reading the listing") + table(["Type", "What it is"], [
              ['<span class="tag g">Grant</span>', "Money you don't repay"], ['<span class="tag b">Subsidy</span>', "Part of a cost paid back to you"], ['<span class="tag a">Loan</span>', "Money you repay, often at low interest"],
              ['<span class="tag v">Equity</span>', "Investment for a share of the company"], ['<span class="tag r">Guarantee</span>', "Cover that helps you get a loan"]], "dense")
              + p("<b>Stage</b> shows who it's for: Idea, Proof of concept, Prototype, Early stage, Seed, Paid pilot, Early revenue, Growth, Scale.", "small mt"))),
    section=S)

KIND = {"grant": '<span class="tag g">Grant</span>', "subsidy": '<span class="tag b">Subsidy</span>', "loan": '<span class="tag a">Loan</span>', "equity": '<span class="tag v">Equity</span>', "guarantee": '<span class="tag r">Guarantee</span>'}
STAGE = {"idea": "Idea", "proof-of-concept": "PoC", "prototype": "Prototype", "early-stage": "Early", "seed": "Seed", "paid-pilot": "Pilot", "early-revenue": "Early revenue", "growth": "Growth", "scale": "Scale"}


def state_name(s):
    fix = {"jammu-and-kashmir": "Jammu & Kashmir", "dadra-and-nagar-haveli-and-daman-and-diu": "DNH & DD"}
    return fix.get(s) or " ".join(w if (i and w in ("and", "of")) else w.capitalize() for i, w in enumerate(s.split("-")))


def amount(p):
    a = (p["amount_band"] or "").strip()
    if not a or a.endswith("…") and len(a) > 34:
        return "See programme" if not a else a[:34]
    return a


def short(n, k=78):
    return n if len(n) <= k else n[:k - 1].rstrip() + "…"


def rows_for(group):
    out = []
    for p in group:
        st = ", ".join(STAGE.get(s, s) for s in p["stages"][:3]) or "All stages"
        where = ", ".join(state_name(s) for s in p["states"][:2]) if p["states"] else "All India"
        out.append([short(p["name"]), KIND[p["kind"]], E(amount(p)), st, where, p["deadline_word"] if p["deadline_word"] != "See the programme" else "See programme"])
    return out


PER = 35
groups = [("central", "Central government programmes"), ("bank", "Banks and SIDBI"), ("incubator", "Incubators and funds"), ("state", "State government programmes")]
chunks = []
for key, title in groups:
    g = [p for p in P if p["run_by_kind"] == key]
    g.sort(key=(lambda p: (p["states"][0] if p["states"] else "", p["name"])) if key == "state" else (lambda p: p["name"]))
    for p_ in g:
        chunks.append((title, p_))

pages = [chunks[i:i + PER] for i in range(0, len(chunks), PER)]
seen = set()
for i, pg in enumerate(pages):
    titles = []
    for t, _ in pg:
        if t not in titles:
            titles.append(t)
    for t in titles:
        if t not in seen:
            mark(t)
            seen.add(t)
    body = ""
    for t in titles:
        grp = [p_ for tt, p_ in pg if tt == t]
        body += h3(f"{t} <span class='small'>({sum(1 for p_ in P if p_['run_by_kind'] == dict((b, a) for a, b in groups)[t])} in all)</span>") + table(
            ["Programme", "Type", "Amount", "Stage", "Where", "Deadline"], rows_for(grp), "dense fund", widths=["40%", "9%", "17%", "12%", "11%", "11%"])
    add(head("Funding directory", f"Startup funding programmes", f"({i + 1} of {len(pages)})") + body
        + p(f"Source: CapEasy scheme directory (capeasy.in/schemes), {F['fetchedAt']}. Amounts and deadlines change; open the programme in Startups › Funding for current details.", "small push"),
        section=S)
