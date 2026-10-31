from lib import *
from tools import *

divider(5, "dash", "Your Dashboard: Explore", "Your report becomes a dashboard you use. This part shows you how to find your way around, then gives each exploring tool its own chapter with missions you can finish this week.",
        ["How to use your dashboard", "Your dashboard home", "Finding your way, and your results", "Your results pages", "Career Library", "Entrance Exams", "Scholarships", "Study Abroad", "Internships & Jobs"],
        "feat/progress.webp")
S = "Your Dashboard"

# ---------------------------------------------------------------- home
mark("How to use your dashboard")
add(head("Start here", "How to use", "your dashboard.", "Your dashboard is where the report turns into action. Use it in this order the first time, then come back every week.")
    + two(vsteps([("Sign in", "Go to careerfitment.onegrasp.com and sign in with the email and password you used for the assessment."),
                  ("Open your report", "On the home screen tap <b>Open my full report</b>. Use <b>Download</b> to save the PDF."),
                  ("Explore your results", "In the left menu, open <b>Your results</b>: profile, 8 dimensions, best-fit fields, how you think, my plan."),
                  ("Pick a tool", "Choose a tool from <b>Explore</b> in the left menu, starting with your top career field in the Career Library."),
                  ("Do the missions", "Each tool chapter in this book ends with a mission card. Tick tasks off as you finish them on the dashboard."),
                  ("Track your progress", "Open <b>My Progress</b> to see lessons done, time spent and your streak; collect certificates as you finish courses.")]),
          laptop("shots/dash-home.jpg", "The dashboard home: report at the top, tools below, menu on the left.") + p("", "mt") + laptop("shots/progress.jpg", "My Progress: everything you have done, in one place."), ratio="1fr 1fr", gap="5mm")
    + h3("A simple weekly routine", "calendar-check")
    + table(["When", "What to do", "Where"], [["Once a week", "Do the three Career GPS missions", "Career GPS"], ["Twice a week", "Work on one tool's mission card", "Any tool in the Explore menu"],
                                              ["Every day (10 min)", "One lesson, game or speaking challenge", "Money, AI, Communication Lab"], ["Every month", "Check your progress and update your plan", "My Progress · My plan"]], "dense", ["22%", "48%", "30%"]),
    section=S)

mark("Your dashboard home")
add(head("Dashboard home", "Your report becomes", "a dashboard you use.",
         "Sign in at careerfitment.onegrasp.com. You land on the dashboard home: your report at the top, your toolkit below, the menu on the left.")
    + laptop("shots/dash-home.jpg", pins=[(1, 9, 11), (2, 33, 3.5), (3, 63, 3.5), (4, 80, 17), (5, 92, 17), (6, 23, 28), (7, 9, 22), (8, 9, 74)])
    + grid([f'<div class="lab"><span>{i + 1}</span><div><b>{t}</b><p>{x}</p></div></div>' for i, (t, x) in enumerate([
        ("Your name and class", "You're in the right account."), ("Search (press /)", "Find any tool or page."), ("My progress", "Everything you've done."),
        ("Open my full report", "Every page, with Download."), ("See my profile", "Results at a glance."), ("Your toolkit", "One card per tool; new ones say NEW."),
        ("Explore menu", "Every tool, always on the left."), ("Your results", "Profile, dimensions, fields, plan.")])], 4, "mt", gap="2.4mm 4mm")
    + callout("task", "Sign in today and open every menu item once. It takes 10 minutes and you'll never feel lost again.", cls="push"),
    section=S)

mark("Finding your way, and your results")
groups = [("Explore", "#B92B32", ["Career Library", "Entrance Exams", "Scholarships", "Study Abroad", "Internships", "Jobs", "Financial Literacy", "Law & Rights", "Research", "Startups", "AI & Certifications", "Communication Lab", "Spotlight"]),
          ("Your results", "#17243A", ["Your profile", "8 Dimensions", "Best-fit fields", "How you think", "My plan"]), ("Track", "#5E7189", ["My Progress", "Certificates"]), ("Create", "#3D4F66", ["Resume & Interview", "Build your website"])]
add(head("Navigation", "Finding your way,", "and your results.", "The left menu stays on every screen. The Your results pages are your report made interactive.")
    + two('<div class="navmap">' + "".join(f'<div class="ng" style="--g:{c}"><b>{g}</b><div>' + "".join(f"<span>{i}</span>" for i in its) + "</div></div>" for g, c, its in groups) + "</div>",
          browser("shots/res-profile.jpg", "Your profile: title, type, strongest interest, top field."), ratio="1fr 1fr", gap="5mm")
    + grid([browser("shots/res-fields.jpg", "Best-fit fields with fit % and the reason."), browser("shots/res-plan.jpg", "My plan: next 30 and 90 days, with tick boxes.")], 2, "mt", gap="4mm")
    + callout("task", "Open <b>My plan</b> and tick the three “next 30 days” items this month. They're chosen for your top field.", cls="push"),
    section=S)

mark("Your results pages")
add(head("Your results", "Your report,", "made interactive.", "The <b>Your results</b> pages in the left menu show the same results as your PDF report, but you can tap into each one.")
    + two(browser("shots/res-dims.jpg", "8 Dimensions: tap a dimension for its score, meaning and actions."), browser("shots/res-mind.jpg", "How you think: intelligences, aptitudes, motivators and learning styles."), gap="4mm")
    + two(browser("shots/res-fields.jpg", "Best-fit fields: ranked, with a fit % and the reason."), browser("shots/res-plan.jpg", "My plan: next 30 and 90 days, with tick boxes."), "mt", gap="4mm")
    + callout("task", "Tick all three “next 30 days” items in <b>My plan</b> this month. They're picked for your top field.", cls="push"),
    section=S)

# ---------------------------------------------------------------- 1 Career Library
mark("Career Library")
tool_theme("t-careers", "Career Library", "#17243A", "#5E7189")
opener(1, "Career Library", "930 careers explained simply, with salaries, skills and a degree roadmap for each, plus a Test-Drive and a Family Decision Room.", "feat/careers.webp",
       [("930", "careers"), ("8", "fields"), ("2,500+", "roadmaps")],
       pills(["Class 6–8: explore", "Class 9–10: choose a stream", "Class 11–12: choose a degree", "Parents: compare paths"]),
       ["Most students can name only 10–15 careers. Seeing hundreds, with real pay and real routes, widens your choices.", "A degree roadmap turns a dream into year-by-year steps.", "Test-Drive lets you feel a career before you spend years on it."],
       [("search", "Search 930 careers", "By job, skill or subject."), ("layers", "8 fields", "Technology to trades."), ("route", "Degree roadmaps", "Year-by-year plans for 1,500+ roles."),
        ("indian-rupee", "Salary and demand", "Indicative pay in India."), ("play", "Career Test-Drive", "Live a day in a career."), ("users", "Family Decision Room", "Compare two paths together.")],
       ("Menu", "Career Library"), "Career Library")
howto("Career Library", [("careers", "Search any career, or browse 8 fields."), ("test-drive", "Career Test-Drive: five moments of a working day."), ("decision-room", "Family Decision Room: two paths side by side.")],
      [("Search or browse", "Type a job, skill or subject, or tap a field."), ("Open a career", "Read what it is, skills, salary, demand and entry routes."), ("Open its roadmap", "Year by year: skills, internships, exams, first jobs."),
       ("Test-drive it", "Live five real moments; rate each one; read the honest summary."), ("Decide together", "Compare your top two paths in the Decision Room.")],
      [callout("simple", "Read about it → feel it (Test-Drive) → decide with facts (Decision Room)."), callout("warn", "A roadmap is a guide, not a guarantee. Confirm entry routes with colleges and employers.")], "Career Library")
mission("Career Library",
        [("Build your shortlist", "20 min", ["Open your top best-fit field", "Read 5 careers in it", "Fill the shortlist table below"]),
         ("Feel the work", "15 min", ["Test-drive your #1 career", "Note one moment you loved", "Note one honest downside"]),
         ("Decide as a family", "30 min", ["Put your top 2 paths in the Decision Room", "Each person adds their view", "Write the first step you agreed"])],
        wtable(["Career", "What they do (one line)", "Starting pay", "Degree / exam needed", "My interest 1–5"], 5, ["20%", "30%", "14%", "24%", "12%"])
        + two(box(h3("One moment I loved", "heart") + lines(2)), box(h3("One honest downside", "triangle-alert") + lines(2)), "mt", gap="4mm"),
        "You now have a real shortlist, not a guess.", "Career Library")

# ---------------------------------------------------------------- 2 Exams
mark("Entrance Exams")
tool_theme("t-exams", "Entrance Exams", "#5E7189", "#5E7189")
opener(2, "Entrance Exams", "Every major entrance exam in one place: check if you're eligible, plan backwards from the date, practise with mocks and stay calm.", "feat/exams.webp",
       [("29", "exams"), ("44", "lessons"), ("34", "tools & planners")],
       pills(["Class 6: JNVST, AISSEE", "Class 8: NMMS", "Class 9–10: olympiads, NSEJS", "Class 11–12: JEE, NEET, CUET, CLAT, NDA…"]),
       ["Knowing early which exams you qualify for means no missed deadlines and no last-minute panic.", "A plan that counts back from the exam date turns a huge syllabus into weekly steps.", "Mocks with real marking show exactly what to revise."],
       [("user-round-pen", "Fill your profile once", "See only exams open to you."), ("bell", "Follow exams", "Deadline reminders."), ("calendar-days", "Study planner", "Syllabus built in for 7 major exams."),
        ("timer", "Mock tests", "Real marking scheme + analysis."), ("route", "Stage roadmap", "What to do this year."), ("heart-pulse", "Wellbeing", "Stress support and backup paths.")],
       ("Menu", "Entrance Exams"), "Entrance Exams")
howto("Entrance Exams", [("exams-dash", "My exams and deadlines: only what you can take."), ("exams-planner", "Study planner with syllabus tracker."), ("exams-mocks", "Mock tests and analysis.")],
      [("Fill your profile", "Class, stream, marks, category and state, once."), ("See what you can take", "Exams open to you now or soon, with official links."), ("Follow 2–3 exams", "Their dates appear in My exams."),
       ("Make a plan", "Pick the exam and date; get a week-by-week plan."), ("Practise weekly", "One mock a week; revise what the analysis shows.")],
      [callout("good", "Dates and eligibility change every year. Always confirm on the official website linked from each exam."), callout("simple", "Mock scores are for learning, not prediction. The analysis matters more than the score.")], "Entrance Exams")
mission("Entrance Exams",
        [("Know your exams", "15 min", ["Fill your exam profile", "Follow 2–3 exams", "Write their dates below"]),
         ("Build your plan", "20 min", ["Create a study plan for exam #1", "Block weekly study hours", "Tick 3 syllabus topics this week"]),
         ("Practise and review", "60 min", ["Take one timed mock", "Read the analysis", "List 3 topics to revise"])],
        wtable(["Exam", "Conducted by", "Registration opens", "Exam date", "Status"], 4, ["22%", "22%", "20%", "18%", "18%"])
        + two(box(h3("My weekly study hours", "clock") + table(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], [["&nbsp;"] * 7], "fill")), box(h3("3 topics to revise", "list-checks") + lines(3)), "mt", ratio="1.3fr 0.7fr", gap="4mm"),
        "You know your exams, your dates and your next topic.", "Entrance Exams")

# ---------------------------------------------------------------- 3 Scholarships
mark("Scholarships")
tool_theme("t-sch", "Scholarships", "#17243A", "#8A97A8")
opener(3, "Scholarships", "Find the money you qualify for: central, state and private schemes, with a deadline calendar, essay help and a safe document vault.", "feat/scholarships.webp",
       [("40", "scholarships"), ("53", "lessons"), ("47", "tools")],
       pills(["Class 8: NMMS", "Class 11–12: Pankh, INSPIRE, Pragati", "After Class 12: CSSS, Reliance, PM YASASVI", "Parents: income & category schemes"]),
       ["Cost should never decide a career on its own.", "Many families never apply for money they already qualify for.", "Deadlines are strict: a calendar and tracker mean you never miss one."],
       [("search", "Find for me", "Only schemes you qualify for."), ("calendar", "Deadline calendar", "Every official date."), ("clipboard-list", "My applications", "Track planning → won."),
        ("pen-line", "Essay helper", "Prompts and a checklist."), ("folder-lock", "Document vault", "Upload once, reuse."), ("shield-alert", "Scam check", "Real ones never ask you to pay.")],
       ("Menu", "Scholarships"), "Scholarships")
howto("Scholarships", [("sch-dash", "Money you can apply for: fill your profile once."), ("sch-cal", "Deadline calendar."), ("sch-essay", "Essay and statement helper.")],
      [("Fill your profile", "Class, marks, income, category, state, gender."), ("See matches", "Amount, eligibility and deadline for each."), ("Add to My applications", "Track each from planning to won."),
       ("Prepare documents", "Upload them once to the vault."), ("Write and submit", "Use the essay helper, then apply on the official site.")],
      [callout("warn", "Genuine scholarships never ask you to pay to receive money. Never share OTPs, PINs or bank passwords."), callout("parent", "Income and caste certificates take weeks. Start them early.")], "Scholarships")
mission("Scholarships",
        [("Find 5 matches", "15 min", ["Fill your scholarship profile", "Shortlist 5 schemes", "Copy them into the tracker"]),
         ("Get documents ready", "1 week", ["Collect every document below", "Upload to the vault", "Note what's missing"]),
         ("Apply to 2", "45 min", ["Draft your essay with the helper", "Apply on the official site", "Mark them “applied”"])],
        wtable(["Scholarship", "Amount", "Deadline", "Docs ready?", "Applied ✓"], 5, ["34%", "16%", "18%", "16%", "16%"])
        + box(h3("Document checklist", "folder-check") + check_list(["Aadhaar card", "Latest marksheet", "Income certificate", "Caste / category certificate (if any)", "Bank passbook (student's name)", "Passport-size photo", "Bonafide / admission letter", "Disability certificate (if any)"], 4), "soft mt"),
        "You have money on the way, not just a wish.", "Scholarships")

# ---------------------------------------------------------------- 4 Study Abroad
mark("Study Abroad")
tool_theme("t-abroad", "Study Abroad", "#7A2A30", "#5E7189")
opener(4, "Study Abroad", "Abroad Compass: decide whether to go, where and for what, and check the money works before anyone sells you a university.", "feat/study-abroad.webp",
       [("6", "steps"), ("30", "lessons"), ("8", "countries")],
       pills(["Class 9–10: plan early", "Class 11–12: degree abroad", "Parents: the money check"]),
       ["Study abroad is one of the biggest money decisions a family makes.", "A calm, step-by-step check avoids expensive mistakes and agent pressure.", "The ROI calculator shows how many years a degree takes to pay back."],
       [("globe", "Compare countries", "US, Canada, UK, Australia, Germany, France, Ireland, NZ."), ("book-open", "Course finder", "What to study, where."), ("building-2", "Universities", "Reach, match or safe."),
        ("calculator", "ROI calculator", "Years to pay back."), ("file-text", "SOP & LOR helper", "Statements that sound like you."), ("shield-alert", "Agent checks", "Before you pay anyone.")],
       ("Menu", "Study Abroad"), "Study Abroad")
howto("Study Abroad", [("sa-countries", "Compare up to four countries."), ("sa-roi", "ROI calculator."), ("sa-unis", "Universities: reach, match, safe.")],
      [("Decide", "Is abroad right for you, and when?"), ("Pick a country", "Real costs, work rights, what's next."), ("Pick a course", "Match it to your report."), ("Shortlist universities", "2 reach, 3 match, 2 safe."),
       ("Run the money check", "ROI, loans, scholarships, then prepare SOP, LOR, documents.")],
      [callout("warn", "The calculator gives a planning estimate, not a loan offer. Real budgets have extra costs."), callout("parent", "Check the total cost (tuition + living + travel) before paying any application fee or agent.")], "Study Abroad")
mission("Study Abroad",
        [("Compare 3 countries", "30 min", ["Compare costs, work rights, visas", "Fill the comparison table", "Pick your top country"]),
         ("Do the money check", "20 min", ["Run the ROI calculator", "Check 2 abroad scholarships", "Fill the budget box"]),
         ("Shortlist and prepare", "1 hour", ["Shortlist 7 universities", "Outline your SOP", "List the documents you need"])],
        wtable(["Country", "Yearly tuition", "Yearly living", "Work rights", "Post-study visa"], 3, ["20%", "20%", "20%", "20%", "20%"])
        + two(box(h3("My budget box", "wallet") + '<div class="bud">' + "".join(f'<div><span>{t}</span><i></i></div>' for t in ["Tuition (total)", "+ Living (total)", "+ Travel & visa", "− Scholarships", "= Total cost", "Loan needed", "Expected first salary", "Years to pay back"]) + "</div>"),
              box(h3("Universities", "building-2") + table(["Reach", "Match", "Safe"], [["&nbsp;", "&nbsp;", "&nbsp;"], ["&nbsp;", "&nbsp;", "&nbsp;"], ["", "&nbsp;", ""]], "fill")), "mt", gap="4mm"),
        "Your family can decide with numbers, not hope.", "Study Abroad")

# ---------------------------------------------------------------- 5 Internships & Jobs
mark("Internships & Jobs")
tool_theme("t-intern", "Internships & Jobs", "#3D4F66", "#3D4F66")
opener(5, "Internships & Jobs", "209 free internship programmes from 135 companies, and fresh jobs every day, checked for scam warning signs.", "feat/internships.webp",
       [("209", "free programmes"), ("135", "companies"), ("₹0", "to join")],
       pills(["Class 9–12: beginner programmes", "Class 11–12: summer internships", "Everyone: certificates for your CV"]),
       ["Employers look for proof, not just marks.", "Certificates and projects from real companies make a CV stand out.", "Fake job offers target freshers; Trust Shield checks every listing."],
       [("laptop", "Free programmes", "Self-paced, from real companies."), ("signal", "Levels", "Beginner, intermediate, advanced."), ("filter", "Filters", "Tech, consulting, finance, AI…"),
        ("award", "Certificates", "Add them to your CV."), ("briefcase", "Fresh jobs", "Internships and fresher roles daily."), ("shield-check", "Trust Shield", "Scam signs checked.")],
       ("Menu", "Internships · Jobs"), "Internships & Jobs")
howto("Internships & Jobs", [("intern", "Internships: filter by level and field."), ("jobs", "Jobs: fresh listings, scam-checked.")],
      [("Pick your level", "Start at beginner if it's your first one."), ("Pick a field", "Use your best-fit field from the report."), ("Start the programme", "Most are self-paced; 2–10 hours."),
       ("Get the certificate", "Add it to your Career Passport and CV."), ("Apply for real roles", "Use Jobs; apply on the original listing.")],
      [callout("warn", "A real employer never asks you to pay for a job, training kit or “security deposit”."), callout("simple", "One finished programme beats five half-started ones.")], "Internships & Jobs")
mission("Internships & Jobs",
        [("Start one programme", "20 min", ["Filter by your field and level", "Pick one programme", "Finish the first module"]),
         ("Finish and prove it", "1–2 weeks", ["Complete the programme", "Download the certificate", "Add it to your Passport"]),
         ("Try the real world", "30 min", ["Find 3 matching roles in Jobs", "Check each for scam signs", "Apply to one"])],
        wtable(["Programme / role", "Company", "Skill I learned", "Hours", "Certificate / status"], 5, ["26%", "18%", "26%", "10%", "20%"]),
        "You have proof of skills that employers can see.", "Internships & Jobs")

theme("dash")
mark("Where do I find…?")
add(head("Quick map", "Where do I find", "…?", "Keep this page next to your screen. Every path starts from the left menu of the dashboard.")
    + table(["I want to…", "Go to"], [
        ["Reopen or download my report", "Home › Open my full report › Download"], ["See my type and interest code", "Your results › Your profile"], ["See one dimension in detail", "Your results › 8 Dimensions"],
        ["See my best-fit careers", "Your results › Best-fit fields"], ["Know what to do this month", "Your results › My plan · Career GPS"], ["Find a career's salary and roadmap", "Career Library › search"],
        ["Check if I can take an exam", "Entrance Exams › Your exams"], ["Make a study plan or take a mock", "Entrance Exams › Prepare"], ["Find scholarships I qualify for", "Scholarships › Find"],
        ["See scholarship deadlines", "Scholarships › Calendar"], ["Compare countries to study in", "Study Abroad › Countries"], ["Check if a degree abroad pays back", "Study Abroad › Money › ROI"],
        ["Find a free internship", "Internships"], ["Find a real job", "Jobs · Resume & Interview › Jobs for you"], ["Learn money skills", "Financial Literacy"],
        ["Check a suspicious message", "Financial Literacy › Scam Shield"], ["Get help with a legal problem", "Law & Rights › Find help"], ["Plan a research project", "Research › Start a project"],
        ["Find startup funding", "Startups › Funding"], ["Learn AI for free", "AI & Certifications › Courses"], ["Practise speaking", "Communication Lab › Daily challenge"],
        ["Build a resume", "Resume & Interview › Resume builder"], ["Practise an interview", "Resume & Interview › Mock interview"], ["See everything I've done", "My Progress"]], "dense", widths=["48%", "52%"]),
    section="Quick map")
