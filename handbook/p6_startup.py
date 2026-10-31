import json, os
from lib import *

divider(6, "startup", "Startups & Funding", "OneGrasp's startup programmes, and every grant, loan, subsidy, equity and credit-guarantee programme in the dashboard's Funding directory: 311 of them.",
        ["Spot, Build, Pitch", "How to use the Funding directory", "Central government programmes", "Banks and SIDBI", "Incubators and funds", "State government programmes"], "feat/startups.webp")
S = "Startups & Funding"
F = json.load(open(os.path.join(os.path.dirname(__file__), "funding.json")))
P = F["programmes"]
T = F["totals"]

mark("Spot, Build, Pitch")
add(head("Entrepreneurship", "Entrepreneurship is best", "learned by doing.",
         "Most students meet entrepreneurship as a chapter, a guest lecture or a case study. OneGrasp's startup programmes give them a real occasion to take one problem, build a first answer and defend it in front of people who ask hard questions.")
    + grid([f'<div class="sbp" style="--sc:{c}"><span>{n}</span>{icon(ic, "9mm", "#fff")}<h4>{t}</h4><p>{x}</p></div>' for n, t, x, ic, c in [
        ("01", "SPOT", "Observe, investigate and define a real problem.", "search", "#D946EF"), ("02", "BUILD", "Develop a prototype or a structured business solution.", "hammer", "#F43F5E"),
        ("03", "PITCH", "Present the idea, answer questions and plan the next steps.", "presentation", "#F97316")]], 3, gap="4mm")
    + h3("From problem to pitch: what students actually do", "route")
    + steps([("Meet a real-world problem", "Chosen by the team.", "globe"), ("Find out who lives with it", "Talk to real users.", "users"), ("Build and test a first solution", "Something people can handle.", "wrench"),
             ("Shape a business model", "Who pays, and why.", "wallet"), ("Present it", "Answer hard questions.", "mic")], cols=5)
    + two(box(h3("In the lecture hall", "book") + p("<b>Learning about business:</b> a chapter on business models, a guest lecture, a case study.")),
          box(h3("In the OneGrasp programme", "rocket") + p("<b>Building and testing an idea:</b> a real problem chosen by the team, a first solution people can handle, a panel that asks hard questions."), "grad"), "mt", gap="4mm")
    + callout("example", "A team of second-year students notices that small vegetable vendors throw away unsold stock every evening. They interview 20 vendors (Spot), build a simple WhatsApp ordering prototype (Build), and present the numbers to a panel (Pitch). Then they check the Funding directory for an idea-stage grant.")
    + band("OneGrasp designs the cohort with the institution and delivers it on campus. Talk to us at support@onegrasp.com.", "For universities:", "building-2", "push"),
    section=S)

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


PER = 35
groups = [("central", "Central government programmes"), ("bank", "Banks and SIDBI"), ("incubator", "Incubators and funds"), ("state", "State government programmes")]
chunks = []
for key, title in groups:
    g = [p for p in P if p["run_by_kind"] == key]
    g.sort(key=(lambda p: (p["states"][0] if p["states"] else "", p["name"])) if key == "state" else (lambda p: p["name"]))
    chunks += [(title, p) for p in g]
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
        grp = [p for tt, p in pg if tt == t]
        cnt = sum(1 for p in P if p["run_by_kind"] == dict((b, a) for a, b in groups)[t])
        rows = [[short(p["name"]), KIND[p["kind"]], E(amt(p)), ", ".join(STAGE.get(s, s) for s in p["stages"][:2]) or "All", ", ".join(sname(s) for s in p["states"][:1]) if p["states"] else "All India",
                 p["deadline_word"].replace("Open now or rolling", "Open / rolling").replace("See the programme", "See programme")] for p in grp]
        body += h3(f"{t} <span class='small'>· {cnt} in all</span>", "landmark") + table(["Programme", "Type", "Amount", "Stage", "Where", "Deadline"], rows, "dense fund", widths=["41%", "10%", "17%", "11%", "10%", "11%"])
    add(head("Funding directory", "Startup funding", f"programmes ({i + 1} of {len(pages)})") + body
        + p(f"Source: CapEasy scheme directory (capeasy.in/schemes), {F['fetchedAt']}. Amounts and deadlines change; open the programme in Startups › Funding for current details.", "small push"),
        section=S)
