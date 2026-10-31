from lib import *

divider(5, "dash", "Your Dashboard", "One login opens every tool. How to find your way around, what's inside each tool, how it works, and the tasks to complete.",
        ["Signing in and the home screen", "Finding your way around", "Your results pages", "Explore: careers, exams, scholarships, study abroad", "Get experience: internships and jobs",
         "Life skills: money and law", "Build and prove: research, startups, AI, communication", "Create: resume, interview, portfolio", "Track: GPS, progress, certificates", "Tasks to complete, and a quick map"],
        "feat/progress.webp")
S = "Your Dashboard"


def toolhead(kicker, t1, t2, lead, art, stats_=None):
    st = ""
    if stats_:
        st = '<div class="statline">' + "".join(f"<span><b>{a}</b>{b}</span>" for a, b in stats_) + "</div>"
    return (f'<div class="toolhead"><div><div class="kicker">{kicker}</div><h1 class="title">{t1}<br><span class="c1">{t2}</span></h1>'
            f'<p class="lead">{lead}</p>{st}</div>{img(art)}</div>')


def shots2(a, b, ca="", cb=""):
    return two(browser("shots/" + a + ".jpg", ca), browser("shots/" + b + ".jpg", cb), gap="4mm")


# ---------------------------------------------------------------- home
mark("Signing in and the home screen")
add(head("Dashboard home", "Your report becomes", "a dashboard you use.",
         "Sign in at careerfitment.onegrasp.com with your email and password. You land on the dashboard home: your report at the top, your toolkit below, the menu on the left.")
    + laptop("shots/dash-home.jpg", pins=[(1, 9, 11), (2, 33, 3.5), (3, 63, 3.5), (4, 80, 17), (5, 92, 17), (6, 23, 28), (7, 9, 22), (8, 9, 74)])
    + grid([f'<div class="lab"><span>{i + 1}</span><div><b>{t}</b><p>{x}</p></div></div>' for i, (t, x) in enumerate([
        ("Your name and class", "Confirms you're in the right account."), ("Search (press /)", "Find any result, tool or page."), ("My progress", "Everything you've done so far."),
        ("Open my full report", "Every page of your report, with Download."), ("See my profile", "Your results at a glance."), ("Your toolkit", "One card per tool; new tools say NEW."),
        ("Explore menu", "All tools, always on the left."), ("Your results", "Profile, 8 dimensions, fields, thinking, plan.")])], 4, "mt", gap="2.4mm 4mm")
    + two(callout("simple", "Think of the dashboard as your <b>career home</b>. The report says <i>who you are</i>; the dashboard helps you <i>do something about it</i>, every week."),
          callout("good", "Forgot your password? Tap “Forgot password” on the sign-in page for a reset link. Nobody, including OneGrasp, can see your password."), "push", gap="4mm"),
    section=S)

mark("Finding your way around")
groups = [("Explore", "#F97316", ["Career Library", "Entrance Exams", "Scholarships", "Study Abroad", "Internships", "Jobs", "Financial Literacy", "Law & Rights", "Research", "Startups", "AI & Certifications", "Communication Lab", "Spotlight"]),
          ("Your results", "#10B981", ["Your profile", "8 Dimensions", "Best-fit fields", "How you think", "My plan"]),
          ("Track", "#8B5CF6", ["My Progress", "Certificates"]), ("Create", "#0EA5E9", ["Resume & Interview", "Build your website"])]
add(head("Navigation", "Finding your", "way around.", "The left menu stays on every screen and is grouped so you always know where a tool lives. On a phone, tap Menu at the top.")
    + two('<div class="navmap">' + "".join(f'<div class="ng" style="--g:{c}"><b>{g}</b><div>' + "".join(f"<span>{i}</span>" for i in its) + "</div></div>" for g, c, its in groups) + "</div>",
          browser("shots/res-dims.jpg", "The menu, on the left of every screen."), ratio="1fr 1fr", gap="5mm")
    + h3("Inside every tool, the same five things", "layers")
    + steps([("Breadcrumb", "Dashboard › Tool › Page. Click any part to go back.", "chevrons-right"), ("Tabs", "Each tool's sections across the top.", "panel-top"),
             ("First-visit tour", "A short tour the first time. Skip any time.", "info"), ("Start here cards", "The four best things to do first.", "sparkles"),
             ("Get certified", "Finish a course, earn a certificate.", "award")], cols=5)
    + callout("try", "Spend 10 minutes clicking every item in the menu once. You'll never feel lost again.", cls="push"),
    section=S)

mark("Your results pages")
add(head("Your results", "Your profile and", "your 8 dimensions.", "The Your results pages are your report made interactive. Open them from the left menu.")
    + shots2("res-profile", "res-dims", "Your profile: title, type, strongest interest, top field.", "8 Dimensions: tap a dimension to open its explanation.")
    + two(card("Your profile", "Your title (for example “The Systematic Organiser”), personality type, interest code, top field, emotional intelligence and learning style in one view, plus a profile at a glance: personality, work style, values.", "user-round", "#F97316"),
          card("8 Dimensions", "A tab for each dimension: your score against a typical student, a plain-words explanation, strengths, areas to grow and recommended actions.", "radar", "#10B981"), "mt", gap="4mm")
    + callout("simple", "Your results pages and your PDF report show the <b>same results</b>. The dashboard version is easier to explore: tap any dimension to open it.", cls="push"),
    section=S)

add(head("Your results", "Best-fit fields, how you", "think, and your plan.")
    + shots2("res-fields", "res-plan", "Best-fit fields: ranked, with a fit % and the reason.", "My plan: next 30 days (quick wins) and next 90 days (momentum).")
    + cards([("compass", "Best-fit fields", "Your top fields ranked with fit % and the reason (“aligned with your hands-on problem-solving”). Tap Explore careers to open them in the Career Library.", "#F97316"),
             ("brain", "How you think", "Your intelligences, aptitudes, motivators and learning styles as bars, side by side.", "#8B5CF6"),
             ("list-checks", "My plan", "Small steps for your top field. Tick each item off; the ring shows how much you've done.", "#10B981")], 3, "mt")
    + callout("task", "Complete the three “next 30 days” items in <b>My plan</b> this month. They're chosen for your top field.", cls="push"),
    section=S)

# ---------------------------------------------------------------- explore
mark("Career Library, Test-Drive and Decision Room")
add(toolhead("Explore · Career Library", "930 careers,", "explained simply.", "What each career is, the skills it needs, what it pays in India, and a degree roadmap to get there.", "feat/careers.webp",
             [("930", "careers"), ("8", "fields"), ("2,500+", "degree roadmaps")])
    + shots2("careers", "career-roadmaps", "Search any career, or browse 8 fields.", "Degree roadmaps: a year-by-year plan for 1,500+ roles.")
    + h3("How to use it", "footprints")
    + steps([("Search or browse", "Type a job, skill or subject, or pick a field.", "search"), ("Open a career", "What the job is, skills, salary, demand, how to get in.", "book-open"),
             ("Open its roadmap", "Year by year: skills, internships, exams, first jobs.", "route"), ("Save and compare", "Shortlist 3–5 careers to discuss at home.", "bookmark")], cols=4)
    + findit("Dashboard menu", "Career Library")
    + callout("warn", "A roadmap is a guide, not a guarantee. Entry routes change, so confirm with the college or employer.", cls="push"),
    section=S)

add(head("Explore · Try before you choose", "Test-drive a career.", "Decide as a family.", "Two tools that turn reading into real experience, and arguments into calm conversations.")
    + shots2("test-drive", "decision-room", "Career Test-Drive: live a working day in five moments.", "Family Decision Room: compare two paths side by side.")
    + two(box(h3("Career Test-Drive", "play") + vsteps([("Pick a career", "Any career you're curious about."), ("Live five moments", "Real situations from a working day."), ("Choose what you'd do", "See what happens next."),
                                                     ("Rate each moment", "How much would you enjoy it?"), ("Get an honest summary", "Likes, honest downsides, facts, and something to try this month.")])),
          box(h3("Family Decision Room", "users") + p("Put two paths side by side (for example B.Tech CSE vs B.Sc Data Science) and compare them with facts: fit with your report, cost, time, exams, jobs and risks.")
              + p("Each family member adds their view, and the page ends with a decision and a first step.") + callout("parent", "Use it whenever you and your child disagree. Facts on a screen cool a debate faster than any lecture."), "soft"), "mt", gap="4mm")
    + findit("Career Library", "Test-drive a career  ·  Decide with your family"),
    section=S)

mark("Entrance Exams")
add(toolhead("Explore · Entrance Exams", "Every entrance exam,", "and the ones you can take.", "Search any exam, check if you're eligible, and plan backwards from its date.", "feat/exams.webp",
             [("29", "exams"), ("44", "lessons"), ("34", "tools and planners")])
    + shots2("exams", "exams-dash", "Entrance Exams home.", "My exams and deadlines: only the exams open to you.")
    + h3("The 29 exams in the directory", "clipboard-list")
    + pills(["JNVST (Navodaya)", "AISSEE (Sainik School)", "NMMS", "NSEP · NSEC · NSEB · NSEA · NSEJS", "JEE Main", "JEE Advanced", "NEET-UG", "CUET-UG", "CLAT", "AILET", "NDA & NA", "NATA", "NIFT", "NID DAT",
             "UCEED", "IPMAT", "BITSAT", "GATE", "CAT", "XAT", "CMAT", "CUET-PG", "UGC NET", "UPSC Civil Services", "CDS", "SSC CGL", "IBPS PO", "IBPS Clerk", "SAT"])
    + steps([("Fill your profile once", "Class, stream, marks, category, state.", "user-round-pen"), ("See what you can take", "Exams open to you now or soon.", "calendar-check"),
             ("Follow exams", "Get deadline reminders on your dashboard.", "bell"), ("Check official links", "Every exam links to its official website.", "external-link")], "mt", cols=4)
    + findit("Dashboard menu", "Entrance Exams", "Your exams"),
    section=S)

add(head("Explore · Entrance Exams", "Plan, practise", "and stay well.", "Four tools take you from “which exam?” to exam day.")
    + shots2("exams-planner", "exams-mocks", "Study planner with the syllabus built in for seven major exams.", "Mock tests with each exam's real marking scheme.")
    + cards([("calendar-days", "Study planner", "Pick an exam and its date. Get a week-by-week plan and tick off syllabus topics as you finish them.", "#F97316"),
             ("timer", "Mock tests", "Short timed practice sets, then a clear view of what to revise.", "#0EA5E9"),
             ("route", "Stage roadmap", "What to do now, this year and next, for your class.", "#8B5CF6"),
             ("heart-pulse", "Wellbeing and backup paths", "Stress support, and good options if an exam doesn't go your way.", "#10B981")], 4, "compact mt")
    + shots2("exams-roadmap", "exams-wellbeing", "Stage roadmap: what should I be doing this year?", "Wellbeing: plan the next step without pressure.")
    + callout("good", "Practice results are never a prediction of your real rank. Use them to find what to revise.", cls="push"),
    section=S)

mark("Scholarships")
add(toolhead("Explore · Scholarships", "Find the money", "you qualify for.", "Search every scholarship, see how much it pays, and track your applications to the deadline.", "feat/scholarships.webp",
             [("40", "scholarships"), ("53", "lessons"), ("47", "tools")])
    + shots2("sch", "sch-dash", "Scholarships home.", "Money you can apply for: only what you qualify for.")
    + h3("Some of the 40 schemes", "award")
    + pills(["Central Sector (CSSS)", "INSPIRE-SHE", "NMMSS", "AICTE Pragati", "AICTE Saksham", "AICTE Swanath", "PM YASASVI", "Post-Matric SC/ST", "Reliance Foundation", "Kotak Kanya",
             "Tata Capital Pankh", "SBI Asha", "HDFC Parivartan", "L'Oréal Women in Science", "Santoor", "ICAR Talent", "Ishan Uday", "PM Scholarship (CAPF/RPF)", "Chevening", "Commonwealth",
             "DAAD", "Erasmus Mundus", "Fulbright-Nehru", "J N Tata", "K C Mahindra", "Inlaks"])
    + callout("warn", "Genuine scholarships <b>never</b> ask you to pay to receive money. Never share bank passwords, OTPs or PINs.", cls="mt")
    + findit("Dashboard menu", "Scholarships", "Find"),
    section=S)

add(head("Explore · Scholarships", "Track it.", "Win it. Keep it.", "Finding a scholarship is half the job. These tools help you apply on time and win.")
    + shots2("sch-cal", "sch-essay", "Deadline calendar: every official date in one place.", "Essay helper: prompts, structure and a checklist.")
    + cards([("calendar", "Deadline calendar", "Official dates with reminders.", "#F97316"), ("clipboard-list", "My applications", "Track each one from planning to won.", "#0EA5E9"),
             ("pen-line", "Essay helper", "Prompts and a checklist for a stronger statement.", "#8B5CF6"), ("folder-lock", "Document vault", "Upload certificates once; reuse everywhere.", "#10B981"),
             ("shield-alert", "Scam check", "Spot fake scholarships and report them.", "#DC2626"), ("trophy", "Money won", "What you won and the renewal rules.", "#F5B700")], 3, "compact mt")
    + callout("task", "Add 3 scholarships to <b>My applications</b> and put their deadlines in the calendar this week.", cls="push"),
    section=S)

mark("Study Abroad")
add(toolhead("Explore · Study Abroad (Abroad Compass)", "Study abroad,", "one decision at a time.", "Decide whether to go, where and for what, and check the money works before anyone sells you a university.", "feat/study-abroad.webp",
             [("6", "steps"), ("30", "lessons"), ("29", "tools"), ("8", "countries")])
    + '<div class="flow6">' + "".join(f'<div><span>{i}</span>{t}</div>' for i, t in enumerate(["Decide", "Country", "Course", "Universities", "Money", "Prepare"], 1)) + "</div>"
    + shots2("sa-countries", "sa-unis", "Compare up to four countries: costs, work rights, what's next.", "Shortlist universities as reach, match or safe.")
    + p("Countries covered: <b>United States, Canada, United Kingdom, Australia, Germany, France, Ireland, New Zealand</b>.", "mt")
    + findit("Dashboard menu", "Study Abroad"),
    section=S)

add(head("Explore · Study Abroad", "Make the money work,", "then prepare.", "Two tools save families from costly surprises; four more get the application right.")
    + shots2("sa-roi", "sa-sop", "ROI calculator: cost, loan and salary → years to pay back.", "SOP and LOR helper: a structure that works.")
    + cards([("calculator", "ROI calculator", "See how many years a degree abroad takes to pay back.", "#F97316"), ("landmark", "Education loans", "Secured vs unsecured, interest, repayment.", "#0EA5E9"),
             ("award", "Scholarship finder", "Abroad scholarships for Indian students.", "#8B5CF6"), ("file-text", "SOP and LOR helper", "A statement of purpose that sounds like you.", "#10B981"),
             ("shield-alert", "Agent and offer checks", "Before you pay anyone. MBBS abroad: NMC rules.", "#DC2626"), ("folder-lock", "Vault and applications", "Documents once; track every application.", "#F5B700")], 3, "compact mt")
    + callout("example", "A family plans an MS in Germany. The ROI calculator shows low tuition but living costs of about ₹10–12 lakh a year, and roughly 2–3 years to pay back on a typical starting salary. They budget for it before applying, not after.")
    + callout("good", "The calculator gives a planning estimate, not a loan offer. A real budget will have other costs too.", cls="push"),
    section=S)

# ---------------------------------------------------------------- experience
mark("Internships and Jobs")
add(toolhead("Get experience", "Free internships", "and fresh jobs.", "Employers look for proof. Free programmes from real companies, and checked job listings, help you build it.", "feat/internships.webp",
             [("209", "free programmes"), ("135", "companies"), ("₹0", "to join"), ("Daily", "fresh jobs")])
    + shots2("intern", "jobs", "Internships: filter by level and field.", "Jobs: fresh listings, checked for scam signs.")
    + two(box(h3("Internships", "laptop") + bullets(["Beginner, intermediate and advanced levels", "Filter by tech, consulting, finance, AI and more", "Each card shows level, time needed and top skills", "Many end with a certificate for your CV"], "tight")),
          box(h3("Jobs", "briefcase") + bullets(["Trust Shield: every listing checked for scam warning signs", "Internships and fresher-friendly jobs first", "Jobs for your best-fit careers show up for you", "You apply on the original listing"], "tight")), "mt", gap="4mm")
    + callout("warn", "A real employer never asks you to pay for a job, a training kit or a “security deposit”.", cls="push"),
    section=S)

# ---------------------------------------------------------------- life skills
mark("Financial Literacy")
add(toolhead("Life skills · Financial Literacy", "Money skills,", "one level at a time.", "Short lessons, money games and calculators, with virtual money so mistakes cost nothing.", "feat/money.webp",
             [("6", "levels"), ("16", "lessons"), ("19", "tools")])
    + shots2("money", "money-play", "The level path, games and labs.", "Money Life: run your money for 12 months, or ten years.")
    + h3("The eight Money Labs", "flask-conical")
    + grid([f'<div class="mlab">{icon(ic, "5mm", "var(--c1)")}<b>{t}</b><span>{x}</span></div>' for ic, t, x in [
        ("trending-up", "Compounding Playground", "Watch savings grow."), ("hourglass", "Inflation Time Machine", "What ₹100 buys later."), ("receipt", "EMI Truth Teller", "The real cost of a loan."),
        ("credit-card", "Minimum-Due Trap", "Why minimum payments hurt."), ("piggy-bank", "Save vs Grow", "Bank vs investing."), ("file-spreadsheet", "Salary Slip Decoder", "Gross, net, PF, tax."),
        ("target", "Goal Planner", "How much to save each month."), ("house", "Rent vs Buy", "Which makes sense, when.")]], 4, gap="2.4mm")
    + findit("Dashboard menu", "Financial Literacy"),
    section=S)

add(head("Life skills · Scam Shield", "Spot a scam", "before it costs you.", "Real, recent scams and quick games that train you to spot fakes, plus calculators that show what money decisions really cost.")
    + shots2("money-scam", "money-emi", "Scam Shield: a real scam each week, with its red flags.", "EMI Truth Teller: move a slider, watch the interest add up.")
    + two(box(h3("Six Scam Shield games", "shield") + bullets(["Spot the Fake: messages and links", "Safe or Scam: swipe through real requests", "Too Good to Be True: deals and offers", "The Call: bank-security and “digital arrest” calls", "Scam of the Week", "Family Guard: protect parents and grandparents"], "tight")),
          box(h3("Four rules to remember", "triangle-alert") + bullets(["<b>Think before you click.</b> Don't rush.", "<b>Check</b> with the official source.", "<b>Never share</b> your OTP, PIN or passwords.", "<b>Report</b> fraud on <b>1930</b> or cybercrime.gov.in."], "tight", "shield-check", "#DC2626"), "soft"), "mt", gap="4mm")
    + callout("example", "“Your bank account is blocked. Click bit.ly/… to verify.” Three red flags: urgency, a short link, and a request to act outside the official app. Scam Shield teaches you to spot all three in seconds.", cls="push"),
    section=S)

mark("Law & Rights")
add(toolhead("Life skills · Law & Rights", "Know your rights.", "Get help in three taps.", "Answer two quick questions and get the right guide, the steps to take and the helpline to call.", "feat/legal.webp",
             [("24", "guides"), ("37", "lessons"), ("112", "always first")])
    + shots2("legal", "legal-help", "Start with what happened.", "Emergency and help directory: 112 first.")
    + h3("Helplines to save in your phone", "phone")
    + grid([f'<div class="hl"><b>{n}</b><span>{t}</span></div>' for t, n in [("Emergency", "112"), ("Child helpline", "1098"), ("Women helpline", "181"), ("Cyber fraud", "1930"), ("Consumer", "1915"),
                                                                            ("NCW", "14490"), ("RBI", "14448"), ("Free legal aid", "15100"), ("Tele-Law", "14454"), ("Mental health (Tele-MANAS)", "14416"),
                                                                            ("Senior citizens", "14567"), ("Anti-ragging", "1800-180-5522")]], 6, gap="2mm")
    + callout("warn", "In an emergency, call <b>112</b> first. The guides explain your rights in simple words; they do not replace a lawyer. A quick-exit button hides the page on shared devices.", cls="push"),
    section=S)

add(head("Life skills · Law & Rights", "Guides, letters", "and rights cards.", "Plain-word guides for real problems, ready-to-send letters, and cards to keep on your phone.")
    + shots2("legal-guides", "legal-police", "All 24 guides, by situation.", "Police complaint draft: fill in the blanks and print.")
    + h3("The 24 guides", "book-open")
    + pills(["Right to education", "Bullying at school", "Safe and unsafe touch", "Ragging in college", "Child labour and marriage", "Cyberbullying", "Online fraud", "Data and privacy", "Morphed images",
             "Consumer rights", "Bank problems", "Loan recovery harassment", "Renting a home", "Your first job", "Harassment at work", "Unpaid salary", "Internships and gig work", "Domestic violence",
             "Public safety", "Senior citizens", "Disability rights", "Police, FIR and arrest", "RTI", "Free legal aid and courts"])
    + two(card("Action tools", "Police complaint and RTI drafts, an evidence log with legal deadlines, and rights cards for your phone.", "file-pen", "#F97316"),
          card("Learn by scenarios", "“What would you do?” real-life situations: pick an answer and see why.", "message-circle-question", "#0EA5E9"), "mt push", gap="4mm"),
    section=S)

# ---------------------------------------------------------------- build and prove
mark("Research & Conferences (the tool)")
add(toolhead("Build and prove · Research", "From a good question", "to your first conference talk.", "Learn how research works, plan a project around a real conference, and practise presenting it.", "feat/research.webp",
             [("8", "studio units"), ("14", "lessons"), ("13", "tools"), ("5", "levels")])
    + shots2("research-studio", "research-new", "Research Studio: eight short units.", "Start a project: plan backwards from a real conference date.")
    + two(box(h3("The 8 studio units", "book-open") + numbered(["What Is Research?", "Asking a Good Question", "Finding and Reading Sources", "Method and Data", "Analysing Results", "Writing the Abstract", "Poster or Slides", "Presenting and Q&A"])),
          box(h3("Tools", "wrench") + bullets(["Conference finder: student conferences in India and worldwide", "Mentor check: 7 items scored 1–4 before an abstract goes forward", "Practice recorder: 3- or 10-minute takes; stays on your device", "Research profile: a public page with a QR code"], "tight"), "soft"), "mt", gap="4mm")
    + findit("Dashboard home", "Career Toolkit", "Research"),
    section=S)

mark("Startups (the course)")
add(toolhead("Build and prove · Startups", "Build a startup,", "lesson by lesson.", "Watch, read, try each idea on your own project and take the quiz. You finish with a startup idea you've shaped yourself.", "feat/startups.webp",
             [("11", "modules"), ("52", "video lessons"), ("311", "funding programmes")])
    + shots2("startups-place", "startups-videos", "The 2-minute placement quiz.", "Video library: talks from founders.")
    + two(box(h3("The 11 modules", "layers") + numbered(["Founder Mindset", "Finding the Right Problem", "Customer Discovery", "Solution and Idea Validation", "Building the MVP", "Business Model",
                                                       "Marketing and First Customers", "Money and Finance", "Team and Leadership", "Legal and Registration (India)", "Pitching and Fundraising"])),
          box(h3("How it works", "cog") + bullets(["Each lesson: a short video, a short read and a task on your own idea", "Pass a lesson's quiz to unlock the next", "Each module ends with a short test",
                                                  "Every mission becomes a page of your Startup Portfolio", "Funding: all 311 programmes are listed in Part 6"], "tight"), "soft"), "mt", gap="4mm"),
    section=S)

mark("AI & Certifications")
add(toolhead("Build and prove · AI & Certifications", "Learn AI for free,", "get certified.", "Free AI courses that end in a real certificate, and AI tools rated for safety and age, picked for your class.", "feat/ai.webp",
             [("4", "levels"), ("Free", "certificates"), ("Age-rated", "AI tools")])
    + shots2("ai-courses", "ai-tools", "Free certificate courses, by level.", "AI tools allowed at your age, with rating cards.")
    + two(box(h3("Four levels", "layers") + '<div class="lvls">' + "".join(f'<div style="--l:{c}"><b>{t}</b><span>{x}</span></div>' for t, x, c in [
        ("AI Aware", "What AI is, where it goes wrong, staying safe. Everyone starts here.", "#22C55E"), ("AI User", "Using AI tools well for study and work.", "#0EA5E9"),
        ("AI Maker", "Making things with AI: no-code and Python.", "#8B5CF6"), ("AI Builder", "Machine learning and building with AI APIs.", "#F97316")]) + "</div>"),
          box(h3("Courses and tools include", "graduation-cap") + p("YUVA AI for All (Government of India) · Elements of AI · Google's Intro to Generative AI · AI Fluency · Kaggle Python, ML and Deep Learning · Harvard CS50 AI · IBM ML with Python · Hugging Face AI Agents · Building with the Claude API · Teachable Machine · Scratch · Bhashini · Google Colab", "small"), "soft"), "mt", gap="4mm")
    + callout("warn", "Use AI to think better, not to stop thinking. Read “Use AI safely”: five rules, schoolwork honesty, deepfakes and scams.", cls="push"),
    section=S)

mark("Communication Lab")
add(toolhead("Build and prove · Communication Lab", "Speak, write and listen", "with confidence.", "Short videos, activities and voice practice with instant feedback, and your Communication Score (CQ) to show how far you've come.", "feat/communication.webp",
             [("4", "tracks by class"), ("1 min", "daily challenge"), ("CQ", "your score")])
    + shots2("comm", "comm-practice", "A course for your class, module by module.", "Today's speaking challenge: one minute, out loud.")
    + cards([("route", "A track for your class", "Class 6–8, 9–10, 11–12 or college. Modules open week by week: introductions, words that work, professional communication, pitch-ready and more.", "#F97316"),
             ("mic", "Practise out loud", "Record yourself; get feedback in seconds on pace, filler words and pauses, plus three things to try next.", "#0EA5E9"),
             ("gauge", "Your CQ", "Speaking, writing, listening and reading roll into one score, with streaks, XP and badges.", "#8B5CF6")], 3, "compact mt")
    + callout("task", "Do the 1-minute speaking challenge five days in a row. Watch your filler words drop.", cls="push"),
    section=S)

mark("Spotlight")
add(toolhead("Build and prove · Spotlight", "Get published,", "get recognised.", "Career boosters from OneGrasp: present research at an international conference, publish a paper, get an ISBN for your book, start a journal with an ISSN, or be featured in Awardees Magazine.", "feat/spotlight.webp")
    + shots2("spot", "spot-isbn", "Spotlight home: five career boosters.", "Your book, with its own ISBN: the rules in plain words.")
    + cards([("presentation", "Submit an abstract", "To an upcoming OneGrasp international conference (Part 7).", "#F97316"), ("pen-line", "Writing help", "From research question to publication-ready draft.", "#0EA5E9"),
             ("book", "Get an ISBN", "Who can get one, the rules, and help to apply.", "#8B5CF6"), ("newspaper", "Start a journal", "What a journal needs before an ISSN.", "#10B981"),
             ("star", "Awardees Magazine", "Articles, stories and podcast interviews.", "#F5B700")], 5, "compact mt")
    + callout("good", "Spotlight services are paid, but asking is free. Send a request and the OneGrasp team replies with the fee and next steps. Nothing is charged in the dashboard.", cls="push"),
    section=S)

# ---------------------------------------------------------------- create
mark("Resume & Interview")
add(toolhead("Create · Resume & Interview", "From your resume", "to your first offer.", "Build an ATS-friendly resume with AI help for your role, apply to jobs that fit with a tailored cover letter, and practise interviews out loud.", "feat/jobready.webp",
             [("6", "steps to an offer"), ("100", "interview questions")])
    + shots2("resume", "interview-practice", "Resume builder: role kit, AI help, live preview, PDF.", "Mock interview: answer out loud, get feedback.")
    + steps([("Target role", "Your plan starts here.", "target"), ("Build resume", "AI bullets from your words; ATS check.", "file-text"), ("Jobs that fit", "Live jobs with a fit score.", "briefcase"),
             ("Cover letter", "Tailored in one click.", "mail"), ("Practise", "100 questions + mock interviews.", "mic"), ("Get the offer", "Track to the finish.", "trophy")], "mt", cols=6)
    + callout("simple", "An <b>ATS</b> (Applicant Tracking System) is software companies use to screen resumes before a human reads them. The builder checks your resume the same way.", cls="push"),
    section=S)

mark("Portfolio, Career Passport and Career GPS")
add(head("Create and track", "Your website, your passport,", "your weekly GPS.", "Three tools that turn what you do into proof you can share.")
    + shots2("passport", "gps", "Career Passport: achievements with proof, verified by your school.", "Career GPS: three missions every week.")
    + cards([("globe", "Build your website", "A professional portfolio page, built tab by tab: summary, experience, education, certifications, skills. Private until you share the link.", "#F97316"),
             ("badge-check", "Career Passport", "Add projects, certificates and wins with proof. Your school verifies them. Share one QR-checkable record.", "#0EA5E9"),
             ("compass", "Career GPS", "Every Monday: explore a career, try a small task, build something. 10–20 minutes each, +10 points per mission. Do all three to keep your streak.", "#10B981")], 3, "mt")
    + callout("good", "Add only what's true and what you can show proof for. A short, honest profile beats a long one.", cls="push"),
    section=S)

mark("My Progress and Certificates")
add(head("Track", "Everything you've done,", "in one place.", "Lessons finished, modules left, time spent and your streak, for every feature you use. Plus certificates you can share.")
    + shots2("progress", "certificates", "My Progress: lessons, time, streak, and one tap to continue.", "Certificates: finish a course, get one with your name.")
    + two(box(h3("What My Progress shows", "chart-column") + bullets(["Lessons done and still to do, per feature", "Your day streak and activity calendar", "Time spent on each feature", "One tap to continue where you stopped"], "tight")),
          box(h3("How to earn a certificate", "award") + bullets(["Finish every lesson of a OneGrasp course", "It carries your name, class and course", "Share it on LinkedIn or with family", "Each one has an ID anyone can verify"], "tight"), "soft"), "mt", gap="4mm")
    + callout("teacher", "If students joined through your school, the Institution Portal shows this progress too, so help arrives at the right time, without seeing their answers.", cls="push"),
    section=S)

# ---------------------------------------------------------------- tasks and quick map
mark("Tasks to complete")
add(head("Your tasks", "Ten weeks to use", "the whole dashboard.", "Complete these in order and you'll have used every major tool within one school term.")
    + table(["Week", "Tool", "Task to complete", "How you know it's done"], [
        ["1", "Your results", "Read Your profile and all 8 Dimensions", "You can explain your type and code"], ["1", "My plan", "Tick the three “next 30 days” items", "The plan ring moves"],
        ["2", "Career Library", "Read 5 careers in your top field; open one roadmap", "Saved in your history"], ["2", "Test-Drive", "Live a day in your top career", "You get a day summary"],
        ["3", "Entrance Exams", "Fill your profile; follow 2 exams; make a plan", "Deadlines appear in My exams"], ["3", "Scholarships", "Add 3 to My applications", "Calendar shows deadlines"],
        ["4", "Financial Literacy", "Finish Level 1; play Money Life once", "Level 2 unlocks"], ["4", "Scam Shield", "Play Safe or Scam and Spot the Fake", "Your score is saved"],
        ["5", "Law & Rights", "Answer “what happened?” once; save rights cards", "Lessons read in Progress"], ["5", "AI & Certifications", "Finish AI Aware; start one free course", "Certificate or badge"],
        ["6", "Communication Lab", "Do 5 daily speaking challenges", "Your CQ and streak appear"], ["7", "Internships", "Start one free programme at your level", "Provider certificate"],
        ["8", "Research / Startups", "Finish studio unit 1 or startup module 1", "Quiz passed; next unlocks"], ["9", "Resume & Portfolio", "Build your resume; publish your website", "PDF downloaded; link copied"],
        ["10", "Career Passport", "Add 2 achievements with proof", "School verifies them"], ["Every week", "Career GPS", "Complete all three missions", "Streak and +30 points"]], "dense", widths=["11%", "20%", "39%", "30%"])
    + callout("simple", "Every lesson works the same way: <b>open → watch or read → do the activity → pass the quiz</b>. The next lesson unlocks. Finish a course to unlock its certificate.", cls="push"),
    section="Tasks")

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
