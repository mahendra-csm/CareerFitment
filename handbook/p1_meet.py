from lib import *
from v5book import v5page

divider(1, "meet", "Meet OneGrasp", "Who we are, what we do, and why we built a career assessment that looks far beyond marks.",
        ["What is OneGrasp?", "Why career choices go wrong", "The future of work", "Real schools, real students"],
        "brochure/c11-i-001.png")
S = "Meet OneGrasp"

mark("What is OneGrasp?")
add(head("About us", "What is", "OneGrasp?",
         "OneGrasp Education Pvt. Ltd. is an education company based in Hyderabad, India. We help students, families, professionals and institutions make better decisions about learning and work.")
    + two(callout("simple", "OneGrasp is like a <b>GPS for your career</b>. First it finds where you are today (your strengths, interests and personality). Then it shows the roads that suit you, and finally it gives you turn-by-turn directions: subjects, exams, colleges, skills, money and jobs."),
          stats([("6–12", "classes covered", "layers"), ("8", "dimensions", "radar"), ("20+", "dashboard tools", "layout-grid")]), ratio="1.1fr .9fr", gap="5mm")
    + mindmap("OneGrasp", "Education Pvt. Ltd.", [
        ("clipboard-check", "Career Fitment Assessment", "Our best-known product: a psychometric career assessment for Class 6 to Class 12.", "#C72D35"),
        ("layout-dashboard", "Report and dashboard", "Eight dimensions turned into a personal report and a dashboard of more than twenty tools.", "#F09A24"),
        ("globe", "Scientific conferences", "International scientific conferences.", "#2196C8"),
        ("rocket", "Startup programmes", "Startup and entrepreneurship programmes.", "#B5891A"),
        ("award", "Certifications", "Certifications, workshops and internships.", "#279B70"),
        ("messages-square", "Counselling", "One-to-one career counselling.", "#7754B8"),
        ("plane", "Admissions guidance", "Admissions guidance for India and abroad.", "#17243A")], height=92, cw=32, nw=50)
    + two(quote("Every student is good at something. A career assessment should never label a child. It should show where they will thrive, what to try next, and how to get there with honest facts about exams, colleges, costs and jobs.", "Our belief"),
          photo("gallery/new1.webp", "Career guidance in a partner school", style="height:30mm"), ratio="1.25fr .75fr", gap="5mm")
    + h3("What makes OneGrasp different", "sparkles")
    + cards([("flask-conical", "Built on science", "Well-known frameworks: personality type, Holland's RIASEC interests, Gardner's intelligences, emotional intelligence and reasoning aptitude.", "#C72D35"),
             ("users", "Written for each age", "Questions and a report written for each class, from Class 6 to Class 12.", "#2196C8"),
             ("map", "A plan, not just a PDF", "The report opens a dashboard of lessons, tools and weekly tasks, so it never sits in a drawer.", "#7754B8"),
             ("shield-check", "Facts you can check", "Every exam, scholarship and funding programme links to its official source.", "#F09A24")], 4, "compact"),
    section=S)



mark("Why career choices go wrong")
v5page("traps", S)

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
    + two(box(h3("Skills employers want most", "trending-up") + numbered(["Analytical thinking", "Resilience, flexibility and agility", "Leadership and social influence", "Creative thinking", "Motivation and self-awareness", "AI and big data"])
              + p("Source: World Economic Forum, Future of Jobs Report 2025. None of these skills shows on a mark sheet.", "small mt")),
          box(h3("Fading or automating", "trending-down") + bullets(fading, "tight", "minus", "#C72D35"), "soft"), ratio="1.1fr 0.9fr")
    + h3("Rising and future-proof", "rocket")
    + grid([f'<div class="rise"><b>{t}</b><span>{d}</span></div>' for t, d in rising], 5, gap="2.4mm")
    + callout("simple", "Jobs that mix <b>human judgement</b> with <b>technology</b> are the safest. That is why the assessment measures how you think, learn, feel and relate to people, not just what you know.", cls="push"),
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
