from lib import *

divider(8, "research", "Research & Conferences", "From a student's first research question to an international stage: OneGrasp's peer-reviewed conferences and the scientific committee behind them.",
        ["The Research Studio", "International scientific conferences", "The researcher journey", "The OneGrasp Scientific Committee", "Keynotes, awards and the conference day"], "feat/research.webp")
S = "Research & Conferences"

from tools import opener, howto, mission
mark("The Research Studio")
opener(14, "Research Studio", "From a good question to your first conference talk: eight short units, a project planned backwards from a real conference date, a mentor check and a practice recorder.", "feat/research.webp",
       [("8", "studio units"), ("14", "lessons"), ("5", "levels")],
       pills(["Class 9–12: first project", "UG: papers and conferences", "Teachers: mentor checks"]),
       ["Research shows colleges and employers that you can think independently.", "Planning back from a real conference date turns curiosity into a finished project.", "Presenting your work builds confidence that lasts."],
       [("book-open", "8 studio units", "Question → method → abstract → talk."), ("flag", "Start a project", "Pick a conference, plan back."), ("search", "Conference finder", "India and worldwide."),
        ("clipboard-check", "Mentor check", "7 items scored 1–4."), ("mic", "Practice recorder", "3 or 10 minutes; stays on device."), ("id-card", "Research profile", "A public page with a QR code.")],
       ("Dashboard", "Career Toolkit", "Research"), S)
howto("Research Studio", [("research-studio", "Eight studio units."), ("research-new", "Start a project from a conference date."), ("research-practice", "Practice recorder.")],
      [("Do unit 1", "What research is, in 10 minutes."), ("Pick a conference", "Find one 3–6 months away."), ("Plan backwards", "Question, sources, method, results, abstract, slides."), ("Mentor check", "7 items, each 1–4, before you submit."),
       ("Rehearse and present", "Record, compare tries, then submit via Spotlight.")],
      [callout("simple", "The 8 units: What is research · A good question · Sources · Method & data · Results · Abstract · Poster or slides · Presenting & Q&A."), callout("teacher", "Use the mentor check as a simple rubric for school projects.")], S)
mission("Research Studio",
        [("Ask a good question", "30 min", ["Finish units 1 and 2", "Write 3 questions below", "Pick the best one"]),
         ("Plan from the date", "20 min", ["Find a conference", "Fill the backward plan", "Tell your mentor"]),
         ("Present", "1 hour", ["Write a 5-line abstract", "Record a 3-minute talk", "Submit through Spotlight"])],
        two(box(h3("My research question", "circle-help") + p("<b>I wonder why / how / whether…</b>", "small") + lines(3) + p("A good question is specific, answerable and interesting to someone else.", "small")),
            box(h3("My backward plan", "calendar-range") + table(["Weeks before", "I will finish"], [["12", "Question + sources"], ["9", "Method and data"], ["6", "Results"], ["4", "Abstract (mentor check)"], ["2", "Slides + rehearsal"], ["0", "Present!"]], "fill dense")), gap="4mm"),
        "You have a real question, a plan and a date.", S)

mark("International scientific conferences")
disc = [("Business & Economics", "FinTech, digital payments", "briefcase"), ("Engineering & Technology", "Green energy, sustainable manufacturing", "cog"), ("Sports & Physical Education", "Performance, exercise physiology", "dumbbell"),
        ("Agriculture & Food Sciences", "Precision farming, crop biotech", "wheat"), ("Interdisciplinary & Emerging", "Quantum, nanotechnology, materials", "atom"), ("Social Sciences & Humanities", "Psychology, behaviour, mental health", "users"),
        ("Education", "EdTech, curriculum, hybrid learning", "graduation-cap"), ("Physical & Life Sciences", "Climate, conservation, marine biology", "leaf"), ("Health & Medical Sciences", "AI in medicine, imaging", "stethoscope"),
        ("Mathematics & Data Science", "Deep learning, statistics, big data", "sigma"), ("Arts, Culture & Communication", "Digital media, heritage, film", "palette")]


def kv_html(items):
    return '<dl class="kv">' + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in items) + "</dl>"


add(head("Conferences", "Where global research", "gets presented.",
         "Present. Publish. Get recognised. Two-evening online conferences across 11 disciplines, with a DOI for every accepted abstract, CPD-accredited certificates and a 50-member international scientific committee.")
    + stats([("500+", "conferences held online", "presentation"), ("70+", "countries", "globe"), ("10,000+", "researchers reached", "users"), ("190M+", "Crossref metadata records", "database"), ("10+", "indexing directories", "list")], "grad")
    + h3("11 disciplines, one global calendar", "calendar")
    + grid([f'<div class="disc">{chip(ic, size="9mm", isz="4.6mm")}<div><b>{t}</b><span>{x}</span></div></div>' for t, x, ic in disc], 3, gap="2.4mm")
    + two(box(h3("The OneGrasp conference model", "badge-check") + kv_html([("Format", "Live online, two evenings"), ("Review", "Committee peer review"), ("Publication", "DOI via Crossref, prefix 10.65838"),
                                                                          ("Accreditation", "CPD via PACE Council"), ("Recognition", "Three awards per event")])),
          box(h3("Who presents", "mic") + pills(["Faculty and professors", "PhD scholars", "Postgraduate students", "Industry professionals", "Policy makers", "School and college students"])
              + p('<span class="small">Calendar and call for papers: <b>onegrasp.com/events</b>. In the dashboard: Spotlight › Submit an abstract.</span>', "mt"), "soft"), "mt", gap="4mm")
    + grid([f'<div class="logo-card" style="height:20mm">{img("logos/" + f + ".png", style="max-height:11mm")}</div>' for f in ("crossref", "doi", "pace", "jci", "metaspectra")], 5, "push", gap="3mm"),
    section=S)

mark("The researcher journey")
journey = [("Submit your abstract", "Online, before the abstract deadline.", "send"), ("Committee review", "Reviewed by experts in your discipline.", "search-check"), ("Register", "Early, standard or late; Razorpay (India) or PayPal.", "credit-card"),
           ("Present live", "In your discipline's paper session.", "mic"), ("Certificate issued", "Unique, verifiable certificate ID.", "award"), ("DOI assigned", "A permanent, citable link via Crossref.", "link"),
           ("Indexed", "Listed in 10+ directories.", "list"), ("Keynote invitation", "Strong presenters keynote future editions.", "trophy")]
cols = ["#1E3A8A", "#3730A3", "#4338CA", "#4F46E5", "#0891B2", "#059669", "#EA580C", "#DC2626"]
add(head("Conferences", "From research paper", "to global recognition.", "A clear eight-step path takes every presenter from first submission to a published, indexed and certified contribution, and for the best, a future keynote.")
    + '<div class="stairs">' + "".join(f'<div class="stair" style="--sc:{cols[i]};margin-left:{(7 - i) * 0 + i * 6}mm"><span>Step {i + 1}</span>{icon(ic, "5mm", "#fff")}<b>{t}</b><em>{x}</em></div>' for i, (t, x, ic) in list(enumerate(journey))[::-1]) + "</div>"
    + h3("What every presenter takes home", "gift")
    + cards([("award", "Certificate with unique ID", "Verifiable by its certificate ID.", "#4338CA"), ("link", "A DOI for your abstract", "Prefix 10.65838, resolvable at doi.org.", "#0891B2"),
             ("badge-check", "CPD credit", "Accredited through PACE Council.", "#059669"), ("globe", "Zero travel, zero visa", "Join from your campus or home.", "#EA580C")], 4, "compact")
    + h3("How students get there from the dashboard", "route")
    + steps([("Research Studio", "Eight units teach the method.", "book-open"), ("Start a project", "Plan back from a conference date.", "flag"), ("Mentor check", "7 items scored 1–4.", "clipboard-check"),
             ("Spotlight", "Submit your abstract.", "send")], cols=4),
    section=S)

mark("The OneGrasp Scientific Committee")
import json as _j, os as _o
CM = _j.load(open(_o.path.join(_o.path.dirname(__file__), "committee.json")))
INTL = sorted([o for o in CM if o["country"] not in ("India", "")], key=lambda o: (o["country"], o["name"]))
HOME = [o for o in CM if o["country"] in ("India", "")]
NC = len({o["country"] for o in INTL}) + 1


def nm(n):
    return n.replace("Dr. ", "Dr ").replace("DR ", "Dr ").replace("Prof. ", "Prof ").replace("Dr.", "Dr ").replace("  ", " ").strip()


def short_aff(a):
    parts = [x.strip() for x in a.split(",")]
    if parts and parts[-1] in ("India",) or (len(parts) > 1 and len(parts[-1]) < 22):
        parts = parts[:-1] if len(parts) > 1 else parts
    t = ", ".join(parts[-2:]) if len(parts) > 1 else parts[0]
    return t[:70]


def card_(o, intl):
    flag = f'<em class="cflag{" in" if intl else ""}">{icon("map-pin", "2.6mm", "#fff")} {o["country"]}</em>' if o["country"] else ""
    return f'<div class="cm"><img src="assets/committee/{o["img"]}"><div><b>{nm(o["name"])}</b><span class="cr">{o["role"][:48]}</span><span>{short_aff(o["aff"])}</span>{flag}</div></div>'


add(head("Scientific committee", "International", "committee members.",
         f"A 50-member committee of professors, researchers and industry experts reviews abstracts, chairs sessions and delivers keynotes across 11 disciplines. Featured: {len(CM)} members from {NC} countries. Here are the {len(INTL)} members based outside India.")
    + grid([card_(o, True) for o in INTL], 3, gap="2mm 2.4mm")
    + band(" · ".join(sorted({o["country"] for o in INTL})), f"{NC - 1} countries outside India:", "globe", "mt push"),
    section=S)
add(head("Scientific committee", "Committee members", "in India.", f"{len(HOME)} professors and researchers from leading Indian universities and institutes.")
    + grid([card_(o, False) for o in HOME], 3, gap="2mm 2.4mm")
    + p("Member details as listed on onegrasp.com/events. The full committee has 50 members; 39 are featured.", "small push"),
    section=S)

mark("Keynotes, awards and the conference day")
add(head("Conferences", "Keynotes from", "leading experts.", "Committee members and invited experts open each day with keynotes that bridge research and practice.")
    + grid([f'<div class="kn" style="--kc:{c}"><img class="knp" style="border-color:{c}" src="assets/committee/{ph}"><b>{n}</b><em>{r}</em><p>{t}</p></div>' for n, r, t, c, ph in [
        ("Dr Manjunath G N", "Professor & Head, Pharmacology, Sri Siddhartha Medical College, India", "Mental health & psychological stress in athletes · Brain–computer interfaces", "#4338CA", "dr-manjunath-g-n.jpg"),
        ("Dr Bishnu Pada Bose", "Professor, Partner & Advisor, Invosystems, Singapore", "Outcome-based vs traditional education · Greenhouse gases & global warming", "#0891B2", "dr-bishnu-pada-bose.jpg"),
        ("Dr Ju Lee Kim", "Senior Researcher, R&D Center, RedGene, Republic of Korea", "Organoids and gene circuits in stem-cell research", "#DB2777", "dr-ju-lee-kim.jpg")]], 3, gap="4mm")
    + h3("Moments from recent conferences", "camera")
    + grid([f'<figure class="hlp"><img src="assets/conf/{f}.jpg"><figcaption>{c}</figcaption></figure>' for f, c in [("h01", "Dr Manjunath G N: stress in athletes"), ("h00", "Dr Bishnu Pada Bose: outcome-based education"), ("h02", "Participants joining a live plenary"), ("h10", "Dr Ju Lee Kim presenting live")]], 4, gap="2.4mm")
    + h3("Two evenings, one clear format (IST)", "clock")
    + two(table(["Day 1", ""], [["6:00", "Inaugural ceremony & welcome"], ["6:30", "Keynote I"], ["7:15", "Keynote II"], ["8:00", "Networking & Q&A"], ["8:15", "Paper session I"], ["9:00", "Paper session II"], ["9:45", "Panel & open Q&A"]], "dense", widths=["22%", "78%"]),
          table(["Day 2", ""], [["6:00", "Welcome & Day 1 recap"], ["6:30", "Keynote III"], ["7:15", "Keynote IV"], ["8:00", "Open networking"], ["8:15", "Paper sessions III & IV"], ["9:00", "Award ceremony"], ["9:45", "Valedictory & certificates"]], "dense", widths=["22%", "78%"]), gap="4mm")
    + h3("Awards at every conference", "trophy")
    + cards([("trophy", "Best Paper Award", "For the strongest paper in each discipline.", "#F5B700"), ("star", "Young Researcher Award", "Recognising early-career excellence.", "#4338CA"), ("mic", "Outstanding Presenter", "For clarity and impact on stage.", "#DB2777")], 3, "compact")
    + callout("try", "Students: start with the <b>Research Studio</b> this term, aim for a student conference next term, and a OneGrasp international conference after that.", cls="push"),
    section=S)
