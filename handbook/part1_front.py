from lib import *

# ---------------------------------------------------------------- cover
add(f'''<div class="cover-wrap"><div class="cv-blob"></div>
{img("art/logo.png", "cv-logo")}<div class="cv-chip">Handbook · 2026–27 Edition</div>
{img("brochure/c11-i-001.png", "cv-girl")}
<div class="cv-text"><div class="cv-kick">Career Fitment Assessment</div>
<div class="cv-title">The Complete<br>Career Fitment<br><span class="red">Handbook.</span></div>
<p class="cv-sub">Everything about the OneGrasp assessment, the 8 dimensions, your report and every tool in your dashboard, explained step by step for students, parents and schools.</p></div>
<div class="cv-stats">{stats([("8", "dimensions of you, measured in one sitting"), ("4", "editions: Class 6–8, 9–10, 11–12 and undergraduates"), ("20+", "tools in one dashboard"), ("311", "startup funding programmes listed")])}</div>
<div class="cv-foot"><span>Know yourself. <b>Choose with confidence.</b> Build your future.</span><span>careerfitment.onegrasp.com</span></div></div>''', kind="cover")

# ---------------------------------------------------------------- how to use this handbook
add(head("Before you begin", "How to use", "this handbook.",
         "This book is a printed companion to the OneGrasp Career Fitment Assessment and its dashboard. You do not need to read it cover to cover. Start with the part that fits you.")
    + cards([
        ("Students", "Read Parts 2 and 3 before the test, Part 4 when your report arrives, and keep Part 5 open next to your dashboard. The task lists show you exactly what to do each week."),
        ("Parents", "Start with Part 1 (what OneGrasp is), then the report pages for your child's class in Part 4, and the parents' chapter in Part 8. You will find questions to talk through together."),
        ("Teachers and counsellors", "Parts 2, 3 and 4 explain the science and the report. Part 8 covers the Institution Portal: tracking, reminders, messages and decision briefs."),
        ("Founders and researchers", "Part 6 lists all 311 startup funding programmes in the dashboard's Funding directory. Part 7 covers Research & Conferences and our international scientific committee."),
    ], 2)
    + h3("Signs used in this book")
    + two(findit("Dashboard menu", "Tool", "Section") + p("<b>Find it</b> shows the exact path to open a tool in your dashboard.", "small")
          + note("Good to know:", "a tip, a limit, or a safety reminder you should not skip."),
          box(h3("Three promises") + bullets([
              "<b>Your answers are private.</b> Schools see progress, never individual answers.",
              "<b>No pass or fail.</b> Only the Aptitude section has right answers.",
              "<b>Facts you can check.</b> Exams, scholarships and funding link to official sources."]), "tint"))
    + note("Please note:", "Screens in this book come from the live dashboard in October 2026 and use a sample student, <b>Ananya Rao</b>. Your screens will show your own name, results and class. Dates, fees, eligibility and amounts change, so always confirm them on the official website before you apply.", "blue push"),
    section="How to use this book")

# ---------------------------------------------------------------- welcome
add(head("Welcome", "Every child is good", "at something.")
    + p('<span class="quote">“Most career decisions are made on marks, peer pressure or guesswork. OneGrasp replaces guesswork with self-knowledge and a clear, honest plan the whole family can see.”</span>')
    + two(p("A career choice is rarely one decision. It is a chain of them: which subjects to take, which stream, which entrance exam, which degree, which college, which first job. Each choice shapes the next one. When the first link is chosen on marks alone, or because a cousin did the same course, the whole chain can pull in the wrong direction.")
          + p("The OneGrasp Career Fitment Assessment starts with you: how you think, what you enjoy, how you learn, what drives you and what you are naturally good at. It then connects that picture to real careers, real exams, real colleges and real money (scholarships, funding and salaries) so the next step is clear."),
          p("After the report, the work begins. Your dashboard turns the report into lessons, tools and weekly tasks: a career library of 930 careers, every major entrance exam, 40 scholarships, study abroad, free internships, money skills, your legal rights, research, startups, AI skills, communication and a job-ready resume.")
          + p("This handbook walks you through all of it, page by page, so that a student, a parent and a teacher can sit at the same table, open the same page and have the same calm conversation.")
          + p("<b>The OneGrasp Team</b><br><span class='small'>OneGrasp Education Pvt. Ltd., Hyderabad</span>"))
    + h3("Start in three steps")
    + two(steps([("Scan the code or visit careerfitment.onegrasp.com", "Open the assessment on any phone, tablet or laptop."),
                 ("Register in about two minutes", "Students sign up themselves, or join through their school or college link."),
                 ("Take the test and get your report", "Answer honestly. Your report is ready the moment you finish.")]),
          f'<div class="box center">{img("art/qr.png", "qr", style="background:#fff;padding:2mm")}<p class="small mt">Scan to take the assessment<br><b>careerfitment.onegrasp.com</b></p></div>', ratio="1fr 52mm"),
    section="Welcome")

# ---------------------------------------------------------------- contents
add(head("Contents", "What's inside", "this handbook.") + '<div class="toc">{{TOC1}}</div>', section="Contents")
add(head("Contents", "What's inside", "(continued).") + '<div class="toc">{{TOC2}}</div>', section="Contents")

# ---------------------------------------------------------------- logos and partners (original Canva pages)
mark("Our international collaborations")
placeholder("canva:DAHXfhMiiR0:48")   # collaborations: Crossref, DOI, JCI, PACE Council, IntelliMindEd, metaSpectra, RMetaHub, KVRSS
mark("Accreditation, DOI and indexing partners")
placeholder("canva:DAHXidPDcII:2")    # accreditation, DOI & indexing partners + media partners
mark("Partner schools")
placeholder("canva:DAHXfhMiiR0:2")    # partner schools

# ================================================================= PART 1
divider(1, "Meet OneGrasp", "Who we are, what we do, and why we built a career assessment that looks beyond marks.",
        ["What is OneGrasp?", "What OneGrasp does", "OneGrasp at a glance", "Why career choices go wrong", "Your journey with OneGrasp", "OneGrasp in schools"],
        image="brochure/c11-i-032.png")

mark("What is OneGrasp?")
add(head("About us", "What is", "OneGrasp?",
         "OneGrasp Education Pvt. Ltd. is an education company based in Hyderabad, India. We help students, families, professionals and institutions make better decisions about learning and work.")
    + two(p("Our best-known product is the <b>Career Fitment Assessment</b>: a psychometric career assessment for Class 6 to undergraduates. It measures eight dimensions of a student (personality, interests, intelligences, emotional intelligence, learning style, motivators, strengths and aptitude) and turns them into a personal report and a dashboard of tools.")
          + p("Around the assessment, OneGrasp runs international scientific conferences, startup and entrepreneurship programmes, certifications, workshops and internships, career counselling, and admissions guidance in India and abroad.")
          + h3("Our belief") + p("Every student is good at something. The job of a career assessment is not to label a child. It is to show them where they will thrive, what to try next, and how to get there with real facts about exams, colleges, costs and jobs."),
          img("brochure/ug-i-001.png", "pic", style="height:92mm;object-position:top"))
    + h3("What makes OneGrasp different")
    + cards([("01", "Built on science", "Well-established frameworks: personality type, Holland's RIASEC interests, Gardner's multiple intelligences, emotional intelligence and reasoning aptitude."),
             ("02", "Written for each age", "Class 6–8, Class 9–10, Class 11–12 and undergraduates each get a test and a report written for their stage."),
             ("03", "A plan, not a PDF", "The report opens a dashboard with lessons, tools and weekly tasks, so it never sits in a drawer."),
             ("04", "Facts you can check", "Every exam, scholarship and funding programme links to its official source.")], 4, "compact"),
    section="Meet OneGrasp")

mark("What OneGrasp does")
add(head("Our work", "One company,", "many ways to help.",
         "The Career Fitment Assessment is where most students meet us. Here is everything else OneGrasp does for students, families and institutions.")
    + cards([("Career Fitment Assessment", "A psychometric assessment for Class 6 to undergraduates, with an instant report and a dashboard of 20+ tools."),
             ("Career counselling", "One-to-one sessions that help a student and their family read the report and choose the next step together."),
             ("Admissions guidance", "Help with colleges and courses in India and abroad: shortlists, applications, SOPs and the money check."),
             ("International scientific conferences", "Online, peer-reviewed conferences in 11 disciplines with a DOI for every accepted abstract and CPD-accredited certificates."),
             ("Startup and entrepreneurship programmes", "Spot, Build, Pitch: short, intensive programmes run with universities, plus an 11-module startup course in the dashboard."),
             ("Certifications, workshops and internships", "Practical, hands-on learning for students and professionals, with certificates that can be verified."),
             ("Faculty development", "Programmes for teachers and faculty, delivered with institutions on campus or online."),
             ("Spotlight career boosters", "Present research at a conference, publish a paper, get an ISBN for a book, start a journal with an ISSN, or be featured in Awardees Magazine.")], 2)
    + band("For institutions", "Schools and colleges can run the assessment on campus: an orientation, the test in the computer lab, and a personal report for every student. The Institution Portal then tracks every student daily.", "navy"),
    section="Meet OneGrasp")

mark("OneGrasp at a glance")
add(head("The big picture", "OneGrasp", "at a glance.")
    + stats([("3,000+", "students assessed"), ("10+", "schools and colleges"), ("2,500+", "career roadmaps")])
    + stats([("1,000+", "parents engaged"), ("500+", "counselling sessions"), ("8", "dimensions measured")])
    + h3("Inside the dashboard")
    + stats([("930", "careers explained"), ("29", "entrance exams"), ("40", "scholarships"), ("209", "free internship programmes")])
    + stats([("311", "startup funding programmes"), ("24", "legal guides"), ("8", "research studio units"), ("11", "startup modules")])
    + h3("Beyond the assessment")
    + stats([("500+", "online conferences held"), ("70+", "countries represented"), ("50", "scientific committee members"), ("11", "conference disciplines")])
    + note("About these numbers:", "dashboard figures are counted from the live platform in October 2026. Library sizes grow as new careers, exams, scholarships and programmes are added.", "blue push"),
    section="Meet OneGrasp")

mark("Why career choices go wrong")
add(head("Why it matters", "Most career choices are", "made on the wrong things.",
         "Marks, peer pressure and guesswork decide too many careers. None of them tells a student what they will enjoy, keep doing, and be good at for years.")
    + table(["Myth", "Fact"], [
        ["“JEE or NEET decides everything.”", "Our library covers 930 careers. Many great routes need neither exam."],
        ["“Marks are enough to choose.”", "Marks show how you did. Fit shows where you will do well."],
        ["“It's too late to change direction.”", "Many degrees accept any stream. Your report shows which ones."],
        ["“My degree decides my career.”", "Many roles hire from more than one degree. Your report shows which fit you."],
        ["“CGPA is all that matters.”", "CGPA shows how you did. Skills and proof show what you can do."],
        ["“Only toppers need career guidance.”", "Every student benefits from knowing their strengths and options."],
        ["“A test tells you one fixed career.”", "It shows best-fit fields and a plan to test them in real life."]], widths=["42%", "58%"])
    + h3("What employers want now")
    + two(p("The World Economic Forum's <i>Future of Jobs Report 2025</i> lists the skills employers value most as AI takes over routine work. None of them shows on a mark sheet.")
          + p("That is why the assessment measures how you think, learn, relate to people and stay motivated, not only what you scored in your last exam.", "small"),
          bullets(["Analytical thinking", "Resilience, flexibility and agility", "Leadership and social influence", "Creative thinking", "Motivation and self-awareness"])),
    section="Meet OneGrasp")

mark("Your journey with OneGrasp")
add(head("The journey", "From “I don't know”", "to a clear plan.",
         "Five steps take a student from the first click to real progress. Each part of this handbook covers one of them.")
    + '<div class="flow mb">' + "".join(f"<div><b>{n}</b>{t}</div>" for n, t in [("1", "Register"), ("2", "Take the assessment"), ("3", "Read your report"), ("4", "Use your dashboard"), ("5", "Act and grow")]) + '</div>'
    + steps([("Register (2 minutes)", "Choose your class or stage, say how sure you are about your career, and create your login. School students can join through their school's link."),
             ("Take the assessment (up to 90 minutes)", "Questions across the 8 dimensions, written for your age. Answers save as you go, and a timer shows the time left."),
             ("Read your report (instant)", "Your profile, best-fit careers with a fit %, your strengths and growth areas, and a long-term roadmap. Download it as a PDF; a copy is emailed."),
             ("Use your dashboard (every week)", "One login opens 20+ tools: careers, exams, scholarships, study abroad, internships, jobs, money, law, research, startups, AI, communication and more."),
             ("Act and grow (all year)", "Weekly Career GPS missions, lessons that unlock step by step, certificates, a portfolio website and a verified Career Passport. My Progress shows how far you have come.")])
    + two(img("brochure/c11-i-029.png", "pic"), img("brochure/c11-i-032.png", "pic"), "mt"),
    section="Meet OneGrasp")

mark("OneGrasp in schools")
placeholder("canva:DAHXfhMiiR0:3")    # on campus with students (photos)
placeholder("canva:DAHXfhMiiR0:4")    # assessment day in pictures (photos)
add(head("On campus", "How an assessment day", "runs in a school.",
         "When a school or college partners with OneGrasp, our team runs the whole day with the students. Here is what happens, start to finish.")
    + '<div class="grid g3 mb">' + "".join(img(f"gallery/{g}.jpg", "pic", style="height:44mm") for g in ("g02", "g08", "g13")) + '</div>'
    + steps([("Orientation on campus", "Our team meets the students, explains what the assessment is (and is not), and answers questions. Students learn that honest answers give the most useful report."),
             ("Assessment in the computer lab", "Students take the test online on the school's computers, one question at a time, with a timer and a navigator. Answers save as they go."),
             ("Instant personal reports", "Every student receives their own Career Fitment Report the moment they finish, on screen, as a PDF and by email."),
             ("One-to-one sessions", "Counsellors sit with students (and parents, where possible) to read the report together and agree the first steps."),
             ("Daily tracking afterwards", "The Institution Portal shows who has finished, who is active in the dashboard, and who needs a reminder.")])
    + note("Bring OneGrasp to your school:", "call +91 89777 60442 / 43 or write to support@onegrasp.com to plan a campus-wide rollout.", "push"),
    section="OneGrasp in schools")
