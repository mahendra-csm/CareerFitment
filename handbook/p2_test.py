from lib import *

divider(2, "test", "The Assessment", "What the Career Fitment Assessment is, who it is for, the science behind it, and exactly how to take it, screen by screen.",
        ["What is a psychometric assessment?", "What we measure: the 8 dimensions", "The science behind every question", "Before you begin",
         "Registering, step by step", "Inside the exam screen", "Six kinds of questions", "Built to be trusted", "After you finish"],
        "feat/exams.webp")
S = "The Assessment"

mark("What is a psychometric assessment?")
add(head("The test", "Is it just", "another exam?",
         "No. A psychometric career assessment is a structured set of questions that looks beyond marks to understand how you think, what interests you, and where your natural strengths lie.")
    + callout("simple", "<b>Psycho</b> means mind and <b>metric</b> means measure. A psychometric assessment measures parts of your mind that an exam does not: your preferences, interests, feelings and ways of thinking. Think of it as a <b>mirror</b>, not a <b>marksheet</b>.")
    + h3("How it works", "route")
    + roadmap([("You answer", "Short, everyday questions: what would you do in this situation, what do you enjoy, how do you like to learn.", "#2196C8"),
               ("We read your answers", "Through well-established psychology frameworks, and turn them into a picture of you.", "#7754B8"),
               ("We match", "That picture is matched against hundreds of careers.", "#F09A24"),
               ("Your report explains", "Which fields fit you best, and why.", "#279B70")])
    + h3("Mirror, not marksheet", "scan-face")
    + compare("A school exam", ["Tests what you studied", "Right or wrong answers", "Gives a mark", "You can fail", "Same for everyone", "Ends with a result"],
              "This assessment", ["Explores who you are", "Mostly no right answers", "Gives a profile", "You can't fail", "Written for your age", "Starts a plan"])
    + two(callout("example", "Two students both score 90% in Class 10. One loves taking machines apart and solving puzzles alone; the other loves debating and organising school events. Same marks, very different best-fit careers. Marks could not tell them apart. The assessment can."),
          callout("good", "Only the <b>Aptitude</b> section has right answers, like a reasoning test. Everything else is about you, so the only wrong answer is a dishonest one."), "mt", gap="4mm")
    + h3("What you get back", "gift")
    + cards([("radar", "Your profile", "Your results across 8 dimensions on one page."), ("target", "Best-fit careers", "Top career areas, each with a fit %."),
             ("route", "A roadmap", "Subjects, exams, degrees, skills and jobs, step by step."), ("layout-dashboard", "A dashboard", "20+ tools to act on it, all year.")], 4, "compact"),
    section=S)

NAMES = ["Personality", "Career\nInterests", "Multiple\nIntelligences", "Emotional\nIntelligence", "Learning\nStyle", "Motivators", "Strengths", "Aptitude"]
QS = ["How do I naturally work and decide?", "What kind of work excites me?", "In which ways am I smart?", "How well do I handle feelings and people?",
      "How do I prefer to study?", "What drives me?", "What do I naturally contribute?", "How quickly can I pick up new skills?"]
mark("What we measure: the 8 dimensions")
add(head("What we measure", "The 8 dimensions.", "One complete you.", center=True)
    + f'<div class="center" style="margin:-1mm 0 2mm">{wheel(NAMES, DIMC, size=118)}</div>'
    + grid([f'<div class="dq" style="--dc:{DIMC[i]}"><b>{i + 1:02d}</b><span>{NAMES[i].replace(chr(10), " ")}</span><p>{QS[i]}</p></div>' for i in range(8)], 4, gap="2.4mm")
    + h3("How the eight work together", "puzzle")
    + cards([("user", "Who you are", "Personality and Emotional Intelligence describe how you work, decide and get on with people.", DIMC[0]),
             ("heart", "What pulls you", "Career Interests and Motivators show the work that excites you and why you keep going.", DIMC[1]),
             ("brain", "How you think", "Multiple Intelligences and Learning Style show the ways you are smart and how you learn.", DIMC[2]),
             ("trophy", "What you can do", "Strengths and Aptitude show what you naturally give and how fast you learn a field's skills.", DIMC[6])], 4, "compact")
    + callout("simple", "No single dimension decides your career. The best-fit careers are where <b>several dimensions agree</b>: for example, an Investigative interest + a Logical intelligence + a strong Numerical aptitude all point toward science and data.", cls="push"),
    section=S)



mark("The science behind every question")
fw = [("01", "Personality", "Personality-type preferences (MBTI-style): introvert–extravert, sensing–intuition, thinking–feeling, judging–perceiving.", "Carl Jung's types; Myers & Briggs"),
      ("02", "Career Interests", "Holland's RIASEC model: Realistic, Investigative, Artistic, Social, Enterprising, Conventional.", "John L. Holland, 1959"),
      ("03", "Multiple Intelligences", "Eight ways of being smart: linguistic, logical, spatial, bodily, musical, interpersonal, intrapersonal, naturalistic.", "Howard Gardner, 1983"),
      ("04", "Emotional Intelligence", "Self-awareness, self-management, social awareness and relationship management.", "Salovey & Mayer; Goleman"),
      ("05", "Learning Style", "Preferences for seeing, hearing, reading/writing and doing.", "VARK-style preference models"),
      ("06", "Motivators", "Work values: achievement, learning, mastery, security, leadership, social impact, autonomy, creativity.", "Work-values research"),
      ("07", "Strengths", "Eight strength domains, using forced-choice situations.", "Strengths-based psychology"),
      ("08", "Aptitude", "Verbal, numerical, abstract, spatial and logical reasoning, plus data.", "Standard reasoning tests")]
add(head("The science", "Built on frameworks", "psychologists trust.",
         "Every dimension is read through a model that has been studied and used for decades. Here is what sits behind each part of your report.")
    + "".join(f'<div class="fw" style="--fc:{DIMC[i]}"><span class="fwn">{n}</span><div><b>{t}</b><p>{d}</p></div><span class="fwo">{icon("book-marked", "3.6mm", DIMC[i])} {o}</span></div>' for i, (n, t, d, o) in enumerate(fw))
    + callout("simple", "A <b>framework</b> is a well-tested way of describing people. It means the same answers always give the same result, and every result can be explained in plain words. Each dimension has its own page in Part 3.", cls="push"),
    section=S)

mark("Before you begin")
add(head("Prepare", "Before you", "begin.",
         "No studying is needed. A calm hour and an honest mind are all it takes. Use this page the day before.")
    + two(box(h3("Your checklist", "list-checks") + check_list([
        "A laptop (easiest), tablet or phone, charged", "A stable internet connection", "Up to 90 minutes in a quiet place, in one sitting",
        "Your login email and password, or your school's link", "Class 11–12: your stream and the career you're aiming for",
        "Headphones, if you want questions read aloud", "Water, and notifications switched off"])),
          box(f'<div class="bigtip">{icon("heart", "10mm", "var(--c1)")}<span class="serif">Answer as you <b class="c1">really are</b>, not as you think you <b>should</b> be.</span></div>'
              + p("There are no good or bad results, only better fits. If you answer the way a parent, teacher or friend would like, the report will describe them, not you.")
              + p("If two options both feel true, pick the one that is true <b>more often</b>.", "small"), "soft"))
    + h3("Good habits during the test", "sparkles")
    + cards([("zap", "Trust your first reaction", "Your first honest answer is usually the most accurate. Don't overthink.", "#2196C8"),
             ("skip-forward", "Skip, then return", "Not sure? Tap Next and come back using the navigator.", "#17243A"),
             ("brain", "Focus on aptitude", "It's the only part with right answers. Read each question fully.", "#279B70"),
             ("save", "Take a break if needed", "Tap Save Progress. You'll resume with the same questions and time.", "#17243A")], 4, "compact")
    + two(callout("parent", "Please let your child answer alone. Sitting beside them changes their answers. You'll read the report together afterwards (Part 8)."),
          callout("teacher", "Run the test in a calm lab session. Remind students there are no marks and no ranking: that single sentence improves honesty."), "push", gap="4mm"),
    section=S)

mark("Registering, step by step")
add(head("Getting in", "Registering,", "step by step.",
         "Registration takes about two minutes. Students can sign up themselves, or join through their school or college link so the institution can follow their progress.")
    + two(laptop("shots/probe.jpg", "<b>Step 1.</b> Enter your name and pick your class or stage."), laptop("shots/flow-0.jpg", "<b>Step 4.</b> Class 11–12: your stream and dream career."), gap="6mm")
    + steps([("Set your milestone", "Go to careerfitment.onegrasp.com, enter your name and pick your class: 6, 7, 8, 9–10, 11, 12.", "flag"),
             ("Set your stage", "Say how sure you are today: no idea · confused · a bit sure · sure but need a plan.", "gauge"),
             ("Create your login", "Your email and password are your login for your report and dashboard.", "key-round"),
             ("Quick questions", "Class 11–12 students pick their stream and dream career. These tailor your report.", "message-circle-question"),
             ("Start", "Read “Before you begin”, tick the box and start. The test opens in full screen.", "play")], cols=5)
    + two(laptop("shots/pick.jpg", "Start typing a career and pick it from the list."), laptop("shots/flow-1.jpg", "<b>Step 5.</b> Read the instructions, then start."), "mt", gap="6mm"),
    section=S)

mark("Inside the exam screen")
pins = [(1, 37, 4.5), (2, 48, 4.5), (3, 57, 4.5), (4, 64, 4.5), (5, 87, 4.5), (6, 30, 10.5), (7, 25, 28), (8, 62.5, 28), (9, 33, 50), (10, 86, 40), (11, 62, 70.5)]
labs = [("Time left", "A 90-minute timer; it auto-submits at zero."), ("Question", "Which question you're on, out of the total."), ("Answered", "How many you've done."), ("Marked", "Questions you flagged to review."),
        ("Save / Exit", "Save and come back later with the same questions and time."), ("Section bar", "Jump between dimensions; a tick means done."), ("The question", "One question at a time, in plain words."),
        ("Read aloud", "Hear the question read out."), ("Options", "Tap one; it saves instantly."), ("Navigator", "Green answered · blue current · amber review · grey pending."), ("Finish", "Opens when every question is answered.")]
add(head("The exam screen", "Everything on", "one screen.",
         "The exam shows one question at a time. Everything you need stays in view. Match the numbers on the screen to the list below.")
    + laptop("shots/flow-3.jpg", pins=pins)
    + grid([f'<div class="lab"><span>{i + 1}</span><div><b>{t}</b><p>{x}</p></div></div>' for i, (t, x) in enumerate(labs)], 3, "mt", gap="2.4mm 4mm")
    + callout("simple", "You cannot get lost: the navigator on the right always shows which questions are still grey. Tap a grey tile, answer it, and the <b>Finish & see report</b> button turns green.", cls="push"),
    section=S)

mark("Six kinds of questions")
mk = {
    "Situation · most like me": ('<div class="mock"><div class="mq">You get a difficult problem with no standard method. What do you do first?</div><div class="mo"><i></i>Think independently</div><div class="mo on"><i></i>Find similar examples</div><div class="mo"><i></i>Discuss with others</div></div>', "Pick the one that sounds most like you, not what you'd ideally do."),
    "Scale · 1 to 10": ('<div class="mock"><div class="mq">How comfortable are you making a big decision on your own?</div><div class="scale">' + "".join(f'<span class="{"on" if i == 7 else ""}">{i}</span>' for i in range(1, 11)) + '</div></div>', "Use the whole scale. 5 is not a “safe” answer."),
    "Pick up to three": ('<div class="mock"><div class="mq">Which areas are you considering?</div><div class="chips"><span>Engineering ×</span><span>Computer Science ×</span><span>Design ×</span></div><div class="dd"><span>Add another…</span><span>▾</span></div></div>', "Search the list; tap × to remove a pick."),
    "Dropdown": ('<div class="mock"><div class="mq">Which subject do you enjoy the most?</div><div class="dd"><span>Physics</span><span>▾</span></div></div>', "Choose honestly. It shapes your subject advice."),
    "Aptitude · one best answer": ('<div class="mock"><div class="mq">2, 6, 12, 20, 30, ?</div><div class="mo"><i></i>40</div><div class="mo on"><i></i>42</div><div class="mo"><i></i>44</div></div>', "Read fully; skip and come back if stuck. (Answer: 42, the gaps grow by 2.)"),
    "Yes / No": ('<div class="mock"><div class="mq">Have you done an internship or project in your field?</div><div class="mo on"><i></i>Yes</div><div class="mo"><i></i>No</div></div>', "Answer for today, not for next year."),
}
add(head("Question types", "Six kinds of", "questions.",
         "Most questions take a few seconds. Here is what each type looks like on screen, and how to answer it well.")
    + grid([f'<div class="qt"><div class="qth">{chip(["mouse-pointer-click", "sliders-horizontal", "list-plus", "chevrons-up-down", "brain", "toggle-left"][i], size="8mm", isz="4.4mm")}<b>{k}</b></div>{m}<p class="small">{icon("lightbulb", "3.4mm", "#F09A24")} {tip}</p></div>' for i, (k, (m, tip)) in enumerate(mk.items())], 3, gap="4mm")
    + two(laptop("shots/flow-2.jpg", "A personality question: tap the option most like you."), laptop("shots/exam-mid.jpg", "Class 11–12: answers save as soon as you tap."), "mt", gap="6mm"),
    section=S)

mark("Built to be trusted")
add(head("Trust", "Built to", "be trusted.",
         "A report is only useful if it really describes the student. Three safeguards protect every result.")
    + cards([("activity", "Answer-quality check", "When you submit, the test looks at how the paper was answered: how many answers came in under 3 seconds, and whether the same option was picked again and again. It never changes your scores. It only flags a report that may not reflect you (high, medium or low trust), so a rushed test can be retaken.", "#2196C8"),
             ("lock", "Your answers stay private", "Your report belongs to you. If you joined through a school, the school sees your progress and activity, never your individual answers.", "#17243A"),
             ("badge-check", "Facts linked to sources", "Exams, scholarships, funded routes and funding programmes link to their official websites, so anyone can check them.", "#17243A")], 3)
    + h3("What a rushed test looks like", "triangle-alert")
    + two(callout("example", "To show you the quality check, we raced through a sample test in about <b>9 minutes</b>, tapping answers in under 3 seconds. The system noticed straight away and marked the report <b>low trust</b>, with the exact reasons below.")
          + table(["Check", "Our rushed sample", "A thoughtful test"], [["Time taken", "9 min", "40–80 min"], ["Answers under 3 seconds", "79%", "Under 15%"], ["Same answer repeated", "74%", "Under 30%"], ["Longest identical run", "42 in a row", "3–4"], ["Trust", tag("LOW", "#C72D35"), tag("HIGH", "#17243A")]], "dense", widths=["40%", "30%", "30%"]),
          '<div class="grid" style="grid-template-columns:1fr 1fr;gap:3mm">' + gauge(79, "answers under 3 seconds", "#C72D35", 36) + gauge(74, "same answer as the one before", "#F09A24", 36) + "</div>"
          + callout("simple", "Rushing doesn't save time. It just gives you a report about nobody. Slow down, read, and answer as yourself.")),
    section=S)

mark("After you finish")
add(head("Submitted", "What happens", "after you finish.",
         "Tap “Finish & see report” when every question is answered. Your personalised report is generated instantly.")
    + laptop("shots/flow-6.jpg", "The confirmation screen: your answers are recorded and your report is being generated.", cls="lim")
    + steps([("Report saved", "It stays on your dashboard permanently. Reopen it any time.", "save"), ("Copy by email", "A confirmation email explains how to sign back in.", "mail"),
             ("Dashboard unlocks", "Your results pages and every tool appear in the menu.", "layout-dashboard"), ("Read it together", "Download the PDF and read it with someone who guides you.", "users")], "mt")
    + two(box(h3("Your first 48 hours", "timer") + check_list(["Open your full report and read the first three pages", "Write your type and interest code on page 2 of this book",
        "Download the PDF and share it with a parent or mentor", "Open “My plan” in the dashboard and tick one task", "Explore 3 careers in your top field in the Career Library"]), "soft"),
          callout("try", "Within 48 hours, sit with a parent, teacher or counsellor for 20 minutes and read the report using the guide on page {{REF:How to read your report}}. Fresh results make the best conversations.")
          + callout("good", "Didn't get the email? Check your spam folder. Your report is always on your dashboard, so nothing is ever lost."), "push"),
    section=S)
