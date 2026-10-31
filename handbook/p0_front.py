from lib import *

theme("brand")

# ---------------------------------------------------------------- 1. cover
add(f'''<div class="cv">
<div class="cv-bg"></div><div class="cv-dots"></div>
<div class="cv-logo">{img("art/logo.png")}</div>
<div class="cv-chip">{icon("book-open", "4mm", "#E5383B")} Handbook · 2026–27 Edition</div>
<div class="cv-photos">
  <div class="cvp p1">{img("gallery/new1.webp")}</div>
  <div class="cvp p2">{img("gallery/old12.webp")}</div>
  <div class="cvp p3">{img("gallery/new5.webp")}</div>
  <div class="cvp p4">{img("gallery/old02.webp")}</div>
</div>
{img("brochure/c11-i-001.png", "cv-girl")}
<div class="cv-text">
  <div class="cv-kick">OneGrasp Career Fitment Assessment</div>
  <h1 class="cv-title">The Complete<br><span>Career Fitment</span><br>Handbook</h1>
  <p class="cv-sub">Know yourself. Choose your path. Build your future.<br>The step-by-step guide to the assessment, the 8 dimensions, your report and all 20+ tools in your dashboard.</p>
  <div class="cv-for"><span>{icon("graduation-cap", "4mm", "#fff")} Students</span><span>{icon("heart-handshake", "4mm", "#fff")} Parents</span><span>{icon("school", "4mm", "#fff")} Schools & colleges</span></div>
</div>
<div class="cv-band">
  <div><b>8</b><span>dimensions<br>of you</span></div><div><b>4</b><span>editions, Class 6<br>to degree</span></div>
  <div><b>930</b><span>careers<br>explained</span></div><div><b>20+</b><span>tools in one<br>dashboard</span></div><div><b>311</b><span>startup funding<br>programmes</span></div>
  <div class="cv-url">{img("art/qr.png", "cv-qr")}<span>Take the assessment<br><b>careerfitment.onegrasp.com</b></span></div>
</div></div>''', kind="cover")

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
    + h3("Our international scientific committee", "globe")
    + '<div class="faces">' + "".join(f'<div><img src="assets/committee/{o["img"]}"><b>{o["name"].replace("Dr. ", "Dr ").replace("Prof. ", "Prof ")}</b><span>{o["country"]}</span></div>' for o in INTL[:10]) + "</div>"
    + p(f"Professors and researchers from <b>{len(COUNTRIES)} countries</b> review abstracts and deliver keynotes: " + " · ".join(COUNTRIES) + ".", "small mt")
    + p("All logos and trademarks belong to their respective owners.", "small center push"),
    section="Partners")


# ---------------------------------------------------------------- 2b. committee photo wall
from committee_wall import wall_page
mark("Our Scientific Committee")
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
# ---------------------------------------------------------------- 2. belongs to + how to use
mark("How to use this handbook")
add(head("Before you begin", "This handbook", "belongs to…")
    + two(box('<div class="own">' + "".join(f'<div class="ownf"><label>{l}</label><div class="wline"></div></div>' for l in
                                           ["My name", "Class / year", "School or college", "Date I took the assessment", "My personality type", "My interest code", "My top career field"]) + "</div>", "soft"),
          box(h3("How to use this book", "compass")
              + p("This is a <b>do-it book</b>, not a read-it book. Every dashboard tool has a mission card with tick boxes and a worksheet. Each part has its own colour on the page edge.")
              + "".join(f'<div class="route" style="--rc:{c}"><span class="rdot"></span><div><b>{t}</b><br><span class="small">{x}</span></div></div>' for c, t, x in [
                  ("#E5383B", "1 · Meet OneGrasp", "Who we are"), ("#0EA5E9", "2 · The Assessment", "Before you take the test"),
                  ("#8B5CF6", "3 · The 8 Dimensions", "What each part of you means"), ("#10B981", "4 · Your Report", "Read with your report open"),
                  ("#F97316", "5 · Dashboard: Explore", "Careers, exams, scholarships, abroad, jobs"), ("#0891B2", "6 · Skills for Life & Work", "Money, law, AI, speaking, resume, proof"),
                  ("#D946EF", "7 · Startups & Funding", "Build an idea; 311 funding programmes"), ("#6366F1", "8 · Research & Conferences", "From question to global stage"),
                  ("#0284C7", "9 · Parents & Schools", "How the adults can help"), ("#F59E0B", "10 · Your Action Plan", "30-day challenge, yearly plans, trackers")])),
          ratio="0.9fr 1.1fr")
    + h3("Look out for these boxes")
    + grid([callout("simple", "The idea explained the way a friend would."), callout("example", "A real situation that shows how it works."),
            callout("ananya", "Follow Ananya, a sample Class 11 student, through her real report."), callout("try", "A small action you can do this week."),
            callout("parent", "Advice for mothers, fathers and guardians."), callout("warn", "Mistakes and scams to avoid.")], 3, gap="0 3mm"),
    section="How to use this book")

# ---------------------------------------------------------------- 4. contents
add(head("Contents", "What's inside", "this handbook.") + "{{TOC}}", section="Contents")

