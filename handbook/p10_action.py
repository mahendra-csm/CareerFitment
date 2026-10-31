from lib import *

THEMES["action"] = ("Your Action Plan", "#F59E0B", "#EF4444", "#FFF7E6", "#92400E")
divider(10, "action", "Your Action Plan", "Reading changes nothing. Doing does. This part is your workbook: a 30-day kickstart, a month-by-month plan for your stage, and trackers to keep you going all year.",
        ["The 30-day kickstart challenge", "Your year: Class 6–10", "Your year: Class 11–12", "Your 90-day plan", "My profile on one page", "My weekly tracker", "My achievements and certificates"],
        "feat/progress.webp")
S = "Your Action Plan"

days = [
    ("Sign in and open every menu item", "Dashboard"), ("Read your full report once", "Report"), ("Fill in page 2 of this book", "Handbook"), ("Read Your profile and 8 Dimensions", "Your results"),
    ("Tick one “next 30 days” item", "My plan"), ("Read 5 careers in your top field", "Career Library"), ("Test-drive your #1 career", "Career Library"),
    ("Talk to your family using 2 questions (Part 9)", "Family"), ("Fill your exam profile", "Entrance Exams"), ("Follow 2 exams; write their dates", "Entrance Exams"),
    ("Fill your scholarship profile", "Scholarships"), ("Shortlist 5 scholarships", "Scholarships"), ("Finish Money Level 1", "Financial Literacy"), ("Play Safe or Scam", "Scam Shield"),
    ("Week 2 review: fill the tracker", "Handbook"), ("Save the emergency helplines", "Law & Rights"), ("Read 2 rights guides for your age", "Law & Rights"),
    ("Start AI Aware", "AI & Certifications"), ("Do the 1-minute speaking challenge", "Communication Lab"), ("Speaking challenge, day 2", "Communication Lab"),
    ("Start one free internship programme", "Internships"), ("Do this week's 3 GPS missions", "Career GPS"), ("Week 3 review: fill the tracker", "Handbook"),
    ("Write your 60-second introduction", "Communication Lab"), ("Start your resume or portfolio", "Resume · Website"), ("Add 2 achievements to your Passport", "Career Passport"),
    ("Finish research unit 1 or startup module 1", "Research · Startups"), ("Make a study plan for exam #1", "Entrance Exams"), ("Check My Progress; continue one course", "My Progress"),
    ("Celebrate! Plan the next 30 days", "Handbook")]
for half in (0, 1):
    if half == 0:
        mark("The 30-day kickstart challenge")
    tiles = "".join(f'<div class="day"><span>DAY {i + 1}</span><b>{t}</b><em>{tool}</em><i></i></div>' for i, (t, tool) in enumerate(days) if (i < 15) == (half == 0))
    add(head("Kickstart", "The 30-day", f"kickstart challenge ({half + 1}/2).",
             "One small action a day, about 15 minutes. Tick the box when it's done. By day 30 you'll have used the whole dashboard and built real proof." if half == 0 else "Halfway there. Keep the streak going; a missed day is fine, two in a row is a habit breaker.")
        + f'<div class="days">{tiles}</div>'
        + two(callout("parent", "Sit with your child for Days 2, 8 and 30. Ten minutes of interest from you matters more than any tool.") if half == 0 else callout("try", "Photograph these two pages when you finish and share them with a teacher or mentor."),
              box(f'<div class="streak"><b>My streak</b>' + "".join(f"<i>{d}</i>" for d in range(1 + half * 15, 16 + half * 15)) + "</div>", "soft"), "push", gap="4mm"),
        section=S)

mark("Your year: Class 6–10")
add(head("Your year", "Class 6–10:", "a plan for every term.", "Typical timings. Exam and scholarship dates change every year, so always confirm on official websites.")
    + two(box(h3("Class 6–8 · Career Discovery", "sparkles")
              + table(["When", "Do this", "Tool"], [["Term 1", "Take the assessment; read the report with parents; explore 3 domains", "Report · Career Library"],
                                                   ["Term 1", "Money Level 1–2; play Money Life", "Financial Literacy"], ["Term 2", "Communication Lab track; 1-minute challenges", "Communication Lab"],
                                                   ["Term 2", "AI Aware; one Scratch or Teachable Machine project", "AI & Certifications"], ["Term 3", "One hobby project; add it to your Passport", "Career Passport"],
                                                   ["Class 5–6", "JNVST (Navodaya) / AISSEE (Sainik) if relevant", "Entrance Exams"], ["Class 8", "NMMS scholarship exam (usually Nov–Dec)", "Exams · Scholarships"]], "dense", ["16%", "56%", "28%"])),
          box(h3("Class 9–10 · Stream Selection", "git-fork")
              + table(["When", "Do this", "Tool"], [["Class 9 start", "Take the assessment; note your top 5 domains", "Report"], ["Class 9", "Read 3 careers per top domain; 2 Test-Drives", "Career Library"],
                                                   ["Class 9", "Olympiads / NSEJS practice; aptitude puzzles weekly", "Entrance Exams"], ["Class 10 Term 1", "Stream map (Part 4); Decision Room with family", "Career Library"],
                                                   ["Class 10 Term 2", "Board-exam plan using your learning style", "Exams planner"], ["Before Class 11", "Confirm stream; list target exams; find scholarships", "Exams · Scholarships"],
                                                   ["All year", "3 GPS missions a week", "Career GPS"]], "dense", ["18%", "54%", "28%"])), gap="4mm")
    + h3("My goals this year", "flag")
    + grid([f'<div class="goal"><b>{t}</b>{lines(2)}</div>' for t in ["Term 1", "Term 2", "Term 3"]], 3, gap="4mm"),
    section=S)

mark("Your year: Class 11–12")
months = [("Apr–Jun", "Take the assessment; choose target exams; set up exam & scholarship profiles", "Settle subjects; read Career Selector roadmap"),
          ("Jul–Sep", "Study planner live; weekly mocks; one internship or AI course", "Follow exam notifications; NDA forms if relevant"),
          ("Oct–Dec", "NSE olympiads (Nov); research or startup project", "JEE Main registration (usually Nov); CLAT (Dec); scholarship deadlines"),
          ("Jan–Mar", "School exams; finish a project; communication practice", "JEE Main (Jan); board exams (Feb–Mar); NEET / CUET registration"),
          ("Apr–May", "Summer internship; portfolio website", "JEE Main (Apr); NEET, CUET, JEE Advanced (May)"),
          ("Jun–Jul", "Plan Class 12; update your report", "Counselling (JoSAA etc.); apply for college scholarships")]
add(head("Your year", "Class 11–12:", "two years, month by month.", "Typical timings for the major exams. Dates change every year; confirm everything on the official websites linked in Entrance Exams.")
    + table(["Months", "Class 11 · build", "Class 12 · decide and apply"], [[f"<b>{m}</b>", a, b] for m, a, b in months], "", ["14%", "43%", "43%"])
    + two(box(h3("My target exams", "clipboard-list") + table(["Exam", "Registration", "Exam date"], [["&nbsp;", "", ""], ["&nbsp;", "", ""], ["&nbsp;", "", ""]], "fill")),
          box(h3("My backup plan", "life-buoy") + p("If my first-choice exam doesn't go my way, my next best route is:", "small") + lines(3)), "mt", gap="4mm")
    + callout("parent", "Class 12 is stressful. Use Entrance Exams › Wellbeing together, and remember the backup plan is a real plan, not a failure.", cls="push"),
    section=S)

mark("Your 90-day plan")
add(head("Reading guide", "Turn your report into", "a 90-day plan.", "Fill this in with your report open. Keep it on your desk, or photograph it and pin it to your phone.")
    + two(box(h3("My report in one line", "pen-line") + p("My type is ________ · my interest code is ________", "small") + lines(1) + h3("My top 3 fields", "target") + lines(3)),
          box(h3("One strength to use", "trophy") + lines(2) + h3("One area to grow", "sprout") + lines(2)), gap="4mm")
    + table(["When", "Goal", "Dashboard tool I'll use", "Done"], [
        ["<b>Days 1–30</b> · Explore", "Read 5 careers from my top field", "Career Library, Test-Drive", "☐"], ["", "", "", "☐"],
        ["<b>Days 31–60</b> · Do", "One small task or free course", "Internships, AI & Certifications", "☐"], ["", "", "", "☐"],
        ["<b>Days 61–90</b> · Build", "One project or proof", "Portfolio, Career Passport", "☐"], ["", "", "", "☐"]], "mt", widths=["22%", "38%", "32%", "8%"])
    + two(callout("try", "The dashboard's <b>My plan</b> page and weekly <b>Career GPS</b> missions turn this sheet into ticked-off tasks (Parts 5 and 6)."),
          callout("parent", "Sign the bottom of this page with your child: <span class='hand' style='font-size:13pt'>We agree to try this together.</span>"), "push", gap="4mm"),
    section=S)

mark("My profile on one page")
add(head("Workbook", "My profile", "on one page.", "Copy your results from your report. This is the page to show a counsellor, teacher or interviewer.")
    + two(box(h3("My eight dimensions", "radar") + table(["Dimension", "My result"], [[d, ""] for d in ["Personality type", "Interest code", "Top intelligences", "Emotional intelligence", "Learning style", "Core motivator", "Signature strengths", "Aptitude: sharpest area"]], "fill")),
          box(h3("Draw my radar", "pencil") + f'<div class="center">{radar(["Pers.", "Interests", "Intell.", "EQ", "Learning", "Motiv.", "Strengths", "Aptitude"], [0] * 8, "#F59E0B", 66)}</div>' + p("Mark each score on its spoke (0 centre, 100 edge) and join the dots.", "small"), "soft"), gap="4mm")
    + two(box(h3("My top 3 fields and fit %", "target") + lines(3)), box(h3("My dream career and its fit", "rocket") + lines(3)), "mt", gap="4mm")
    + two(box(h3("3 strengths I'll use", "trophy") + lines(3)), box(h3("3 areas I'll grow", "sprout") + lines(3)), "mt", gap="4mm"),
    section=S)

mark("My weekly tracker")
add(head("Workbook", "My weekly", "tracker.", "Plan on Sunday, tick through the week. Copy this page if you run out.")
    + table(["Week", "My goal", "Tool", "Done ✓", "What I learned"], [[f"<b>{w}</b>", "", "", "☐", ""] for w in ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8"]], "fill", ["12%", "32%", "18%", "10%", "28%"])
    + h3("My daily habits", "repeat")
    + table(["Habit", "M", "T", "W", "T", "F", "S", "S"], [[h] + ["☐"] * 7 for h in ["1-minute speaking challenge", "20 minutes focused study", "Read about one career", "Log what I spent", "No phone for the first hour"]], "fill", ["37%"] + ["9%"] * 7),
    section=S)

mark("My achievements and certificates")
add(head("Workbook", "My achievements", "and certificates.", "Everything you earn goes here, and into your Career Passport with proof.")
    + table(["Date", "What I achieved / earned", "Proof (link or certificate ID)", "Verified ✓", "In Passport ✓"], [["&nbsp;", "", "", "☐", "☐"] for _ in range(14)], "fill", ["12%", "36%", "30%", "11%", "11%"])
    + callout("try", "Aim for at least one line a month. In a year, this page becomes the strongest part of any application.", cls="push"),
    section=S)
# ---------------------------------------------------------------- back cover
theme("brand")
add(f'''<div class="bk">
<div class="dv-dots"></div><div class="dv-blob b1"></div>
<div class="bk-logo">{img("art/logo.png")}</div>
<div class="bk-t"><div class="cv-kick" style="color:#FFC83D">The view from every seat</div>
<h1>Know yourself.<br>Choose with confidence.<br><span>Build your future.</span></h1></div>
<div class="bk-photos">{"".join(f'<div>{img("gallery/" + g)}</div>' for g in ("new1.webp", "old13.webp", "new5.webp", "old02.webp"))}</div>
<div class="bk-stats">{stats([("3,000+", "students assessed"), ("10+", "schools and colleges"), ("2,500+", "career roadmaps"), ("8", "dimensions measured")], "glass")}</div>
<div class="bk-cta">{img("art/qr.png", "bk-qr")}<div><div class="kicker" style="color:#E5383B">Take the assessment today</div>
<div class="bk-url">careerfitment.onegrasp.com</div>
<p>{icon("mail", "4mm", "#1E2340")} support@onegrasp.com &nbsp; {icon("phone", "4mm", "#1E2340")} +91 89777 60442 / 43 &nbsp; {icon("globe", "4mm", "#1E2340")} onegrasp.com/events</p>
<p class="small">OneGrasp Education Pvt. Ltd., Hyderabad, India</p></div></div>
<div class="bk-foot">© 2026 OneGrasp. Salaries are indicative ranges for India. All logos and trademarks belong to their respective owners.</div></div>''', kind="back")
