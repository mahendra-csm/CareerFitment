from lib import *

S = "The 8 Dimensions"

divider(3, "The 8 Dimensions", "Eight questions about you. Together they show where you will thrive. Plus the eight career-readiness areas of the undergraduate edition.",
        ["The whole you, at a glance", "01 Personality", "02 Career Interests", "03 Multiple Intelligences", "04 Emotional Intelligence", "05 Learning Style", "06 Motivators", "07 Strengths", "08 Aptitude", "Undergraduates: 8 areas of career readiness"],
        image="brochure/c11-i-026.png")

mark("The whole you, at a glance")
add(head("What we measure", "Eight dimensions.", "One complete you.",
         "Each dimension answers one simple question about you. On their own they are interesting; together they point to the careers where you will do well and stay happy.")
    + two(img("brochure/c11-i-026.png", "pic"),
          table(["#", "Dimension", "The question it answers"], [
              ["01", "<b>Personality</b>", "How do I naturally work and decide?"],
              ["02", "<b>Career Interests</b>", "What kind of work excites me?"],
              ["03", "<b>Multiple Intelligences</b>", "In which ways am I smart?"],
              ["04", "<b>Emotional Intelligence</b>", "How well do I handle feelings and people?"],
              ["05", "<b>Learning Style</b>", "How do I prefer to study?"],
              ["06", "<b>Motivators</b>", "What drives me?"],
              ["07", "<b>Strengths</b>", "What do I naturally contribute?"],
              ["08", "<b>Aptitude</b>", "How quickly can I pick up new skills?"]], widths=["9%", "36%", "55%"]), ratio="0.9fr 1.1fr")
    + h3("How the dimensions work together")
    + cards([("Who you are", "Personality and Emotional Intelligence describe how you work, decide and get on with people."),
             ("What pulls you", "Career Interests and Motivators show the work that excites you and the reasons you will keep going."),
             ("How you think and learn", "Multiple Intelligences and Learning Style show the ways you are smart and how you take in new ideas."),
             ("What you can do", "Strengths and Aptitude show what you naturally give and how fast you can pick up a field's skills.")], 4, "compact")
    + note("Class 6–8:", "younger students see the same idea in friendlier words, with Emotional Awareness and Creativity in place of two of the older dimensions (see Part 4).", "blue push"),
    section=S)


def dimension(no, name, q, art, measures, framework, elements, report_shows, sample, ai_list, why, use, good):
    els = "".join(f'<div class="card"><h4>{a}</h4><p>{b}</p></div>' for a, b in elements)
    cols = 2 if len(elements) <= 4 else (3 if len(elements) <= 6 else 4)
    mark(f"{no} {name}")
    add(f'''<div class="dimhead"><div><div class="eyebrow">The 8 Dimensions · {no}</div><div class="dimnum">{no}</div>
<h1 class="title" style="margin:2mm 0 0">{name}</h1><div class="dimq">{q}</div></div>{img(art, "pic")}</div>'''
        + two(box(h3("What it measures") + p(measures)), box(h3("The framework behind it") + p(framework), "tint"))
        + h3("What it looks at") + f'<div class="grid g{cols} compact">{els}</div>'
        + note("Good to know:", good, "push"),
        section=S)
    bars = "".join(f'<div class="barrow"><span>{a}</span><div class="bar"><i style="width:{v}%"></i></div><em>{v}</em></div>' for a, v in sample)
    add(head(f"{name} · in your report", "What your report", "shows you.")
        + two(box(p(report_shows) + h3("Example result") + bars + p("Illustrative only, not a real result.", "small")),
              box(h3("Why it matters") + p(why) + h3("Why it matters in the AI era") + bullets(ai_list), "tint"))
        + h3("How to use it this month")
        + table(["Stage", "Try this"], use, widths=["22%", "78%"])
        + band("Remember", "A dimension describes you today. It is a lens for reflection, not a label, and every part of it can grow with practice.", "push"),
        section=S)


dimension("01", "Personality", "How do I naturally work and decide?", "brochure/c11-i-074.png",
          "Where you get your energy, how you take in information, how you make decisions and how you like to plan. These patterns shape how you prefer to work with others, handle tasks and make choices.",
          "Personality-type preferences in four pairs, widely known as MBTI-style typing. Some stages also look at the five everyday traits psychologists call the Big Five (openness, conscientiousness, extraversion, agreeableness, emotional steadiness).",
          [("Energy: Introvert or Extravert", "Do you recharge alone or with people?"), ("Information: Sensing or Intuition", "Do you trust facts and details, or patterns and possibilities?"),
           ("Decisions: Thinking or Feeling", "Do you decide by logic first, or by values and people first?"), ("Planning: Judging or Perceiving", "Do you like a plan, or prefer to keep options open?")],
          "Your four-letter type (for example ISTP, “The Virtuoso”, or ENFP, “The Campaigner”), how clear each preference is, where you are strong, where you can grow and your next steps.",
          [("Extravert – Introvert", 62), ("Intuition – Sensing", 71), ("Thinking – Feeling", 55), ("Judging – Perceiving", 48)],
          ["Keep learning new skills", "Know how they work best", "Work well with different kinds of people", "Adapt quickly when plans change"],
          "Different work settings suit different patterns. Knowing your personality helps you choose paths where you can contribute in your natural way, enjoy the work more and grow steadily.",
          [["Class 6–8", "Notice when you feel most energetic: in a group, or working alone. Tell a parent."],
           ["Class 9–10", "Read your type's strengths. Pick one club or activity that uses them."],
           ["Class 11–12", "Compare your type with the work style of your top career (Career Library › career page)."],
           ["Undergraduates", "Use your type to explain how you work best in interviews and teams."]],
          "There is no good or bad personality, only better fits. Your type is a preference, and you can act outside it whenever you need to.")

dimension("02", "Career Interests", "What kind of work excites me?", "brochure/c11-i-078.png",
          "Your natural interests and the kinds of work and activities that energise you. Most people are strongest in two or three of six interest types.",
          "Holland's theory of career interests (RIASEC). People and work environments can both be described with the same six themes, so your code points straight at matching careers.",
          [("Realistic (doing)", "Hands-on work with tools, machines, nature."), ("Investigative (thinking)", "Research, analysis, solving puzzles."), ("Artistic (creating)", "Design, writing, music, new ideas."),
           ("Social (helping)", "Teaching, caring, counselling."), ("Enterprising (leading)", "Persuading, selling, starting things."), ("Conventional (organising)", "Data, order, systems and accuracy.")],
          "Your three-letter interest code (for example IAE) and how strongly you lean to each type, with an archetype such as “The Analytical Investigator” or “The Hands-On Builder”.",
          [("Investigative", 82), ("Artistic", 68), ("Enterprising", 57), ("Social", 44), ("Realistic", 38), ("Conventional", 31)],
          ["Choose work they are curious about", "Keep learning as their field changes", "Bring energy and ideas, not only skills", "Stay with hard problems until they are solved"],
          "Interests drive motivation, persistence and satisfaction. When your studies and work match what genuinely holds your attention, you are far more likely to thrive.",
          [["Class 6–8", "Try one activity from each of your top two themes this month."],
           ["Class 9–10", "Match your code to streams: Investigative + Realistic often suit Science; Enterprising + Conventional often suit Commerce."],
           ["Class 11–12", "Test-drive one career from your top theme (Career Library › Test-drive a career)."],
           ["Undergraduates", "Look for an internship that sits in your top theme, not only your degree."]],
          "Interests can change once you try a field for real. That is why the dashboard pushes you to try small tasks, not just read about careers.")

dimension("03", "Multiple Intelligences", "In which ways am I smart?", "brochure/c11-i-083.png",
          "Your natural strengths across eight different ways of thinking, creating and solving problems. It shows how you prefer to learn, express ideas and contribute.",
          "Howard Gardner's theory of multiple intelligences, which recognises that intelligence is not one-size-fits-all.",
          [("Linguistic", "Words, reading, writing."), ("Logical-Mathematical", "Numbers, logic, reasoning."), ("Spatial", "Pictures, shapes, 3D."), ("Bodily-Kinaesthetic", "Learning by doing and moving."),
           ("Musical", "Rhythm, melody, sound."), ("Interpersonal", "Understanding people, teamwork."), ("Intrapersonal", "Self-awareness and reflection."), ("Naturalistic", "Nature, patterns, living things.")],
          "All eight intelligences ranked, with your top two named and explained, plus the kinds of study and work that use them.",
          [("Logical-Mathematical", 78), ("Spatial", 70), ("Intrapersonal", 64), ("Linguistic", 52), ("Interpersonal", 47)],
          ["Learn new tools quickly", "Solve problems creatively", "Think in more than one way", "Explain ideas to different people"],
          "When you understand your mix of intelligences, you can choose learning approaches that suit you, build confidence, and contribute your strengths in real-world ways.",
          [["Class 6–8", "Learn one school topic using your top intelligence (draw it, act it, or explain it)."],
           ["Class 9–10", "Pick an elective or club that uses your top intelligence."],
           ["Class 11–12", "Use your top two to choose between two similar degrees."],
           ["Undergraduates", "Build one portfolio project that shows your strongest intelligence."]],
          "Your lowest score is not a flaw. It is just not how you think first.")

dimension("04", "Emotional Intelligence", "How well do I handle feelings and people?", "brochure/c11-i-087.png",
          "Your ability to understand yourself and others, manage emotions, build positive relationships and respond wisely in different situations.",
          "Widely used emotional-intelligence models that look at four areas shaping how you think, feel and interact every day.",
          [("Self-awareness", "Recognising your emotions, strengths, values and how your actions affect others."), ("Self-management", "Staying calm and focused, and adapting to change."),
           ("Social awareness", "Understanding others' feelings and points of view with empathy."), ("Relationship management", "Building trust, resolving conflict and working well with others.")],
          "Your EQ level, a score for each of the four areas, and the one area to practise first.",
          [("Self-awareness", 72), ("Self-management", 58), ("Social awareness", 66), ("Relationships", 61)],
          ["Stay calm under pressure", "Handle conflict with respect", "Listen before they respond", "Lead and support a team"],
          "Strong emotional intelligence improves communication, builds healthier relationships, helps you work in teams and prepares you to adapt, lead and thrive.",
          [["Class 6–8", "Name one feeling a day. Talk about it at dinner."],
           ["Class 9–10", "Before exams, try the wellbeing tools in Entrance Exams › Wellbeing."],
           ["Class 11–12", "Practise one hard conversation (a disagreement with a friend) calmly."],
           ["Undergraduates", "Ask for feedback after a group project and act on one point."]],
          "Every part of EQ improves with practice and support. Answer honestly to see where you are today and how you can grow.")

dimension("05", "Learning Style", "How do I prefer to study?", "brochure/c11-i-092.png",
          "The ways you naturally like to take in, process and organise information. It shows preferences, not potential, so you can choose methods that help you learn with less effort.",
          "Four common learning preferences. You can be good at all four; this shows which ones you prefer more.",
          [("Seeing (visual)", "Diagrams, charts, images, videos and demonstrations."), ("Hearing (auditory)", "Listening, discussions, explanations and spoken examples."),
           ("Reading / writing", "Reading text, taking notes, summarising and writing things down."), ("Doing (hands-on)", "Trying, practising, experimenting and applying.")],
          "Your preferred and second style, with revision and exam-preparation techniques that suit them.",
          [("Seeing", 74), ("Doing", 66), ("Reading / writing", 49), ("Hearing", 41)],
          ["Adapt when the way of working changes", "Learn new tools and skills quickly", "Know how they learn best", "Keep learning without being told"],
          "When you study in the ways you prefer, revision is easier to start and to keep up. Building flexibility across all four makes you a stronger, more adaptable learner.",
          [["Class 6–8", "Turn one chapter into a picture, a song, a summary or a model, whichever fits you."],
           ["Class 9–10", "Plan board-exam revision with your top style; use the second for variety."],
           ["Class 11–12", "Use the Entrance Exams planner and pick a method per subject."],
           ["Undergraduates", "Choose courses and certifications that match how you learn best."]],
          "A learning style is a preference, not an ability, and never a reason to pick or rule out a career.")

dimension("06", "Motivators", "What drives me?", "brochure/c11-i-096.png",
          "What energises you to put in effort, keep going through challenges and feel satisfied with your work: the reasons that make a task feel meaningful.",
          "Work-values and motivation research. Situations tag your choices with values; your result is your personal ranking, not a fixed label.",
          [("Achievement", "Reaching goals and seeing results."), ("Learning", "Growing and understanding more."), ("Mastery", "Becoming excellent at something."), ("Security", "Stability and a steady future."),
           ("Leadership", "Guiding people and decisions."), ("Social impact", "Helping people and society."), ("Autonomy", "Freedom to work your way."), ("Creativity", "Making new things.")],
          "Your core driver, how your other drivers rank (including recognition, collaboration and financial security), and what kind of role feeds them.",
          [("Learning", 80), ("Achievement", 69), ("Autonomy", 55), ("Social impact", 46), ("Security", 35)],
          ["Start work without being pushed", "Keep going when the work gets hard", "Finish what they begin", "Know what keeps them motivated"],
          "A role that feeds your top driver keeps you engaged for years. A role that ignores it can feel empty even when it pays well.",
          [["Class 6–8", "Notice which reward works for you: praise, learning something new, or helping someone."],
           ["Class 9–10", "Ask of each stream: will it feed my top driver?"],
           ["Class 11–12", "Compare two careers by how well they feed your top two drivers."],
           ["Undergraduates", "When choosing between job offers, rank them against your drivers, not just salary."]],
          "Motivators shift over life. Revisit your report as you grow.")

dimension("07", "Strengths", "What do I naturally contribute?", "brochure/c11-i-101.png",
          "How you naturally add value in a group, across strength domains such as leading, analysing, relating to people, creating, design thinking, strategy and planning ahead.",
          "A strengths model with eight domains. You answer forced-choice situations (pick the option most like you), and there are no wrong answers.",
          [("Problem-solving", "Finding a way through."), ("Communication", "Explaining and persuading."), ("Organisation", "Planning and order."), ("Creativity", "New ideas and design."),
           ("Empathy", "Understanding people."), ("Persistence", "Sticking with it."), ("Leadership", "Taking the lead."), ("Strategy", "Thinking ahead.")],
          "Your two signature strengths, a Strong / Moderate / Developing view of the others, and the fields that reward your signature strengths.",
          [("Problem-solving", 84), ("Creativity", 76), ("Persistence", 60), ("Communication", 52), ("Organisation", 40)],
          ["Know their top strengths and can name them", "Use them to solve real problems", "Work well with people who are different", "Keep building what they do best"],
          "Your strengths are already there. Knowing them helps you choose paths where you contribute in meaningful ways and build confidence by practising what comes naturally.",
          [["Class 6–8", "Ask two people what you are good at. Compare with your report."],
           ["Class 9–10", "Use a signature strength in one school event or project."],
           ["Class 11–12", "Write one paragraph on each signature strength for future SOPs and interviews."],
           ["Undergraduates", "Add proof of each strength to your Career Passport."]],
          "Your last-ranked strength is not a weakness, just not your first instinct.")

dimension("08", "Aptitude", "How quickly can I pick up new skills?", "brochure/c11-i-105.png",
          "Your ability to learn new concepts, solve problems and think logically across different kinds of challenge. It shows how quickly you can pick up the skills a field demands.",
          "Standard reasoning areas used in entrance-style tests. This is the only section with right-or-wrong answers, and each question has one best answer.",
          [("Verbal reasoning", "Words, ideas and meaning."), ("Numerical reasoning", "Numbers and quantities."), ("Abstract reasoning", "Patterns in shapes and relationships."),
           ("Spatial reasoning", "Visualising and turning objects."), ("Logical reasoning", "Rules, sequences and deductions."), ("Data interpretation", "Reading charts and tables.")],
          "Your overall aptitude, how many reasoning questions you got right area by area, your sharpest area and practice tips for exams.",
          [("Numerical", 75), ("Logical", 70), ("Abstract", 62), ("Verbal", 58), ("Spatial", 50)],
          ["Think through unfamiliar problems", "Check whether an answer makes sense", "Pick up technical skills quickly", "Work confidently with numbers and data"],
          "A strong aptitude helps you grasp new ideas faster, adapt to change and tackle complex problems. It also helps with entrance-exam preparation. Analytical thinking is the number one skill employers want (World Economic Forum, 2025).",
          [["Class 6–8", "Do 10 minutes of puzzles three times a week."],
           ["Class 9–10", "Try NMMS or olympiad-style practice in Entrance Exams."],
           ["Class 11–12", "Take a timed mock test and study the analysis of what you got wrong."],
           ["Undergraduates", "Practise placement-style aptitude sets before campus drives."]],
          "Aptitude improves with regular, timed practice. It is not fixed, and the overall assessment is still not a pass-or-fail exam.")

# ---------------------------------------------------------------- undergraduates: 8 areas
mark("Undergraduates: 8 areas of career readiness")
ug = [("01", "Personality & Behaviour", "How you naturally work, decide and react to change.", "Your four-letter type and how clear your preferences are."),
      ("02", "Interests & Motivation", "The work you enjoy, what keeps you going, and the life you want your career to give you.", "Your top interest types and what drives you."),
      ("03", "Cognitive Capability", "Reasoning with numbers, words, logic, patterns, charts and practical problems.", "How many reasoning questions you got right, area by area."),
      ("04", "Academic & Domain Fit", "How well you know your subject, where your degree leads, and whether you enjoy it.", "A score and breakdown for your degree and specialisation.")]
ug2 = [("05", "Human & Professional Skills", "Explaining ideas, handling feedback, teamwork, leading, finishing and bouncing back.", "How you would handle real work situations."),
       ("06", "Digital & Future Skills", "Learning new tools, using AI sensibly, checking data, preparing for future skills.", "Your digital and AI readiness."),
       ("07", "Career & Employability Readiness", "Knowing the role you want, real experience, proof of your skills, showing your value.", "How ready you are for your first job."),
       ("08", "Future Career Adaptability & Fit", "How quickly you learn, handle change, and the career, industry and place that suit you.", "How well you adapt, and your long-term preferences.")]
arts = ["ug-i-026", "ug-i-057", "ug-i-060", "ug-i-063", "ug-i-066", "ug-i-069", "ug-i-072", "ug-i-075"]


def ugpage(items, offset, t1, t2):
    rows = "".join(f'''<div class="card" style="display:grid;grid-template-columns:42mm 1fr;gap:4mm;align-items:center">{img("brochure/" + arts[offset + i] + ".png", "pic")}
<div><div class="cnum">AREA {n}</div><h4>{name}</h4><p><b>Measures:</b> {m}</p><p><b>Your report shows:</b> {r} A score, your strengths, where to grow and next steps.</p></div></div>''' for i, (n, name, m, r) in enumerate(items))
    add(head("Undergraduate edition", t1, t2) + f'<div class="grid g1">{rows}</div>', section="Undergraduate edition")


ugpage(ug, 0, "Eight areas of career readiness:", "who you are and how you think.")
ugpage(ug2, 4, "Eight areas of career readiness:", "how ready you are for work.")
