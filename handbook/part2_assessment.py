from lib import *

S = "The Assessment"

divider(2, "The Assessment", "What the Career Fitment Assessment is, who it is for, the science behind it, and exactly how to take it.",
        ["What is a psychometric career assessment?", "Who is it for: four editions", "The science behind the test", "Before you begin", "Registering, step by step", "Inside the exam screen", "Question types", "Built to be trusted", "After you finish"],
        image="shots/flow-4.jpg")

mark("What is a psychometric career assessment?")
add(head("The test", "Is it just", "another test?",
         "No. A psychometric career assessment is a structured tool that looks beyond marks to understand how you think, what interests you, and where your natural strengths lie.")
    + two(p("The OneGrasp Career Fitment Assessment is built on well-established psychology frameworks. It asks short, everyday questions (what would you do, what do you enjoy, how do you prefer to learn) and reads your answers through those frameworks.")
          + p("The result is not a single “right career”. It is a clear picture of you, the career fields where that picture fits best, and a plan to explore them in real life.")
          + h3("What it is not")
          + bullets(["Not an exam you can fail. Only the Aptitude section has right answers.", "Not a label. Results describe preferences today, and people grow.", "Not a replacement for a conversation. It is the best starting point for one."], "red"),
          box(h3("What you get back") + bullets([
              "Your profile across 8 dimensions, on one page",
              "Your top career areas, each with a fit %",
              "Where you are strong and where to grow",
              "A long-term roadmap: subjects, exams, degrees, skills, jobs",
              "Scholarships, funded routes and resources",
              "A page for parents: how to guide, not decide",
              "A dashboard of 20+ tools to act on it"]), "tint"))
    + table(["Myth", "Fact"], [
        ["Only toppers need it.", "It helps every student. Knowing your strengths matters most when you are unsure."],
        ["It tells you one fixed career.", "It shows best-fit fields and a plan to test them."],
        ["It's an exam you can fail.", "There are no good or bad results, only better fits."],
        ["Marks are enough.", "Marks show performance. This shows fit."]], "mt", widths=["35%", "65%"]),
    section=S)

mark("Who is it for: four editions")
add(head("Who it is for", "One assessment,", "four editions.",
         "Each class group takes a test written for its own age and its own decisions. The questions, the report and the advice all change with the stage.")
    + table(["Edition", "For", "The big question", "Questions*", "Report focus"], [
        ["<b>Career Discovery</b>", "Class 6, 7 and 8", "What am I like, and what could I enjoy?", "about 60", "Career DNA, best-fit domains, a 20-year picture, habits to build"],
        ["<b>Stream Selection</b>", "Class 9 and 10", "Which stream after Class 10?", "about 60", "Best-fit domains, stream guidance, your choice vs your result"],
        ["<b>Career Planning</b>", "Class 11 and 12", "Which exam, degree and college?", "75", "Fitment, Suitability and Career Selector; a 15-step roadmap"],
        ["<b>Employability Readiness</b>", "Undergraduates", "What job, what skills, PG or work?", "100", "17 career clusters, skill gap, 2026–2046 career horizon"],
    ], widths=["19%", "15%", "23%", "11%", "32%"])
    + p("* Question counts can change slightly as the question banks are updated. Every edition has up to 90 minutes.", "small")
    + h3("And for the adults around the student")
    + cards([("For students", "Understand yourself and see clear next steps you can take with confidence."),
             ("For parents", "Have a shared, calm conversation with practical questions that help you support better."),
             ("For schools and colleges", "Track every student, send reminders and messages, and support guidance with care and privacy.")], 3)
    + band("Working professionals", "Professionals take a separate stress and wellbeing check in the dashboard rather than the student assessment.", "push"),
    section=S)

mark("The science behind the test")
add(head("The science", "Built on frameworks", "psychologists trust.",
         "Each dimension is read through a well-established model. Here is what sits behind every part of your report.")
    + table(["Dimension", "Framework behind it", "How questions look"], [
        ["Personality", "Personality-type preferences (introvert–extravert, sensing–intuition, thinking–feeling, judging–perceiving), widely known as MBTI-style typing; the Big Five traits for some stages", "Situations: pick the option most like you"],
        ["Career Interests", "Holland's RIASEC model: Realistic, Investigative, Artistic, Social, Enterprising, Conventional", "Pick the activity that appeals most"],
        ["Multiple Intelligences", "Howard Gardner's theory of multiple intelligences (8 kinds)", "Pick the role you'd enjoy most"],
        ["Emotional Intelligence", "Self-awareness, self-management, social awareness, relationship management", "Pick what you'd genuinely do"],
        ["Learning Style", "Visual, auditory, reading/writing and hands-on preferences", "Pick how you naturally learn"],
        ["Motivators", "Work-values and motivation research: security, mastery, achievement, leadership, learning and more", "Pick what feels MOST like you"],
        ["Strengths", "A strengths model with eight domains, using forced-choice situations", "Pick the option most like you"],
        ["Aptitude", "Standard reasoning areas used in entrance-style tests: verbal, numerical, abstract, spatial, data", "One best answer, like a real test"],
        ["Class 11–12 extras", "Subject fit, career and stream fit, career aspiration", "Your stream, subjects and goals"],
        ["Undergraduate areas", "Eight career-readiness pillars (see Part 3)", "Work situations and skill checks"],
    ], widths=["19%", "52%", "29%"])
    + note("Why it matters:", "a framework turns your answers into something meaningful and comparable. The same answers always give the same result, and every result is explained in plain words in your report.", "blue push"),
    section=S)

mark("Before you begin")
add(head("Prepare", "Before you", "begin.",
         "No studying is needed. A calm 90 minutes and an honest mind are all it takes. Use this checklist the day before.")
    + two(box(h3("Your checklist") + "".join(f'<div class="check"><i></i><span>{t}</span></div>' for t in [
        "A phone, tablet or laptop with a stable internet connection (a laptop is easiest)",
        "Up to 90 minutes in a quiet place, ideally in one sitting",
        "Your login email and password (or your school's link)",
        "For Class 11–12: your current stream and the career you are aiming for",
        "For undergraduates: your degree, specialisation and year",
        "Headphones if you want questions read aloud",
        "Water, and phone notifications switched off"])),
          box(h3("One tip before you start") + p('<span class="quote" style="font-size:12pt">Answer as you really are, not as you think you should be.</span>')
              + p("There are no good or bad results, only better fits. If you answer the way a parent, teacher or friend would like you to, the report will describe them, not you.")
              + p("If two options both feel true, pick the one that is true <b>more often</b>.", "small"), "tint"))
    + h3("Good habits during the test")
    + cards([("Don't overthink", "Your first honest reaction is usually the most accurate."),
             ("Use Next to skip", "Not sure? Move on and come back using the navigator."),
             ("Take the aptitude part seriously", "It is the only section with right answers. Read each question fully."),
             ("Save progress", "Need a break? Tap Save Progress. You resume with the same questions and time.")], 4, "compact")
    + note("For parents:", "please let your child answer alone. You will see the report together afterwards, and Part 8 of this book explains how to talk about it.", "push"),
    section=S)

mark("Registering, step by step")
add(head("Getting in", "Registering,", "step by step.",
         "Registration takes about two minutes. Students can sign up themselves, or join through their school or college link so the institution can follow their progress.")
    + two(shot("shots/probe.jpg", "Step 1. Set your milestone: enter your name and pick your class or stage."),
          shot("shots/flow-0.jpg", "Step 4. Class 11–12: your stream and dream career (undergraduates give their degree)."))
    + steps([("Set your milestone", "Go to careerfitment.onegrasp.com, enter your name and pick Class 6, 7, 8, 9–10, 11, 12, Undergraduates or Working Professionals."),
             ("Set your current stage", "Say how sure you are today: no idea, confused among options, a bit sure but exploring, or sure but needing an execution plan."),
             ("Create your login", "Your email and password are your login. You will use them to open your report and dashboard any time. Existing users tap “Existing user login”."),
             ("Answer a couple of quick questions", "Class 11–12 students pick their stream (MPC, BiPC, PCMB, MEC, CEC, Humanities, Vocational) and search for their dream career; undergraduates pick their degree, specialisation and year. These do not score you; they shape Career Suitability and Career Selector."),
             ("Read the instructions and start", "The test opens in full screen for focus. You can exit any time.")], "mt"),
    section=S)

mark("Inside the exam screen")
add(head("The exam screen", "Everything on", "one screen.",
         "The exam shows one question at a time. Everything you need (time, progress, sections and a navigator) stays in view.")
    + shot("shots/flow-4.jpg")
    + '<div class="grid g3 mt">' + "".join(f'<div class="card"><div class="cnum">{n}</div><h4>{t}</h4><p>{x}</p></div>' for n, t, x in [
        ("TOP BAR", "Time left, question, answered, marked", "A 90-minute timer counts down and auto-submits at zero. Counters show your progress."),
        ("SECTION BAR", "Jump between dimensions", "Personality, Interests, Aptitude and the rest. A tick appears when a section is complete."),
        ("NAVIGATOR", "Every question as a tile", "Green = answered, blue = current, amber = marked for review, grey = pending. Tap any tile to jump."),
        ("READ ALOUD", "Speaker button", "Hear the question read out. Useful for younger students and different learners."),
        ("MARK", "Bookmark for review", "Unsure? Mark the question and come back before you finish."),
        ("SAVE / EXIT", "Save progress any time", "Close and sign back in later; you resume with the same questions and time.")]) + '</div>',
    section=S)

mark("Question types")
add(head("Question types", "Six kinds of", "questions.",
         "Most questions take a few seconds. Here is what each type looks like and how to answer it.")
    + two(shot("shots/flow-2.jpg", "A situation question: tap the option most like you."),
          shot("shots/exam-mid.jpg", "Questions save as soon as you answer; use Next to move on."))
    + table(["Type", "What you do", "Tip"], [
        ["Situation (most like me)", "Pick the one option that sounds most like you", "Think of what you usually do, not what you'd ideally do"],
        ["Scale (1 to 10)", "Tap a number from “not at all” to “very”", "Use the whole scale; 5 is not a safe answer"],
        ["Pick up to three", "Choose up to 3 options (careers or fields)", "Search the list; remove a pick with ×"],
        ["Dropdown", "Pick your favourite or hardest subject", "Choose honestly; this shapes your subject advice"],
        ["Aptitude (one best answer)", "Reasoning with words, numbers, logic, shapes, data", "Read fully; skip and return if stuck"],
        ["Yes / No", "Simple facts about you", "Answer for today, not for next year"]], "mt", widths=["24%", "40%", "36%"]),
    section=S)

mark("Built to be trusted")
add(head("Trust", "Built to", "be trusted.",
         "A report is only useful if it reflects the student. Three safeguards protect every result.")
    + cards([("01", "Answer-quality check", "When you submit, the test looks at how the paper was answered: how many answers came in under 3 seconds, and whether the same option was chosen again and again. It never changes your scores. It only flags a report that may not reflect you (high, medium or low trust), so a rushed test can be retaken."),
             ("02", "Your answers stay private", "Your report belongs to you. If you joined through a school or college, the institution sees your progress and activity, never your individual answers."),
             ("03", "Facts linked to sources", "Entrance exams, scholarships, funded routes and funding programmes link to their official websites, so anyone can check them.")], 3)
    + h3("How your data is used")
    + two(bullets(["Your answers are used to build your report and dashboard.", "Your results are saved to your account so you can reopen the report any time.", "A PDF copy is emailed to your registered address.", "Tools that store documents (such as the scholarship and study abroad vaults) keep them for your applications only."]),
          bullets(["Recordings in the research practice recorder stay on your device.", "The Law & Rights section has a quick-exit button and private browsing for shared devices.", "AI tools in the dashboard are rated for age and privacy before you see them.", "You decide what goes on your public portfolio page."]))
    + band("Our honesty note", "Your results come from your own answers, read through established psychometric frameworks. Nothing in the report is a limit on what you can become.", "navy push"),
    section=S)

mark("After you finish")
add(head("Submitted", "What happens", "after you finish.",
         "Tap “Finish & see report” when every question is answered. Your report is generated instantly.")
    + shot("shots/flow-6.jpg", "The confirmation screen: your answers are recorded and your personalised report is being generated.")
    + steps([("Your report is saved to your dashboard", "It stays there permanently. Open it any time from “Open my full report” on the dashboard home."),
             ("A copy arrives by email", "A confirmation email explains how to sign back in whenever you want to reread your report."),
             ("Your dashboard unlocks", "Your results (profile, 8 dimensions, best-fit fields, how you think, my plan) and every tool appear in the menu."),
             ("Share it with someone who guides you", "Download the PDF and read it with a parent, teacher or counsellor. Part 4 of this book shows you how.")], "mt"),
    section=S)
