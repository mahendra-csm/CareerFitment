"""Bodies for pages built directly in the v3 prototype style (dashboard guide, 90-day plan)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
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


DASH = (f'''
<div class="kick">{ic("map", "sm")}Start here</div>
<h1 class="h1">How to use <em>your dashboard</em></h1>
<p class="lead">Your dashboard is where the report turns into action. Use it in this order the first time, then come back every week.</p>
<div class="flow mt">''' + "".join(f'<div class="fstep"><div class="ptop"><span class="pnum">{i + 1:02d}</span>{ic(c, "sm solid")}<span class="ph3">{t}</span></div><p>{x}</p></div>' for i, (c, t, x) in enumerate(steps)) + f'''</div>
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
''')

phases = [("blue", "compass", "Days 1–30", "Explore", "Read 5 careers from my top field", "Career Library, Test-Drive"),
          ("orange", "hammer", "Days 31–60", "Do", "One small task or free course", "Internships, AI & Certifications"),
          ("green", "trophy", "Days 61–90", "Build", "One project or proof", "Portfolio, Career Passport")]
mine = [("purple", "file-text", "My report in one line", '<div class="field" style="margin-top:1mm">My type is<i></i></div><div class="field">Interest code<i></i></div>'),
        ("blue", "target", "My top 3 fields", '<div class="field">1<i></i></div><div class="field">2<i></i></div><div class="field">3<i></i></div>'),
        ("green", "trophy", "One strength to use", '<div class="wl"></div><div class="wl"></div>'),
        ("orange", "sprout", "One area to grow", '<div class="wl"></div><div class="wl"></div>')]
weeks = "".join(f'<div class="wk ch-{"blue" if w <= 4 else "orange" if w <= 8 else "green"}"><i></i>W{w}</div>' for w in range(1, 13))
PLAN90 = (f'''
<div class="kick">{ic("map", "sm")}Reading guide</div>
<h1 class="h1">Turn your report into <em>a 90-day plan</em></h1>
<p class="lead">Fill this in with your report open. Keep it on your desk, or photograph it and pin it to your phone.</p>
<div class="mine mt">''' + "".join(f'<div class="pcard t ch-{c}"><div class="ch">{ic(i, "sm")}<span class="ph3">{t}</span></div>{body}</div>' for c, i, t, body in mine) + '''</div>
<div class="h2 mt">''' + ic("route", "sm") + '''Three steps, ninety days</div>
<div class="phases grow">''' + "".join(f'''<div class="ph ch-{c}"><div class="phh">{ic(i, "white")}<div><small>{d}</small><b>{n}</b></div></div><div class="phb">
<div><div class="plab">Goal</div><div class="val">{g}</div></div><div><div class="plab">Dashboard tool I'll use</div><div class="val">{tl}</div></div>
<div><div class="plab">My own goal</div><div class="chk"><i></i></div><div class="chk"><i></i></div><div class="chk"><i></i></div></div><div><div class="plab">What I did / proof</div><div class="chk"><i></i></div><div class="chk"><i></i></div></div>
<div class="chk" style="align-items:center"><span class="cbx"></span><span class="sm">Done</span></div></div></div>''' for c, i, d, n, g, tl in phases) + f'''</div>
<div class="pcard line mt"><div class="ch">{ic("calendar-check", "sm")}<span class="ph3">Tick a box at the end of each week</span><span class="mut sm" style="margin-left:auto">12 weeks, about 90 days</span></div>
<div class="timeline" style="grid-template-columns:repeat(12,1fr)">{weeks}</div></div>
<div class="row c2 mt">
  <div class="callout action">{ic("lightbulb", "sm")}<div><div class="lbl">Try this</div><p class="sm">The dashboard's <b>My plan</b> page and weekly <b>Career GPS</b> missions turn this sheet into ticked-off tasks (Parts 5 and 6).</p></div></div>
  <div class="callout parent">{ic("heart-handshake", "sm")}<div><div class="lbl">For parents</div><p class="sm">Sign the bottom of this page with your child: <b>We agree to try this together.</b></p></div></div>
</div>
<div class="psign"><div class="field">Student<i></i></div><div class="field">Parent<i></i></div><div class="field">Date<i></i></div></div>
''')
