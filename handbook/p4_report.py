import json, os
from lib import *

divider(4, "report", "Your Report", "What every class receives, page by page, a complete worked example, and how to read your own report with confidence.",
        ["One assessment, four reports", "Your report, page by page", "Meet Ananya: a worked example", "Class 6–8: Career Discovery", "Class 9–10: Stream Selection",
         "The 15 career domains", "Class 11–12: Career Planning", "Undergraduates: Employability Readiness", "How to read your report", "Your 90-day plan"],
        "brochure/c11-i-005.png")
S = "Your Report"
DOM = json.load(open(os.path.join(os.path.dirname(__file__), "domains.json")))
Y = '<span class="yes">✓</span>'

mark("One assessment, four reports")
add(head("By stage", "One assessment,", "four reports.",
         "Every report is built only from the student's own answers. What it focuses on changes with the decisions in front of them.")
    + table(["What's in the report", "Class 6–8", "Class 9–10", "Class 11–12", "Undergraduates"], [
        ["Dimension scorecard on one page", Y + " 8–9 dimensions", Y + " 8 dimensions", Y + " 8 dimensions", Y + " 8 readiness areas"],
        ["A deep dive for every dimension", Y, Y, Y, Y], ["Personality type and interest code", Y, Y, Y, Y],
        ["Best-fit fields with a fit %", "Top 5 of 15 domains", "Top 5 of 15 domains", "16 career clusters", "17 career clusters"],
        ["Fitment · Suitability · Selector", "", "", Y + " by stream", Y + " by degree"], ["Your choice vs your result", Y, Y, Y, Y],
        ["Long-term roadmap", "20-year roadmap", "20-year roadmap", "15-step roadmap", "3-year learning roadmap"],
        ["Skill gap vs what jobs need", "", "", "", Y], ["2026–2046 career horizon", "", "", "", Y], ["Entrance / PG exams", "", "Exam awareness", Y + " for your stream", Y + " PG exams"],
        ["What's rising, what's fading (WEF 2025)", Y, Y, Y, Y], ["Learn, find work and get funded", Y, Y, Y, Y], ["A page for parents and mentors", Y, Y, Y, Y], ["PDF download + email copy", Y, Y, Y, Y]],
        widths=["31%", "17%", "17%", "17%", "18%"])
    + two(callout("simple", "Younger students get a report that <b>opens doors</b> (what could I enjoy?). Older students get a report that <b>plans routes</b> (which exam, which degree, which skills?)."),
          callout("good", "The same report powers the <b>Your results</b> pages of your dashboard, so you can explore it on screen too (Part 5)."), "push", gap="4mm"),
    section=S)

mark("Your report, page by page")
pages = [("r11-00", "Cover", "Your name, school, class and date."), ("r11-01", "What's inside", "A map of the report's four sections."), ("r11-02", "Scorecard", "Your real result in each dimension."),
         ("r11-04", "Deep dives", "One page per dimension."), ("r11-11", "Cluster fit", "How you match every career cluster."), ("r11-12", "Path at a glance", "Fitment, Suitability, Selector."),
         ("r11-17", "Future of work", "What's rising and fading."), ("r11-19", "For parents", "How to guide, not decide.")]
add(head("Anatomy", "Your report,", "page by page.", "This is a real Class 11 report, the one our sample student Ananya received. Every report follows the same clear order.")
    + grid([f'<div class="pp"><span class="ppn">{i + 1}</span>{paper("shots/" + f + ".jpg")}<b>{t}</b><span>{x}</span></div>' for i, (f, t, x) in enumerate(pages)], 4, gap="5mm 4mm")
    + callout("simple", "Read it in this order: <b>who you are</b> (scorecard and deep dives), then <b>what fits you</b> (clusters and the three views), then <b>how to get there</b> (roadmap, exams, money), then share the <b>parents' page</b>.", cls="push"),
    section=S)

# ---------------------------------------------------------------- Ananya
mark("Meet Ananya: a worked example")
an = [100, 100, 60, 25, 74, 19, 70, 25]
add(head("Worked example", "Meet Ananya.", "Let's read her report together.",
         "Ananya Rao is a sample Class 11 MPC student we created to show you every screen in this handbook. Her answers were generated for demonstration, so treat her numbers as an example, not a real person's profile.")
    + two(box(h3("Her eight dimensions", "radar") + f'<div class="center">{radar(["Personality", "Interests", "Intelligence", "EQ", "Learning", "Motivators", "Strengths", "Aptitude"], an, "#10B981", 72)}</div>'
              + p("The shape shows where her answers were clearest. Big points: personality, interests, learning style, strengths. Small points: emotional intelligence, motivators, aptitude.", "small")),
          box(h3("What her profile says", "user-round")
              + '<div class="typecard" style="--dc:#10B981"><b>ISFJ</b><span>“The Systematic Organiser”: draws energy from quiet, focused time and prefers structure and planning.</span></div>'
              + table(["Dimension", "Her result"], [["Strongest interest", "Investigative (I): curious, analytical"], ["Top intelligences", "Logical-Mathematical, Interpersonal"], ["Learning style", "Reading/Writing, then hands-on"],
                                                     ["Signature strength", "Creative & innovative"], ["Core motivators", "Creativity, social impact, achievement"]], "dense mt", widths=["42%", "58%"])), ratio="0.95fr 1.05fr", gap="4mm")
    + callout("ananya", "When Ananya first saw “EQ 25”, she worried it meant she was bad with people. It doesn't. It means her answers didn't show a clear pattern yet, and the report suggests small, practical ways to build it. <b>A low score is a starting point, not a verdict.</b>")
    + two(callout("simple", "Look for the <b>2–3 points that stick out</b> on the radar. Those are what make a profile unique. Don't worry about the small ones on day one."),
          callout("try", "Draw your own radar on this page with a pencil, using your scorecard. Compare it with Ananya's: what's different?"), "push", gap="4mm"),
    section="Worked example")

doms = [("Computer Science / IT", 92), ("AI / Data Science", 92), ("Pure Science", 90), ("Research", 89), ("Mathematics / Statistics", 88), ("Biotechnology", 88), ("Engineering", 87), ("Economics", 86)]
add(head("Worked example", "Ananya's best fits", "and her dream career.")
    + two(box(h3("Her top career fields", "target") + hbars([(d, v, "#10B981" if i < 2 else "#6EE7B7") for i, (d, v) in enumerate(doms)], maxv=100, unit="%")
              + p("Computer Science / IT and AI / Data Science tie at the top: both reward an investigative, logical, organised profile.", "small mt")),
          box(h3("Her dream career: Software Engineer", "rocket")
              + '<div class="grid" style="grid-template-columns:repeat(4,1fr);gap:2mm">' + ring(92, "Fits her profile", "#10B981", 16) + ring(85, "Fits her stream", "#0EA5A4", 16) + ring(25, "Aptitude today", "#F59E0B", 16) + ring(67, "Overall fitment", "#065F46", 16) + "</div>"
              + callout("simple", "Her dream career <b>matches</b> her best-fit field. Her profile and stream fit strongly; her aptitude score is the gap to work on, and aptitude grows with practice.")), ratio="1fr 1fr", gap="4mm")
    + two(box(h3("Strengths to use", "trophy") + bullets(["Clear personality (100/100)", "Clear career interest (100/100)", "Learning style (74/100)"], "tight"), "soft"),
          box(h3("Areas to grow", "sprout") + bullets(["Motivator clarity (19/100)", "Aptitude and reasoning (25/100)", "Emotional intelligence (25/100)"], "tight", "arrow-up-right", "#F59E0B"), "soft"), gap="4mm")
    + h3("What Ananya did next", "footprints")
    + steps([("Week 1", "Read 5 careers in Computer Science in the Career Library.", "book-open"), ("Week 2", "Took a Career Test-Drive as a software engineer.", "play"),
             ("Week 3", "Started a JEE Main study plan and a mock test.", "clipboard-list"), ("Week 4", "Joined a free coding programme in Internships.", "laptop")], cols=4),
    section="Worked example")

# ---------------------------------------------------------------- Class 6-8
mark("Class 6–8: Career Discovery")
add(head("Class 6–8 · Career Discovery", "Curiosity first,", "labels never.",
         "At 11 or 12, nobody should pick a career. The Class 6–8 report is shorter and friendlier, and it is built to spark curiosity and good habits.")
    + two(paper("shots/r7-02.jpg", "The Class 6–8 scorecard: every dimension's result at a glance."),
          box(h3("What Class 6–8 students get", "gift") + bullets([
              "About 60 short, age-appropriate questions", "A scorecard across Personality, Career Interest, Strengths, Aptitude, Motivators, Learning Style, Emotional Awareness and Creativity & Innovation",
              "Your personality type and interest code in simple words", "Top 5 career domains out of 15, each with a fit %", "“Your career, in one page”: a profile wheel and best-fit fields",
              "A 20-year roadmap: what to explore now, in school and beyond", "Free resources, and a page for parents"], "tight")), ratio="0.9fr 1.1fr", gap="5mm")
    + h3("Two dimensions made for younger students", "baby")
    + two(card("Emotional Awareness", "Noticing your own feelings and other people's in everyday school and home situations. It grows into full Emotional Intelligence in later editions.", "heart", "#D6336C"),
          card("Creativity & Innovation", "Four indicators: problem-solving, adaptability, innovation and future orientation. How you come up with ideas and handle the new.", "lightbulb", "#F08C00"), gap="4mm")
    + callout("parent", "A Class 7 report is a snapshot of a growing child. Celebrate the strengths, don't worry about the lowest scores, and plan to retake the assessment in Class 9–10.", cls="push"),
    section="Class 6–8")

add(head("Class 6–8 · Career Discovery", "Reading the Class 6–8", "report together.")
    + two(paper("shots/r7-12.jpg", "“Your career, in one page”: the profile wheel and best-fit domains."), paper("shots/r7-15.jpg", "The 20-year roadmap, rising step by step from today."), gap="6mm")
    + h3("What to do with it at this age", "list-checks")
    + cards([("compass", "Explore, don't decide", "Use the top 5 domains as a menu of things to try: clubs, books, videos, visits.", "#F08C00"),
             ("repeat", "Build habits", "The roadmap's first steps are habits: reading, curiosity, money basics, asking good questions.", "#16A34A"),
             ("gamepad-2", "Play the dashboard", "Financial Literacy games, Communication Lab and AI Aware are made for younger students too.", "#7048E8"),
             ("calendar", "Know the early exams", "JNVST (Navodaya, Class 6), AISSEE (Sainik School, Class 6 and 9) and NMMS (Class 8).", "#0EA5E9")], 4, "compact"),
    section="Class 6–8")

# ---------------------------------------------------------------- Class 9-10
mark("Class 9–10: Stream Selection")
add(head("Class 9–10 · Stream Selection", "The first big choice:", "your stream.",
         "After Class 10 every student picks a stream: MPC, BiPC, MEC, CEC, HEC or vocational. It's easier to choose than to change, so the Class 9–10 report makes sure the stream follows the student, not the crowd.")
    + two(paper("shots/r910-02.jpg", "The Class 9–10 scorecard."), paper("shots/r910-11.jpg", "“Your career, in one page”: radar and best-fit domains."), gap="6mm")
    + h3("What Class 9–10 students get", "gift")
    + grid([card(t, x, ic, c) for t, x, ic, c in [
        ("8 dimensions", "About 60 questions, ordered interests and aptitude first.", "radar", "#16A34A"), ("Top 5 domains", "From 15, each with fit % and Strong / Good / Worth exploring.", "target", "#0EA5E9"),
        ("Domain deep dives", "What it is, key roles, skills, how to get in, salary.", "book-open", "#7048E8"), ("Your choice vs your result", "The career you want, compared with your profile.", "git-compare", "#F08C00"),
        ("20-year roadmap", "From the stream choice to long-term growth.", "route", "#E03131"), ("Money and parents", "Scholarships, free courses and a parents' page.", "wallet", "#0C8599")]], 3, "compact"),
    section="Class 9–10")

stream = {"A": "MEC, CEC (any)", "B": "MEC, CEC", "C": "MPC", "D": "MPC (MEC for BCA)", "E": "BiPC", "F": "BiPC", "G": "MPC or BiPC", "H": "MPC (arch.), any (design)", "I": "Any; HEC helps",
          "J": "Any; HEC/CEC helps", "K": "Any; HEC/BiPC helps", "L": "Any", "M": "MPC (NDA, pilot)", "N": "BiPC or MPC", "O": "Any"}
exams = {"A": "IPMAT, CUET-UG", "B": "CUET-UG, CA Foundation", "C": "JEE Main/Adv, BITSAT", "D": "JEE Main, BITSAT, CUET", "E": "NEET-UG", "F": "NEET-UG, ICAR, CUET", "G": "CUET-UG, IISER/NEST",
         "H": "NATA, NID, UCEED, NIFT", "I": "CUET-UG", "J": "CLAT, AILET, CUET", "K": "CUET-UG", "L": "NCHM JEE, CUET", "M": "NDA & NA", "N": "CUET-UG, ICAR", "O": "CUET-UG, sports quotas"}
add(head("Class 9–10 · Stream Selection", "From your top domains", "to a stream.",
         "Find your top domains from the report in the first column. The next columns show the streams that lead there most directly, and the exams you'll meet.")
    + table(["Career domain", "Most direct stream", "Exams you may meet"], [[f"<b>{d['name']}</b>", stream[d["key"]], exams[d["key"]]] for d in DOM], "dense", widths=["40%", "30%", "30%"])
    + two(callout("simple", "<b>M</b>aths <b>P</b>hysics <b>C</b>hemistry · <b>Bi</b>ology <b>P</b>hysics <b>C</b>hemistry · <b>M</b>aths <b>E</b>conomics <b>C</b>ommerce · <b>C</b>ivics <b>E</b>conomics <b>C</b>ommerce · <b>H</b>istory <b>E</b>conomics <b>C</b>ivics."),
          callout("warn", "This is a starting guide. Many degrees accept any stream and rules change, so confirm eligibility on each exam's official site (linked in Entrance Exams)."), "push", gap="4mm"),
    section="Class 9–10")

add(head("Class 9–10 · Stream Selection", "Your roadmap and", "a stream checklist.")
    + two(paper("shots/r910-13.jpg", "Your 20-year roadmap."), paper("shots/r910-14.jpg", "Take the next step: learn, find work and get funded."), gap="6mm")
    + h3("Before you sign the stream form", "clipboard-check")
    + box(check_list(["Our top 2 domains from the report point to this stream", "The student enjoys at least two core subjects of this stream",
                      "We checked aptitude: the maths or biology load is manageable", "We read 3 careers from this stream in the Career Library",
                      "We tried one Career Test-Drive in this stream", "We know the main entrance exam and its eligibility",
                      "We have a backup plan if the first-choice exam doesn't work out", "The decision is the student's, with the family's support"], 2), "soft")
    + callout("parent", "If the report and the family's wish disagree, don't fight. Use the dashboard's <b>Family Decision Room</b> to compare both paths side by side with facts.", cls="push"),
    section="Class 9–10")

mark("The 15 career domains")
cols = ["#E03131", "#F08C00", "#2F9E44", "#1C7ED6", "#D6336C", "#0C8599", "#7048E8", "#E8590C", "#3B5BDB", "#5C940D", "#AE3EC9", "#0B7285", "#495057", "#2B8A3E", "#C92A2A"]
add(head("Reference", "The 15 career", "domains.", "Class 6–10 reports rank these 15 broad fields. Each domain card in the report adds what it is, key roles, skills, how to get in, salary in India and abroad, and future scope.")
    + grid([f'<div class="dom" style="--dc:{cols[i]}"><span>{d["key"]}</span><b>{d["name"]}</b><p>{d["tagline"]}</p><em>{", ".join(d["roles"][:3])}</em><i>{d["salary"].split(" · ")[0].replace(" entry", " to start")}</i></div>' for i, d in enumerate(DOM)], 3, gap="2.6mm")
    + p("Salaries are typical starting ranges in India: indicative, not guarantees.", "small push"),
    section="Career domains")

# ---------------------------------------------------------------- Class 11-12
mark("Class 11–12: Career Planning")
add(head("Class 11–12 · Career Planning", "Four big decisions.", "Two short years.",
         "Subjects, entrance exams, degree and college. The Class 11–12 report answers all four with the same clear picture of the student.")
    + '<div class="grid" style="grid-template-columns:repeat(4,1fr);gap:3mm">' + "".join(f'<div class="dec"><span>{n}</span>{icon(ic, "6mm", "var(--c1)")}<b>{t}</b><p>{x}</p></div>' for n, t, x, ic in [
        ("01", "Subjects", "Which subjects to go deeper in, and why.", "book-open"), ("02", "Entrance exams", "Which exams you can take; which to prepare first.", "clipboard-list"),
        ("03", "Degree", "Courses that fit your strengths, not just marks.", "graduation-cap"), ("04", "College", "Where to apply, the cost, and funding.", "building-2")]) + "</div>"
    + two(paper("shots/r11-01.jpg", "What's inside: four sections, in order."),
          box(h3("What Class 11–12 students get", "gift") + bullets([
              "75 questions: the 8 dimensions plus subject fit, career and stream fit, and career aspiration", "An 8-dimension scorecard and a deep dive per dimension",
              "Career cluster fit across 16 clusters", "Three views: Career Fitment, Career Suitability, Career Selector", "A 15-step roadmap to the career you choose",
              "Entrance exams for your stream with official links", "Funded routes such as NDA, Army 10+2 TES, IIST, apprenticeships", "What's rising and fading, resources and a parents' page"], "tight")), "mt", ratio="0.85fr 1.15fr", gap="5mm"),
    section="Class 11–12")

add(head("Class 11–12 · The heart of the report", "Three ways to see", "your future.",
         "Your report compares what fits you, what fits your stream, and the career you dream of, side by side.")
    + two(paper("shots/r11-11.jpg", "Career cluster fit: how closely you match each of 16 clusters."), paper("shots/r11-12.jpg", "Your career path at a glance: the three views."), gap="6mm")
    + grid([f'<div class="view" style="--vc:{c}"><span>{n}</span><b>{t}</b><em>{q}</em><p>{x}</p></div>' for n, t, q, x, c in [
        ("1", "Career Fitment", "What fits YOU", "Your top 5 career areas, ranked purely by your answers. Each shows key roles, skills to build, salary in India (indicative) and entrance exams.", "#10B981"),
        ("2", "Career Suitability", "What fits your STREAM", "Careers your current stream (MPC, BiPC, MEC, CEC, HEC) already reaches, plus top companies that hire and funded routes.", "#0EA5E9"),
        ("3", "Career Selector", "Your DREAM career", "The career you choose, how well it fits, and the realistic route from Class 11 to senior roles.", "#8B5CF6")]], 3, "mt")
    + callout("simple", "If all three views agree, you have a clear path. If they disagree, that's useful too: it shows exactly what you'd need to build or change to reach your dream.", cls="push"),
    section="Class 11–12")

add(head("Class 11–12 · Career Selector", "Pick your dream career.", "Get the whole route.",
         "Choose the career you want. Your report shows how well it fits, and lays out every step from Class 11 to senior roles.")
    + two(img("brochure/c11-i-139.png", "pic"), img("brochure/c11-i-142.png", "pic"), gap="4mm")
    + '<div class="road15">' + "".join(f'<div><span>{i + 1}</span>{t}</div>' for i, t in enumerate(["Subjects in 11–12", "Entrance exam", "Degree options", "Colleges in India", "Scholarships", "Year-by-year skills", "Internships",
                                                                                                  "First job titles", "PG and study abroad", "Long-term growth"])) + "</div>"
    + callout("example", "For Ananya (MPC → Software Engineer), the selector says: fit 92%. Route: JEE Main / CUET → B.Tech CSE or BCA → build projects and a portfolio from year 1 → internships in year 2–3 → first job as a junior developer.")
    + callout("warn", "A roadmap is a guide, not a guarantee. Entry routes and requirements change; always confirm with the college, exam body or employer.", cls="push"),
    section="Class 11–12")

add(head("Class 11–12 · Also in your report", "Real facts.", "Not guesses.",
         "Every exam and funded programme links to its official source, so you can check it yourself.")
    + two(img("brochure/c11-i-158.png", "pic"), paper("shots/r11-17.jpg", "What's rising, what's fading (WEF 2025)."), gap="5mm")
    + cards([("clipboard-list", "Entrance exams for your stream", "With who conducts them and official links.", "#10B981"), ("landmark", "Funded programmes", "Genuinely funded or stipend-linked routes, checked against official sources.", "#0EA5E9"),
             ("graduation-cap", "Learn, work, get funded", "Free courses (NPTEL, Coursera, edX, Khan Academy), job sites and scholarships.", "#8B5CF6"), ("heart-handshake", "A page for parents", "“Guide, not decide”: simple ways to support.", "#D6336C")], 4, "compact mt"),
    section="Class 11–12")

# ---------------------------------------------------------------- UG
mark("Undergraduates: Employability Readiness")
add(head("Undergraduate edition", "Know your fit.", "Build your career.",
         "Skills, internships, first job and higher study: the undergraduate report covers the four choices to make before graduation.")
    + '<div class="grid" style="grid-template-columns:repeat(4,1fr);gap:3mm">' + "".join(f'<div class="dec"><span>{n}</span>{icon(ic, "6mm", "var(--c1)")}<b>{t}</b><p>{x}</p></div>' for n, t, x, ic in [
        ("01", "Skills", "Which skills to build each year, and which matter most.", "wrench"), ("02", "Internships", "Where to get real experience, and how to make it count.", "laptop"),
        ("03", "First job", "Roles that fit your strengths, not just your degree name.", "briefcase"), ("04", "Higher study", "Whether a PG or study abroad is right, and when.", "graduation-cap")]) + "</div>"
    + two(paper("shots/rug-02.jpg", "The undergraduate scorecard: eight career-readiness areas."),
          box(h3("What undergraduates get", "gift") + bullets([
              "100 questions across 8 areas of career readiness", "A scorecard and a deep dive per area", "Career cluster fit across 17 clusters",
              "Fitment (what fits you), Suitability (what fits your degree), Selector (your target role)", "A skill gap: your level vs what jobs need",
              "Your 2026–2046 career horizon", "PG entrance exams for your field: CAT, CUET-PG, state PGCETs and more", "Learn, find work and get funded; a page for parents and mentors"], "tight")), "mt", ratio="0.85fr 1.15fr", gap="5mm"),
    section="Undergraduate edition")

add(head("Undergraduate edition", "Your clusters and", "your realistic path.")
    + two(paper("shots/rug-11.jpg", "Your career cluster fit across 17 clusters."), paper("shots/rug-12.jpg", "Your career path at a glance."), gap="6mm")
    + h3("The Career Selector's realistic path includes", "route")
    + grid([f'<div class="pill2">{icon("check", "3.4mm", "var(--c1)", 3)} {t}</div>' for t in ["Career overview and horizons", "Three-year learning roadmap", "Technical skills to master", "Portfolio projects", "Skill-gap assessment", "Internship strategy",
                                                                                              "Entry-level job titles", "Employer skill matrix", "Certifications and short courses", "Higher education options", "Specialisations and progression", "Target profile by graduation"]], 3, gap="2mm"),
    section="Undergraduate edition")

add(head("Undergraduate edition", "Know your gaps.", "See 20 years ahead.")
    + two(paper("shots/rug-16.jpg", "Your skill gap: your level (1–5) next to what jobs in your area usually need."), img("brochure/ug-i-147.png", "pic"), gap="5mm")
    + two(box(h3("Reading the skill gap", "gauge") + table(["Mark", "Meaning", "Do this"], [[tag("Ready", "#16A34A"), "At the level jobs need", "Show proof of it"],
                                                                                         [tag("Almost there", "#F08C00"), "A little practice closes it", "One course or project"],
                                                                                         [tag("Needs work", "#DC2626"), "Your clear focus", "Make it this year's goal"]], "dense")),
          box(h3("Your 2026–2046 career horizon", "telescope") + p("Four stages (entry, specialisation, evolution and long-term adaptability) and the skills that matter at each. It shows how your field is likely to change over 20 years, so you can plan to keep up.")
              + callout("simple", "The skill gap is your <b>to-do list for this year</b>. The horizon is your <b>compass for the next twenty</b>.")), "mt", gap="4mm"),
    section="Undergraduate edition")

add(head("Undergraduate edition", "Plan your next step", "with real facts.")
    + two(paper("shots/rug-18.jpg", "PG entrance exams for your field, with what each is for."), paper("shots/rug-20.jpg", "Take the next step: learn, find work and get funded."), gap="6mm")
    + two(box(h3("Free places to learn", "graduation-cap") + table(["Platform", "Good for"], [["NPTEL", "Free courses from the IITs"], ["Coursera / edX", "University courses, many free to audit"], ["freeCodeCamp", "Hands-on coding"], ["Khan Academy", "Maths and science basics"]], "dense")),
          box(h3("Where to find work", "briefcase") + table(["Portal", "Good for"], [["LinkedIn Jobs", "Jobs and networking"], ["Naukri / Indeed", "Indian job listings"], ["Internshala", "Internships"], ["Wellfound", "Startup jobs"]], "dense")), "mt", gap="4mm")
    + band("Your profile shows where you will thrive today, but you are still growing. Revisit your report as you change, and share it with someone who is guiding you.", "This is a map, not a verdict.", "map", "mt push"),
    section="Undergraduate edition")

# ---------------------------------------------------------------- how to read
mark("How to read your report")
add(head("Reading guide", "How to read your report", "in 20 minutes.",
         "Read it in this order the first time. Have a pen and the 90-day plan on the next page ready.")
    + vsteps([("Start with “At a glance” (2 min)", "The scorecard shows your real result in each dimension. Notice the two or three that stand out."),
              ("Read your personality type and interest code (4 min)", "These two explain most of the rest. Ask yourself: does this sound like me?"),
              ("Look at your best-fit fields (4 min)", "Note the top 3 and their fit %. Read why each was matched."),
              ("Compare with your own choice (3 min)", "“Your choice vs your result” or the Career Selector shows how your dream career fits. A gap is not a no; it's a plan to build."),
              ("Read strengths and growth areas (3 min)", "Pick one strength to use and one area to practise this month."),
              ("Read the roadmap and next steps (4 min)", "Circle the very first step. That's your homework for this week.")])
    + two(box(h3("Scores (0–100)", "gauge") + table(["Score", "Label", "Read it as"], [["75–100", tag("Very High", "#16A34A"), "Clear, strong preference or ability"], ["65–74", tag("High", "#16A34A"), "A real strength"],
                                                                                    ["50–64", tag("Medium", "#0EA5E9"), "Balanced either way"], ["35–49", tag("Developing", "#F08C00"), "Not your first instinct yet"], ["0–34", tag("Emerging", "#F08C00"), "Early days; a place to practise"]], "dense")),
          box(h3("Fit % and match labels", "target") + table(["Fit", "Label", "Do this"], [["65%+", tag("Strong match", "#16A34A"), "Explore deeply; test-drive"], ["45–64%", tag("Good match", "#0EA5E9"), "Keep on the list; try a task"],
                                                                                         ["under 45%", tag("Worth exploring", "#F08C00"), "Read about it; stay curious"]], "dense")
              + p("Fit % compares your whole profile with what a field rewards. It is <b>not</b> a probability of success.", "small mt")), "mt", gap="4mm")
    + callout("simple", "In Personality, Learning Style and Motivators a score shows a <b>preference</b>, not quality. Only Aptitude has right answers, and even Aptitude grows with practice.", cls="push"),
    section="Reading guide")

mark("Your 90-day plan")
add(head("Reading guide", "Turn your report into", "a 90-day plan.", "Fill this in with your report open. Keep it on your desk, or photograph it and pin it to your phone.")
    + two(box(h3("My report in one line", "pen-line") + p("My type is ________ · my interest code is ________", "small") + lines(1) + h3("My top 3 fields", "target") + lines(3)),
          box(h3("One strength to use", "trophy") + lines(2) + h3("One area to grow", "sprout") + lines(2)), gap="4mm")
    + table(["When", "Goal", "Dashboard tool I'll use", "Done"], [
        ["<b>Days 1–30</b> · Explore", "Read 5 careers from my top field", "Career Library, Test-Drive", "☐"], ["", "", "", "☐"],
        ["<b>Days 31–60</b> · Do", "One small task or free course", "Internships, AI & Certifications", "☐"], ["", "", "", "☐"],
        ["<b>Days 61–90</b> · Build", "One project or proof", "Portfolio, Career Passport", "☐"], ["", "", "", "☐"]], "mt", widths=["22%", "38%", "32%", "8%"])
    + two(callout("try", "The dashboard's <b>My plan</b> page and weekly <b>Career GPS</b> missions turn this sheet into ticked-off tasks (Part 5)."),
          callout("parent", "Sign the bottom of this page with your child: <span class='hand' style='font-size:13pt'>We agree to try this together.</span>"), "push", gap="4mm"),
    section="Reading guide")
