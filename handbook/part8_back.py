from lib import *

divider(8, "For Parents & Schools", "How families and institutions can support students with care, and what everyone gains.",
        ["For parents: guide, not decide", "Questions to talk through together", "For schools and colleges: the Institution Portal", "What everyone gains", "Questions, answers and a glossary"],
        image="brochure/c11-i-281.png")

S = "For parents"
mark("For parents: guide, not decide")
add(head("For parents", "Guide,", "not decide.",
         "Your child's report is a map of who they are today. Your role is to help them read it, test it in real life and make their own choice, with your support.")
    + two(box(h3("Do") + bullets(["Read the report together, slowly, the first time", "Start with strengths. Say them out loud.", "Ask what surprised them, and what felt true", "Help them try things: a visit, a course, a conversation with someone in the field",
                                  "Check facts together: fees, exams, deadlines", "Use the dashboard's Decision Room to compare two paths calmly", "Revisit the report every 6–12 months"]), "green"),
          box(h3("Avoid") + bullets(["Choosing for them because of marks, relatives or neighbours", "Treating a lower score as a failure", "Comparing with siblings or friends", "Pushing a stream or exam they have no interest in",
                                     "Paying anyone who promises a guaranteed admission, job or scholarship", "Ending the conversation with “because I said so”"], "red"), "red"))
    + h3("What you can see")
    + cards([("The full report", "Your child can share the PDF or open it with you on their dashboard."), ("Weekly progress", "Career GPS shows parents the week's missions and progress."),
             ("A parents' page", "Every report ends with “Supporting your child”: simple ways to help, in plain words.")], 3, "compact")
    + band("Remember", "A child who chooses a path that fits them works harder, stays longer and recovers faster from setbacks than one who was told what to do.", "navy push"),
    section=S)

mark("Questions to talk through together")
add(head("For parents", "Ten questions to", "talk through together.",
         "Use one or two questions per conversation. Listen more than you speak.")
    + '<div class="grid g2">' + "".join(f'<div class="card"><div class="cnum">{i:02d}</div><h4>{q}</h4></div>' for i, q in enumerate([
        "Which part of the report sounds most like you?", "Which part surprised you, and why?", "What are your top two strengths? Where have you used them recently?",
        "Which of your top fields would you like to try first, and how?", "What would a normal working day look like in that career? (Try the Test-Drive.)",
        "Which subjects or exams does that path need? Are you ready to work for them?", "What does it cost, and which scholarships could help?",
        "What is our backup plan if the first choice doesn't work out?", "Who could you talk to who already does this work?", "What is one small thing you'll do this week?"], 1)) + "</div>"
    + note("For younger children (Class 6–8):", "keep it light. Ask what they enjoyed in the test and which careers sounded fun. The goal is curiosity, not a decision.", "push"),
    section=S)

S = "For schools"
mark("For schools and colleges: the Institution Portal")
add(head("For schools and colleges", "See every student.", "Nudge the ones who need it.",
         "The Institution Portal shows a school or college its own students every day: who has taken the assessment, who is active, and who needs a reminder.")
    + two(img("brochure/c11-i-281.png", "pic"),
          cards([("Daily tracking", "Assessment status, activity and time spent for every student."), ("One-click reminders", "Remind students who haven't started or have gone quiet."),
                 ("Messages", "Send updates and learning nudges. Students can reply."), ("Decision briefs", "Short summaries that support career conversations.")], 1, "compact"), ratio="1.2fr 1fr")
    + cards([("Opportunities", "Share useful opportunities with your students."), ("Insights", "Career journeys, life skills and future skills at a glance."),
             ("School report", "A whole-school view of results and progress."), ("Parents, mentors and counselling", "Coordinate parents, mentors and counselling sessions."),
             ("Observations", "Teachers record what they notice, alongside the data."), ("Career Passport", "Verify students' achievements with proof.")], 3, "compact mt")
    + band("Privacy", "Schools only ever see their own students, and never a student's individual answers. A trust flag shows if a test looks rushed, so it can be retaken.", "navy push"),
    section=S)

mark("What everyone gains")
add(head("Benefits", "What everyone", "gains.")
    + '<div class="grid g3">'
    + box(h3("Students") + bullets(["Know yourself: type, interests, strengths", "See careers that fit, with real facts", "A clear plan: subjects, exams, degree, college", "Money: scholarships and funding you qualify for",
                                    "Skills school doesn't teach: money, law, AI, communication", "Proof: certificates, portfolio, verified passport", "Confidence to choose, and to change your mind"], "tight"))
    + box(h3("Parents") + bullets(["A calm, shared conversation, based on evidence", "Practical questions to support better", "Visibility of weekly progress", "Honest cost checks before big spends",
                                   "Protection from scams and false promises", "A report to revisit as your child grows"], "tight"), "tint")
    + box(h3("Schools and colleges") + bullets(["A structured guidance programme on campus", "Daily tracking and one-click reminders", "Decision briefs for counsellors", "Life skills and future skills for every student",
                                                "Privacy built in", "Better-prepared students for admissions and placements"], "tight"))
    + "</div>"
    + h3("Built for the world of work that's coming")
    + table(["What employers want (WEF 2025)", "Where the dashboard builds it"], [
        ["Analytical thinking", "Aptitude practice, mock tests, research projects, Money Labs"], ["Resilience, flexibility and agility", "Career GPS streaks, exam wellbeing, startup missions"],
        ["Leadership and social influence", "Communication Lab, startup pitching, research presentations"], ["Creative thinking", "Startup Builder, research questions, portfolio projects"],
        ["Motivation and self-awareness", "Your report, My plan, My Progress"], ["AI and big data", "AI & Certifications: AI Aware to AI Builder"]], "mt", widths=["40%", "60%"]),
    section="Benefits")

mark("Questions, answers and a glossary")
add(head("FAQ", "Questions people", "often ask.")
    + '<div class="cols2">' + "".join(f'<div class="mb"><h4 style="font:700 9.8pt \'Plus Jakarta Sans\'">{q}</h4><p class="small">{a}</p></div>' for q, a in [
        ("How long does the test take?", "You have up to 90 minutes. Answers save as you go, and you can stop and resume."),
        ("Can I fail?", "No. Only the Aptitude section has right answers, and the report is never pass or fail."),
        ("Can I retake it?", "Yes. Many students retake it as they move up a stage (for example Class 8, then Class 10, then Class 12)."),
        ("Who sees my answers?", "Only you. Schools see progress and activity, never individual answers."),
        ("Is the report accurate?", "It reflects your honest answers through established frameworks. A trust check flags rushed tests."),
        ("My result doesn't match my dream career. Now what?", "A gap is a plan to build, not a no. Use the Career Selector, Test-Drive and My plan."),
        ("Can I use it on a phone?", "Yes: phone, tablet or laptop. A laptop is easiest for the test."),
        ("Are the salaries real?", "They are indicative ranges for India, for planning. Actual pay varies."),
        ("Are the exams and scholarships up to date?", "They link to official sources. Always confirm dates and eligibility there."),
        ("Do the tools cost extra?", "The dashboard tools are included. Spotlight services are paid; asking is free."),
        ("I lost my password.", "Use “Forgot password” on the sign-in page for a reset link."),
        ("How do I get help?", "Email support@onegrasp.com or call +91 89777 60442 / 43.")]) + "</div>"
    + h3("Glossary")
    + '<dl class="gloss cols3">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in [
        ("Aptitude", "How quickly you can learn a field's skills; the only part with right answers."), ("ATS", "Applicant Tracking System: software employers use to screen resumes."),
        ("Career cluster / domain", "A broad family of related careers."), ("CPD", "Continuing Professional Development credit."), ("CQ", "Communication Score in the Communication Lab."),
        ("DOI", "Digital Object Identifier: a permanent link to published work."), ("Fit %", "How closely your profile matches what a field rewards."), ("ISBN / ISSN", "Official numbers for a book / a journal."),
        ("MBTI-style type", "A four-letter personality type, e.g. ISFJ."), ("RIASEC", "Holland's six interest themes."), ("ROI", "Return on investment: how long a cost takes to pay back."),
        ("SOP / LOR", "Statement of purpose / letter of recommendation."), ("Stream", "MPC, BiPC, MEC, CEC, HEC: subject groups after Class 10."), ("WEF", "World Economic Forum.")]) + "</dl>",
    section="FAQ & Glossary")

# ---------------------------------------------------------------- back cover
add(f'''<div class="cover-wrap" style="background:var(--navy);color:#fff">
<div style="position:absolute;left:16mm;top:16mm;background:#fff;border-radius:3mm;padding:2.5mm 4mm">{img("art/logo.png", "", style="height:12mm;display:block")}</div>
<div style="position:absolute;left:16mm;top:60mm;width:175mm"><div class="cv-kick" style="color:#ff8a80">The view from every seat</div>
<div class="cv-title" style="font-size:40pt">Know yourself.<br>Choose with<br>confidence.<br><span style="color:#ff6b61">Build your future.</span></div></div>
<div style="position:absolute;left:16mm;right:16mm;top:160mm">{stats([("3,000+", "students assessed"), ("10+", "schools and colleges"), ("2,500+", "career roadmaps"), ("8", "dimensions measured")], "navy")}</div>
<div style="position:absolute;left:16mm;right:16mm;bottom:28mm;background:#fff;color:var(--ink);border-radius:4mm;padding:7mm;display:grid;grid-template-columns:36mm 1fr;gap:8mm;align-items:center">
{img("art/qr.png", "qr", style="width:36mm;height:36mm")}<div><div class="eyebrow">Take the assessment today</div>
<div style="font:800 20pt 'Plus Jakarta Sans'">careerfitment.onegrasp.com</div>
<p style="margin-top:2mm">support@onegrasp.com  ·  +91 89777 60442 / 43  ·  onegrasp.com/events</p>
<p class="small">OneGrasp Education Pvt. Ltd., Hyderabad, India</p></div></div>
<div style="position:absolute;left:16mm;right:16mm;bottom:10mm;font-size:7pt;color:rgba(255,255,255,.6)">© 2026 OneGrasp. Salaries are indicative ranges for India. Figures marked as indicative are estimates for planning. All logos and trademarks belong to their respective owners.</div></div>''', kind="back")
