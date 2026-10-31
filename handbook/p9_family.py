from lib import *

divider(9, "family", "Parents & Schools", "How families and institutions can support students with care, and what everyone gains.",
        ["For parents: guide, not decide", "Ten questions to talk through", "For schools: the Institution Portal", "What everyone gains", "Questions people often ask"], "home/faq.webp")
S = "Parents & Schools"

mark("For parents: guide, not decide")
add(head("For parents", "Guide,", "not decide.",
         "Your child's report is a map of who they are today. Your role is to help them read it, test it in real life, and make their own choice, with your support.")
    + two(img("home/faq.webp", "pic", style="height:72mm;object-position:center"),
          quote("A child who chooses a path that fits them works harder, stays longer and recovers faster from setbacks than one who was told what to do.")
          + callout("parent", "Your experience is valuable. Use the report as a <b>neutral third voice</b> at the table, so the conversation is about facts, not who wins."), ratio="0.9fr 1.1fr", gap="5mm")
    + two(box(h3("Do", "thumbs-up") + bullets(["Read the report together, slowly, the first time", "Start with strengths. Say them out loud.", "Ask what surprised them, and what felt true",
                                              "Help them try things: a visit, a course, a conversation with someone in the field", "Check facts together: fees, exams, deadlines",
                                              "Use the Decision Room to compare two paths calmly", "Revisit the report every 6–12 months"], "tight", "check", "#16A34A")),
          box(h3("Avoid", "thumbs-down") + bullets(["Choosing for them because of marks, relatives or neighbours", "Treating a lower score as a failure", "Comparing with siblings or friends",
                                                   "Pushing a stream or exam they have no interest in", "Paying anyone who promises a guaranteed admission, job or scholarship", "Ending the talk with “because I said so”"], "tight", "x", "#DC2626"), "soft"), "mt", gap="4mm")
    + h3("What you can see", "eye")
    + cards([("file-text", "The full report", "Your child can share the PDF or open it with you.", "#0284C7"), ("compass", "Weekly progress", "Career GPS shows the week's missions.", "#22C55E"),
             ("heart-handshake", "A parents' page", "Every report ends with “Supporting your child”.", "#DB2777")], 3, "compact push"),
    section=S)

mark("Ten questions to talk through")
qs = ["Which part of the report sounds most like you?", "Which part surprised you, and why?", "What are your top two strengths? Where did you use them recently?",
      "Which of your top fields would you like to try first, and how?", "What would a normal working day look like? (Try the Test-Drive together.)", "Which subjects or exams does that path need? Are you ready to work for them?",
      "What does it cost, and which scholarships could help?", "What's our backup plan if the first choice doesn't work out?", "Who could you talk to who already does this work?", "What's one small thing you'll do this week?"]
add(head("For parents", "Ten questions to", "talk through together.", "Use one or two questions per conversation, over a meal or a walk. Listen more than you speak.")
    + grid([f'<div class="q10"><span>{i + 1:02d}</span><b>{q}</b></div>' for i, q in enumerate(qs)], 2, gap="3mm")
    + two(callout("parent", "For Class 6–8, keep it light: ask what they enjoyed in the test and which careers sounded fun. The goal is curiosity, not a decision."),
          callout("try", "Write your child's answers to questions 4 and 10 on page 2 of this handbook. Read them again in three months."), "mt push", gap="4mm"),
    section=S)

mark("For schools: the Institution Portal")
add(head("For schools and colleges", "See every student.", "Nudge the ones who need it.",
         "The Institution Portal shows a school or college its own students every day: who has taken the assessment, who is active, and who needs a reminder.")
    + two(paper("brochure/c11-i-281.png", "The Institution Portal overview."),
          vsteps([("Daily tracking", "Assessment status, activity and time spent for every student."), ("One-click reminders", "Nudge students who haven't started or have gone quiet."),
                  ("Messages", "Send updates and learning nudges; students can reply."), ("Decision briefs", "Short summaries that support career conversations.")]), ratio="1.1fr 0.9fr", gap="5mm")
    + cards([("sparkles", "Opportunities", "Share useful opportunities with students.", "#0284C7"), ("chart-column", "Insights", "Career journeys, life skills and future skills at a glance.", "#22C55E"),
             ("file-bar-chart" if False else "file-chart-column", "School report", "A whole-school view of results and progress.", "#7C3AED"), ("users", "Parents & mentors", "Coordinate parents, mentors and counselling.", "#F97316"),
             ("eye", "Observations", "Teachers record what they notice.", "#DB2777"), ("badge-check", "Career Passport", "Verify students' achievements with proof.", "#0D9488")], 3, "compact mt")
    + band("Schools only ever see their own students, never a student's individual answers. A trust flag shows if a test looks rushed, so it can be retaken.", "Privacy:", "lock", "mt push"),
    section=S)

mark("What everyone gains")
add(head("Benefits", "What everyone", "gains.", center=True)
    + grid([f'<div class="gain" style="--gc:{c}"><div class="gh">{icon(ic, "9mm", "#fff")}<h4>{t}</h4></div>' + bullets(items, "tight", "check", c) + "</div>" for t, ic, c, items in [
        ("Students", "graduation-cap", "#0284C7", ["Know yourself: type, interests, strengths", "Careers that fit, with real facts", "A plan: subjects, exams, degree, college", "Money: scholarships and funding",
                                                 "Skills school doesn't teach", "Proof: certificates, portfolio, passport", "Confidence to choose, and to change"]),
        ("Parents", "heart-handshake", "#DB2777", ["A calm conversation based on evidence", "Practical questions to support better", "Visibility of weekly progress", "Honest cost checks before big spends",
                                                  "Protection from scams and false promises", "A report to revisit as your child grows"]),
        ("Schools and colleges", "school", "#22C55E", ["A structured guidance programme on campus", "Daily tracking and one-click reminders", "Decision briefs for counsellors", "Life and future skills for every student",
                                                       "Privacy built in", "Better-prepared students for admissions and placements"])]], 3, gap="4mm")
    + h3("Built for the world of work that's coming", "rocket")
    + table(["What employers want (WEF 2025)", "Where OneGrasp builds it"], [
        ["Analytical thinking", "Aptitude practice, mock tests, research projects, Money Labs"], ["Resilience, flexibility, agility", "Career GPS streaks, exam wellbeing, startup missions"],
        ["Leadership and social influence", "Communication Lab, startup pitching, research talks"], ["Creative thinking", "Startup Builder, research questions, portfolio projects"],
        ["Motivation and self-awareness", "Your report, My plan, My Progress"], ["AI and big data", "AI & Certifications: AI Aware to AI Builder"]], "", widths=["40%", "60%"]),
    section=S)

mark("Questions people often ask")
faq = [("How long does the test take?", "Up to 90 minutes. Answers save as you go, and you can stop and resume."), ("Can I fail?", "No. Only the Aptitude section has right answers, and the report is never pass or fail."),
       ("Can I retake it?", "Yes. Many students retake it as they move up a stage (Class 8, then 10, then 12)."), ("Who sees my answers?", "Only you. Schools see progress and activity, never answers."),
       ("Is the report accurate?", "It reflects your honest answers through established frameworks. A trust check flags rushed tests."),
       ("My result doesn't match my dream career.", "A gap is a plan to build, not a no. Use the Career Selector, Test-Drive and My plan."),
       ("Can I use a phone?", "Yes: phone, tablet or laptop. A laptop is easiest for the test."), ("Are the salaries real?", "They're indicative ranges for India, for planning. Actual pay varies."),
       ("Are exams and scholarships current?", "They link to official sources. Always confirm dates and eligibility there."), ("Do the tools cost extra?", "Dashboard tools are included. Spotlight services are paid; asking is free."),
       ("I lost my password.", "Tap “Forgot password” on the sign-in page for a reset link."), ("How do I get help?", "Email support@onegrasp.com or call +91 89777 60442 / 43.")]
gl = [("Aptitude", "How quickly you learn a field's skills."), ("ATS", "Software that screens resumes."), ("Career domain", "A broad family of careers."), ("CPD", "Continuing professional development credit."),
      ("CQ", "Your Communication Score."), ("DOI", "A permanent link to published work."), ("Fit %", "How closely you match what a field rewards."), ("ISBN / ISSN", "Official numbers for a book / journal."),
      ("MBTI-style type", "A four-letter personality type, e.g. ISFJ."), ("RIASEC", "Holland's six interest themes."), ("ROI", "How long a cost takes to pay back."), ("SOP / LOR", "Statement of purpose / letter of recommendation."),
      ("Stream", "MPC, BiPC, MEC, CEC, HEC after Class 10."), ("WEF", "World Economic Forum.")]
add(head("FAQ", "Questions people", "often ask.")
    + grid([f'<div class="faq"><b>{icon("circle-help", "4mm", "var(--c1)")} {q}</b><p>{a}</p></div>' for q, a in faq], 2, gap="2.4mm 4mm")
    + h3("Glossary", "book-a")
    + grid([f'<div class="gl2"><b>{a}</b><span>{b}</span></div>' for a, b in gl], 2, gap="1.4mm 4mm"),
    section=S)

