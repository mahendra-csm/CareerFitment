"""Design system v3 prototype: five sample pages.

    python3 proto.py   -> out/proto.html, then print with print.js
Content is taken verbatim from the book's source modules (p0, p3, p5, p10);
page numbers in the contents come from the current 120-page build.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import lib, content  # noqa: F401  (fills lib.TOC with real page numbers)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
_IC = {}


def ic(name, cls=""):
    if name not in _IC:
        s = open(os.path.join(HERE, "vendor", "lucide", name + ".svg")).read()
        _IC[name] = s[s.index("<svg"):].replace('class="lucide', 'data-i="lucide')
    return f'<span class="ico {cls}">{_IC[name]}</span>'


def raw(name):
    ic(name)
    return _IC[name]


# chapter → accent and icon (one system for the whole book)
CH = {1: ("red", "building-2"), 2: ("blue", "clipboard-check"), 3: ("purple", "brain"), 4: ("blue", "file-chart-column"), 5: ("orange", "layout-dashboard"),
      6: ("green", "sprout"), 7: ("gold", "rocket"), 8: ("blue", "microscope"), 9: ("red", "heart-handshake"), 10: ("orange", "flag")}


def page(n, ch, chname, body, kind=""):
    acc = CH[ch][0] if ch else "red"
    side = "even" if n % 2 == 0 else "odd"
    chrome = ""
    if kind != "cover":
        no = f"{ch:02d}" if ch else "00"
        chip = f'<span class="chno">{no}</span>' if ch else ""
        chrome = (f'<div class="edge"></div><div class="hdr">{chip}<span class="chname">{chname}</span><span class="line"></span>'
                  f'<span class="bk">Career Fitment Handbook 2026–27</span></div>'
                  f'<div class="ftr"><span class="fol">{n}</span><span>OneGrasp Education Pvt. Ltd. · careerfitment.onegrasp.com</span></div>')
    return f'<section class="page {side} {kind} ch-{acc}">{chrome}<div class="pc">{body}</div></section>' if kind != "cover" else f'<section class="page cover ch-{acc}">{body}</section>'


pages = []

# ------------------------------------------------------------------ 1 cover
facts = [("purple", "brain", "8", "dimensions measured"), ("blue", "school", "6–12", "classes covered"), ("orange", "layout-dashboard", "10", "parts, with dashboard guides"),
         ("green", "list-checks", "Workbook", "activities and action plans")]
pages.append(page(1, 0, "", f'''
<div class="top">
  <img class="photo" src="assets/gallery/g02.jpg" alt="Students in a OneGrasp career session">
  <div class="photo-fade"></div>
  <div class="brand"><div class="lg"><img src="assets/art/logo.png" alt="OneGrasp"></div><div class="pub">OneGrasp Education Pvt. Ltd.</div></div>
  <div class="ttl">
    <div class="series">Career Fitment Assessment</div>
    <div class="ed">2026–27 Edition</div>
    <h1>Career Fitment Handbook</h1>
    <div class="redrule"></div>
  </div>
</div>
<div class="bars"><i style="background:var(--red)"></i><i style="background:var(--orange)"></i><i style="background:var(--gold)"></i><i style="background:var(--green)"></i><i style="background:var(--blue)"></i><i style="background:var(--purple)"></i></div>
<div class="low">
  <div class="tag">Know Yourself. <span>Choose Your Path.</span> Build Your Future.</div>
  <p class="desc">A comprehensive career guidance and student development handbook for Classes 6–12.</p>
  <div class="facts">''' + "".join(f'<div class="fact ch-{c}">{ic(i)}<div><b>{a}</b><span>{b}</span></div></div>' for c, i, a, b in facts) + '''</div>
</div>
<div class="trust" style="position:absolute;left:20mm;right:20mm;bottom:24mm"><span>Schools that chose OneGrasp</span><div><img src="assets/logos/school-shanthinikethan.png" alt=""><img src="assets/logos/school-dps.png" alt=""><img src="assets/logos/school-oxford.png" alt=""><img src="assets/logos/school-excellencia.png" alt=""></div></div>
<div class="cft"><span>For students, parents, teachers and schools</span><b>careerfitment.onegrasp.com</b></div>''', kind="cover"))

# ------------------------------------------------------------------ 2 contents
parts = []
for kind, no, title, idx, key in lib.TOC:
    if kind == "part":
        parts.append({"no": no, "title": title, "idx": idx, "subs": []})
    elif parts:
        parts[-1]["subs"].append((title, idx))
    else:
        parts.append({"no": 0, "title": "Getting started", "idx": idx, "subs": [(title, idx)]})
skip = ("Central government programmes", "Banks and SIDBI", "Incubators and funds", "State government programmes")
toc = []
for pt in parts:
    acc, icn = CH.get(pt["no"], ("navy", "compass"))
    num = f'{pt["no"]:02d}' if pt["no"] else raw("compass")
    subs = "".join(f'<div class="ts"><span>{t}</span><i></i><b>{i + 1}</b></div>' for t, i in pt["subs"] if t not in skip)
    toc.append(f'<div class="tp ch-{acc}"><div class="tph"><span class="n">{num}</span><b>{pt["title"]}</b><em>{pt["idx"] + 1}</em></div>{subs}</div>')
half = 5
legend = [("purple", "brain", "Understand yourself", "Parts 2–4"), ("orange", "layout-dashboard", "Use the dashboard", "Parts 5–8"), ("blue", "heart-handshake", "For parents and schools", "Part 9"), ("green", "flag", "Plan and act", "Part 10")]
pages.append(page(2, 0, "Contents", f'''
<div class="kick">{raw("book-open")[:0]}Contents</div>
<h1 class="h1">What's inside <em>this handbook</em></h1>
<div class="tlegend" style="display:none">''' + "".join(f'<div class="ch-{c}">{ic(i, "sm")}<span><b>{a}</b><br>{b}</span></div>' for c, i, a, b in legend) + f'''</div>
<div class="toc"><div>{"".join(toc[:half])}</div><div>{"".join(toc[half:])}</div></div>'''))

# ------------------------------------------------------------------ 3 personality (dimension 01) — text from p3_dims.py
pairs = [("battery-charging", "Energy", "Introvert", "Extravert", "Do you recharge alone or with people?"), ("eye", "Information", "Sensing", "Intuition", "Facts and details, or patterns and possibilities?"),
         ("scale", "Decisions", "Thinking", "Feeling", "Logic first, or values and people first?"), ("calendar-check", "Planning", "Judging", "Perceiving", "A clear plan, or keep options open?")]
sliders = [("Introvert", "Extravert", 28), ("Sensing", "Intuition", 64), ("Thinking", "Feeling", 72), ("Judging", "Perceiving", 30)]
careers = [["Introversion + Sensing", "Accountant, lab scientist, software developer, archivist"], ["Extraversion + Feeling", "Teacher, counsellor, HR, sales, hospitality"],
           ["Intuition + Thinking", "Engineer, scientist, strategist, architect, entrepreneur"], ["Sensing + Judging", "Doctor, civil services, operations, banking, law"]]
ages = [("Class 6–8", "Notice when you feel most energetic: in a group or alone."), ("Class 9–10", "Pick one club that uses your type's strengths."),
        ("Class 11–12", "Compare your type with your top career's daily work."), ("With your family", "Ask a parent which of your four letters sound like you.")]
pages.append(page(24, 3, "The 8 Dimensions", f"""
<div class="dimhero">
  {ic("fingerprint", "lg solid")}
  <div><div class="kick">Dimension 01 of 08</div><h1 class="h1">Personality</h1><div class="q">“How do I naturally work and decide?”</div>
  <div class="dprog"><i class="on"></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
  <div class="simple">{ic("lightbulb", "sm")}<p><span class="lbl">In simple words</span> Your personality is your <b>natural style</b>, like being left- or right-handed. You can use both hands, but one feels easier. This dimension finds the style that feels easiest for you, so you can choose work where you don't have to fight yourself every day.</p></div>
</div>
<div class="row c3 mt">
  <div class="card t"><div class="ch">{ic("ruler", "sm")}<span class="h3">What it measures</span></div><p class="sm">Where you get your energy, how you take in information, how you make decisions and how you like to plan. These patterns shape how you prefer to work with others, handle tasks and make choices.</p></div>
  <div class="card t"><div class="ch">{ic("book-open", "sm")}<span class="h3">The framework</span></div><p class="sm">Personality-type preferences in four pairs, widely known as MBTI-style typing (from Carl Jung's work, developed by Myers and Briggs). Some stages also look at the five everyday traits psychologists call the Big Five.</p></div>
  <div class="card t"><div class="ch">{ic("target", "sm")}<span class="h3">Why it matters</span></div><p class="sm">Different work settings suit different patterns. Knowing your personality helps you pick paths where you contribute in your natural way, enjoy the work and grow steadily.</p></div>
</div>
<div class="row mt" style="grid-template-columns:1.18fr .82fr">
  <div><div class="h2">{ic("layers", "sm")}The four preference pairs</div>
    <div class="prs">""" + "".join(f'<div class="pr">{ic(i)}<div><div class="k">{k}</div><p>{q}</p></div><div class="sl"><div class="lr">{"<b>"+a+"</b>" if v < 50 else a}<span>{"<b>"+b+"</b>" if v >= 50 else b}</span></div><div class="tr"><i style="left:{v}%"></i></div></div></div>' for (i, k, a, b, q), (_, _, v) in zip(pairs, sliders)) + f"""</div></div>
  <div style="display:flex;flex-direction:column;gap:3.4mm">
    <div><div class="typecard"><b>ISFJ</b><span>“The Defender” · quiet, practical, caring, organised</span></div>
    <p class="cap">Each slider shows which side you lean to and how clearly. Your four letters together make your type, for example ISFJ. <i>Illustrative.</i></p></div>
    <div class="callout grow-c" style="flex:1">{ic("users", "sm")}<div><div class="lbl">Example</div><p class="sm">Before a school trip, <b>Ravi</b> makes a checklist a week early (Judging); <b>Meera</b> packs the night before and enjoys deciding on the spot (Perceiving). Neither is wrong. But Ravi may enjoy project management, and Meera may thrive in fast-changing roles like journalism or event work.</p></div></div>
  </div>
</div>
<div class="h2 mt">{ic("briefcase", "sm")}Careers that often suit each pattern</div>
<table class="tbl c4t"><colgroup><col style="width:19%"><col style="width:31%"><col style="width:19%"><col style="width:31%"></colgroup><tr><th>If you lean towards…</th><th>You may enjoy careers such as…</th><th>If you lean towards…</th><th>You may enjoy careers such as…</th></tr>""" + "".join(f"<tr><td>{careers[r][0]}</td><td>{careers[r][1]}</td><td>{careers[r+2][0]}</td><td>{careers[r+2][1]}</td></tr>" for r in (0, 1)) + f"""</table>
<div class="h2 mt">{ic("footprints", "sm")}<span>Try this at your stage</span></div>
<div class="ages">""" + "".join(f'<div class="age"><b>{a}</b><span>{b}</span></div>' for a, b in ages) + f"""</div>
<div class="card t mt grow-end" style="padding:3mm 4mm"><div class="ch" style="margin-bottom:1mm">{ic("pen-line", "sm")}<span class="h3">Fill in from your report</span><span class="mut sm" style="margin-left:auto">There is no good or bad personality, only better fits.</span></div>
  <div class="refl"><div class="field">My score<i></i></div><div class="field">My top result<i></i></div><div class="field">One way I'll use it<i></i></div></div></div>
"""))

# ------------------------------------------------------------------ 4 dashboard guide — text from p5_explore.py
steps = [("log-in", "Sign in", "Go to <b>careerfitment.onegrasp.com</b> and sign in with the email and password you used for the assessment."),
         ("file-text", "Open your report", "On the home screen tap <b>Open my full report</b>. Use <b>Download</b> to save the PDF."),
         ("chart-pie", "Explore your results", "In the left menu, open <b>Your results</b>: profile, 8 dimensions, best-fit fields, how you think, my plan."),
         ("compass", "Pick a tool", "Choose a tool from <b>Explore</b> in the left menu, starting with your top career field in the Career Library."),
         ("list-checks", "Do the missions", "Each tool chapter in this book ends with a mission card. Tick tasks off as you finish them on the dashboard."),
         ("trending-up", "Track your progress", "Open <b>My Progress</b> to see lessons done, time spent and your streak; collect certificates as you finish courses.")]
pins = [(1, 9, 11), (2, 33, 3.5), (3, 63, 3.5), (4, 80, 17), (5, 92, 17), (6, 23, 28), (7, 9, 22), (8, 9, 74)]
keys = [("Your name and class", "You're in the right account."), ("Search (press /)", "Find any tool or page."), ("My progress", "Everything you've done."),
        ("Open my full report", "Every page, with Download."), ("See my profile", "Results at a glance."), ("Your toolkit", "One card per tool; new ones say NEW."),
        ("Explore menu", "Every tool, always on the left."), ("Your results", "Profile, dimensions, fields, plan.")]
rhythm = [("calendar-days", "Once a week", "Do the three Career GPS missions", "Career GPS"), ("calendar-range", "Twice a week", "Work on one tool's mission card", "Any tool in the Explore menu"),
          ("clock", "Every day (10 min)", "One lesson, game or speaking challenge", "Money, AI, Communication Lab"), ("calendar-check", "Every month", "Check your progress and update your plan", "My Progress · My plan")]


def shot(src, cap, pins_=()):
    pn = "".join(f'<span class="pin" style="left:{x}%;top:{y}%">{n}</span>' for n, x, y in pins_)
    return f'<figure><div class="shot"><div class="bar"><i></i><i></i><i></i><span>careerfitment.onegrasp.com</span></div><div class="im"><img src="assets/{src}" alt="">{pn}</div></div><figcaption class="cap">{cap}</figcaption></figure>'


pages.append(page(45, 5, "Your Dashboard: Explore", f'''
<div class="kick">{ic("map", "sm")}Start here</div>
<h1 class="h1">How to use <em>your dashboard</em></h1>
<p class="lead">Your dashboard is where the report turns into action. Use it in this order the first time, then come back every week.</p>
<div class="flow mt">''' + "".join(f'<div class="fstep"><div class="top"><span class="num">{i + 1:02d}</span>{ic(c, "sm solid")}<span class="h3">{t}</span></div><p>{x}</p></div>' for i, (c, t, x) in enumerate(steps)) + f'''</div>
<div class="row mt" style="grid-template-columns:1.25fr .75fr">
  {shot("shots/dash-home.jpg", "The dashboard home: report at the top, tools below, menu on the left.", pins)}
  <div><div class="h2">{ic("mouse-pointer-click", "sm")}What you see</div><div class="keys">''' + "".join(f'<div class="key"><span class="pn">{i + 1}</span><span><b>{t}</b> · {x}</span></div>' for i, (t, x) in enumerate(keys)) + f'''</div></div>
</div>
<div class="row mt" style="grid-template-columns:.75fr 1.25fr;align-items:start">
  {shot("shots/progress.jpg", "My Progress: everything you have done, in one place.")}
  <div><div class="h2">{ic("repeat", "sm")}A simple weekly routine</div>
  <div class="rhythm" style="grid-template-columns:1fr 1fr">''' + "".join(f'<div class="rh"><div class="when">{raw(i)}{w}</div><b>{a}</b><span>{raw("map-pin")}{b}</span></div>' for i, w, a, b in rhythm) + f'''</div></div>
</div>
<div class="callout action mt" style="align-items:center;padding:2.6mm 4mm">{ic("square-check-big", "sm")}<div><p class="sm"><span class="lbl" style="margin-right:2mm">Mission</span>Sign in today and open every menu item once. It takes 10 minutes and you'll never feel lost again.</p></div></div>
'''))

# ------------------------------------------------------------------ 5 90-day plan — text from p10_action.py
phases = [("blue", "compass", "Days 1–30", "Explore", "Read 5 careers from my top field", "Career Library, Test-Drive"),
          ("orange", "hammer", "Days 31–60", "Do", "One small task or free course", "Internships, AI & Certifications"),
          ("green", "trophy", "Days 61–90", "Build", "One project or proof", "Portfolio, Career Passport")]
mine = [("purple", "file-text", "My report in one line", '<div class="field" style="margin-top:1mm">My type is<i></i></div><div class="field">Interest code<i></i></div>'),
        ("blue", "target", "My top 3 fields", '<div class="field">1<i></i></div><div class="field">2<i></i></div><div class="field">3<i></i></div>'),
        ("green", "trophy", "One strength to use", '<div class="wl"></div><div class="wl"></div>'),
        ("orange", "sprout", "One area to grow", '<div class="wl"></div><div class="wl"></div>')]
weeks = "".join(f'<div class="wk ch-{"blue" if w <= 4 else "orange" if w <= 8 else "green"}"><i></i>W{w}</div>' for w in range(1, 13))
pages.append(page(116, 10, "Your Action Plan", f'''
<div class="kick">{ic("map", "sm")}Reading guide</div>
<h1 class="h1">Turn your report into <em>a 90-day plan</em></h1>
<p class="lead">Fill this in with your report open. Keep it on your desk, or photograph it and pin it to your phone.</p>
<div class="mine mt">''' + "".join(f'<div class="card t ch-{c}"><div class="ch">{ic(i, "sm")}<span class="h3">{t}</span></div>{body}</div>' for c, i, t, body in mine) + '''</div>
<div class="h2 mt">''' + ic("route", "sm") + '''Three steps, ninety days</div>
<div class="phases grow">''' + "".join(f'''<div class="ph ch-{c}"><div class="phh">{ic(i, "white")}<div><small>{d}</small><b>{n}</b></div></div><div class="phb">
<div><div class="lab">Goal</div><div class="val">{g}</div></div><div><div class="lab">Dashboard tool I'll use</div><div class="val">{tl}</div></div>
<div><div class="lab">My own goal</div><div class="chk"><i></i></div><div class="chk"><i></i></div><div class="chk"><i></i></div></div><div><div class="lab">What I did / proof</div><div class="chk"><i></i></div><div class="chk"><i></i></div></div>
<div class="chk" style="align-items:center"><span class="box"></span><span class="sm">Done</span></div></div></div>''' for c, i, d, n, g, tl in phases) + f'''</div>
<div class="card line mt"><div class="ch">{ic("calendar-check", "sm")}<span class="h3">Tick a box at the end of each week</span><span class="mut sm" style="margin-left:auto">12 weeks, about 90 days</span></div>
<div class="timeline" style="grid-template-columns:repeat(12,1fr)">{weeks}</div></div>
<div class="row c2 mt">
  <div class="callout action">{ic("lightbulb", "sm")}<div><div class="lbl">Try this</div><p class="sm">The dashboard's <b>My plan</b> page and weekly <b>Career GPS</b> missions turn this sheet into ticked-off tasks (Parts 5 and 6).</p></div></div>
  <div class="callout parent">{ic("heart-handshake", "sm")}<div><div class="lbl">For parents</div><p class="sm">Sign the bottom of this page with your child: <b>We agree to try this together.</b></p></div></div>
</div>
<div class="sign"><div class="field">Student<i></i></div><div class="field">Parent<i></i></div><div class="field">Date<i></i></div></div>
'''))

css = open(os.path.join(HERE, "fonts.css")).read() + open(os.path.join(HERE, "v3.css")).read()
doc = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><base href="../"><title>OneGrasp Handbook v3 prototype</title><style>{css}</style></head><body>{"".join(pages)}</body></html>'
open(os.path.join(OUT, "proto.html"), "w").write(doc)
print("prototype pages:", len(pages))
