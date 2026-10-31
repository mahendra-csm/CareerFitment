from lib import *

theme("brand")

# ---------------------------------------------------------------- 1. cover
add(f'''<div class="bc"><div class="bc-edge"></div>
<div class="bc-top"><span>Career Fitment Assessment</span><span>2026–27 Edition</span></div>
<div class="bc-logo">{img("art/logo.png")}</div>
<div class="bc-mid"><div class="bc-kick">The official handbook</div>
<h1>Career Fitment<br>Handbook</h1>
<div class="bc-rule"></div>
<p>Know yourself. Choose your path. Build your future.</p>
<p class="bc-sub">A practical guide and workbook for students, parents and schools: the assessment, the eight dimensions, your report, and every tool in your dashboard.</p></div>
<div class="bc-foot"><span>OneGrasp Education Pvt. Ltd.</span><span>careerfitment.onegrasp.com</span></div></div>''', kind="cover")

# ---------------------------------------------------------------- 2. contents
add(head("Contents", "What's inside", "this handbook.") + "{{TOC}}", section="Contents")

# ---------------------------------------------------------------- 3. belongs to + start here
mark("Start here")
route = [("Before the test", "#0EA5E9", [("Do Activity 1 and 2", "{{REF:Activity 1: Predict yourself}}"), ("Read how the test works", "{{REF:What is a psychometric assessment?}}"), ("Get ready for test day", "{{REF:Before you begin}}")]),
         ("After your report", "#10B981", [("Learn the 8 dimensions", "{{REF:What we measure: the 8 dimensions}}"), ("Read your report", "{{REF:How to read your report}}"), ("Do the Reality check", "{{REF:Reality check: how well do you know yourself?}}")]),
         ("Every week", "#F97316", [("Use your dashboard tools", "{{REF:Your dashboard home}}"), ("Finish the mission cards", "{{REF:Career Library}}"), ("Follow the 30-day challenge", "{{REF:The 30-day kickstart challenge}}")]),
         ("Parents and teachers", "#0284C7", [("Guide, not decide", "{{REF:For parents: guide, not decide}}"), ("Ten questions to ask", "{{REF:Ten questions to talk through}}"), ("For schools", "{{REF:For schools: the Institution Portal}}")])]
add(head("Start here", "This handbook", "belongs to…")
    + box('<div class="own2">' + "".join(f'<div><label>{l}</label><i></i></div>' for l in ["Name", "Class / year", "School or college", "Assessment date"]) + "</div>", "soft")
    + h3("Your route through this book", "map")
    + p("This is a do-it book. You don't need to read it in order. Follow the four stages below and go straight to the page shown.", "small")
    + '<div class="route2">' + "".join(f'<div class="rt" style="--rc:{c}"><div class="rth"><span>{i + 1}</span>{t}</div>' + "".join(f'<div class="rtl"><span>{x}</span><b>p. {pg}</b></div>' for x, pg in items) + "</div>" for i, (t, c, items) in enumerate(route)) + "</div>"
    + h3("Signs you'll see on the pages", "info")
    + grid([callout("simple", "The idea in plain words."), callout("example", "A real situation."), callout("try", "A small action this week."),
            callout("task", "A mission to tick off."), callout("parent", "Advice for parents."), callout("warn", "Mistakes and scams to avoid.")], 3, gap="0 3mm"),
    section="Start here")

# ---------------------------------------------------------------- 2. partners (trust first)
import json, os
CM = json.load(open(os.path.join(os.path.dirname(__file__), "committee.json")))
INTL = [o for o in CM if o["country"] not in ("India", "")]
COUNTRIES = ["India"] + sorted({o["country"] for o in INTL})
mark("Our partners and collaborations")
logos = [("crossref", "Crossref", "DOI registration"), ("doi", "DOI 10.65838", "Permanent citable links"), ("pace", "PACE Council", "CPD accreditation"), ("jci", "Journal Citation Index", "Citation indexing"),
         ("intellimind", "IntelliMindEd", "Academic partner"), ("metaspectra", "metaSpectra", "Indexing partner"), ("rmetahub", "RMetaHub", "Indexing partner"), ("kvrss", "KVRSS Group", "Partner")]
schools = [("school-shanthinikethan", "Sree Shanthinikethan English Medium School"), ("school-dps", "Delhi Public School"), ("school-oxford", "Oxford Grammar High School"), ("school-excellencia", "Excellencia Junior College")]
add(head("Trusted worldwide", "Our partners and", "collaborations.", "Before you turn the page: these are the international organisations, schools, platforms and scientists who work with OneGrasp.")
    + h3("International collaborations", "globe")
    + grid([f'<div class="logo-card">{img("logos/" + f + ".png")}<span>{n}<br><span class="small">{d}</span></span></div>' for f, n, d in logos], 4)
    + h3("Schools that chose OneGrasp for their students", "school")
    + grid([f'<div class="logo-card" style="height:34mm">{img("logos/" + f + ".png", style="max-height:19mm")}<span>{n}</span></div>' for f, n in schools], 4)
    + h3("Free courses and tools in the dashboard come from", "graduation-cap")
    + grid([f'<div class="logo-card" style="height:16mm">{img("logos/" + f + ".svg", style="max-height:8mm")}</div>' for f in ("google", "microsoft", "ibm", "harvard")], 4)
    + p("All logos and trademarks belong to their respective owners.", "small center push"),
    section="Partners")


# ---------------------------------------------------------------- 2b. committee photo wall
from committee_wall import wall_page
mark("Our international scientific committee")
wall_page("Trusted worldwide", "Scientific Committee")

# ---------------------------------------------------------------- 3. activity: predict yourself
theme("meet")
mark("Activity 1: Predict yourself")
rows = [
    ("Personality type", "Circle one in each pair", '<span class="opt">E · I</span><span class="opt">S · N</span><span class="opt">T · F</span><span class="opt">J · P</span>'),
    ("Interest code", "Circle your top 3", " ".join(f'<span class="opt">{x}</span>' for x in ["R Doing", "I Thinking", "A Creating", "S Helping", "E Leading", "C Organising"])),
    ("Top intelligence", "Circle 2", " ".join(f'<span class="opt">{x}</span>' for x in ["Words", "Numbers", "Pictures", "Body", "Music", "People", "Self", "Nature"])),
    ("Learning style", "Circle 1", " ".join(f'<span class="opt">{x}</span>' for x in ["Seeing", "Hearing", "Reading", "Doing"])),
    ("Core motivator", "Circle 1", " ".join(f'<span class="opt">{x}</span>' for x in ["Achievement", "Learning", "Security", "Impact", "Freedom", "Creativity", "Leading"])),
    ("Signature strength", "Circle 2", " ".join(f'<span class="opt">{x}</span>' for x in ["Solving", "Creating", "Organising", "Speaking", "Caring", "Persisting", "Leading", "Planning"])),
    ("Emotional intelligence", "Rate 1–5", '<span class="opt">1</span><span class="opt">2</span><span class="opt">3</span><span class="opt">4</span><span class="opt">5</span>'),
    ("Sharpest aptitude", "Circle 1", " ".join(f'<span class="opt">{x}</span>' for x in ["Numbers", "Words", "Logic", "Shapes", "Patterns"])),
]
add(f'''<div class="actban"><div class="actno">ACTIVITY 1 · 10 MINUTES</div><h1>Predict <span>yourself.</span></h1>
<p>Before you take the assessment, guess your own results. Then ask a parent to guess too. After your report arrives, turn to page {{{{REF:Reality check: how well do you know yourself?}}}} and see who knows you best.</p>{img("brochure/c11-i-001.png", "actart")}</div>'''
    + table(["Dimension", "", "My guess", "Parent's guess ✎"], [[f"<b>{d}</b><br><span class='small'>{h}</span>", "", o, ""] for d, h, o in rows], "pred", ["22%", "0%", "50%", "28%"])
    + two(box(h3("My top 3 career fields", "target") + lines(3)), box(h3("My dream career", "rocket") + lines(1) + h3("How well will it fit? Circle", "gauge") + pills(["Below 45%", "45–64%", "65% +"])), "mt", gap="4mm")
    + f'<div class="seal push">{icon("lock-keyhole", "8mm", "#E5383B")}<div><b>Seal your prediction</b><span>Don’t change it after the test. That’s the fun.</span></div><div class="sig"><span>Date</span><i></i></div><div class="sig"><span>My signature</span><i></i></div><div class="sig"><span>Parent’s signature</span><i></i></div></div>',
    section="Activity")

# ---------------------------------------------------------------- 4. activity: 2-minute interest quiz
mark("Activity 2: The 2-minute interest quiz")
qs = {"R": ["Fixing a bicycle or gadget", "Building a model or a robot", "Working outdoors with plants or animals"],
      "I": ["Solving a tricky puzzle", "Finding out how something works", "Doing a science experiment"],
      "A": ["Drawing, designing or decorating", "Writing a story or making a video", "Playing music, dancing or acting"],
      "S": ["Teaching a friend something", "Helping someone who is upset", "Volunteering for a good cause"],
      "E": ["Leading a team or a club", "Convincing people to agree with you", "Selling something or starting a small business"],
      "C": ["Making a neat plan or timetable", "Keeping accounts or records", "Organising files, notes or a cupboard"]}
cols = {"R": "#E8590C", "I": "#3B5BDB", "A": "#AE3EC9", "S": "#2F9E44", "E": "#E03131", "C": "#0C8599"}
items = [(k, t) for i in range(3) for k in qs for t in [qs[k][i]]]
cells = "".join(f'<div class="qz"><i></i><span>{t}</span><b style="background:{cols[k]}">{k}</b></div>' for k, t in items)
car = {"R": "Engineer, pilot, chef, architect, farmer", "I": "Doctor, scientist, data analyst, programmer", "A": "Designer, writer, filmmaker, UX, architect",
       "S": "Teacher, nurse, psychologist, social worker", "E": "Entrepreneur, lawyer, manager, marketer", "C": "Chartered accountant, banker, analyst, administrator"}
add(f'''<div class="actban b2"><div class="actno">ACTIVITY 2 · 2 MINUTES</div><h1>The 2-minute <span>interest quiz.</span></h1>
<p>Tick every activity you'd <b>enjoy</b>, even if you've never tried it. Then count your ticks for each letter. A fun warm-up, not the real assessment.</p>{img("feat/careers.webp", "actart")}</div>'''
    + f'<div class="qzg">{cells}</div>'
    + h3("Count your ticks", "calculator")
    + '<div class="tally">' + "".join(f'<div style="--t:{cols[k]}"><b>{k}</b><span>{n}</span><i></i></div>' for k, n in [("R", "Realistic"), ("I", "Investigative"), ("A", "Artistic"), ("S", "Social"), ("E", "Enterprising"), ("C", "Conventional")]) + "</div>"
    + two(box(h3("My quick code (top 3 letters)", "sparkles") + '<div class="code3"><i></i><i></i><i></i></div>' + p("Later, compare it with the interest code in your real report.", "small")),
          table(["Letter", "Careers people with this letter often enjoy"], [[f'<b style="color:{cols[k]}">{k}</b>', v] for k, v in car.items()], "dense"), "mt", ratio="0.8fr 1.2fr", gap="4mm"),
    section="Activity")

theme("brand")
