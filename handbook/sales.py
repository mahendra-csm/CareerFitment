"""v5 'Sales edition' prototype: 10 poster-grade pages.

    python3 sales.py  -> out/sales.html ; then print with pp.js
All facts come from the OneGrasp Class 11-12 brochure, the live app (captured October 2026)
and this handbook's existing content. Testimonials are the ones published on the OneGrasp
landing page (careerfitment.onegrasp.com).
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
CM = json.load(open(os.path.join(HERE, "committee.json")))
from committee_wall import ordered


BODIES = []


def page(body, cls="", n=None, dark=False):
    BODIES.append((cls, body))
    fol = f'<div class="x-fol"><span>Career Fitment Handbook 2026–27</span><span>{n}</span></div>' if n else ""
    return f'<section class="page {cls}">{body}{fol}</section>'


def shot(src, x, y, w, h=None, blk="var(--red)", cls=""):
    hh = f"height:{h}mm;" if h else ""
    inner = f'<div class="x-crop" style="{hh}"><img src="assets/{src}" style="{hh}"></div>' if h else f'<img src="assets/{src}">'
    return f'<div class="x-shot {cls}" style="left:{x}mm;top:{y}mm;width:{w}mm;--blk:{blk}">{inner}</div>'


def cta(title, sub, light=False):
    return f'<div class="x-cta"><img src="assets/art/qr.png"><div><b>{title}</b><span>{sub}</span></div></div>'


P = []

# 1 ─ cover (kept as approved: full red, logo centred)
P.append(page('''<div class="x-abs" style="inset:0;background:var(--red)"></div>
<div class="x-abs" style="left:19mm;top:34mm;width:172mm;height:172mm;border-radius:50%;border:.5mm solid rgba(255,255,255,.18)"></div>
<div class="x-abs" style="left:41mm;top:56mm;width:128mm;height:128mm;border-radius:50%;border:.5mm solid rgba(255,255,255,.25)"></div>
<div class="x-abs x-eyebrow" style="left:18mm;right:18mm;top:18mm;display:flex;justify-content:space-between;color:#fff"><span>OneGrasp Education Pvt. Ltd.</span><span>Career Fitment Assessment</span></div>
<div class="x-abs" style="left:72mm;top:87mm;width:66mm;height:66mm;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center"><img src="assets/art/logo.png" style="width:48mm"></div>
<div class="x-abs" style="left:16mm;right:16mm;top:170mm;text-align:center;color:#fff">
 <div class="x-eyebrow" style="opacity:.9">Career Fitment Assessment · Classes 6–12</div>
 <div class="x-huge" style="margin-top:4mm">Career Fitment Handbook</div>
 <div style="display:inline-block;margin-top:5mm;background:#fff;color:var(--red);font:700 8.6pt Inter;padding:1.2mm 4mm">2026–27 Edition</div>
 <div class="x-mid" style="margin-top:8mm">Know Yourself. Choose Your Path. Build Your Future.</div>
 <p class="x-lede" style="margin-top:2mm;opacity:.9">A comprehensive career guidance and student development handbook for Classes 6–12.</p></div>
<div class="x-abs" style="left:18mm;right:18mm;bottom:13mm;display:flex;justify-content:space-between;color:#fff;font:600 8pt Inter;border-top:.3mm solid rgba(255,255,255,.4);padding-top:3.4mm"><span>For students, parents, teachers and schools</span><span>careerfitment.onegrasp.com</span></div>''', n=None))

# 2 ─ the hook
P.append(page(f'''<div class="x-abs x-navy" style="inset:0"></div><div class="x-slash"></div>
<div class="x-abs" style="left:16mm;right:16mm;top:20mm;color:#fff">
 <div class="x-eyebrow" style="color:var(--sun)">For Class 6 to Class 12</div>
 <div class="x-mega" style="margin-top:6mm">Stop guessing<br>your career.<br><span class="x-hl">Start knowing it.</span></div>
 <p class="x-lede" style="margin-top:7mm;max-width:118mm;color:rgba(255,255,255,.88)">One assessment reads eight dimensions of who you are. A personal report shows the careers that fit, and a dashboard of 12 tools turns it into a plan you can act on, every week.</p>
 <div class="x-stats" style="margin-top:11mm;max-width:178mm"><div><b>8</b><span>dimensions of you,<br>measured in one sitting</span></div><div><b>930</b><span>careers explained,<br>with pay in India</span></div><div><b>2,500+</b><span>degree roadmaps,<br>year by year</span></div><div><b>12</b><span>tools in your<br>dashboard</span></div></div>
</div>
{shot("s2/landing.jpg", 82, 176, 140, 88, "var(--sun)")}
<div class="x-abs" style="left:16mm;top:226mm;width:58mm;color:#fff"><img src="assets/art/qr.png" style="width:30mm;background:#fff;padding:1.6mm;display:block"><b style="display:block;font:700 12pt/1.2 Poppins;margin-top:3mm">Scan to take<br>the assessment</b><span style="font:500 8pt Inter;opacity:.85">careerfitment.onegrasp.com</span></div>''', "x-p2", 2))

# 3 ─ the problem
traps = [("01", "Marks", "You scored 95 in maths, so take engineering.", "Marks show how you did in an exam. They do not show what you'd enjoy doing for 30 years."),
         ("02", "Peer pressure", "All my friends are taking MPC.", "Your friends have different strengths and dreams. Following the crowd feels safe, until it doesn't."),
         ("03", "Guesswork", "My cousin did B.Com, so…", "Most families know only a handful of careers. Our library explains 930.")]
P.append(page(f'''<div class="x-abs" style="left:16mm;right:16mm;top:18mm">
 <div class="x-eyebrow x-hl">Why career choices go wrong</div>
 <div class="x-huge" style="margin-top:5mm;color:var(--ink)">Three traps decide<br>too many careers.</div>
 <p class="x-lede" style="margin-top:5mm;max-width:150mm">Ask ten adults why they chose their career and many will say “I didn't really choose.” Here are the three most common traps, and what OneGrasp puts in their place.</p>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;margin-top:9mm">''' + "".join(f'<div class="x-trap"><div class="x-n">{n}</div><b>{t}</b><q>{q}</q><p>{x}</p></div>' for n, t, q, x in traps) + '''</div>
</div>
<div class="x-abs x-paper" style="left:0;right:0;top:150mm;bottom:0"></div>
<div class="x-abs" style="left:16mm;right:16mm;top:160mm">
 <div class="x-eyebrow" style="color:var(--muted)">What OneGrasp does instead</div>
 <div class="x-big" style="margin-top:3mm;color:var(--ink)">From “I don't know” to a <span class="x-hl">clear plan.</span></div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:8mm;border-top:.4mm solid var(--ink)">''' + "".join(f'<div style="padding:4mm 5mm 0 0"><div style="font:800 26pt/1 Poppins;color:var(--red)">{n}</div><b style="display:block;font:700 12.5pt Poppins;color:var(--ink);margin-top:2mm">{t}</b><p style="font-size:9pt;margin-top:1.4mm">{x}</p></div>' for n, t, x in [("1", "The assessment", "8 dimensions of you, in one sitting. Any device, saves as you go."), ("2", "Your report", "Instant and personal: careers that fit you, and the path to them."), ("3", "Your dashboard", "Lessons, tools and next steps, linked to your report.")]) + '''</div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:10mm">
  <div style="background:#fff;padding:4mm 5mm"><div class="x-eyebrow" style="color:var(--red)">Myth</div><div class="x-mid" style="color:var(--ink);margin-top:1.6mm">“JEE or NEET decides everything.”</div><p style="margin-top:2mm;font-size:9pt"><b style="color:var(--ink)">Fact:</b> our library covers 930 careers. Many great routes need neither exam.</p></div>
  <div style="background:#fff;padding:4mm 5mm"><div class="x-eyebrow" style="color:var(--red)">Myth</div><div class="x-mid" style="color:var(--ink);margin-top:1.6mm">“Marks are enough to choose.”</div><p style="margin-top:2mm;font-size:9pt"><b style="color:var(--ink)">Fact:</b> marks show how you did. Fit shows where you will do well.</p></div></div>
</div>''', "", 3))

# 4 ─ the elements of you (8 dimensions)
D = [("Pe", "Personality", "How do I naturally work and decide?", "Your four-letter type, a score for each preference, strengths and next steps.", "--d1"),
     ("In", "Career Interests", "What kind of work excites me?", "Your three-letter interest code (Holland's RIASEC) and how strongly you lean to each type.", "--d2"),
     ("Mi", "Multiple Intelligences", "In which ways am I smart?", "All eight intelligences ranked (Gardner), with your top two named.", "--d3"),
     ("Eq", "Emotional Intelligence", "How well do I handle feelings and people?", "Your EQ level, a score for each of four areas and what to practise first.", "--d4"),
     ("Ls", "Learning Style", "How do I prefer to study?", "Your preferred style, with revision tips that suit it.", "--d5"),
     ("Mo", "Motivators", "What drives me?", "Your core driver and how your other drivers rank.", "--d6"),
     ("St", "Strengths", "What do I naturally contribute?", "Your two signature strengths and the fields that reward them.", "--d7"),
     ("Ap", "Aptitude", "How quickly can I pick up new skills?", "Your overall aptitude, your sharpest area and practice tips for exams.", "--d8")]
els = "".join(f'<div class="x-el" style="--c:var({c})"><div class="x-no">{i + 1:02d}</div><div class="x-sym">{s}</div><div class="x-nm">{n}</div><div class="x-q">{q}</div></div>' for i, (s, n, q, _, c) in enumerate(D))
shows = "".join(f'<div style="--c:var({c})"><i>{s}</i><span><b>{n}.</b> {x}</span></div>' for s, n, _, x, c in D)
P.append(page(f'''<div class="x-abs x-navy" style="inset:0"></div>
<div class="x-abs" style="left:16mm;right:16mm;top:18mm;color:#fff">
 <div class="x-eyebrow" style="color:var(--sun)">What we measure</div>
 <div class="x-huge" style="margin-top:5mm">The elements<br>of <span class="x-hl">you.</span></div>
 <p class="x-lede" style="margin-top:5mm;max-width:150mm;color:rgba(255,255,255,.85)">Eight dimensions, each answering one simple question. Together they show where you will thrive, built on frameworks psychologists have used for decades.</p>
 <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2.4mm;margin-top:9mm">{els}</div>
 <div class="x-eyebrow" style="margin-top:9mm;color:rgba(255,255,255,.7)">What your report shows for each one</div>
 <div class="x-shows" style="margin-top:4mm">{shows}</div>
 <div style="margin-top:9mm;border-top:.4mm solid rgba(255,255,255,.35);padding-top:4mm;display:grid;grid-template-columns:30mm 1fr;gap:4mm;font:500 8.4pt/1.5 Inter;color:rgba(255,255,255,.8)"><span class="x-eyebrow" style="color:var(--sun)">Built on</span><span>Personality-type preferences (Jung; Myers and Briggs) · Holland's RIASEC interests · Gardner's multiple intelligences · Emotional intelligence (Salovey and Mayer; Goleman) · Learning preferences similar to VARK · Work-values research · Strengths-based psychology · Standard reasoning tests</span></div>
</div>''', "", 4))

# 5 ─ the report
P.append(page(f'''<div class="x-abs x-red" style="inset:0"></div>
<div class="x-abs" style="left:16mm;top:18mm;width:96mm;color:#fff">
 <div class="x-eyebrow x-hl2">Your report</div>
 <div class="x-huge" style="margin-top:5mm">A report you'll actually want to read.</div>
 <p class="x-lede" style="margin-top:5mm;color:rgba(255,255,255,.9)">Clear charts, plain words and real next steps, built only from your own answers. Delivered instantly: on screen, as a PDF and by email.</p>
 <ol class="x-rlist" style="margin-top:8mm">
  <li><div><b>8-dimension scorecard</b><span>Your real result in each dimension, on one page.</span></div></li>
  <li><div><b>A deep dive per dimension</b><span>What it means, where you're strong, where to grow.</span></div></li>
  <li><div><b>Career cluster fit</b><span>How closely you match 16 career clusters.</span></div></li>
  <li><div><b>Fitment · Suitability · Selector</b><span>Three views of your options.</span></div></li>
  <li><div><b>A step-by-step roadmap</b><span>From school to senior roles.</span></div></li>
  <li><div><b>Exams, funding and the future</b><span>Entrance exams, funded routes, rising careers.</span></div></li>
  <li><div><b>A page for parents</b><span>How to guide, not decide.</span></div></li>
 </ol></div>
<div class="x-fan">
 <img src="assets/shots/r910-00.jpg" style="left:118mm;top:22mm;width:78mm">
 <img src="assets/shots/r910-02.jpg" style="left:116mm;top:132mm;width:82mm">
 <img src="assets/shots/r910-07.jpg" style="left:126mm;top:196mm;width:70mm;height:82mm;object-fit:cover;object-position:top">
</div>
<div class="x-abs" style="left:16mm;bottom:22mm;width:90mm;color:#fff;background:var(--navy);padding:4mm">{cta("See a sample report", "Scan, sign up, and your own report is ready the moment you finish.")}</div>''', "", 5))

# 6 ─ three ways to see your future
P.append(page(f'''<div class="x-abs" style="left:16mm;right:16mm;top:18mm">
 <div class="x-eyebrow x-hl">The heart of your report</div>
 <div class="x-huge" style="margin-top:5mm;color:var(--ink)">Three ways to see<br>your future.</div>
 <p class="x-lede" style="margin-top:5mm;max-width:150mm">Your report compares what fits you, what fits where you are now, and the career you dream of, side by side.</p>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8mm;margin-top:9mm">
  <div class="x-view"><div class="x-num">1</div><div class="x-k">What fits you</div><b>Career Fitment</b><p>Your top 5 career areas, ranked purely by your answers. Each shows key roles, skills to build, salary range in India (indicative) and entrance exams.</p></div>
  <div class="x-view"><div class="x-num">2</div><div class="x-k">What fits your stream</div><b>Career Suitability</b><p>Careers you can reach from MPC, BiPC, MEC, CEC or HEC today, plus top companies that hire and funded routes such as NDA, IIST and apprenticeships.</p></div>
  <div class="x-view"><div class="x-num">3</div><div class="x-k">Your dream career</div><b>Career Selector</b><p>Choose the career you want. See how well it fits, and every step from subjects and exams to degrees, colleges, skills, jobs and career growth.</p></div>
 </div></div>
{shot("shots/r11-11.jpg", 16, 168, 84, 100, "var(--navy)")}
{shot("shots/r11-12.jpg", 108, 168, 84, 100, "var(--red)")}
<div class="x-abs" style="left:16mm;right:16mm;bottom:15mm;font:500 7.6pt Inter;color:var(--muted)">Real pages from a sample report. Salaries are indicative ranges for India.</div>''', "", 6))

# 7 ─ the dashboard
tools = [("930", "", "Career Library", "What careers do and pay"), ("29", "exams", "Entrance Exams", "Eligibility, planner, mocks"), ("40", "schemes", "Scholarships", "Money you qualify for"), ("6", "steps", "Study Abroad", "Where, what and the money"),
         ("209", "free", "Internships", "Programmes from 135 companies"), ("Daily", "", "Jobs", "Fresh, scam-checked listings"), ("6", "levels", "Money Skills", "Games, labs, Scam Shield"), ("24", "guides", "Law & Rights", "Helplines, letters, rights"),
         ("8", "units", "Research", "From a question to a conference"), ("52", "videos", "Startups", "11 modules, lesson by lesson"), ("20", "courses", "AI & Certifications", "Free, with certificates"), ("100", "questions", "Resume & Interview", "ATS resume + mock interview")]
P.append(page(f'''<div class="x-abs x-navy" style="inset:0"></div>
<div class="x-abs" style="left:16mm;right:16mm;top:18mm;color:#fff">
 <div class="x-eyebrow" style="color:var(--sun)">After the report</div>
 <div class="x-huge" style="margin-top:5mm">Your report becomes<br>a dashboard <span class="x-hl">you use.</span></div>
 <p class="x-lede" style="margin-top:5mm;max-width:150mm;color:rgba(255,255,255,.85)">One login opens every tool, linked to your report. Your progress is always saved, and you pick up where you left off.</p></div>
{shot("s2/library.jpg", 16, 92, 120, 75, "var(--red)")}
{shot("s2/progress.jpg", 128, 120, 78, 49, "var(--sun)")}
<div class="x-abs x-tools" style="left:16mm;right:16mm;top:182mm">''' + "".join(f'<div><b>{a}<small>{u}</small></b><span>{t}</span><em>{x}</em></div>' for a, u, t, x in tools) + '''</div>''', "", 7))

# 8 ─ job-ready
P.append(page(f'''<div class="x-abs" style="left:16mm;right:16mm;top:18mm">
 <div class="x-eyebrow x-hl">Skills for life and work</div>
 <div class="x-huge" style="margin-top:5mm;color:var(--ink)">Job-ready before<br>college even starts.</div></div>
<div class="x-abs x-feat" style="left:16mm;top:70mm;width:84mm">
 <span class="x-tag">AI & Certifications</span><h3>Learn AI for free. Get certified.</h3>
 <div class="x-nums"><div><b>20</b><span>free certificate courses</span></div><div><b>16</b><span>AI tools, rated</span></div><div><b>₹0</b><span>for every course</span></div></div>
 <ul class="x-ticks"><li>Start with YUVA AI for All, the Government of India's national AI course, with an official certificate</li><li>Four levels: AI Aware → User → Maker → Builder, with courses from IBM, Kaggle, Hugging Face and Anthropic Academy</li><li>Every tool rated for age, privacy and what's free</li></ul></div>
{shot("s2/ai.jpg", 108, 68, 88, 55, "var(--navy)")}
{shot("s2/resume.jpg", 16, 150, 84, 52, "var(--red)")}
<div class="x-abs x-feat" style="left:110mm;top:148mm;width:86mm">
 <span class="x-tag">Resume builder</span><h3>A resume that gets past the robots.</h3>
 <ul class="x-ticks"><li>Built-in ATS check, scored as you type, and “Match a job” for each role</li><li>Write your summary with AI; import your OneGrasp certificates</li><li>Four one-column templates: Modern, Classic, Compact, Executive. Download a PDF</li></ul></div>
<div class="x-abs x-feat" style="left:16mm;top:222mm;width:84mm">
 <span class="x-tag">Mock interview</span><h3>Practise out loud. Get feedback.</h3>
 <ul class="x-ticks"><li>The 100 questions asked most in internship, placement, college and scholarship interviews, with model answers</li><li>Five-question rounds in 10 categories; feedback on what you said and how you said it</li></ul></div>
{shot("s2/interview-practice.jpg", 108, 222, 88, 52, "var(--sun)")}''', "", 8))

# 9 ─ trust
faces = "".join(f'<img src="assets/committee/{m["img"]}">' for m in ordered()[:39])
logos = "".join(f'<img src="assets/logos/{f}">' for f in ("crossref.png", "doi.png", "pace.png", "jci.png", "metaspectra.png", "intellimind.png"))
schools = "".join(f'<img src="assets/logos/{f}">' for f in ("school-shanthinikethan.png", "school-dps.png", "school-oxford.png", "school-excellencia.png"))
says = [("The assessment helped us understand our child beyond just marks. We had a real conversation about their strengths and interests for the first time.", "Parent, Mumbai"),
        ("I discovered that I'm good at things I never realized. It gave me confidence to explore careers I didn't think were for me.", "Student, Class 10"),
        ("The report is incredibly detailed. We used it to guide our counseling sessions with students. It made a real difference.", "School counselor")]
P.append(page(f'''<div class="x-abs" style="left:16mm;right:16mm;top:18mm">
 <div class="x-eyebrow x-hl">Why families trust OneGrasp</div>
 <div class="x-huge" style="margin-top:5mm;color:var(--ink)">Chosen by schools.<br>Recognised worldwide.</div>
 <p class="x-lede" style="margin-top:5mm;max-width:155mm">Partner schools use the Career Fitment Assessment with their students. Beyond the assessment, OneGrasp runs international scientific conferences, guided by a scientific committee of researchers and professors from 15 countries.</p>
 <div class="x-eyebrow" style="color:var(--muted);margin-top:6mm">OneGrasp International Conferences · Scientific Committee</div><div class="x-faces" style="margin-top:3mm">{faces}</div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:10mm;margin-top:9mm">
  <div><div class="x-eyebrow" style="color:var(--muted)">Schools that chose OneGrasp</div><div class="x-logos" style="grid-template-columns:repeat(4,1fr);margin-top:4mm">{schools}</div></div>
  <div><div class="x-eyebrow" style="color:var(--muted)">International collaborations</div><div class="x-logos" style="grid-template-columns:repeat(3,1fr);margin-top:4mm">{logos}</div></div></div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr) 1.6fr;gap:0;margin-top:8mm;border-top:.4mm solid var(--ink);padding-top:3mm">
  <div><b style="font:800 24pt/1 Poppins;color:var(--red)">39</b><div style="font:500 8pt Inter;color:var(--muted)">conference committee<br>members featured</div></div>
  <div><b style="font:800 24pt/1 Poppins;color:var(--red)">15</b><div style="font:500 8pt Inter;color:var(--muted)">countries</div></div>
  <div><b style="font:800 24pt/1 Poppins;color:var(--red)">11</b><div style="font:500 8pt Inter;color:var(--muted)">disciplines</div></div>
  <div><div style="font:500 8pt Inter;color:var(--muted)">Free courses in your dashboard come from</div><div class="x-logos" style="grid-template-columns:repeat(4,1fr);margin-top:2mm"><img src="assets/logos/google.svg" style="max-height:6mm"><img src="assets/logos/microsoft.svg" style="max-height:6mm"><img src="assets/logos/ibm.svg" style="max-height:6mm"><img src="assets/logos/harvard.svg" style="max-height:6mm"></div></div></div>
</div>
<div class="x-abs x-paper" style="left:0;right:0;top:196mm;bottom:0"></div>
<div class="x-abs" style="left:16mm;right:16mm;top:205mm">
 <div class="x-eyebrow" style="color:var(--muted)">What parents, students and counsellors say</div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;margin-top:5mm">''' + "".join(f'<div class="x-say"><p>“{t}”</p><span>{w}</span></div>' for t, w in says) + '''</div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;margin-top:7mm;font:500 8.4pt/1.4 Inter;color:var(--body)">
  <div><b style="color:var(--ink)">Honest results.</b> Rushed or careless answers are flagged so the test can be retaken.</div>
  <div><b style="color:var(--ink)">Private by design.</b> Schools see progress, never a student's individual answers.</div>
  <div><b style="color:var(--ink)">Facts you can check.</b> Every exam and funded programme links to its official source.</div></div>
</div>''', "", 9))

# 10 ─ call to action
P.append(page(f'''<div class="x-abs x-red" style="inset:0"></div>
<div class="x-abs" style="right:0;top:0;width:84mm;height:140mm;background:url(assets/gallery/g14.jpg) center/cover;filter:grayscale(1);mix-blend-mode:multiply;opacity:.9"></div>
<div class="x-abs" style="left:16mm;right:16mm;top:20mm;color:#fff">
 <div class="x-eyebrow x-hl2">Take the assessment today</div>
 <div class="x-mega" style="margin-top:6mm">Know yourself.<br>Choose with<br>confidence.</div>
 <div class="x-big" style="margin-top:4mm;color:var(--sun)">Build your future.</div></div>
<div class="x-abs" style="left:16mm;top:150mm;display:grid;grid-template-columns:64mm 1fr;gap:9mm;right:16mm;color:#fff;align-items:center">
 <img class="x-bigqr" src="assets/art/qr.png">
 <div><div class="x-big">careerfitment<br>.onegrasp.com</div><p class="x-lede" style="margin-top:4mm">Scan, register in about two minutes, and your report is ready the moment you finish.</p>
  <p style="margin-top:5mm;font:600 10pt Inter">support@onegrasp.com · +91 89777 60442 / 43</p></div></div>
<div class="x-abs x-who" style="left:16mm;right:16mm;top:232mm;display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;color:#fff">
 <div><b>For students</b><span>Understand yourself and see clear next steps you can take with confidence.</span></div>
 <div><b>For parents</b><span>A shared, calm conversation, with practical questions that help you support better.</span></div>
 <div><b>For schools</b><span>Track every student daily, send reminders and messages, and support guidance with care. Talk to us about a school-wide rollout.</span></div></div>''', "", 10))

css = open(os.path.join(HERE, "fonts.css")).read() + open(os.path.join(HERE, "sales.css")).read()
open(os.path.join(OUT, "sales.html"), "w").write(f'<!doctype html><html><head><meta charset="utf-8"><base href="../"><style>{css}</style></head><body>{"".join(P)}</body></html>')
print("pages", len(P))
