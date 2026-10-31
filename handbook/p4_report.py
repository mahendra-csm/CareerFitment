import json, os
from lib import *

divider(4, "report", "Your Report at a Glance", "How to read your report, what each part shows, and how to turn it into decisions, for every student from Class 6 to Class 12.",
        ["How to read your report", "Your report, page by page", "Your scorecard and deep dives", "Careers that fit you", "Your dream career vs your result",
         "Choosing your stream", "The 15 career domains", "Your roadmap and next steps", "Meet Ananya: a worked example", "Reality check"],
        "brochure/c11-i-005.png")
S = "Your Report"
DOM = json.load(open(os.path.join(os.path.dirname(__file__), "domains.json")))
Y = '<span class="yes">✓</span>'

mark("How to read your report")
add(head("Reading guide", "How to read your report", "in 20 minutes.",
         "Read it in this order the first time, with a pen in hand. Then do the Reality check at the end of this part.")
    + vsteps([("Start with “At a glance” (2 min)", "The scorecard shows your real result in each dimension. Notice the two or three that stand out."),
              ("Read your personality type and interest code (4 min)", "These two explain most of the rest. Ask yourself: does this sound like me?"),
              ("Look at your best-fit fields (4 min)", "Note the top 3 and their fit %. Read why each was matched."),
              ("Compare with your own choice (3 min)", "“Your choice vs your result” or the Career Selector shows how your dream career fits. A gap is not a no; it's a plan to build."),
              ("Read strengths and growth areas (3 min)", "Pick one strength to use and one area to practise this month."),
              ("Read the roadmap and next steps (4 min)", "Circle the very first step. That's your homework for this week.")])
    + two(box(h3("Scores (0–100)", "gauge") + table(["Score", "Label", "Read it as"], [["75–100", tag("Very High", "#17243A"), "Clear, strong preference or ability"], ["65–74", tag("High", "#17243A"), "A real strength"],
                                                                                    ["50–64", tag("Medium", "#2196C8"), "Balanced either way"], ["35–49", tag("Developing", "#F09A24"), "Not your first instinct yet"], ["0–34", tag("Emerging", "#F09A24"), "Early days; a place to practise"]], "dense")),
          box(h3("Fit % and match labels", "target") + table(["Fit", "Label", "Do this"], [["65%+", tag("Strong match", "#17243A"), "Explore deeply; test-drive"], ["45–64%", tag("Good match", "#2196C8"), "Keep on the list; try a task"],
                                                                                         ["under 45%", tag("Worth exploring", "#F09A24"), "Read about it; stay curious"]], "dense")
              + p("Fit % compares your whole profile with what a field rewards. It is <b>not</b> a probability of success.", "small mt")), "mt", gap="4mm")
    + callout("simple", "In Personality, Learning Style and Motivators a score shows a <b>preference</b>, not quality. Only Aptitude has right answers, and even Aptitude grows with practice.", cls="push"),
    section=S)


mark("Your report, page by page")
pages = [("r11-00", "Cover", "Your name, school, class and date."), ("r11-01", "What's inside", "A map of the report's four sections."), ("r11-02", "Scorecard", "Your real result in each dimension."),
         ("r11-04", "Deep dives", "One page per dimension."), ("r11-11", "Cluster fit", "How you match every career cluster."), ("r11-12", "Path at a glance", "Fitment, Suitability, Selector."),
         ("r11-17", "Future of work", "What's rising and fading."), ("r11-19", "For parents", "How to guide, not decide.")]
add(head("Anatomy", "Your report,", "page by page.", "This is the real report of our sample student, Ananya. Every report, from Class 6 to Class 12, follows the same clear order.")
    + grid([f'<div class="pp"><span class="ppn">{i + 1}</span>{paper("shots/" + f + ".jpg")}<b>{t}</b><span>{x}</span></div>' for i, (f, t, x) in enumerate(pages)], 4, gap="5mm 4mm")
    + callout("simple", "Read it in this order: <b>who you are</b> (scorecard and deep dives), then <b>what fits you</b> (clusters and the three views), then <b>how to get there</b> (roadmap, exams, money), then share the <b>parents' page</b>.", cls="push"),
    section=S)

mark("Your scorecard and deep dives")
_pins = [(1, 7, 36), (2, 29.5, 36), (3, 52, 36), (4, 74.5, 36), (5, 7, 61.5), (6, 29.5, 61.5), (7, 52, 61.5), (8, 74.5, 61.5)]
_key = [("Personality", "your four-letter type (ESTJ in this sample)"), ("Career interest", "your strongest interest theme"), ("Multiple intelligence", "your top way of being smart"),
        ("Emotional intelligence", "your score as a percentage; <b>Strongest</b> marks your top dimension"), ("Learning preferences", "the way you prefer to study"),
        ("Motivators", "your core driver"), ("Strengths", "your signature strength"), ("Aptitude", "your sharpest reasoning area")]
add(head("Who you are", "Your scorecard", "and deep dives.", "The first part of your report shows your real result in each of the 8 dimensions on one page, then explains each one in detail.")
    + '<div class="scrow"><figure class="d4shot" style="margin:0"><div class="d4img" style="--c1:#2196C8">' + img("shots/r910-02.jpg") + "".join(f'<span class="pin" style="left:{x}%;top:{y}%">{n}</span>' for n, x, y in _pins)
    + '</div><figcaption>The scorecard page from a sample Class 9–10 report: one result per dimension, in the order the report explains them.</figcaption></figure>'
    + '<ol class="sckey">' + "".join(f'<li><span>{i + 1}</span><b>{t}</b> {x}</li>' for i, (t, x) in enumerate(_key)) + "</ol></div>"
    + h3("Every deep-dive page has the same five parts", "layers")
    + roadmap([("Score", "0–100, with a typical-student marker"), ("Meaning", "In plain words"), ("Strong", "Where you shine"), ("Grow", "Where to practise"), ("Next steps", "Three actions")], per_row=5)
    + callout("try", "On each deep-dive page, underline one line that sounds exactly like you and circle one thing to practise. Part 3 walks through every deep-dive page, one dimension at a time.", cls="push"),
    section=S)

mark("Careers that fit you")
add(head("Careers that fit you", "Three ways to see", "your future.",
         "Your report compares what fits you, what fits your stream, and the career you dream of, side by side.")
    + two(paper("shots/r11-11.jpg", "Career cluster fit: how closely you match each career cluster."), paper("shots/r11-12.jpg", "Your career path at a glance: the three views."), gap="6mm")
    + grid([f'<div class="view" style="--vc:{c}"><span>{n}</span><b>{t}</b><em>{q}</em><p>{x}</p></div>' for n, t, q, x, c in [
        ("1", "Career Fitment", "What fits YOU", "Your top 5 career areas, ranked purely by your answers. Each shows key roles, skills to build, salary in India (indicative) and entrance exams.", "#17243A"),
        ("2", "Career Suitability", "What fits your STREAM", "Once you have a stream (MPC, BiPC, MEC, CEC, HEC), the careers it already reaches, plus companies that hire and funded routes.", "#2196C8"),
        ("3", "Career Selector", "Your DREAM career", "The career you choose, how well it fits, and the realistic route from where you are today.", "#279B70")]], 3, "mt")
    + callout("simple", "If all three views agree, you have a clear path. If they disagree, that's useful too: it shows exactly what you'd need to build or change to reach your dream.", cls="push"),
    section=S)

mark("Your dream career vs your result")
add(head("Your dream career", "Pick your dream career.", "See how it fits.",
         "Choose the career you want. Your report shows how well it fits you, and lays out the steps from where you are today.")
    + two(img("brochure/c11-i-139.png", "pic"), img("brochure/c11-i-142.png", "pic"), gap="4mm")
    + '<div class="road15">' + "".join(f'<div><span>{i + 1}</span>{t}</div>' for i, t in enumerate(["Subjects to choose", "Entrance exam", "Degree options", "Colleges in India", "Scholarships", "Year-by-year skills", "Internships",
                                                                                                  "First job titles", "PG and study abroad", "Long-term growth"])) + "</div>"
    + callout("warn", "A roadmap is a guide, not a guarantee. Entry routes and requirements change; always confirm with the college, exam body or employer.", cls="push"),
    section=S)

mark("Choosing your stream")
stream = {"A": "MEC, CEC (any)", "B": "MEC, CEC", "C": "MPC", "D": "MPC (MEC for BCA)", "E": "BiPC", "F": "BiPC", "G": "MPC or BiPC", "H": "MPC (arch.), any (design)", "I": "Any; HEC helps",
          "J": "Any; HEC/CEC helps", "K": "Any; HEC/BiPC helps", "L": "Any", "M": "MPC (NDA, pilot)", "N": "BiPC or MPC", "O": "Any"}
exams = {"A": "IPMAT, CUET-UG", "B": "CUET-UG, CA Foundation", "C": "JEE Main/Adv, BITSAT", "D": "JEE Main, BITSAT, CUET", "E": "NEET-UG", "F": "NEET-UG, ICAR, CUET", "G": "CUET-UG, IISER/NEST",
         "H": "NATA, NID, UCEED, NIFT", "I": "CUET-UG", "J": "CLAT, AILET, CUET", "K": "CUET-UG", "L": "NCHM JEE, CUET", "M": "NDA & NA", "N": "CUET-UG, ICAR", "O": "CUET-UG, sports quotas"}
add(head("Choosing your stream", "From your top fields", "to a stream.",
         "Find your top domains from the report in the first column. The next columns show the streams that lead there most directly, and the exams you'll meet.")
    + table(["Career domain", "Most direct stream", "Exams you may meet"], [[f"<b>{d['name']}</b>", stream[d["key"]], exams[d["key"]]] for d in DOM], "dense", widths=["40%", "30%", "30%"])
    + two(callout("simple", "<b>M</b>aths <b>P</b>hysics <b>C</b>hemistry · <b>Bi</b>ology <b>P</b>hysics <b>C</b>hemistry · <b>M</b>aths <b>E</b>conomics <b>C</b>ommerce · <b>C</b>ivics <b>E</b>conomics <b>C</b>ommerce · <b>H</b>istory <b>E</b>conomics <b>C</b>ivics."),
          callout("warn", "This is a starting guide. Many degrees accept any stream and rules change, so confirm eligibility on each exam's official site (linked in Entrance Exams)."), "push", gap="4mm"),
    section=S)

mark("The 15 career domains")
cols = ["#C72D35", "#F09A24", "#2196C8", "#2196C8", "#7754B8", "#279B70", "#279B70", "#F09A24", "#17243A", "#E5B73B", "#7754B8", "#279B70", "#E5B73B", "#2196C8", "#C72D35"]
add(head("Reference", "The 15 career", "domains.", "Your report ranks careers across these 15 broad fields. Each domain card in the report adds what it is, key roles, skills, how to get in, salary in India and abroad, and future scope.")
    + grid([f'<div class="dom" style="--dc:{cols[i]}"><span>{d["key"]}</span><b>{d["name"]}</b><p>{d["tagline"]}</p><em>{", ".join(d["roles"][:3])}</em><i>{d["salary"].split(" · ")[0].replace(" entry", " to start")}</i></div>' for i, d in enumerate(DOM)], 3, gap="2.6mm")
    + p("Salaries are typical starting ranges in India: indicative, not guarantees.", "small push"),
    section=S)

mark("Your roadmap and next steps")
add(head("How to get there", "Your roadmap", "and next steps.", "The last part of your report turns your results into a route: what to do now, in school and after, plus where the world of work is heading.")
    + grid([paper("shots/r910-13.jpg", "Your long-term roadmap, step by step from today."), paper("shots/r11-17.jpg", "What's rising and what's fading (WEF 2025)."), paper("shots/r910-14.jpg", "Learn, find work and get funded.")], 3, "crop3", gap="4mm")
    + h3("Use this part well", "list-checks")
    + roadmap([("Circle the first step", "Find the very first step of your roadmap and circle it."), ("Read one rising field", "Pick one rising field to read about this week."),
               ("Open a free course", "Open one free course from the list."), ("Read it together", "Read the parents' page together.")])
    + callout("try", "Write your first step here and the date you'll do it by: ______________________________  by ____ / ____", cls="push"),
    section=S)

# ---------------------------------------------------------------- Ananya
mark("Meet Ananya: a worked example")
an = [100, 100, 60, 25, 74, 19, 70, 25]
doms = [("Computer Science / IT", 92), ("AI / Data Science", 92), ("Pure Science", 90), ("Research", 89), ("Mathematics / Statistics", 88), ("Biotechnology", 88), ("Engineering", 87), ("Economics", 86)]
add(head("Worked example", "Meet Ananya:", "her best fits and dream career.", "Ananya Rao is a sample Class 11 MPC student we created to show every screen in this handbook. Her answers were generated for demonstration: an ISFJ, Investigative, logical learner who dreams of software engineering.")
    + two(box(h3("Her top career fields", "target") + hbars([(d, v, "#17243A" if i < 2 else "#9AA5B1") for i, (d, v) in enumerate(doms)], maxv=100, unit="%")
              + p("Computer Science / IT and AI / Data Science tie at the top: both reward an investigative, logical, organised profile.", "small mt")),
          box(h3("Her dream career: Software Engineer", "rocket")
              + '<div class="grid" style="grid-template-columns:repeat(4,1fr);gap:2mm">' + ring(92, "Fits her profile", "#17243A", 16) + ring(85, "Fits her stream", "#2196C8", 16) + ring(25, "Aptitude today", "#C72D35", 16) + ring(67, "Overall fitment", "#17243A", 16) + "</div>"
              + callout("simple", "Her dream career <b>matches</b> her best-fit field. Her profile and stream fit strongly; her aptitude score is the gap to work on, and aptitude grows with practice.")), ratio="1fr 1fr", gap="4mm")
    + two(box(h3("Strengths to use", "trophy") + bullets(["Clear personality (100/100)", "Clear career interest (100/100)", "Learning style (74/100)"], "tight"), "soft"),
          box(h3("Areas to grow", "sprout") + bullets(["Motivator clarity (19/100)", "Aptitude and reasoning (25/100)", "Emotional intelligence (25/100)"], "tight", "arrow-up-right", "#C72D35"), "soft"), gap="4mm")
    + h3("What Ananya could do next", "footprints")
    + steps([("Week 1", "Read 5 careers in Computer Science in the Career Library.", "book-open"), ("Week 2", "Test-drive software engineering.", "play"),
             ("Week 3", "Make a JEE Main study plan; take one mock.", "clipboard-list"), ("Week 4", "Start a free coding programme in Internships.", "laptop")], cols=4),
    section=S)

mark("Reality check: how well do you know yourself?")
rc = ["Personality type", "Interest code", "Top intelligence", "Learning style", "Core motivator", "Signature strength", "Emotional intelligence", "Sharpest aptitude", "Top career field", "Dream-career fit"]
add(f'''<div class="actban b3"><div class="actno">ACTIVITY 3 · AFTER YOUR REPORT</div><h1>Reality <span>check.</span></h1>
<p>Remember Activity 1? Open your sealed prediction (page {{{{REF:Activity 1: Predict yourself}}}}) and your report side by side. Score one point for every match. Who knows you best, you or your parent?</p>{img("brochure/c11-i-005.png", "actart")}</div>'''
    + table(["What", "My guess", "Parent's guess", "My report says", "Me ✓", "Parent ✓"], [[f"<b>{r}</b>", "", "", "", "☐", "☐"] for r in rc] + [["<b>TOTAL</b>", "", "", "", "<b>/10</b>", "<b>/10</b>"]], "fill", ["22%", "17%", "17%", "22%", "11%", "11%"])
    + grid([f'<div class="band2" style="--b:{c}"><b>{s}</b><span>{t}</span><p>{x}</p></div>' for s, t, x, c in [
        ("8–10", "You know yourself well", "Great. Now act on it: start the 30-day challenge in Part 10.", "#17243A"),
        ("5–7", "Some surprises", "Read the deep dives for the dimensions you missed. Surprises are where you learn the most.", "#C72D35"),
        ("0–4", "Big discovery", "That's exactly why the assessment exists. Talk it through with a parent or counsellor.", "#279B70")]], 3, "mt", gap="3mm")
    + two(box(h3("My biggest surprise", "sparkles") + lines(2)), box(h3("What I'll do about it", "flag") + lines(2)), "mt push", gap="4mm"),
    section=S)
