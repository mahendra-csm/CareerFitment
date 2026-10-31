from lib import *

divider(1, "meet", "Meet OneGrasp", "Who we are, what we do, and why we built a career assessment that looks far beyond marks.",
        ["What is OneGrasp?", "Everything OneGrasp does", "Why career choices go wrong", "Myths and facts", "The future of work", "Your journey with OneGrasp", "An assessment day on campus", "Real schools, real students"],
        "brochure/ug-i-001.png")
S = "Meet OneGrasp"

mark("What is OneGrasp?")
add(head("About us", "What is", "OneGrasp?",
         "OneGrasp Education Pvt. Ltd. is an education company based in Hyderabad, India. We help students, families, professionals and institutions make better decisions about learning and work.")
    + two(callout("simple", "OneGrasp is like a <b>GPS for your career</b>. First it finds where you are today (your strengths, interests and personality). Then it shows the roads that suit you, and finally it gives you turn-by-turn directions: subjects, exams, colleges, skills, money and jobs.")
          + p("Our best-known product is the <b>Career Fitment Assessment</b>: a psychometric career assessment for students from Class 6 to undergraduates. It measures eight dimensions of a student and turns them into a personal report and a dashboard of more than twenty tools.")
          + p("Around the assessment, OneGrasp runs international scientific conferences, startup and entrepreneurship programmes, certifications, workshops and internships, one-to-one career counselling, and admissions guidance for India and abroad.")
          + h3("Our belief", "heart")
          + p("Every student is good at something. A career assessment should never label a child. It should show where they will thrive, what to try next, and how to get there with honest facts about exams, colleges, costs and jobs."),
          photo("gallery/new1.webp", "Career guidance in a partner school", style="height:66mm") + p("", "mt")
          + stats([("4", "editions, Class 6 to UG", "layers"), ("8", "dimensions", "radar")]) + stats([("20+", "dashboard tools", "layout-grid"), ("100%", "facts linked to sources", "badge-check")]),
          ratio="1.15fr 0.85fr", gap="6mm")
    + h3("What makes OneGrasp different", "sparkles")
    + cards([("flask-conical", "Built on science", "Well-known frameworks: personality type, Holland's RIASEC interests, Gardner's intelligences, emotional intelligence and reasoning aptitude.", "#E5383B"),
             ("users", "Written for each age", "Class 6–8, Class 9–10, Class 11–12 and undergraduates each get questions and a report made for their stage.", "#4C5FD5"),
             ("map", "A plan, not just a PDF", "The report opens a dashboard of lessons, tools and weekly tasks, so it never sits in a drawer.", "#16A34A"),
             ("shield-check", "Facts you can check", "Every exam, scholarship and funding programme links to its official source.", "#F08C00")], 4, "compact"),
    section=S)

mark("Everything OneGrasp does")
svc = [("clipboard-check", "Career Fitment Assessment", "Class 6 to UG; instant report and dashboard", "#E5383B"),
       ("messages-square", "Career counselling", "One-to-one sessions with students and parents", "#4C5FD5"),
       ("plane", "Admissions guidance", "Colleges and courses in India and abroad", "#0EA5E9"),
       ("presentation", "Scientific conferences", "Online, peer-reviewed, DOI-indexed, 11 disciplines", "#7048E8"),
       ("rocket", "Startup programmes", "Spot, Build, Pitch with universities", "#D946EF"),
       ("award", "Certifications & internships", "Hands-on learning with verifiable certificates", "#F08C00"),
       ("chalkboard" if False else "book-open-check", "Faculty development", "Programmes for teachers on campus or online", "#16A34A"),
       ("star", "Spotlight boosters", "Publish, ISBN, ISSN and Awardees Magazine", "#E64980")]
cells = []
for i, (ic, t, x, c) in enumerate(svc):
    cells.append(f'<div class="hubc" style="--hc:{c}">{chip(ic, c, f"color-mix(in srgb, {c} 14%, white)", "11mm", "5.6mm")}<h4>{t}</h4><p>{x}</p></div>')
hub = cells[:4] + [f'<div class="hubm">{img("art/logo.png")}<span>One login.<br>One partner.<br>Every step.</span></div>'] + cells[4:]
add(head("Our work", "One company,", "many ways to help.",
         "Most families meet OneGrasp through the Career Fitment Assessment. Behind it is a whole ecosystem built to support a student from Class 6 to their first job.")
    + '<div class="hub">' + "".join(hub[:4]) + hub[4] + "".join(hub[5:]) + "</div>"
    + callout("example", "A Class 11 student takes the assessment in her school's computer lab. Her report says Computer Science fits her best. She uses the dashboard to plan for JEE Main, finds two scholarships, joins a free coding internship, and later presents a small research project at a OneGrasp student conference. <b>One partner, every step.</b>")
    + band("Schools and colleges can run the assessment on campus: an orientation, the test in the computer lab, and a personal report for every student. The Institution Portal then tracks every student daily.", "For institutions:", "school", "push"),
    section=S)

mark("Why career choices go wrong")
traps = [("Marks", "“You scored 95 in maths, so take engineering.”", "Marks show how you did in an exam. They do not show what you enjoy, how you work, or what you will want to do for 30 years.", "percent", "#E5383B"),
         ("Peer pressure", "“All my friends are taking MPC.”", "Your friends have different strengths and dreams. Following the crowd feels safe today and costly later.", "users", "#F08C00"),
         ("Guesswork", "“My cousin did B.Com, so…”", "Most families know only a handful of careers. With 930 careers in our library, guessing means missing most of your options.", "shuffle", "#7048E8")]
add(head("Why it matters", "Three traps that decide", "too many careers.",
         "Ask ten adults why they chose their career and many will say “I didn't really choose.” These are the three most common traps.")
    + grid([f'<div class="trap" style="--tc:{c}"><div class="trh">{chip(ic, "#fff", c, "12mm", "6mm")}<b>Trap {i + 1}</b><h4>{t}</h4></div><p class="trq">{q}</p><p>{x}</p></div>' for i, (t, q, x, ic, c) in enumerate(traps)], 3)
    + h3("What a better decision looks like", "check-check")
    + two(table(["Old way", "OneGrasp way"], [["Choose by marks", "Choose by fit: interests + strengths + aptitude"], ["Follow friends", "Follow your own profile"], ["Know 5 careers", "Explore 930 careers"],
                                              ["Decide once, alone", "Decide in steps, as a family"], ["Hope it works", "Test it first: Test-Drive, internships, projects"]], widths=["45%", "55%"]),
          callout("simple", "A good career fit is where three circles overlap: <b>what you enjoy</b> (interests), <b>what you are good at</b> (strengths and aptitude) and <b>what the world needs and pays for</b> (real careers). The assessment finds the first two; the dashboard shows you the third.")
          + callout("parent", "Your experience matters, and so does your child's profile. Use the report as a shared, neutral starting point for the conversation.")),
    section=S)

mark("Myths and facts")
myths = [("“JEE or NEET decides everything.”", "Our library covers 930 careers. Many great routes need neither exam."),
         ("“Marks are enough to choose a career.”", "Marks show how you did. Fit shows where you will do well."),
         ("“It's too late to change direction.”", "Many degrees accept any stream. Your report shows which ones."),
         ("“My degree decides my career.”", "Many roles hire from more than one degree. Your report shows which fit you."),
         ("“CGPA is all that matters.”", "CGPA shows how you did. Skills and proof show what you can do."),
         ("“Only toppers need career guidance.”", "Every student benefits from knowing their strengths and options."),
         ("“A test tells you one fixed career.”", "It shows best-fit fields and a plan to test them in real life."),
         ("“It's an exam you can fail.”", "There are no good or bad results, only better fits.")]
add(head("Clearing the air", "Myth or fact?", "", "Eight things students and parents often believe, and what is actually true.")
    + "".join(f'<div class="vs-row mb" style="margin-bottom:2.6mm"><div class="myth"><div class="lbl">{icon("x", "3.4mm", "#DC2626", 3)} MYTH</div>{m}</div><div class="fact"><div class="lbl">{icon("check", "3.4mm", "#16A34A", 3)} FACT</div>{f}</div></div>' for m, f in myths)
    + callout("good", "Career guidance is not about predicting the future. It is about making the next decision with better information than you had yesterday.", cls="push"),
    section=S)

mark("The future of work")
rising = [("AI & Machine Learning", "The biggest skill multiplier of the decade."), ("Big Data & Analytics", "One of the fastest-growing job groups worldwide."),
          ("Cybersecurity", "Protecting systems and data: a permanent, growing need."), ("Green & Climate Tech", "Renewables, EVs and sustainability engineering."),
          ("Healthcare & Biotech", "Ageing populations and genomics keep demand rising."), ("Fintech", "Digital payments and banking technology."),
          ("Robotics & Automation", "Designing machines that automate physical work."), ("Creative × Tech", "UX, product, content and design."),
          ("Care Economy", "Health support, elder care, community health."), ("EdTech & Education", "Teaching and training remain in steady demand.")]
fading = ["Cashiers and ticket clerks", "Administrative assistants and secretaries", "Postal service clerks", "Bank tellers and routine banking clerks",
          "Data entry and manual bookkeeping", "Scripted telemarketing and call-centre work", "Repetitive assembly-line and sorting work", "Generic content writing without expertise"]
add(head("The next decade", "The world of work", "is changing fast.",
         "AI is taking over routine tasks. The World Economic Forum's <i>Future of Jobs Report 2025</i> shows which skills and jobs are rising, and which are fading.")
    + two(box(h3("Skills employers want most", "trending-up") + hbars([("Analytical thinking", 96, "#E5383B"), ("Resilience, flexibility, agility", 90, "#F08C00"), ("Leadership & social influence", 84, "#7048E8"),
                                                                    ("Creative thinking", 80, "#4C5FD5"), ("Motivation & self-awareness", 76, "#16A34A"), ("AI and big data", 72, "#0EA5E9")], maxv=100, unit="")
              + p("Relative importance, illustrative. Source: WEF, Future of Jobs Report 2025. None of these skills shows on a mark sheet.", "small mt")),
          box(h3("Fading or automating", "trending-down") + bullets(fading, "tight", "minus", "#DC2626"), "soft"), ratio="1.1fr 0.9fr")
    + h3("Rising and future-proof", "rocket")
    + grid([f'<div class="rise"><b>{t}</b><span>{d}</span></div>' for t, d in rising], 5, gap="2.4mm")
    + callout("simple", "Jobs that mix <b>human judgement</b> with <b>technology</b> are the safest. That is why the assessment measures how you think, learn, feel and relate to people, not just what you know.", cls="push"),
    section=S)

mark("Your journey with OneGrasp")
add(head("The journey", "From “I don't know”", "to a clear plan.",
         "Five stages take a student from the first click to real progress. Each part of this handbook covers one of them.")
    + '<div class="road">' + "".join(f'<div class="rs" style="--rc:{c}"><div class="rsn">{icon(ic, "6.4mm", "#fff")}</div><b>{t}</b><span>{x}</span></div>' for t, x, ic, c in [
        ("Register", "2 minutes", "user-plus", "#E5383B"), ("Assess", "Up to 90 minutes", "clipboard-check", "#0EA5E9"), ("Report", "Instant", "file-text", "#10B981"),
        ("Dashboard", "Every week", "layout-dashboard", "#F97316"), ("Grow", "All year", "trending-up", "#8B5CF6")]) + "</div>"
    + vsteps([("Register (about 2 minutes)", "Choose your class, say how sure you are about your career, and create your login. School students can join through their school's link. (Part 2)"),
              ("Take the assessment (up to 90 minutes)", "Questions across the 8 dimensions, written for your age. Answers save as you go, and a timer shows the time left. (Parts 2 and 3)"),
              ("Read your report (instant)", "Your profile, best-fit careers with a fit %, strengths and growth areas, and a long-term roadmap. Download the PDF; a copy is emailed. (Part 4)"),
              ("Use your dashboard (every week)", "One login opens 20+ tools: careers, exams, scholarships, study abroad, internships, jobs, money, law, research, startups, AI and more. (Part 5)"),
              ("Act and grow (all year)", "Weekly Career GPS missions, lessons that unlock step by step, certificates, a portfolio website and a verified Career Passport. (Parts 5 to 7)")])
    + two(img("brochure/c11-i-032.png", "pic"), img("brochure/c11-i-029.png", "pic"), "mt push", gap="4mm"),
    section=S)

mark("An assessment day on campus")
add(head("On campus", "How an assessment day", "runs in a school.",
         "When a school or college partners with OneGrasp, our team runs the whole day with the students. Here is what happens, start to finish.")
    + grid([photo("gallery/old02.webp", "1 · Orientation in the hall", style="height:44mm"), photo("gallery/new2.webp", "2 · The assessment in the lab", style="height:44mm"),
            photo("gallery/old13.webp", "3 · One-to-one report reading", style="height:44mm")], 3, gap="4mm")
    + vsteps([("Orientation on campus (30–45 minutes)", "Our team meets the students, explains what the assessment is and is not, and answers questions. Students learn that honest answers give the most useful report."),
              ("Assessment in the computer lab (up to 90 minutes)", "Students take the test online on the school's computers, one question at a time, with a timer and a navigator. Answers save as they go."),
              ("Instant personal reports", "Every student receives their own Career Fitment Report the moment they finish: on screen, as a PDF and by email."),
              ("One-to-one sessions", "Counsellors sit with students (and parents where possible) to read the report together and agree the first steps."),
              ("Daily tracking afterwards", "The Institution Portal shows who has finished, who is active in the dashboard, and who needs a reminder.")], "mt")
    + band("Call +91 89777 60442 / 43 or write to support@onegrasp.com to plan a campus-wide rollout.", "Bring OneGrasp to your school:", "phone", "push"),
    section=S)

mark("Real schools, real students")
add(head("Our work in schools", "Real schools.", "Real students.",
         "Moments from Career Fitment Assessment days at Oxford Grammar High School, Sree Shanthinikethan English Medium School and Excellencia Junior College.", center=True)
    + '<div class="collage">'
    + photo("gallery/old08.webp", "Orientation session", cls="c1", tape=True)
    + photo("gallery/new3.webp", "Students in the session", cls="c2")
    + photo("gallery/old05.webp", "Assessment in the lab", cls="c3")
    + photo("gallery/old07.webp", "Our counsellors on campus", cls="c4")
    + photo("gallery/old04.webp", "Explaining the report", cls="c5")
    + photo("gallery/old11.webp", "One-to-one session", cls="c6")
    + photo("gallery/old14.webp", "Reading the report together", cls="c7")
    + photo("gallery/g08.jpg", "Taking the assessment", cls="c8")
    + "</div>"
    + grid([f'<div class="logo-card" style="height:22mm">{img("logos/" + f + ".png", style="max-height:14mm")}</div>' for f in ("school-shanthinikethan", "school-dps", "school-oxford", "school-excellencia")], 4, "push"),
    section="Our work in schools")
