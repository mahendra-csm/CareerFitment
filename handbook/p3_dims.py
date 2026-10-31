from lib import *

divider(3, "dims", "The 8 Dimensions", "Eight simple questions about you. Together they show where you will thrive. Plus the eight career-readiness areas of the undergraduate edition.",
        ["The whole you, at a glance", "01 Personality", "02 Career Interests", "03 Multiple Intelligences", "04 Emotional Intelligence", "05 Learning Style", "06 Motivators",
         "07 Strengths", "08 Aptitude", "Undergraduates: 8 areas of career readiness"], "ug/cognitive-capability.webp")
S = "The 8 Dimensions"
NAMES = ["Personality", "Career\nInterests", "Multiple\nIntelligences", "Emotional\nIntelligence", "Learning\nStyle", "Motivators", "Strengths", "Aptitude"]
QS = ["How do I naturally work and decide?", "What kind of work excites me?", "In which ways am I smart?", "How well do I handle feelings and people?",
      "How do I prefer to study?", "What drives me?", "What do I naturally contribute?", "How quickly can I pick up new skills?"]

mark("The whole you, at a glance")
add(head("What makes you, you?", "Eight dimensions.", "One complete you.", center=True)
    + f'<div class="center" style="margin:-1mm 0 2mm">{wheel(NAMES, DIMC, size=118)}</div>'
    + grid([f'<div class="dq" style="--dc:{DIMC[i]}"><b>{i + 1:02d}</b><span>{NAMES[i].replace(chr(10), " ")}</span><p>{QS[i]}</p></div>' for i in range(8)], 4, gap="2.4mm")
    + h3("How the eight work together", "puzzle")
    + cards([("user", "Who you are", "Personality and Emotional Intelligence describe how you work, decide and get on with people.", DIMC[0]),
             ("heart", "What pulls you", "Career Interests and Motivators show the work that excites you and why you keep going.", DIMC[1]),
             ("brain", "How you think", "Multiple Intelligences and Learning Style show the ways you are smart and how you learn.", DIMC[2]),
             ("trophy", "What you can do", "Strengths and Aptitude show what you naturally give and how fast you learn a field's skills.", DIMC[6])], 4, "compact")
    + callout("simple", "No single dimension decides your career. The best-fit careers are where <b>several dimensions agree</b>: for example, an Investigative interest + a Logical intelligence + a strong Numerical aptitude all point toward science and data.", cls="push"),
    section=S)


def dim(i, art, simple, measures, framework, elems, example, chart, chart_note, why, ai, careers, tries, good):
    c = DIMC[i]
    nm = NAMES[i].replace("\n", " ")
    mark(f"{i + 1:02d} {nm}")
    eg = "".join(f'<div class="el" style="--dc:{c}">{chip(ic, c, f"color-mix(in srgb, {c} 12%, white)", "9mm", "4.6mm")}<div><b>{t}</b><span>{x}</span></div></div>' for ic, t, x in elems)
    v = f'--dc:{c};--c1:{c};--c2:{c};--soft:color-mix(in srgb, {c} 9%, white);--deep:color-mix(in srgb, {c} 70%, #1E2340)'
    add(f'<div class="dwrap" style="{v}"><div class="dimtop sm"><div><span class="dimbadge">Dimension {i + 1:02d} of 08</span><div class="dimnum">{i + 1:02d}</div>'
        f'<h1 class="title" style="font-size:27pt">{nm}</h1><div class="dimq">“{QS[i]}”</div></div>{img(art, "dimart")}</div>'
        + callout("simple", simple)
        + two(box(h3("What it measures", "ruler") + p(measures, "small") + h3("The framework", "book-open") + p(framework, "small")),
              box(h3("How it looks in your report", "chart-column") + chart + p(chart_note + " <i>Illustrative.</i>", "small mt")), ratio="1fr 1fr", gap="4mm")
        + f'<div class="els c4">{eg}</div>'
        + h3("Careers that often suit each pattern", "briefcase")
        + table(["If you lean towards…", "You may enjoy careers such as…"], careers, "dense", widths=["30%", "70%"])
        + two(grid([f'<div class="tryc" style="--dc:{c}"><b>{s_}</b><span>{t}</span></div>' for s_, t in tries], 2, gap="2mm"),
              box(h3("Fill in from your report", "pen-line") + '<div class="myr"><span>My score</span><i></i><span>My top result</span><i></i><span>One way I\'ll use it</span><i></i></div>', "soft"), "mt push", ratio="1.2fr 0.8fr", gap="4mm")
        + "</div>",
        section=S)


def sliders(rows):
    out = []
    for l, r, v in rows:
        out.append(f'<div class="sl2"><span>{l}</span><div class="slt"><i style="left:{v}%"></i></div><span>{r}</span></div>')
    return '<div class="sls">' + "".join(out) + "</div>"


dim(0, "ug/personality-behaviour.webp",
    "Your personality is your <b>natural style</b>, like being left- or right-handed. You can use both hands, but one feels easier. This dimension finds the style that feels easiest for you, so you can choose work where you don't have to fight yourself every day.",
    "Where you get your energy, how you take in information, how you make decisions and how you like to plan. These patterns shape how you prefer to work with others, handle tasks and make choices.",
    "Personality-type preferences in four pairs, widely known as MBTI-style typing (from Carl Jung's work, developed by Myers and Briggs). Some stages also look at the five everyday traits psychologists call the Big Five.",
    [("battery-charging", "Energy: Introvert or Extravert", "Do you recharge alone or with people?"), ("eye", "Information: Sensing or Intuition", "Facts and details, or patterns and possibilities?"),
     ("scale", "Decisions: Thinking or Feeling", "Logic first, or values and people first?"), ("calendar-check", "Planning: Judging or Perceiving", "A clear plan, or keep options open?")],
    "Before a school trip, <b>Ravi</b> makes a checklist a week early (Judging); <b>Meera</b> packs the night before and enjoys deciding on the spot (Perceiving). Neither is wrong. But Ravi may enjoy project management, and Meera may thrive in fast-changing roles like journalism or event work.",
    sliders([("Introvert", "Extravert", 28), ("Sensing", "Intuition", 64), ("Thinking", "Feeling", 72), ("Judging", "Perceiving", 30)])
    + '<div class="typecard"><b>ISFJ</b><span>“The Defender” · quiet, practical, caring, organised</span></div>',
    "Each slider shows which side you lean to and how clearly. Your four letters together make your type, for example ISFJ.",
    "Different work settings suit different patterns. Knowing your personality helps you pick paths where you contribute in your natural way, enjoy the work and grow steadily.",
    ["Know how they work best", "Work well with different kinds of people", "Adapt quickly when plans change", "Keep learning new skills"],
    [["Introversion + Sensing", "Accountant, lab scientist, software developer, archivist"], ["Extraversion + Feeling", "Teacher, counsellor, HR, sales, hospitality"],
     ["Intuition + Thinking", "Engineer, scientist, strategist, architect, entrepreneur"], ["Sensing + Judging", "Doctor, civil services, operations, banking, law"]],
    [("Class 6–8", "Notice when you feel most energetic: in a group or alone."), ("Class 9–10", "Pick one club that uses your type's strengths."),
     ("Class 11–12", "Compare your type with your top career's daily work."), ("Undergraduates", "Use your type to explain how you work in interviews.")],
    "There is no good or bad personality, only better fits. Your type is a preference; you can act outside it whenever you need to.")

dim(1, "ug/interests-motivation.webp",
    "Interests are the <b>activities that pull you in</b>, the things you'd happily do even without marks. When your work matches your interests, effort feels lighter and you keep going longer.",
    "Your natural interests and the kinds of work and activities that energise you. Most people are strongest in two or three of six interest themes.",
    "John L. Holland's theory of career interests (RIASEC), used by career counsellors worldwide since 1959. People and work environments are described with the same six themes, so your code points straight to matching careers.",
    [("wrench", "Realistic · doing", "Tools, machines, nature, building things."), ("microscope", "Investigative · thinking", "Research, analysis, solving puzzles."), ("palette", "Artistic · creating", "Design, writing, music, new ideas."),
     ("hand-heart", "Social · helping", "Teaching, caring, counselling."), ("megaphone", "Enterprising · leading", "Persuading, selling, starting things."), ("table", "Conventional · organising", "Data, order, systems and accuracy.")],
    "<b>Arjun</b> loves fixing his bicycle and building science-fair models (Realistic + Investigative). His friend <b>Sana</b> loves organising the school fest and convincing sponsors (Enterprising + Social). Their codes, RIE and ESA, point to very different but equally good careers.",
    f'<div class="center">{hexagon(["Realistic", "Investigative", "Artistic", "Social", "Enterprising", "Conventional"], [38, 86, 66, 44, 57, 31], DIMC[1], 62)}</div><div class="typecard" style="--dc:{DIMC[1]}"><b>IAE</b><span>“The Analytical Investigator” · curious, creative, driven</span></div>',
    "The further a corner reaches out, the stronger that interest. Your top three letters make your interest code.",
    "Interests drive motivation, persistence and satisfaction. When your studies and work match what genuinely holds your attention, you are far more likely to thrive.",
    ["Choose work they are curious about", "Keep learning as their field changes", "Bring energy and ideas, not only skills", "Stay with hard problems until solved"],
    [["Realistic", "Mechanical engineer, pilot, chef, agriculture, architecture"], ["Investigative", "Doctor, data scientist, researcher, software engineer"], ["Artistic", "Designer, architect, writer, filmmaker, UX"],
     ["Social", "Teacher, nurse, psychologist, social worker"], ["Enterprising", "Entrepreneur, lawyer, marketing, management"], ["Conventional", "Chartered accountant, banker, analyst, administrator"]],
    [("Class 6–8", "Try one activity from each of your top two themes."), ("Class 9–10", "Match your code to streams (Part 4)."),
     ("Class 11–12", "Test-drive one career from your top theme."), ("Undergraduates", "Pick an internship in your top theme.")],
    "Interests can change once you try a field for real. That's why the dashboard pushes you to try small tasks, not just read about careers.")

dim(2, "ug/cognitive-capability.webp",
    "Being “smart” isn't just about maths marks. A dancer, a debater and a gardener are all smart, in different ways. This dimension finds <b>your</b> kinds of smart.",
    "Your natural strengths across eight different ways of thinking, creating and solving problems. It shows how you prefer to learn, express ideas and contribute.",
    "Howard Gardner's theory of multiple intelligences (1983), which recognises that intelligence is not one-size-fits-all.",
    [("book-open", "Linguistic", "Words, reading, writing."), ("sigma", "Logical-Mathematical", "Numbers, logic, reasoning."), ("box", "Spatial", "Pictures, shapes, 3D."), ("activity", "Bodily-Kinaesthetic", "Learning by doing and moving."),
     ("music", "Musical", "Rhythm, melody, sound."), ("users", "Interpersonal", "Understanding people."), ("brain", "Intrapersonal", "Self-awareness, reflection."), ("leaf", "Naturalistic", "Nature, patterns, living things.")],
    "<b>Kavya</b> struggles with long essays but can picture a 3D model in her head and sketch it perfectly (Spatial). That is a real intelligence, and architects, product designers and surgeons rely on it every day.",
    hbars([("Logical-Mathematical", 78, DIMC[2]), ("Spatial", 70, DIMC[2]), ("Intrapersonal", 64, DIMC[2]), ("Linguistic", 52, DIMC[2]), ("Interpersonal", 47, DIMC[2]),
           ("Musical", 41, DIMC[2]), ("Naturalistic", 38, DIMC[2]), ("Bodily-Kinaesthetic", 33, DIMC[2])]),
    "All eight are ranked; your top two are named and explained.",
    "When you understand your mix of intelligences, you can choose learning methods that suit you, build confidence and contribute your strengths in real-world ways.",
    ["Learn new tools quickly", "Solve problems creatively", "Think in more than one way", "Explain ideas to different people"],
    [["Linguistic", "Lawyer, journalist, author, teacher"], ["Logical-Mathematical", "Engineer, data analyst, economist, programmer"], ["Spatial", "Architect, designer, surgeon, pilot"],
     ["Interpersonal", "Manager, counsellor, sales, HR"], ["Naturalistic", "Environmental scientist, agronomist, vet"]],
    [("Class 6–8", "Learn one topic using your top intelligence."), ("Class 9–10", "Pick an elective that uses it."),
     ("Class 11–12", "Use your top two to choose between two degrees."), ("Undergraduates", "Build a portfolio project that shows it.")],
    "Your lowest score isn't a flaw. It's just not how you think first.")

dim(3, "ug/human-professional-skills.webp",
    "Emotional intelligence (EQ) is how well you <b>understand and manage feelings</b>, your own and other people's. Many studies find EQ matters as much as IQ for success at work.",
    "Your ability to understand yourself and others, manage emotions, build positive relationships and respond wisely in different situations.",
    "Widely used emotional-intelligence models (Salovey and Mayer; popularised by Daniel Goleman) that look at four everyday areas.",
    [("scan-eye", "Self-awareness", "Recognising your emotions, strengths and values."), ("anchor", "Self-management", "Staying calm, focused and adaptable."),
     ("eye", "Social awareness", "Understanding others' feelings with empathy."), ("handshake", "Relationship management", "Building trust and resolving conflict.")],
    "In a group project, <b>Nikhil</b> notices a teammate has gone quiet, checks in with her privately, and adjusts the plan. That's social awareness plus relationship management, and every good team leader does it.",
    '<div class="eqgrid">' + "".join(f'<div style="--q:{c}"><b>{v}</b><span>{t}</span></div>' for t, v, c in [("Self-awareness", 72, "#D6336C"), ("Self-management", 58, "#E8590C"), ("Social awareness", 66, "#7048E8"), ("Relationships", 61, "#1C7ED6")]) + "</div>",
    "Four areas, each scored out of 100. Your report names the area to practise first.",
    "Strong emotional intelligence improves communication, builds healthier relationships, helps you work in teams and prepares you to lead and adapt.",
    ["Stay calm under pressure", "Handle conflict with respect", "Listen before they respond", "Lead and support a team"],
    [["High social awareness", "Doctor, nurse, teacher, counsellor, HR"], ["High self-management", "Pilot, surgeon, defence, finance, law"], ["High relationship skills", "Manager, sales, politics, entrepreneur"]],
    [("Class 6–8", "Name one feeling a day at dinner."), ("Class 9–10", "Try Entrance Exams › Wellbeing before exams."),
     ("Class 11–12", "Practise one calm hard conversation."), ("Undergraduates", "Ask for feedback and act on one point.")],
    "Every part of EQ improves with practice. Answer honestly to see where you are today and how you can grow.")

dim(4, "ug/academic-domain-fit.webp",
    "Some people remember what they <b>see</b>, some what they <b>hear</b>, some what they <b>write</b>, and some what they <b>do</b>. Knowing your style makes studying easier, not harder.",
    "The ways you naturally like to take in, process and organise information. It shows preferences, not potential, so you can choose methods that help you learn with less effort.",
    "Four common learning preferences (similar to the VARK model). You can be good at all four; this shows which ones you prefer.",
    [("eye", "Seeing (visual)", "Diagrams, charts, videos, demonstrations."), ("ear", "Hearing (auditory)", "Listening, discussing, explaining aloud."),
     ("pen-line", "Reading / writing", "Notes, summaries, lists, re-writing."), ("hand", "Doing (hands-on)", "Trying, practising, experimenting.")],
    "<b>Priya</b> read her biology chapter three times and still forgot it. Then she drew the digestive system as a coloured flowchart and remembered it in one go. She's a visual learner, and now she revises with diagrams.",
    f'<div class="two mid" style="display:grid;grid-template-columns:1fr 1fr;gap:3mm"><div class="center">{donut([("Seeing", 38, "#1C7ED6"), ("Doing", 30, "#2F9E44"), ("Reading", 19, "#F08C00"), ("Hearing", 13, "#D6336C")], 40, 0.55, ("Seeing", "top style"))}</div>{legend([("Seeing", "38%", "#1C7ED6"), ("Doing", "30%", "#2F9E44"), ("Reading / writing", "19%", "#F08C00"), ("Hearing", "13%", "#D6336C")])}</div>',
    "Your report names your top and second style, with revision tips for each.",
    "When you study in the ways you prefer, revision is easier to start and keep up. Building flexibility across all four makes you a stronger, more adaptable learner.",
    ["Adapt when the way of working changes", "Learn new tools quickly", "Know how they learn best", "Keep learning without being told"],
    [["Seeing", "Revise with mind maps, colour-coding, diagrams, videos"], ["Hearing", "Explain topics aloud, study groups, recorded notes"], ["Reading / writing", "Summaries, flashcards, rewriting notes"],
     ["Doing", "Practice problems, models, experiments, teaching others"]],
    [("Class 6–8", "Turn one chapter into a picture or model."), ("Class 9–10", "Plan board revision with your top style."),
     ("Class 11–12", "Use the exam planner, one method per subject."), ("Undergraduates", "Pick courses that match how you learn.")],
    "A learning style is a preference, not an ability, and never a reason to pick or rule out a career.")

dim(5, "ug/career-readiness.webp",
    "Motivators are your <b>reasons</b>: what makes effort feel worth it. Two people can do the same job for different reasons. One wants security, another wants to make a difference. Knowing yours keeps you going on hard days.",
    "What energises you to put in effort, keep going through challenges and feel satisfied with your work: the reasons that make a task meaningful.",
    "Work-values and motivation research. Situations tag your choices with values such as achievement, learning, social impact, recognition, autonomy, mastery, financial security, creativity, collaboration, security and leadership.",
    [("trophy", "Achievement", "Reaching goals and seeing results."), ("graduation-cap", "Learning", "Growing and understanding more."), ("crown", "Leadership", "Guiding people and decisions."), ("shield", "Security", "Stability and a steady future."),
     ("globe", "Social impact", "Helping people and society."), ("feather", "Autonomy", "Freedom to work your way."), ("lightbulb", "Creativity", "Making new things."), ("star", "Recognition", "Being valued and seen.")],
    "<b>Two cousins</b> both become engineers. One loves the steady salary and clear career ladder at a big company (Security). The other quits after two years to build a startup (Autonomy + Achievement). Same degree, different motivators, different happy endings.",
    hbars([("Learning", 80, DIMC[5]), ("Achievement", 69, DIMC[5]), ("Autonomy", 55, DIMC[5]), ("Social impact", 46, DIMC[5]), ("Creativity", 40, DIMC[5]), ("Security", 35, DIMC[5])]),
    "Your motivators ranked; the top one is your core driver.",
    "A role that feeds your top driver keeps you engaged for years. A role that ignores it can feel empty, even when it pays well.",
    ["Start work without being pushed", "Keep going when the work gets hard", "Finish what they begin", "Know what keeps them motivated"],
    [["Security", "Government services, banking, PSU engineering, teaching"], ["Achievement / Recognition", "Sales, consulting, sports, law, medicine"], ["Social impact", "Healthcare, NGOs, education, public policy"],
     ["Autonomy / Creativity", "Startups, design, freelancing, research, media"]],
    [("Class 6–8", "Notice which reward works for you."), ("Class 9–10", "Ask of each stream: will it feed my top driver?"),
     ("Class 11–12", "Compare two careers against your top two drivers."), ("Undergraduates", "Rank job offers by drivers, not just salary.")],
    "Motivators shift as you grow. Revisit your report every year or two.")

dim(6, "ug/future-adaptability.webp",
    "Strengths are what you <b>reach for first</b>, the role you naturally take in a group. Some people organise, some invent, some keep everyone together. The world needs all of them.",
    "How you naturally contribute in a group, across strength domains such as leading, analysing, relating to people, creating, design thinking, strategy and planning ahead.",
    "A strengths model with eight domains. You answer forced-choice situations (you pick the option most like you), and there are no wrong answers.",
    [("puzzle", "Problem-solving", "Finding a way through."), ("message-square", "Communication", "Explaining and persuading."), ("list-checks", "Organisation", "Planning and order."), ("sparkles", "Creativity", "New ideas and design."),
     ("heart", "Empathy", "Understanding people."), ("mountain", "Persistence", "Sticking with it."), ("flag", "Leadership", "Taking the lead."), ("compass", "Strategy", "Thinking ahead.")],
    "In the school science exhibition, <b>Aditi</b> designed the model (Creativity), <b>Rahul</b> made the timetable (Organisation) and <b>Faiz</b> presented it to the judges (Communication). They won because each used their strength.",
    '<div class="strg">' + "".join(f'<div class="sg {k}"><b>{t}</b><span>{lab}</span></div>' for t, lab, k in [("Problem-solving", "Strong", "s"), ("Creativity", "Strong", "s"), ("Persistence", "Moderate", "m"),
                                                                                                             ("Communication", "Moderate", "m"), ("Organisation", "Developing", "d"), ("Empathy", "Developing", "d")]) + "</div>",
    "Strong = natural strength · Moderate = situational strength · Developing = area to build.",
    "Your strengths are already there. Seeing them helps you choose paths where you contribute meaningfully, and build confidence by practising what comes naturally.",
    ["Know their top strengths and can name them", "Use them to solve real problems", "Work well with people who are different", "Keep building what they do best"],
    [["Problem-solving / Strategy", "Engineer, consultant, analyst, scientist"], ["Creativity", "Designer, architect, marketer, entrepreneur"], ["Empathy / Communication", "Doctor, teacher, counsellor, journalist"],
     ["Organisation / Persistence", "Operations, civil services, project manager, CA"]],
    [("Class 6–8", "Ask two people what you're good at."), ("Class 9–10", "Use a signature strength in one event."),
     ("Class 11–12", "Write a paragraph on each signature strength."), ("Undergraduates", "Add proof of each strength to your Passport.")],
    "Your last-ranked strength isn't a weakness, just not your first instinct.")

dim(7, "ug/digital-future-skills.webp",
    "Aptitude is how <b>quickly you can learn</b> the thinking a field needs. It's the only section with right answers, like a puzzle round. And unlike height, it grows with regular practice.",
    "Your ability to learn new concepts, solve problems and think logically across different kinds of challenge. It shows how quickly you can pick up the skills a field demands.",
    "Standard reasoning areas used in entrance-style and placement tests. Each question has one best answer.",
    [("book-a", "Verbal reasoning", "Words, ideas and meaning."), ("calculator", "Numerical reasoning", "Numbers and quantities."), ("shapes", "Abstract reasoning", "Patterns in shapes."),
     ("rotate-3d", "Spatial reasoning", "Turning objects in your mind."), ("git-branch", "Logical reasoning", "Rules and deductions."), ("chart-line", "Data interpretation", "Reading charts and tables.")],
    "Try one: <b>2, 6, 12, 20, 30, ?</b> The gaps are 4, 6, 8, 10, so the next gap is 12 and the answer is <b>42</b>. Questions like this test numerical and logical reasoning, the core of JEE, CAT and placement tests.",
    hbars([("Numerical (3 of 4)", 75, DIMC[7]), ("Logical (2 of 3)", 67, DIMC[7]), ("Abstract (2 of 3)", 67, DIMC[7]), ("Verbal (1 of 2)", 50, DIMC[7]), ("Spatial (1 of 2)", 50, DIMC[7])]),
    "Each area shows how many you got right; your sharpest area is named, with exam-practice tips.",
    "A strong aptitude helps you grasp new ideas faster and tackle complex problems. Analytical thinking is the number one skill employers want (World Economic Forum, 2025).",
    ["Think through unfamiliar problems", "Check whether an answer makes sense", "Pick up technical skills quickly", "Work confidently with numbers and data"],
    [["Numerical + Logical", "Engineering, finance, data science, actuarial"], ["Verbal", "Law, civil services, journalism, management"], ["Spatial", "Architecture, design, aviation, surgery"],
     ["Abstract", "Programming, research, mathematics, AI"]],
    [("Class 6–8", "10 minutes of puzzles, three times a week."), ("Class 9–10", "Try NMMS or olympiad practice."),
     ("Class 11–12", "Take a timed mock and study the analysis."), ("Undergraduates", "Practise placement aptitude sets.")],
    "Aptitude improves with regular, timed practice. It is not fixed, and the overall assessment is still not a pass-or-fail exam.")

# ---------------------------------------------------------------- undergraduates: 8 areas
mark("Undergraduates: 8 areas of career readiness")
ug = [("01", "Personality & Behaviour", "How you naturally work, decide and react to change.", "Your four-letter type and how clear your preferences are.", "ug-i-026"),
      ("02", "Interests & Motivation", "The work you enjoy, what keeps you going, the life you want.", "Your top interest types and what drives you.", "ug-i-057"),
      ("03", "Cognitive Capability", "Reasoning with numbers, words, logic, patterns, charts.", "How many reasoning questions you got right, area by area.", "ug-i-060"),
      ("04", "Academic & Domain Fit", "How well you know your subject and where your degree leads.", "A score and breakdown for your degree and specialisation.", "ug-i-063"),
      ("05", "Human & Professional Skills", "Explaining ideas, feedback, teamwork, leading, bouncing back.", "How you'd handle real work situations.", "ug-i-066"),
      ("06", "Digital & Future Skills", "Learning new tools, using AI sensibly, checking data.", "Your digital and AI readiness.", "ug-i-069"),
      ("07", "Career & Employability Readiness", "Knowing the role you want, experience, proof of skills.", "How ready you are for your first job.", "ug-i-072"),
      ("08", "Future Career Adaptability & Fit", "How fast you learn, handle change; the career and place that suit you.", "How well you adapt, and your long-term preferences.", "ug-i-075")]
rows = "".join(f'''<div class="ugc" style="--dc:{DIMC[i]}">{img("brochure/" + a + ".png", "uga")}<div><span class="dimbadge">Area {n}</span><h4>{t}</h4><p>{m}</p><p class="small"><b>Report shows:</b> {r}</p></div></div>''' for i, (n, t, m, r, a) in enumerate(ug))
add(head("Undergraduate edition", "Eight areas of", "career readiness.", "Undergraduates don't need to discover themselves from scratch; they need to know how ready they are for the job market. Areas 1–4 describe you and your subject; areas 5–8 describe how ready you are for work.")
    + f'<div class="ugg">{rows}</div>'
    + callout("simple", "Each area gets a score, your strengths, where to grow and next steps. The report adds a skill gap and a 20-year career horizon (Part 4).", cls="push"),
    section="Undergraduate edition")
