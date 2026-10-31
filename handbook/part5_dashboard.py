from lib import *

S = "Your Dashboard"

divider(5, "Your Dashboard", "One login opens every tool. How to find your way around, what is inside each tool, how it works, and the tasks to complete.",
        ["Signing in and the home screen", "Finding your way around", "Your results pages", "Explore: careers, exams, scholarships, study abroad", "Get experience: internships and jobs",
         "Life skills: money and law", "Build and prove: research, startups, AI, communication, Spotlight", "Create: resume, interview, portfolio, passport", "Track: GPS, progress, certificates",
         "Tasks to complete, and a quick map"],
        image="shots/dash-home.jpg")


def tool(eyebrow, t1, t2, lead, shots, body, find, good=None, sec=S):
    if len(shots) == 1:
        top = shot(shots[0][0], shots[0][1])
    else:
        top = two(shot(shots[0][0], shots[0][1]), shot(shots[1][0], shots[1][1]))
    add(head(eyebrow, t1, t2, lead) + top + findit(*find) + body + (note("Good to know:", good, "push") if good else ""), section=sec)


mark("Signing in and the home screen")
tool("Dashboard home", "Your report becomes", "a dashboard you use.",
     "Sign in at careerfitment.onegrasp.com with your email and password. You land on the dashboard home: your report at the top, your toolkit below.",
     [("shots/dash-home.jpg", "The home screen: “Your report is ready”, then Your toolkit, with every tool as a card.")],
     two(box(h3("On the home screen") + bullets([
         "<b>Open my full report</b>: every page of your report, with Download.",
         "<b>See my profile</b>: your results at a glance.",
         "<b>Your toolkit</b>: one card per tool. New tools are marked NEW.",
         "<b>My progress</b> (top right): everything you've done.",
         "<b>Search</b> (press /): find any result, tool or page."], "tight")),
         box(h3("Three things that are always true") + bullets([
             "<b>One login.</b> Every tool, one place.",
             "<b>Always saved.</b> Pick up where you left off.",
             "<b>Linked to your report.</b> Tools show you what fits your results first."], "tight"), "tint")),
     ("careerfitment.onegrasp.com", "Sign in", "Dashboard"),
     "forgot your password? Use “Forgot password” on the sign-in page to get a reset link by email. Nobody, including OneGrasp, can see your password.")

mark("Finding your way around")
add(head("Navigation", "Finding your", "way around.",
         "The menu on the left stays on every screen. It is grouped so you always know where a tool lives. On a phone, tap Menu.")
    + two(shot("shots/res-dims.jpg", "The left menu: Explore, Your results, Track and Create."),
          table(["Group", "What's in it"], [
              ["<b>Explore</b>", "Career Library, Entrance Exams, Scholarships, Study Abroad, Internships, Jobs, Financial Literacy, Law & Rights, Research, Startups, AI & Certifications, Communication Lab, Spotlight"],
              ["<b>Your results</b>", "Your profile, 8 Dimensions, Best-fit fields, How you think, My plan"],
              ["<b>Track</b>", "My Progress, Certificates"],
              ["<b>Create</b>", "Resume & Interview, Build your website"]], "dense", widths=["28%", "72%"]), ratio="1.1fr 1fr")
    + h3("Inside every tool, the same pattern")
    + steps([("A breadcrumb at the top", "Dashboard › Tool › Page. Click any part to go back."),
             ("Tabs across the top", "For example Scholarships has Overview, Find, All scholarships, Track and prepare."),
             ("A first-visit tour", "A short tour explains the tool the first time you open it. Skip it any time."),
             ("“Start here” cards", "The four most useful things to do first in that tool."),
             ("Back to Dashboard", "Always one click away, top right.")], "row"),
    section=S)

mark("Your results pages")
add(head("Your results", "Your profile and", "your 8 dimensions.",
         "The Your results pages are your report, made interactive. Open them from the left menu.")
    + two(shot("shots/res-profile.jpg", "Your profile: your type and title (here, “The Systematic Organiser”), strongest interest, profile at a glance."),
          shot("shots/res-dims.jpg", "8 Dimensions: tap a dimension to see your score, what it means, strengths, areas to grow and actions."))
    + cards([("Your profile", "Your title, personality type, interest code, top field, emotional intelligence and learning style in one view, plus a profile at a glance (personality, work style, values)."),
             ("8 Dimensions", "A tab for each dimension with your score against a typical student, a plain-words explanation, strengths, areas to grow and recommended actions.")], 2, "mt"),
    section=S)

add(head("Your results", "Best-fit fields, how you", "think, and your plan.")
    + two(shot("shots/res-fields.jpg", "Best-fit fields: your top fields with a fit % and why each one matched you."),
          shot("shots/res-plan.jpg", "My plan: next 30 days (quick wins) and next 90 days (momentum), with tick boxes."))
    + cards([("Best-fit fields", "Your top career fields ranked, with fit % and the reason (for example “aligned with your hands-on problem-solving”). Tap “Explore careers” to open them in the Career Library."),
             ("How you think", "Your intelligences, aptitudes, motivators and learning styles as bars, side by side, so you can see your thinking style at a glance."),
             ("My plan", "Small steps for your top field: next 30 days (quick wins) and next 90 days (momentum). Tick each item off. The ring shows how much of the plan you've done.")], 3, "mt")
    + note("Task:", "complete at least the three “next 30 days” items in My plan this month. They are chosen for your top field.", "push"),
    section=S)

# ---------------------------------------------------------------- explore
mark("Career Library, Test-Drive and Decision Room")
tool("Explore · Career Library", "930 careers,", "explained simply.",
     "What each career is, the skills it needs, what it pays in India, and a degree roadmap to get there.",
     [("shots/careers.jpg", "Search any career by job title, keyword or domain, or browse 8 fields."), ("shots/career-roadmaps.jpg", "Degree roadmaps: a year-by-year plan for 1,500+ roles.")],
     stats([("930", "careers explained"), ("8", "fields to browse"), ("2,500+", "degree roadmaps")])
     + steps([("Search or browse", "Type a job, skill or subject (doctor, design, coding), or pick a field from technology to trades."),
              ("Open a career", "Read what the job is, skills, salary range and demand, and how to get in."),
              ("Open its degree roadmap", "Year by year: skills, internships, exams and first jobs for your exact degree.")], "row"),
     ("Dashboard menu", "Career Library"), "a roadmap is a guide, not a guarantee. Entry routes and requirements change, so confirm them with the college or employer.")

tool("Explore · Try before you choose", "Test-drive a career.", "Decide as a family.",
     "Two tools that turn reading into real experience and calm conversations.",
     [("shots/test-drive.jpg", "Career Test-Drive: live one working day in a career, in five moments."), ("shots/decision-room.jpg", "Family Decision Room: compare two paths side by side, then decide together.")],
     two(box(h3("Career Test-Drive") + steps([("Pick a career", "Any career you are curious about."), ("Live five moments", "Real situations from a working day."),
                                            ("Choose what you'd do", "See what happens."), ("Rate each moment", "How much would you enjoy it?"),
                                            ("Get an honest summary", "Likes, honest downsides, facts, and something to try this month.")])),
         box(h3("Family Decision Room") + p("Put two paths side by side (for example B.Tech CSE vs B.Sc Data Science) and compare them with facts: fit with your report, cost, time, exams, jobs and risks.")
             + p("Each family member adds their view. The page ends with a decision and a first step, so the conversation ends with action, not an argument.") + note("Tip:", "use it with the parents' questions in Part 8."), "tint")),
     ("Career Library", "Test-drive a career  ·  Decide with your family"),
     "Test-Drive is exploration, not commitment. It is written with AI from OneGrasp's career information, and real days vary.")

mark("Entrance Exams")
tool("Explore · Entrance Exams", "Every entrance exam,", "and the ones you can take.",
     "Search any exam, check if you're eligible, and plan backwards from its date.",
     [("shots/exams.jpg", "Entrance Exams home: search, see what you can take, plan and practise."), ("shots/exams-dash.jpg", "My exams and deadlines: fill in your profile once, see only exams open to you.")],
     stats([("29", "exams in the directory"), ("44", "short lessons"), ("34", "tools and planners")])
     + box(h3("Exams in the directory") + '<p class="small">' + " · ".join([
         "JNVST (Navodaya, Class 6)", "AISSEE (Sainik School)", "NMMS", "National Standard Exams (NSEP, NSEC, NSEB, NSEA, NSEJS)", "JEE Main", "JEE Advanced", "NEET-UG", "CUET-UG",
         "CLAT", "AILET", "NDA & NA", "NATA", "NIFT", "NID DAT", "UCEED", "IPMAT", "BITSAT", "GATE", "CAT", "XAT", "CMAT", "CUET-PG", "UGC NET", "UPSC Civil Services", "CDS",
         "SSC CGL", "IBPS PO", "IBPS Clerk", "SAT"]) + "</p>"),
     ("Dashboard menu", "Entrance Exams", "Your exams"), "eligibility and dates change. Always check the official exam website, linked from every exam page.")

tool("Explore · Entrance Exams", "Plan, practise", "and stay well.",
     "Four tools take you from “which exam?” to exam day.",
     [("shots/exams-planner.jpg", "Study planner and syllabus tracker: a week-by-week plan with the syllabus built in for seven major exams."), ("shots/exams-mocks.jpg", "Mock tests and analysis: practise with each exam's real marking scheme.")],
     cards([("Study planner", "Pick an exam and date. Get a week-by-week plan and tick off syllabus topics as you finish them."),
            ("Mock tests", "Short practice sets with the real marking scheme, then a clear view of what to revise."),
            ("Stage roadmap", "What to do now, this year and next, for your class (Class 6 to college)."),
            ("Wellbeing and backup paths", "Plan the next step without pressure: stress support, and good options if an exam doesn't go your way.")], 4, "compact"),
     ("Entrance Exams", "Prepare", "Planner  ·  Mocks  ·  Roadmap  ·  Wellbeing"),
     "practice results are never a prediction of your real rank.")

mark("Scholarships")
tool("Explore · Scholarships", "Find the money", "you qualify for.",
     "Search every scholarship, see how much it pays, and track your applications to the deadline.",
     [("shots/sch.jpg", "Scholarships home: find, track and prepare."), ("shots/sch-dash.jpg", "Money you can apply for: fill in your profile once and see only what you qualify for.")],
     stats([("40", "scholarships listed"), ("53", "short lessons in 6 modules"), ("47", "tools and trackers")])
     + box(h3("Some of the schemes listed") + p("Central Sector Scheme (CSSS) · INSPIRE-SHE · NMMSS · AICTE Pragati, Saksham and Swanath · PM YASASVI · Post-Matric SC / ST / disability · Reliance Foundation UG and PG · Kotak Kanya · Tata Capital Pankh · SBI Asha · HDFC Parivartan · L'Oréal Women in Science · Santoor · ICAR National Talent · Ishan Uday · PM Scholarship (CAPF, RPF, police) · Chevening · Commonwealth · DAAD · Erasmus Mundus · Fulbright-Nehru · J N Tata · K C Mahindra · Inlaks", "small")),
     ("Dashboard menu", "Scholarships", "Find"), "genuine scholarships never ask you to pay to receive money. Never share bank passwords, OTPs or PINs.")

tool("Explore · Scholarships", "Track it.", "Win it. Keep it.",
     "Finding a scholarship is half the job. These tools help you apply on time and win.",
     [("shots/sch-cal.jpg", "Deadline calendar: every official date in one place."), ("shots/sch-essay.jpg", "Essay and statement helper: prompts and a checklist.")],
     cards([("Deadline calendar", "Official dates, with reminders, so you never miss one."), ("My applications", "Track each application from “planning” to “won”."),
            ("Essay helper", "Prompts, structure and a checklist for a stronger statement."), ("Document vault", "Upload certificates and ID once; reuse them for every form."),
            ("Scam check", "How to spot fake scholarships and what to report."), ("Money won and renewals", "Record what you've won and the renewal rules to keep it.")], 3, "compact"),
     ("Scholarships", "Track and prepare"))

mark("Study Abroad")
tool("Explore · Study Abroad (Abroad Compass)", "Study abroad,", "one decision at a time.",
     "Decide whether to go, where and for what, and check the money works before anyone sells you a university.",
     [("shots/sa-countries.jpg", "Compare up to four countries side by side: real costs, work rights, what's next."), ("shots/sa-unis.jpg", "Universities: browse by country and shortlist each as reach, match or safe.")],
     stats([("6", "clear steps to decide"), ("30", "short lessons"), ("29", "tools and checks"), ("8", "countries compared")])
     + '<div class="flow">' + "".join(f"<div><b>{i}</b>{t}</div>" for i, t in enumerate(["Decide", "Country", "Course", "Universities", "Money", "Prepare"], 1)) + "</div>"
     + p("Countries: United States, Canada, United Kingdom, Australia, Germany, France, Ireland and New Zealand.", "small mt"),
     ("Dashboard menu", "Study Abroad"))

tool("Explore · Study Abroad", "Make the money work,", "then prepare.",
     "Two tools save families from costly surprises; four more get the application right.",
     [("shots/sa-roi.jpg", "ROI calculator: cost, loan and expected salary give the years to pay back."), ("shots/sa-sop.jpg", "SOP and LOR helper: a structure that works, section by section.")],
     cards([("ROI calculator", "Enter cost, loan and expected salary. See how many years it takes to pay back."), ("Education loans", "Secured vs unsecured, interest, and how repayment works."),
            ("Scholarship finder", "Study-abroad scholarships for Indian students, by country and level."), ("SOP and LOR helper", "Write a statement of purpose that sounds like you."),
            ("Agent and offer safety", "Checks to run before you pay anyone. MBBS abroad: India's NMC rules."), ("Document vault and applications", "Passport, transcripts and letters once; track every application.")], 3, "compact"),
     ("Study Abroad", "Money  ·  Prepare"), "the calculator gives a planning estimate, not a loan offer. A real budget will have other costs too.")

# ---------------------------------------------------------------- experience
mark("Internships and Jobs")
tool("Get experience", "Free internships", "and fresh jobs.",
     "Employers look for proof. Free programmes from real companies, and checked job listings, help you build it.",
     [("shots/intern.jpg", "Internships: 209 free programmes from 135 companies, filtered by level and field."), ("shots/jobs.jpg", "Jobs: fresh listings every day, checked for scam signs.")],
     two(box(h3("Internships") + stats([("209", "free programmes"), ("135", "companies"), ("₹0", "to join any")]) + bullets(["Beginner, intermediate and advanced levels", "Filter by tech, consulting, finance, AI and more", "Each card shows level, time needed and top skills", "Many end with a certificate for your CV"], "tight")),
         box(h3("Jobs") + stats([("Daily", "fresh listings"), ("10", "fields"), ("4", "tabs")]) + bullets(["Trust Shield: every listing checked for scam warning signs", "Internships and fresher-friendly jobs first", "Jobs for your best-fit careers show up for you", "You apply on the original listing"], "tight"))),
     ("Dashboard menu", "Internships  ·  Jobs"), "fake job offers target freshers. A real employer never asks you to pay for a job, training kit or “security deposit”.")

# ---------------------------------------------------------------- life skills
mark("Financial Literacy")
tool("Life skills · Financial Literacy", "Money skills,", "one level at a time.",
     "Short lessons, money games and calculators, with virtual money so mistakes cost nothing.",
     [("shots/money.jpg", "Financial Literacy home: the level path, games and labs."), ("shots/money-play.jpg", "Money Life: run your money for 12 months, or fast-forward ten years.")],
     stats([("6", "levels"), ("16", "lessons"), ("19", "tools")])
     + cards([("Climb the level path", "Money basics, salary and taxes, banking and payments, saving and growing, borrowing and credit. Tick a lesson off and the next level opens."),
              ("Play Money Life", "Split each month's money into needs, wants, savings and growth, and watch your money score change."),
              ("Money Labs", "Compounding Playground, Inflation Time Machine, EMI Truth Teller, Credit Card Minimum-Due Trap, Save vs Grow, Salary Slip Decoder, Goal Planner, Rent vs Buy."),
              ("Cards, habits and journey", "One idea per card, a habit tracker for what you really spend, and your money journey.")], 2, "compact"),
     ("Dashboard menu", "Financial Literacy"), "the simulation uses virtual money only. Financial Age is a fun estimate, not a measurement.")

tool("Life skills · Scam Shield and labs", "Spot a scam", "before it costs you.",
     "Real, recent scams and quick games that train you to spot fakes, plus calculators that show what money decisions really cost.",
     [("shots/money-scam.jpg", "Scam Shield: a real scam each week with its red flags, and six game modes."), ("shots/money-emi.jpg", "EMI Truth Teller: move a slider and watch the interest add up.")],
     two(box(h3("Six Scam Shield modes") + bullets(["Spot the Fake: fake messages and links", "Safe or Scam: swipe through real requests", "Too Good to Be True: deals and offers", "The Call: bank-security and “digital arrest” calls", "Scam of the Week", "Family Guard: protect parents and grandparents"], "tight")),
         box(h3("Four rules to remember") + bullets(["<b>Think before you click.</b> Don't rush.", "<b>Check</b> with the official source or website.", "<b>Never share</b> your OTP, PIN or passwords.", "<b>Report</b> fraud on <b>1930</b> or cybercrime.gov.in."], "tight"), "red")),
     ("Financial Literacy", "Scam Shield  ·  Money Labs"))

mark("Law & Rights")
tool("Life skills · Law & Rights", "Know your rights.", "Get help in three taps.",
     "Answer two quick questions and get the right guide, the steps to take and the helpline to call.",
     [("shots/legal.jpg", "Law & Rights: start with what happened."), ("shots/legal-help.jpg", "Emergency and help directory: 112 first, then every helpline one tap away.")],
     table(["Helpline", "Number", "Helpline", "Number"], [
         ["Emergency (police, fire, ambulance)", "<b>112</b>", "Cyber fraud", "<b>1930</b>"], ["Child helpline", "<b>1098</b>", "Consumer complaints", "<b>1915</b>"],
         ["Women helpline", "<b>181</b>", "RBI contact centre", "<b>14448</b>"], ["National Commission for Women", "<b>14490</b>", "Free legal aid", "<b>15100</b>"],
         ["Anti-ragging", "<b>1800-180-5522</b>", "Tele-Law", "<b>14454</b>"], ["Mental health support (Tele-MANAS)", "<b>14416</b>", "Senior citizens", "<b>14567</b>"]], "dense", widths=["34%", "16%", "32%", "18%"]),
     ("Dashboard menu", "Law & Rights"), "in an emergency, call 112 first. The guides explain your rights in simple words; they do not replace a lawyer. A quick-exit button hides the page on shared devices.")

tool("Life skills · Law & Rights", "Guides, letters", "and rights cards.",
     "Plain-word guides for real problems, ready-to-send letters, and cards to keep on your phone.",
     [("shots/legal-guides.jpg", "All 24 guides, grouped by situation."), ("shots/legal-police.jpg", "Police complaint draft: fill in the blanks and print.")],
     two(box(h3("The 24 guides") + '<p class="small">' + " · ".join(["Right to education", "Bullying and punishment at school", "Safe and unsafe touch", "Ragging in college", "Child labour and child marriage", "Cyberbullying",
                                                                      "Online fraud and scams", "Personal data and privacy", "Morphed images", "Consumer rights", "Problems with your bank", "Loan recovery harassment",
                                                                      "Renting a home", "Your first job", "Sexual harassment at work", "Unpaid salary", "Internships, freelance and gig work", "Domestic violence",
                                                                      "Safety in public places", "Senior citizens", "Rights of persons with disabilities", "Police, FIR and arrest", "Right to Information (RTI)", "Free legal aid and courts"]) + "</p>"),
         box(h3("Action tools") + bullets(["Police complaint and RTI drafts", "Evidence log with legal deadlines", "Rights cards for your phone", "“What would you do?” real-life scenarios", "37 short lessons"], "tight"), "tint")),
     ("Law & Rights", "Guides  ·  Action tools  ·  Learn"))

# ---------------------------------------------------------------- build and prove
mark("Research & Conferences (the tool)")
tool("Build and prove · Research", "From a good question", "to your first conference talk.",
     "Learn how research works, plan a project around a real conference, and practise presenting it.",
     [("shots/research-studio.jpg", "Research Studio: eight short units."), ("shots/research-new.jpg", "Start a project: choose your level, plan backwards from a real conference date.")],
     stats([("8", "studio units"), ("14", "lessons"), ("13", "tools"), ("5", "participation levels")])
     + two(box(h3("The 8 studio units") + '<ol class="num small">' + "".join(f"<li>{u}</li>" for u in ["What Is Research?", "Asking a Good Question", "Finding and Reading Sources", "Method and Data", "Analysing Results", "Writing the Abstract", "Poster or Slides", "Presenting and Q&A"]) + "</ol>"),
           box(h3("Tools") + bullets(["Conference finder: student conferences in India and worldwide", "Mentor check: 7 items scored 1–4 before an abstract goes forward", "Practice recorder: 3- or 10-minute takes; recordings stay on your device", "Research profile: a public page with a QR code"], "tight"), "tint")),
     ("Dashboard home", "Career Toolkit", "Research"))

mark("Startups (the course)")
tool("Build and prove · Startups", "Build a startup,", "lesson by lesson.",
     "Watch, read, try each idea on your own project and take the quiz. You finish with a startup idea you have shaped yourself.",
     [("shots/startups.jpg", "Startups: the Builder track, with progress saved."), ("shots/startups-place.jpg", "The 2-minute placement quiz points you to the right module.")],
     stats([("11", "modules"), ("52", "video lessons"), ("311", "funding programmes")])
     + two(box(h3("The 11 modules") + '<ol class="num small">' + "".join(f"<li>{m}</li>" for m in ["Founder Mindset", "Finding the Right Problem", "Customer Discovery", "Solution and Idea Validation", "Building the MVP", "Business Model", "Marketing and First Customers", "Money and Finance", "Team and Leadership", "Legal and Registration (India)", "Pitching and Fundraising"]) + "</ol>"),
           box(h3("How it works") + bullets(["Each lesson: a short video, a short read and a task on your own idea", "Pass a lesson's quiz to unlock the next", "Each module ends with a short test", "Every module's mission becomes a page of your Startup Portfolio", "A video library of talks from founders", "Funding: grants, loans and incubators (Part 6)"], "tight"), "tint")),
     ("Dashboard home", "Career Toolkit", "Startups"), "learning from failure is part of the course. Module 10 covers legal and registration basics for starting up in India.")

mark("AI & Certifications")
tool("Build and prove · AI & Certifications", "Learn AI for free,", "get certified.",
     "Free AI courses that end in a real certificate, and AI tools rated for safety and age, picked for your class.",
     [("shots/ai-courses.jpg", "Free certificate courses, by level."), ("shots/ai-tools.jpg", "AI tools allowed at your age, each with a rating card.")],
     two(box(h3("Four levels") + table(["Level", "You learn"], [["AI Aware", "What AI is, where it goes wrong, staying safe (everyone starts here)"], ["AI User", "Using AI tools well for study and work"], ["AI Maker", "Making things with AI: no-code and Python"], ["AI Builder", "Machine learning and building with AI APIs"]], "dense")),
         box(h3("Courses and tools include") + p("YUVA AI for All (Government of India) · AI For All · Elements of AI · Google's Introduction to Generative AI · AI Fluency · Kaggle Python, Intro to ML and Deep Learning · Harvard CS50 AI · IBM ML with Python · Hugging Face AI Agents · Building with the Claude API · Teachable Machine · Scratch · Bhashini · Google Colab · Gemini · ChatGPT · Copilot · Claude", "small"), "tint")),
     ("Dashboard menu", "AI & Certifications"), "AI tools are shown only if they are allowed at your age. Read “Use AI safely”: five rules, schoolwork honesty, deepfakes and scams.")

mark("Communication Lab")
tool("Build and prove · Communication Lab", "Speak, write and listen", "with confidence.",
     "Short videos, activities and voice practice with instant feedback, and your Communication Score (CQ) to show how far you've come.",
     [("shots/comm.jpg", "Communication Lab: a course for your class, module by module."), ("shots/comm-practice.jpg", "Today's speaking challenge: a new prompt every day, one minute, out loud.")],
     cards([("A track for your class", "Class 6–8, 9–10, 11–12 or college. Modules open one after another, week by week: introductions, words that work, professional communication, pitch-ready and more."),
            ("Practise out loud", "Record yourself and get feedback in seconds: your pace, filler words, pauses and three things to try next."),
            ("Your CQ", "Speaking, writing, listening and reading roll into one Communication Score, with streaks, XP and badges.")], 3, "compact"),
     ("Dashboard menu", "Communication Lab"))

mark("Spotlight")
tool("Build and prove · Spotlight", "Get published,", "get recognised.",
     "Career boosters from OneGrasp: present research at an international conference, publish a paper, get an ISBN for your book, start a journal with an ISSN, or be featured in Awardees Magazine.",
     [("shots/spot.jpg", "Spotlight home: five career boosters."), ("shots/spot-isbn.jpg", "Your book, with its own ISBN: the official rules in plain words.")],
     cards([("Submit an abstract", "Pick an upcoming OneGrasp international conference and send your abstract (Part 7)."), ("Research writing help", "From your research question to a publication-ready draft."),
            ("Get an ISBN", "Who can get one, the rules, and help to apply."), ("Start a journal (ISSN)", "What a journal needs before it can apply."),
            ("Awardees Magazine", "Articles, blogs, stories and podcast interviews.")], 5, "compact"),
     ("Dashboard menu", "Spotlight"), "Spotlight services are paid, but asking is free. Send a request and the OneGrasp team replies with the fee and next steps. Nothing is charged in the dashboard.")

# ---------------------------------------------------------------- create
mark("Resume & Interview")
tool("Create · Resume & Interview", "From your resume", "to your first offer.",
     "Build an ATS-friendly resume with AI help for your role, apply to jobs that fit with a tailored cover letter, and practise interviews out loud.",
     [("shots/resume.jpg", "Resume builder: the role kit and AI help, with a live preview and PDF download."), ("shots/interview-practice.jpg", "Mock interview: choose a type, answer out loud, get feedback.")],
     steps([("Pick a target role", "Your job plan starts here; each step updates as you go."), ("Build the resume", "The role kit shows what employers ask for; AI writes bullets from your own words and checks it like an ATS."),
            ("See jobs that fit", "Live jobs matched to your resume with a fit score and the skills you're missing."), ("Write a cover letter", "Tailored to each job in one click."),
            ("Practise interviews", "The 100 most common questions with model answers, questions for your role, and mock interviews."), ("Get the offer", "Track applications to the finish.")], "row"),
     ("Dashboard menu", "Resume & Interview", "My job plan"))

mark("Portfolio, Career Passport and Career GPS")
add(head("Create and track", "Your website, your passport,", "your weekly GPS.",
         "Three tools that turn what you do into proof you can share.")
    + two(shot("shots/passport.jpg", "Career Passport: add projects and wins with proof; your school verifies them."),
          shot("shots/gps.jpg", "Career GPS: three short missions every week, picked for you."))
    + cards([("Build your website", "A professional portfolio page you build tab by tab: summary, experience, education, certifications and skills. You decide what is public and share it with Copy Link only when you are ready."),
             ("Career Passport", "Add projects, certificates and wins with proof. Your school verifies them, and you share one QR-checkable record with colleges and employers."),
             ("Career GPS", "Every Monday: three missions (explore a career, try a small task, build something), 10–20 minutes each. +10 points per mission. Do all three to keep your streak. Parents see the week's progress; schools see points and streaks.")], 3)
    + note("Good to know:", "add only what is true and what you can show proof for. A short, honest profile works better than a long one.", "push"),
    section=S)

mark("My Progress and Certificates")
add(head("Track", "Everything you've done,", "in one place.",
         "Lessons finished, modules left, time spent and your streak, for every feature you use. Plus certificates you can share.")
    + two(shot("shots/progress.jpg", "My Progress: lessons done, time spent, your streak, and one tap to continue."),
          shot("shots/certificates.jpg", "Certificates: finish a course, get a certificate with your name."))
    + two(box(h3("What My Progress shows") + bullets(["Lessons done and still to do, per feature", "Your day streak and activity calendar", "Time spent on each feature", "One tap to continue where you stopped"], "tight")),
          box(h3("How to earn a certificate") + bullets(["Finish every lesson of a OneGrasp course (for example all 37 Law & Rights lessons, or the 11 Startup modules)", "Your certificate carries your name, class and course", "Share it on LinkedIn or with friends and family", "Each certificate has an ID anyone can verify"], "tight"), "tint"))
    + note("For schools:", "if you joined through your school, it can see this progress too, so help arrives at the right time. It never sees your answers.", "push"),
    section=S)

# ---------------------------------------------------------------- tasks and quick map
mark("Tasks to complete")
add(head("Your tasks", "What to complete,", "tool by tool.",
         "Every tool has a few core tasks. Complete them in this order and you will have used the whole dashboard within one term.")
    + table(["Week", "Tool", "Task to complete", "How you know it's done"], [
        ["1", "Your results", "Read Your profile and all 8 Dimensions", "You can explain your type and code"],
        ["1", "My plan", "Tick the three “next 30 days” items", "The plan ring moves"],
        ["2", "Career Library", "Read 5 careers in your top field; open one roadmap", "Saved in your history"],
        ["2", "Career Test-Drive", "Live a day in your top career", "You get a day summary"],
        ["3", "Entrance Exams", "Fill your profile; follow 2 exams; make a plan", "Deadlines appear in My exams"],
        ["3", "Scholarships", "Fill your profile; add 3 to My applications", "Calendar shows the deadlines"],
        ["4", "Financial Literacy", "Finish Level 1; play Money Life once", "Level 2 unlocks"],
        ["4", "Scam Shield", "Play Safe or Scam and Spot the Fake", "Your score is saved"],
        ["5", "Law & Rights", "Answer “what happened?” once; save rights cards", "Progress shows lessons read"],
        ["5", "AI & Certifications", "Finish AI Aware; start one free course", "A certificate or badge"],
        ["6", "Communication Lab", "Do 5 daily speaking challenges", "Your CQ and streak appear"],
        ["7", "Internships", "Start one free programme at your level", "Provider certificate"],
        ["8", "Research or Startups", "Finish studio unit 1 or startup module 1", "Quiz passed; next unlocks"],
        ["9", "Resume & Portfolio", "Build your resume; publish your website", "PDF downloaded; link copied"],
        ["10", "Career Passport", "Add 2 achievements with proof", "School verifies them"],
        ["Every week", "Career GPS", "Complete all three missions", "Streak and +30 points"]], "dense", widths=["10%", "20%", "40%", "30%"])
    + note("How lessons work everywhere:", "open a lesson, watch or read, do the activity, pass the quiz. The next lesson unlocks. Finish a course to unlock its certificate.", "push"),
    section="Tasks")

add(head("Quick map", "Where do I find", "…?",
         "Keep this page next to your screen. Every path starts from the left menu of the dashboard.")
    + table(["I want to…", "Go to"], [
        ["Reopen or download my report", "Home › Open my full report › Download"], ["See my type and interest code", "Your results › Your profile"],
        ["See one dimension in detail", "Your results › 8 Dimensions › tap the dimension"], ["See my best-fit careers", "Your results › Best-fit fields"],
        ["Know what to do this month", "Your results › My plan  ·  Career GPS"], ["Find a career's salary and roadmap", "Career Library › search › career page"],
        ["Check if I can take an exam", "Entrance Exams › Your exams"], ["Make a study plan or take a mock", "Entrance Exams › Prepare"],
        ["Find scholarships I qualify for", "Scholarships › Find"], ["See scholarship deadlines", "Scholarships › Track and prepare › Calendar"],
        ["Compare countries to study in", "Study Abroad › Countries"], ["Check if a degree abroad pays back", "Study Abroad › Money › ROI calculator"],
        ["Find a free internship", "Internships"], ["Find a real job", "Jobs  ·  Resume & Interview › Jobs for you"],
        ["Learn money skills", "Financial Literacy"], ["Check a suspicious message", "Financial Literacy › Scam Shield"],
        ["Get help with a legal problem", "Law & Rights › Find help for my situation"], ["Plan a research project", "Research › Start a research project"],
        ["Find startup funding", "Startups › Funding"], ["Learn AI for free", "AI & Certifications › Courses"],
        ["Practise speaking", "Communication Lab › Today's speaking challenge"], ["Build a resume", "Resume & Interview › Resume builder"],
        ["Practise an interview", "Resume & Interview › Mock interview"], ["Make my portfolio website", "Create › Build your website"],
        ["See everything I've done", "My Progress"], ["Get my certificates", "Track › Certificates"]], "dense", widths=["48%", "52%"]),
    section="Quick map")
