from lib import *
from tools import *

THEMES["skills"] = ("Skills for Life & Work", "#0891B2", "#22C55E", "#E8F7FB", "#155E75")
divider(6, "skills", "Skills for Life & Work", "School teaches subjects. These tools teach the skills that decide how well life and work go: money, rights, AI, communication, a job-ready resume, and proof of what you can do.",
        ["Financial Literacy", "Law & Rights", "AI & Certifications", "Communication Lab", "Resume & Interview", "Portfolio, Passport, GPS & Progress", "Spotlight"], "feat/money.webp")

# ---------------------------------------------------------------- 6 Money
mark("Financial Literacy")
tool_theme("t-money", "Financial Literacy", "#CA8A04", "#16A34A")
opener(6, "Financial Literacy", "Money skills, one level at a time: short lessons, a life simulation, eight money labs and Scam Shield games, with virtual money so mistakes cost nothing.", "feat/money.webp",
       [("6", "levels"), ("16", "lessons"), ("19", "tools")],
       pills(["Class 6–8: needs vs wants", "Class 9–12: saving, banking, scams", "UG: salary, tax, credit, EMIs"]),
       ["Every career pays a salary; few schools teach what to do with it.", "Scams cost Indian families crores every year; spotting them is a life skill.", "Compounding rewards people who start early, even with ₹500 a month."],
       [("route", "Level path", "Basics → salary & tax → credit."), ("play", "Money Life", "Run 12 months, or 10 years."), ("flask-conical", "8 Money Labs", "EMI, inflation, compounding…"),
        ("shield", "Scam Shield", "6 games to spot fakes."), ("credit-card", "Money cards", "One idea, one minute."), ("receipt", "Habits", "Track what you really spend.")],
       ("Menu", "Financial Literacy"), "Financial Literacy")
howto("Financial Literacy", [("money-play", "Money Life: split each month into needs, wants, savings and growth."), ("money-scam", "Scam Shield: a real scam each week."), ("money-emi", "EMI Truth Teller.")],
      [("Climb Level 1", "Money basics: two or three short lessons."), ("Play Money Life", "See where your monthly choices lead."), ("Try two labs", "Compounding and EMI first."), ("Play Scam Shield", "Spot the Fake, Safe or Scam, The Call."),
       ("Track a week", "Use Habits to log what you spend.")],
      [callout("warn", "Report fraud on <b>1930</b> or cybercrime.gov.in. Never share OTP, PIN or passwords, with anyone."), callout("simple", "Needs first, then save, then wants. Saving is not what's left over; it's paid first.")], "Financial Literacy")
mission("Financial Literacy",
        [("Learn the basics", "20 min", ["Finish Level 1", "Read 3 money cards", "Unlock Level 2"]),
         ("Play your life", "20 min", ["Play Money Life for 12 months", "Try the Compounding lab", "Note your money score"]),
         ("Become scam-proof", "15 min", ["Play Safe or Scam", "Play The Call", "Teach Family Guard to a parent"])],
        two(box(h3("My monthly budget", "wallet") + table(["", "Plan", "Actual"], [["Needs", "", ""], ["Wants", "", ""], ["Savings", "", ""], ["Growth (invest / learn)", "", ""], ["<b>Total</b>", "", ""]], "fill")),
            box(h3("7-day spending tracker", "receipt") + table(["Day", "Spent on", "₹", "Need / want"], [[d, "", "", ""] for d in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]], "fill dense")), gap="4mm"),
        "You can budget, save first and spot a scam in seconds.", "Financial Literacy")

# ---------------------------------------------------------------- 7 Law
mark("Law & Rights")
tool_theme("t-law", "Law & Rights", "#475569", "#6366F1")
opener(7, "Law & Rights", "Know your rights and what to do first. Answer two questions and get the right guide, the steps to take, ready-made letters and the helpline to call.", "feat/legal.webp",
       [("24", "guides"), ("37", "lessons"), ("112", "always first")],
       pills(["School: bullying, safe touch, cyberbullying", "College: ragging, privacy, fraud", "First job: offer letter, wages, harassment"]),
       ["Knowing your rights is protection: most problems get worse when people don't know the first step.", "Ready-made complaint and RTI letters save time and fear.", "Helplines in your phone can save a life."],
       [("signpost", "What happened?", "Two questions → the right guide."), ("phone", "Helplines", "112 first, then every helpline."), ("book-open", "24 guides", "Plain-word steps."),
        ("file-pen", "Letters", "Police complaint and RTI drafts."), ("clipboard-list", "Evidence log", "With legal deadlines."), ("eye-off", "Quick exit", "Private on shared devices.")],
       ("Menu", "Law & Rights"), "Law & Rights")
howto("Law & Rights", [("legal-guides", "All 24 guides, by situation."), ("legal-help", "Emergency and help directory."), ("legal-police", "Police complaint draft.")],
      [("Start with what happened", "Answer two quick questions."), ("Read the guide", "Your rights and the first steps, in plain words."), ("Call the right helpline", "One tap from the guide."), ("Use the letter", "Fill in the blanks; print or send."),
       ("Keep an evidence log", "Dates, screenshots, deadlines.")],
      [callout("warn", "In danger? Call <b>112</b> first. Guides explain rights; they don't replace a lawyer. Free legal aid: <b>15100</b>."), callout("parent", "Read the safe-touch and cyberbullying guides with younger children.")], "Law & Rights")
mission("Law & Rights",
        [("Save the helplines", "10 min", ["Save 112, 1098, 181, 1930 in your phone", "Fill the emergency card", "Keep it in your bag"]),
         ("Know your rights", "20 min", ["Read 2 guides for your age", "Save your rights cards", "Tell one friend one right"]),
         ("Practise", "15 min", ["Do 3 “What would you do?” scenarios", "Open the police complaint draft", "Learn where RTI lives"])],
        two(box(h3("✂ My emergency card", "id-card") + table(["Who", "Number"], [["Emergency", "<b>112</b>"], ["Child helpline", "<b>1098</b>"], ["Women helpline", "<b>181</b>"], ["Cyber fraud", "<b>1930</b>"],
                                                                                ["Mental health (Tele-MANAS)", "<b>14416</b>"], ["Free legal aid", "<b>15100</b>"], ["Trusted adult 1", ""], ["Trusted adult 2", ""], ["My blood group", ""]], "fill dense"), "cutcard"),
            box(h3("Two rights I learned", "scale") + lines(4) + h3("Where I'd go first if…", "signpost") + lines(2)), gap="4mm"),
        "You know what to do, and who to call, before you ever need it.", "Law & Rights")

# ---------------------------------------------------------------- 8 AI
mark("AI & Certifications")
tool_theme("t-ai", "AI & Certifications", "#DB2777", "#A855F7")
opener(8, "AI & Certifications", "Learn AI for free and get certified: courses from the Government of India's YUVA AI for All to Harvard, Google, IBM and Kaggle, plus AI tools rated for your age.", "feat/ai.webp",
       [("4", "levels"), ("Free", "certificates"), ("Age-rated", "tools")],
       pills(["Everyone: AI Aware", "Class 9–12: AI User & Maker", "UG: AI Builder"]),
       ["AI and big data are among the fastest-growing skills employers want (WEF 2025).", "Free certificates from Google, IBM or Harvard add real weight to a CV.", "Using AI safely and honestly is now part of being a good student."],
       [("layers", "4 levels", "Aware → User → Maker → Builder."), ("award", "Free courses", "End in a certificate or badge."), ("cpu", "AI tools", "Rated for age, privacy, cost."),
        ("shield", "Use AI safely", "5 rules, honesty, deepfakes."), ("graduation-cap", "Partners", "Google, Microsoft, IBM, Harvard."), ("check", "OneGrasp certificates", "For finished courses.")],
       ("Menu", "AI & Certifications"), "AI & Certifications")
howto("AI & Certifications", [("ai-courses", "Free certificate courses by level."), ("ai-tools", "AI tools allowed at your age."), ("ai-safety", "Use AI to think better, not stop thinking.")],
      [("Start at AI Aware", "What AI is, where it goes wrong, staying safe."), ("Pick one free course", "At your level; note the hours."), ("Try one rated tool", "Only the ones shown for your age."), ("Finish and certify", "Download the certificate or badge."),
       ("Climb a level", "User → Maker → Builder.")],
      [callout("warn", "Never paste personal details into AI tools. Check every AI answer; it can be confidently wrong."), callout("simple", "Use AI like a tutor, not a ghost-writer: ask it to explain, then do the work yourself.")], "AI & Certifications")
mission("AI & Certifications",
        [("Become AI Aware", "30 min", ["Finish the AI Aware level", "Read “Use AI safely”", "Sign the pledge below"]),
         ("Earn a certificate", "2–8 hours", ["Pick one free course", "Finish it", "Add it to your Passport"]),
         ("Make something", "45 min", ["Try Teachable Machine or Scratch", "Build one tiny AI project", "Show it to someone"])],
        two(box(h3("My AI learning log", "notebook-pen") + table(["Course / tool", "Provider", "Hours", "Certificate"], [["&nbsp;"] * 4] * 4, "fill")),
            box(h3("My AI honesty pledge", "hand") + bullets(["I'll check AI answers before I trust them", "I'll say when I used AI for schoolwork", "I won't share personal data with AI tools", "I'll use AI to learn, not to skip learning"], "tight") + p("Signed: ______________", "mt"), "soft"), gap="4mm"),
        "You're AI-literate and you have a certificate to prove it.", "AI & Certifications")

# ---------------------------------------------------------------- 9 Communication
mark("Communication Lab")
tool_theme("t-comm", "Communication Lab", "#0891B2", "#2563EB")
opener(9, "Communication Lab", "Speak, write and listen with confidence: a course for your class, a one-minute daily speaking challenge with instant feedback, and your Communication Score (CQ).", "feat/communication.webp",
       [("4", "class tracks"), ("1 min", "daily challenge"), ("CQ", "your score")],
       pills(["Class 6–8 track", "Class 9–10 track", "Class 11–12 track", "College track"]),
       ["Interviews, presentations, group discussions and vivas all reward clear speaking.", "Feedback on pace, filler words and pauses improves you fast.", "A rising CQ is visible proof of growth."],
       [("route", "A course for your class", "Weekly modules."), ("mic", "Speak out loud", "Feedback in seconds."), ("sparkles", "Daily challenge", "A new prompt every day."),
        ("gauge", "Your CQ", "Speaking, writing, listening, reading."), ("flame", "Streaks & XP", "Badges for consistency."), ("trending-up", "Progress", "Your trend over time.")],
       ("Menu", "Communication Lab"), "Communication Lab")
howto("Communication Lab", [("comm", "A course for your class, module by module."), ("comm-practice", "Today's speaking challenge.")],
      [("Open your track", "It matches your class automatically."), ("Do this week's module", "Video, activity, short check-in."), ("Take the daily challenge", "Speak for one minute."), ("Read your feedback", "Pace, filler words, pauses, 3 tips."),
       ("Watch your CQ", "Check the trend every Sunday.")],
      [callout("simple", "Fewer “umm”s and slower pace are the two fastest wins for most students."), callout("try", "Record the same prompt on Monday and Friday. Hear the difference.")], "Communication Lab")
mission("Communication Lab",
        [("Start strong", "15 min", ["Open your track", "Finish module 1", "Note your starting CQ"]),
         ("Five-day streak", "5 × 1 min", ["Do the daily challenge 5 days running", "Read each feedback", "Fix one habit"]),
         ("Your introduction", "20 min", ["Write your 60-second intro below", "Record it", "Re-record until it flows"])],
        two(box(h3("My CQ tracker", "gauge") + table(["Week", "CQ", "Filler words", "One thing I fixed"], [[f"Week {i}", "", "", ""] for i in range(1, 6)], "fill")),
            box(h3("My 60-second introduction", "mic") + p("<b>Who I am:</b>", "small") + lines(1) + p("<b>What I'm good at:</b>", "small") + lines(1) + p("<b>What I'm working towards:</b>", "small") + lines(1) + p("<b>Why it matters to me:</b>", "small") + lines(1)), gap="4mm"),
        "You can introduce yourself confidently to anyone, in one minute.", "Communication Lab")

# ---------------------------------------------------------------- 10 Resume & Interview
mark("Resume & Interview")
tool_theme("t-job", "Resume & Interview", "#E11D48", "#F97316")
opener(10, "Resume & Interview", "From your resume to your first offer: an ATS-friendly resume with AI help, jobs matched with a fit score, tailored cover letters and interview practice out loud.", "feat/jobready.webp",
       [("6", "steps to an offer"), ("100", "interview questions"), ("PDF", "resume download")],
       pills(["Class 11–12: first resume for internships", "UG: placements and first job"]),
       ["Most companies screen resumes with software (ATS) before a human reads them.", "Tailoring each application raises your chances sharply.", "Practising answers out loud is the best cure for interview nerves."],
       [("target", "Target role", "Your job plan starts here."), ("file-text", "Resume builder", "Role kit + AI bullets + ATS check."), ("briefcase", "Jobs for you", "Live jobs with a fit score."),
        ("mail", "Cover letters", "Tailored in one click."), ("messages-square", "100 questions", "With model answers."), ("mic", "Mock interviews", "Feedback on content and delivery.")],
       ("Menu", "Resume & Interview"), "Resume & Interview")
howto("Resume & Interview", [("resume", "Resume builder with live preview and PDF."), ("resume-jobs", "Jobs matched to your resume."), ("interview-practice", "Mock interview.")],
      [("Pick a target role", "From your best-fit fields."), ("Build your resume", "Use the role kit; let AI polish your own words."), ("Check it like an ATS", "Fix missing keywords."), ("Apply with a cover letter", "One tailored letter per job."),
       ("Practise interviews", "Answer out loud; read the feedback.")],
      [callout("simple", "Use the <b>STAR</b> method for answers: Situation, Task, Action, Result."), callout("warn", "Only write what's true. Interviewers ask about every line.")], "Resume & Interview")
mission("Resume & Interview",
        [("Build your resume", "45 min", ["Choose your target role", "Complete every section", "Download the PDF"]),
         ("Apply smart", "30 min", ["Find 3 jobs with a high fit score", "Generate a cover letter for one", "Apply on the original listing"]),
         ("Practise out loud", "30 min", ["Do one mock interview", "Prepare the 3 STAR answers below", "Redo your weakest answer"])],
        table(["Question", "Situation", "Task", "Action", "Result"], [["Tell me about a challenge you solved", "", "", "", ""], ["A time you worked in a team", "", "", "", ""], ["A mistake you learned from", "", "", "", ""]], "fill", ["22%", "19.5%", "19.5%", "19.5%", "19.5%"]),
        "Your resume is ready and your three best stories are rehearsed.", "Resume & Interview")

# ---------------------------------------------------------------- 11 Portfolio / Passport / GPS / Progress
mark("Portfolio, Passport, GPS & Progress")
tool_theme("t-prog", "Proof & Progress", "#EA580C", "#DB2777")
opener(11, "Proof & Progress", "Build your website, collect verified achievements in your Career Passport, follow three Career GPS missions every week, and watch it all add up in My Progress.", "feat/progress.webp",
       [("3", "missions a week"), ("+10", "points each"), ("QR", "verified passport")],
       pills(["Every class", "Parents see weekly progress", "Schools verify achievements"]),
       ["Colleges and employers trust proof more than claims.", "Three small missions a week build a habit that lasts.", "Seeing your streak and progress keeps you going."],
       [("globe", "Build your website", "A portfolio page with one link."), ("badge-check", "Career Passport", "Wins with proof, school-verified."), ("compass", "Career GPS", "Explore · Do · Build, weekly."),
        ("chart-column", "My Progress", "Lessons, time, streak."), ("award", "Certificates", "Verifiable, shareable."), ("qr-code", "QR record", "One check for everything.")],
       ("Menu", "My Progress · Certificates · Build your website"), "Proof & Progress")
howto("Proof & Progress", [("gps", "Career GPS: three missions every Monday."), ("passport", "Career Passport."), ("progress", "My Progress.")],
      [("Do this week's GPS", "Explore a career, try a task, build something."), ("Log achievements", "Add proof to your Passport."), ("Get them verified", "Your school confirms them."), ("Publish your website", "Share the link only when ready."),
       ("Check My Progress weekly", "Continue where you stopped.")],
      [callout("simple", "GPS = small steps, every week. Passport = proof. Website = your shop window."), callout("good", "Add only what's true and what you can prove. A short, honest profile beats a long one.")], "Proof & Progress")
mission("Proof & Progress",
        [("Go live", "40 min", ["Fill every tab of your website", "Preview it", "Copy your link"]),
         ("Collect proof", "20 min", ["Add 2 achievements to your Passport", "Upload proof for each", "Ask your school to verify"]),
         ("Keep the streak", "4 weeks", ["Do all 3 GPS missions each week", "Tick the grid below", "Check My Progress every Sunday"])],
        table(["Week", "Explore ✓", "Do ✓", "Build ✓", "Points", "What I did"], [[f"Week {i}", "☐", "☐", "☐", "", ""] for i in range(1, 5)], "fill", ["12%", "12%", "12%", "12%", "12%", "40%"])
        + box(h3("My website link", "link") + lines(1), "soft mt"),
        "Your growth is visible, verified and easy to share.", "Proof & Progress")

# ---------------------------------------------------------------- 12 Spotlight (2 pages)
mark("Spotlight")
tool_theme("t-spot", "Spotlight", "#D97706", "#E11D48")
opener(12, "Spotlight", "Career boosters from OneGrasp: present research at an international conference, publish a paper, get an ISBN for your book, start a journal with an ISSN, or be featured in Awardees Magazine.", "feat/spotlight.webp",
       [("5", "boosters"), ("DOI", "for abstracts"), ("Free", "to ask")],
       pills(["Class 11–12 and UG researchers", "Young authors", "Faculty and professionals"]),
       ["A published paper, a DOI or an ISBN is permanent, checkable proof of your work.", "Presenting internationally builds confidence and a network.", "The team guides you through official rules step by step."],
       [("presentation", "Submit an abstract", "To a OneGrasp conference."), ("pen-line", "Writing help", "Question → publication-ready draft."), ("book", "Get an ISBN", "For your own book."),
        ("newspaper", "Start a journal", "What an ISSN needs."), ("star", "Awardees Magazine", "Articles, stories, podcasts."), ("wallet", "Paid, but free to ask", "Fee shared before anything.")],
       ("Menu", "Spotlight"), "Spotlight")
mission("Spotlight",
        [("Pick your booster", "10 min", ["Read all five boosters", "Choose one that fits your goal", "Note it below"]),
         ("Prepare", "1–4 weeks", ["Finish your abstract, article or manuscript", "Use writing help if needed", "Get a mentor's feedback"]),
         ("Submit", "15 min", ["Send the request in Spotlight", "Read the fee and next steps", "Add the result to your Passport"])],
        two(box(h3("My booster plan", "rocket") + p("<b>Booster I chose:</b>", "small") + lines(1) + p("<b>Title of my work:</b>", "small") + lines(1) + p("<b>Mentor / guide:</b>", "small") + lines(1) + p("<b>Target date:</b>", "small") + lines(1)),
            box(h3("Abstract in 5 lines", "file-text") + p("1 · Problem  2 · Why it matters  3 · What I did  4 · What I found  5 · What it means", "small") + lines(5)), gap="4mm"),
        "Your work is ready for an international audience.", "Spotlight")
