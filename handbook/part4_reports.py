import json, os
from lib import *

S = "Your Report"
DOM = json.load(open(os.path.join(os.path.dirname(__file__), "domains.json")))

divider(4, "Your Report", "What every class receives, page by page, and how to read it with confidence.",
        ["One assessment, four reports", "Class 6–8: Career Discovery", "Class 9–10: Stream Selection", "The 15 career domains", "Class 11–12: Career Planning", "Undergraduates: Employability Readiness", "How to read your report"],
        image="shots/r11-00.jpg")

mark("One assessment, four reports")
add(head("By stage", "One assessment,", "four reports.",
         "Every report is built only from the student's own answers, but what it focuses on changes with the decisions in front of them.")
    + table(["Report section", "Class 6–8", "Class 9–10", "Class 11–12", "Undergraduates"], [
        ["Dimension scorecard on one page", "✓ 8–9 dimensions", "✓ 8 dimensions", "✓ 8 dimensions", "✓ 8 career-readiness areas"],
        ["Deep dive per dimension", "✓", "✓", "✓", "✓"],
        ["Personality type and interest code", "✓", "✓", "✓", "✓"],
        ["Best-fit fields with a fit %", "Top 5 of 15 domains", "Top 5 of 15 domains", "16 career clusters", "17 career clusters"],
        ["Career Fitment · Suitability · Selector", "", "", "✓ (by stream)", "✓ (by degree)"],
        ["Your choice vs your result", "✓", "✓", "✓ Career Selector", "✓ Career Selector"],
        ["Long-term roadmap", "20-year roadmap", "20-year roadmap", "15-step roadmap to your goal", "3-year learning roadmap"],
        ["Skill gap vs what jobs need", "", "", "", "✓"],
        ["2026–2046 career horizon", "", "", "", "✓"],
        ["Entrance / PG exams", "", "Exam awareness", "✓ for your stream", "✓ PG entrance exams"],
        ["What's rising, what's fading (WEF 2025)", "✓", "✓", "✓", "✓"],
        ["Learn, find work and get funded", "✓", "✓", "✓", "✓"],
        ["A page for parents and mentors", "✓", "✓", "✓", "✓"],
        ["PDF download and email copy", "✓", "✓", "✓", "✓"]], widths=["31%", "17%", "17%", "17%", "18%"])
    + note("Delivered instantly:", "see it on screen, download the PDF, and get a copy by email. The same report also powers the “Your results” pages in the dashboard.", "push"),
    section=S)

# ---------------------------------------------------------------- Class 6-8
mark("Class 6–8: Career Discovery")
add(head("Class 6–8 · Career Discovery", "Curiosity first,", "labels never.",
         "For students beginning the journey. The Class 6–8 edition is shorter, friendlier and built to spark curiosity, not to pick a career at 11.")
    + two(shot("shots/r7-02.jpg", "The Class 6–8 scorecard: every dimension's real result, at a glance."),
          box(h3("What Class 6–8 students get") + bullets([
              "About 60 short, age-appropriate questions",
              "A scorecard across Personality, Career Interest, Strengths, Aptitude, Motivators, Learning Style, Emotional Awareness and Creativity & Innovation",
              "Your four-letter personality type and three-letter interest code, in simple words",
              "Top 5 career domains from 15, each with a fit %",
              "“Your career, in one page”: a profile wheel and best-fit fields",
              "A 20-year roadmap: what to explore now, in school and beyond",
              "Free resources, and a page for parents"], "tight")), ratio="1fr 1fr")
    + h3("Two dimensions made for younger students")
    + two(box("<h4>Emotional Awareness</h4>" + p("Noticing your own feelings and other people's, in everyday school and home situations. It grows into full Emotional Intelligence in later editions.", "small")),
          box("<h4>Creativity & Innovation</h4>" + p("Four indicators: problem-solving, adaptability, innovation and future orientation. How you come up with ideas and handle the new.", "small"))),
    section="Class 6–8")

add(head("Class 6–8 · Career Discovery", "Reading the Class 6–8", "report together.")
    + two(shot("shots/r7-12.jpg", "“Your career, in one page”: the profile wheel and best-fit domains."),
          shot("shots/r7-14.jpg", "The 20-year roadmap, rising step by step from today."))
    + h3("What to do with it at this age")
    + cards([("Explore, don't decide", "Use the top 5 domains as a menu of things to try: clubs, books, videos, visits."),
             ("Build habits", "The roadmap's first steps are habits: reading, curiosity, money basics, asking good questions."),
             ("Try the dashboard tools", "Financial Literacy, Communication Lab and AI Aware are built for younger students too."),
             ("Watch for exams", "JNVST (Navodaya, Class 6), AISSEE (Sainik School, Class 6 and 9) and NMMS (Class 8) are in Entrance Exams.")], 2)
    + note("For parents:", "a Class 7 report is a snapshot of a growing child. Celebrate the strengths, don't worry about the lowest scores, and plan to retake the assessment in Class 9–10.", "push"),
    section="Class 6–8")

# ---------------------------------------------------------------- Class 9-10
mark("Class 9–10: Stream Selection")
add(head("Class 9–10 · Stream Selection", "The first big choice:", "your stream.",
         "After Class 10, students pick a stream: MPC, BiPC, MEC, CEC, HEC or vocational. The Class 9–10 report shows which fields fit, so the stream follows the student, not the crowd.")
    + two(shot("shots/r910-02.jpg", "The Class 9–10 scorecard: eight dimensions with the real result in each."),
          box(h3("What Class 9–10 students get") + bullets([
              "About 60 questions across the 8 dimensions, ordered interests and aptitude first",
              "Your personality type, interest code and signature strengths",
              "Top 5 career domains from 15, each with a fit % and Strong / Good / Worth exploring",
              "What each domain is, its key roles, skills, how to get in and salary ranges",
              "“Your choice vs your result”: the career you want, compared with your profile",
              "A 20-year roadmap and next steps for this year",
              "Scholarships, free courses and a parents' page"], "tight")), ratio="1fr 1fr")
    + band("Why it matters", "A stream is easier to choose than to change. Two calm conversations now, with the report on the table, save years later.", "navy push"),
    section="Class 9–10")

stream = {"A": "MEC, CEC (any stream welcome)", "B": "MEC, CEC", "C": "MPC", "D": "MPC (MEC for BCA)", "E": "BiPC", "F": "BiPC", "G": "MPC or BiPC",
          "H": "MPC for architecture; any for design", "I": "Any; HEC helps", "J": "Any; HEC or CEC helps", "K": "Any; HEC or BiPC helps", "L": "Any",
          "M": "MPC (NDA, pilot)", "N": "BiPC or MPC", "O": "Any"}
add(head("Class 9–10 · Stream Selection", "From your top domains", "to a stream.",
         "Find your top domains from the report in the left column. The middle column shows the streams that most directly lead there.")
    + table(["Career domain", "Streams that lead there most directly", "Entrance exams you may meet"], [
        [f"<b>{d['name']}</b>", stream[d["key"]], {"A": "IPMAT, CUET-UG", "B": "CUET-UG, CA Foundation", "C": "JEE Main, JEE Advanced, BITSAT", "D": "JEE Main, BITSAT, CUET-UG",
                                                    "E": "NEET-UG", "F": "NEET-UG, ICAR AIEEA, CUET-UG", "G": "CUET-UG, IISER/NEST", "H": "NATA, JEE Paper 2, NID DAT, UCEED, NIFT",
                                                    "I": "CUET-UG", "J": "CLAT, AILET, CUET-UG", "K": "CUET-UG", "L": "NCHM JEE, CUET-UG", "M": "NDA & NA",
                                                    "N": "CUET-UG, ICAR AIEEA", "O": "CUET-UG, sports quotas"}[d["key"]]] for d in DOM], "dense", widths=["34%", "34%", "32%"])
    + note("Good to know:", "this table is a starting guide. Many degrees accept any stream, and rules change, so confirm eligibility on each exam's official site (Entrance Exams in your dashboard links to them).", "push"),
    section="Class 9–10")

add(head("Class 9–10 · Stream Selection", "Your roadmap and", "a stream checklist.")
    + two(shot("shots/r910-13.jpg", "Your 20-year roadmap: from the stream choice to long-term growth."),
          shot("shots/r910-14.jpg", "Take the next step: learn, find work and get funded."))
    + h3("Before you sign the stream form")
    + '<div class="grid g2">' + "".join(f'<div class="check"><i></i><span>{t}</span></div>' for t in [
        "Our top 2 domains from the report point to this stream", "The student enjoys at least two core subjects of this stream",
        "We checked aptitude: the stream's maths or biology load is manageable", "We read 3 careers from this stream in the Career Library",
        "We tried one Career Test-Drive for a career in this stream", "We know the main entrance exam and its eligibility",
        "We have a backup plan if the first-choice exam doesn't work out", "The decision is the student's, with the family's support"]) + '</div>',
    section="Class 9–10")

# ---------------------------------------------------------------- 15 domains
mark("The 15 career domains")
add(head("Reference", "The 15 career", "domains.",
         "Class 6–10 reports rank these 15 broad fields. In the report, each card adds what the domain is, key roles, skills, how to get in, salary in India and abroad, and future scope.")
    + table(["Domain", "In one line", "Example roles", "Entry pay (India)"],
            [[f"<b>{d['key']}. {d['name']}</b>", d["tagline"], ", ".join(d["roles"][:3]), d["salary"].split(" · ")[0].replace(" entry", "")] for d in DOM], "dense", widths=["24%", "32%", "28%", "16%"])
    + note("Salaries:", "typical entry-level ranges, indicative for India and not guarantees.", "push"),
    section="Career domains")

# ---------------------------------------------------------------- Class 11-12
mark("Class 11–12: Career Planning")
add(head("Class 11–12 · Career Planning", "Four big decisions.", "Two short years.",
         "Subjects, entrance exams, degree and college. The Class 11–12 report answers all four with the same clear picture of the student.")
    + two(shot("shots/r11-01.jpg", "What's inside: your eight dimensions, careers that fit you, your path and plan, resources and scholarships."),
          box(h3("What Class 11–12 students get") + bullets([
              "75 questions: the 8 dimensions plus subject fit, career and stream fit, and career aspiration",
              "An 8-dimension scorecard and a deep dive per dimension",
              "Career cluster fit across 16 clusters",
              "Three views: Career Fitment, Career Suitability, Career Selector",
              "A 15-step roadmap to the career you choose",
              "Entrance exams for your stream with official links",
              "Funded routes (NDA, Army 10+2 TES, IIST, apprenticeships)",
              "What's rising and fading (WEF 2025), resources and a parents' page"], "tight")), ratio="1fr 1fr"),
    section="Class 11–12")

add(head("Class 11–12 · Career Planning", "Your scorecard", "and the deep dives.")
    + two(shot("shots/r11-02.jpg", "Your eight-dimension scorecard: the real, specific result in each dimension."),
          shot("shots/r11-05.jpg", "A deep dive: score, what it means for you, where you are strong, where to grow, next steps."))
    + h3("Every deep-dive page has the same five parts")
    + '<div class="flow">' + "".join(f"<div><b>{a}</b>{b}</div>" for a, b in [("Score", "0–100 with a typical-student marker"), ("Meaning", "In plain words"), ("Strong", "Where you shine"), ("Grow", "Where to practise"), ("Next steps", "Three actions")]) + "</div>",
    section="Class 11–12")

add(head("Class 11–12 · The heart of the report", "Three ways to see", "your future.",
         "Your report compares what fits you, what fits your stream, and the career you dream of, side by side.")
    + two(shot("shots/r11-11.jpg", "Your career cluster fit: how closely you match each of 16 clusters."),
          shot("shots/r11-12.jpg", "Your career path at a glance: Fitment, Suitability and Selector."))
    + cards([("1", "Career Fitment · what fits you", "Your top 5 career areas, ranked purely by your answers. Each shows key roles, skills to build, salary range in India (indicative) and entrance exams to know."),
             ("2", "Career Suitability · what fits your stream", "The same areas, kept to careers your current stream (MPC, BiPC, MEC, CEC or HEC) already reaches, plus top companies that hire and funded routes."),
             ("3", "Career Selector · your dream career", "The career you choose, how well it fits, and the realistic route from Class 11 to senior roles.")], 3, "compact mt"),
    section="Class 11–12")

add(head("Class 11–12 · Career Selector", "Pick your dream career.", "Get the whole route.",
         "Choose the career you want. Your report shows how well it fits, and lays out every step from Class 11 to senior roles.")
    + two(img("brochure/c11-i-139.png", "pic"), img("brochure/c11-i-142.png", "pic"))
    + table(["Step", "What it covers"], [
        ["Subjects and entrance exams", "What to choose now, and which exams lead there"],
        ["Degrees, colleges and scholarships", "Top colleges in India and the money to study"],
        ["Skills, internships and jobs", "What to build each year, and first job titles"],
        ["PG and specialisation", "Where to go further"],
        ["Study or work abroad", "Requirements and routes"],
        ["Career progression", "How the career grows over time"]], "mt", widths=["38%", "62%"])
    + note("A guide, not a guarantee:", "entry routes and requirements change. Confirm with the college, exam body or employer.", "push"),
    section="Class 11–12")

add(head("Class 11–12 · Also in your report", "Real facts.", "Not guesses.",
         "Every exam and funded programme links to its official source, so you can check it yourself.")
    + two(img("brochure/c11-i-158.png", "pic"), shot("shots/r11-17.jpg", "What's rising, what's fading: based on the WEF Future of Jobs Report 2025."))
    + cards([("Entrance exams for your stream", "With who conducts them and official links."),
             ("Funded programmes", "Genuinely funded or stipend-linked routes, checked against official sources."),
             ("Learn, find work and get funded", "Free courses, job sites and scholarships to apply for."),
             ("A page for parents", "“Guide, not decide”: simple ways to support your child.")], 4, "compact mt"),
    section="Class 11–12")

# ---------------------------------------------------------------- UG
mark("Undergraduates: Employability Readiness")
add(head("Undergraduate edition", "Know your fit.", "Build your career.",
         "Skills, internships, first job and higher study: the undergraduate report covers the four choices to make before graduation.")
    + two(shot("shots/rug-02.jpg", "Your eight-area scorecard: personality, interests, cognitive capability, domain fit and four readiness areas."),
          box(h3("What undergraduates get") + bullets([
              "100 questions across 8 areas of career readiness",
              "A scorecard and a deep dive per area",
              "Career cluster fit across 17 clusters",
              "Fitment (what fits you), Suitability (what fits your degree) and Selector (your target role)",
              "A skill gap: your level vs what jobs need",
              "Your 2026–2046 career horizon",
              "PG entrance exams for your field (CAT, CUET-PG, state PGCETs and more)",
              "Learn, find work and get funded; a page for parents and mentors"], "tight")), ratio="1fr 1fr"),
    section="Undergraduate edition")

add(head("Undergraduate edition", "Your clusters and", "your realistic path.")
    + two(shot("shots/rug-11.jpg", "Your career cluster fit across 17 clusters."), shot("shots/rug-12.jpg", "Your career path at a glance: Fitment, Suitability, Selector."))
    + h3("The Career Selector's realistic path includes")
    + '<div class="cols3 small">' + bullets(["Career overview and horizons", "Three-year learning roadmap", "Technical skills to master", "Portfolio projects", "Skill-gap assessment", "Internship strategy",
                                             "Entry-level job titles", "Employer skill matrix", "Certifications and short courses", "Higher education options", "Specialisations and progression", "Target profile by graduation"], "tight") + '</div>',
    section="Undergraduate edition")

add(head("Undergraduate edition", "Know your gaps.", "See 20 years ahead.")
    + two(shot("shots/rug-16.jpg", "Your skill gap: your level for each skill (1–5) next to what jobs in your area usually need."),
          img("brochure/ug-i-147.png", "pic"))
    + two(box(h3("Reading the skill gap") + table(["Mark", "Meaning", "Do this"], [
        ['<span class="tag g">Ready</span>', "At the level jobs need", "Show proof of it"],
        ['<span class="tag a">Almost there</span>', "A little practice closes it", "One course or project"],
        ['<span class="tag r">Needs work</span>', "Your clear focus", "Make it this year's goal"]])),
          box(h3("Your 2026–2046 career horizon") + p("Four stages (entry, specialisation, evolution and long-term adaptability) with the skills that matter at each. It shows how your field is likely to change over 20 years, so you can plan to keep up.")), "mt"),
    section="Undergraduate edition")

add(head("Undergraduate edition", "Plan your next step", "with real facts.")
    + two(shot("shots/rug-18.jpg", "PG entrance exams for your field, with what each one is for."), shot("shots/rug-20.jpg", "Take the next step: learn, find work and get funded."))
    + band("This is a map, not a verdict", "Your profile shows where you will thrive today, but you are still growing. Revisit your report as you change, and share it with someone who is guiding you.", "navy push"),
    section="Undergraduate edition")

# ---------------------------------------------------------------- how to read
S = "How to read your report"
mark("How to read your report")
add(head("Reading guide", "How to read your report", "in 20 minutes.",
         "Read your report in this order the first time. Have a pen and the action plan on page 2 of this guide ready.")
    + steps([("Start with “At a glance” (2 min)", "The scorecard shows your real result in each dimension. Notice the two or three that stand out."),
             ("Read your personality type and interest code (4 min)", "These two explain most of the rest. Ask: does this sound like me?"),
             ("Look at your best-fit fields (4 min)", "Note the top 3 and their fit %. Read why each was matched."),
             ("Compare with your own choice (3 min)", "“Your choice vs your result” or the Career Selector shows how your dream career fits. A gap is not a no; it is a plan to build."),
             ("Read strengths and growth areas (3 min)", "Pick one strength to use and one area to practise this month."),
             ("Read the roadmap and next steps (4 min)", "Circle the very first step. That is your homework for this week.")])
    + note("Then share it:", "read the parents' page together and talk through the questions in Part 8 of this handbook.", "push"),
    section=S)

add(head("Reading guide", "What the scores", "and labels mean.")
    + two(box(h3("Dimension scores (0–100)") + table(["Score", "Label", "Read it as"], [
        ["75–100", '<span class="tag g">Very High</span>', "A clear, strong preference or ability"],
        ["65–74", '<span class="tag g">High</span>', "A real strength"],
        ["50–64", '<span class="tag b">Medium</span>', "Balanced; you can go either way"],
        ["35–49", '<span class="tag a">Developing</span>', "Not your first instinct; can grow"],
        ["0–34", '<span class="tag a">Emerging</span>', "Early days; a place to practise"]])
        + p("A <b>typical-student marker</b> shows where most students at your stage score, so you can see whether you are well above, about, or below typical.", "small mt")),
          box(h3("Fit % and match labels") + table(["Fit", "Label", "What to do"], [
              ["65% +", '<span class="tag g">Strong match</span>', "Explore deeply; test-drive it"],
              ["45–64%", '<span class="tag b">Good match</span>', "Keep on the list; try a task"],
              ["below 45%", '<span class="tag a">Worth exploring</span>', "Read about it; stay curious"]])
              + p("Fit % compares your whole profile with what a career field rewards. It is not a probability of success.", "small mt")))
    + h3("Three rules for reading any score")
    + cards([("Higher isn't always better", "In Personality, Learning Style and Motivators a score shows a preference, not quality. A 50 means balanced, not average."),
             ("Look at patterns, not one number", "The best careers sit where several dimensions agree: interests, strengths and aptitude."),
             ("Only Aptitude has right answers", "And even Aptitude improves with regular, timed practice.")], 3),
    section=S)

add(head("Reading guide", "Personality types and", "interest codes, decoded.")
    + two(box(h3("Your four-letter type") + table(["Letter", "Means", "Opposite"], [
        ["E", "Extravert: energy from people", "I: Introvert, energy from quiet"], ["S", "Sensing: facts and details", "N: Intuition, patterns and ideas"],
        ["T", "Thinking: logic first", "F: Feeling, values and people first"], ["J", "Judging: likes a plan", "P: Perceiving, keeps options open"]], "dense")
        + p("Example: <b>ISFJ, “The Defender”</b> is quiet, practical, caring and organised. <b>ENFP, “The Campaigner”</b> is outgoing, imaginative, warm and flexible.", "small mt")),
          box(h3("Your three-letter interest code") + table(["Letter", "Theme", "Archetype"], [
              ["R", "Realistic: doing", "The Hands-On Builder"], ["I", "Investigative: thinking", "The Analytical Investigator"], ["A", "Artistic: creating", "The Creative Originator"],
              ["S", "Social: helping", "The Helper"], ["E", "Enterprising: leading", "The Persuader"], ["C", "Conventional: organising", "The Organiser"]], "dense")
              + p("Example: <b>IRA</b> = Investigative first, then Realistic, then Artistic. The first letter matters most.", "small mt")))
    + shot("shots/res-profile.jpg", "In the dashboard, “Your profile” shows your type, interest code, top field and fit at a glance.", "mt"),
    section=S)

add(head("Reading guide", "Turn your report into", "a 90-day plan.",
         "Fill this in with your report open. Keep it on your desk, or photograph it and pin it to your phone.")
    + '<div class="worksheet">'
    + two(box(h3("My report in one line") + p("My type is ______  ·  my interest code is ______", "small") + '<div class="line"></div>' + h3("My top 3 fields") + '<div class="line"></div><div class="line"></div><div class="line"></div>'),
          box(h3("One strength to use") + '<div class="line"></div><div class="line"></div>' + h3("One area to grow") + '<div class="line"></div><div class="line"></div>'))
    + table(["When", "Goal", "Dashboard tool I'll use", "Done"], [
        ["Days 1–30", "Explore: read 5 careers from my top field", "Career Library, Test-Drive", "☐"],
        ["", "", "", "☐"],
        ["Days 31–60", "Do: one small task or course", "Internships, AI & Certifications", "☐"],
        ["", "", "", "☐"],
        ["Days 61–90", "Build: one project or proof", "Portfolio, Career Passport", "☐"],
        ["", "", "", "☐"]], "mt", widths=["16%", "42%", "34%", "8%"])
    + '</div>'
    + note("Tip:", "the dashboard's <b>My plan</b> page and weekly <b>Career GPS</b> missions turn this sheet into ticked-off tasks (see Part 5).", "push"),
    section=S)
