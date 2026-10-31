from lib import *

divider(7, "research", "Research & Conferences", "From a student's first research question to an international stage: OneGrasp's peer-reviewed conferences and the scientific committee behind them.",
        ["International scientific conferences", "The researcher journey", "The OneGrasp Scientific Committee", "Keynotes, awards and the conference day"], "feat/research.webp")
S = "Research & Conferences"

mark("International scientific conferences")
disc = [("Business & Economics", "FinTech, digital payments", "briefcase"), ("Engineering & Technology", "Green energy, sustainable manufacturing", "cog"), ("Sports & Physical Education", "Performance, exercise physiology", "dumbbell"),
        ("Agriculture & Food Sciences", "Precision farming, crop biotech", "wheat"), ("Interdisciplinary & Emerging", "Quantum, nanotechnology, materials", "atom"), ("Social Sciences & Humanities", "Psychology, behaviour, mental health", "users"),
        ("Education", "EdTech, curriculum, hybrid learning", "graduation-cap"), ("Physical & Life Sciences", "Climate, conservation, marine biology", "leaf"), ("Health & Medical Sciences", "AI in medicine, imaging", "stethoscope"),
        ("Mathematics & Data Science", "Deep learning, statistics, big data", "sigma"), ("Arts, Culture & Communication", "Digital media, heritage, film", "palette")]


def kv_html(items):
    return '<dl class="kv">' + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in items) + "</dl>"


add(head("Conferences", "Where global research", "gets presented.",
         "Present. Publish. Get recognised. Two-evening online conferences across 11 disciplines, with a DOI for every accepted abstract, CPD-accredited certificates and a 50-member international scientific committee.")
    + stats([("500+", "conferences held online", "presentation"), ("70+", "countries", "globe"), ("10,000+", "researchers reached", "users"), ("190M+", "Crossref metadata records", "database"), ("10+", "indexing directories", "list")], "grad")
    + h3("11 disciplines, one global calendar", "calendar")
    + grid([f'<div class="disc">{chip(ic, size="9mm", isz="4.6mm")}<div><b>{t}</b><span>{x}</span></div></div>' for t, x, ic in disc], 3, gap="2.4mm")
    + two(box(h3("The OneGrasp conference model", "badge-check") + kv_html([("Format", "Live online, two evenings"), ("Review", "Committee peer review"), ("Publication", "DOI via Crossref, prefix 10.65838"),
                                                                          ("Accreditation", "CPD via PACE Council"), ("Recognition", "Three awards per event")])),
          box(h3("Who presents", "mic") + pills(["Faculty and professors", "PhD scholars", "Postgraduate students", "Industry professionals", "Policy makers", "School and college students"])
              + p('<span class="small">Calendar and call for papers: <b>onegrasp.com/events</b>. In the dashboard: Spotlight › Submit an abstract.</span>', "mt"), "soft"), "mt", gap="4mm")
    + grid([f'<div class="logo-card" style="height:20mm">{img("logos/" + f + ".png", style="max-height:11mm")}</div>' for f in ("crossref", "doi", "pace", "jci", "metaspectra")], 5, "push", gap="3mm"),
    section=S)

mark("The researcher journey")
journey = [("Submit your abstract", "Online, before the abstract deadline.", "send"), ("Committee review", "Reviewed by experts in your discipline.", "search-check"), ("Register", "Early, standard or late; Razorpay (India) or PayPal.", "credit-card"),
           ("Present live", "In your discipline's paper session.", "mic"), ("Certificate issued", "Unique, verifiable certificate ID.", "award"), ("DOI assigned", "A permanent, citable link via Crossref.", "link"),
           ("Indexed", "Listed in 10+ directories.", "list"), ("Keynote invitation", "Strong presenters keynote future editions.", "trophy")]
cols = ["#1E3A8A", "#3730A3", "#4338CA", "#4F46E5", "#0891B2", "#059669", "#EA580C", "#DC2626"]
add(head("Conferences", "From research paper", "to global recognition.", "A clear eight-step path takes every presenter from first submission to a published, indexed and certified contribution, and for the best, a future keynote.")
    + '<div class="stairs">' + "".join(f'<div class="stair" style="--sc:{cols[i]};margin-left:{(7 - i) * 0 + i * 6}mm"><span>Step {i + 1}</span>{icon(ic, "5mm", "#fff")}<b>{t}</b><em>{x}</em></div>' for i, (t, x, ic) in list(enumerate(journey))[::-1]) + "</div>"
    + h3("What every presenter takes home", "gift")
    + cards([("award", "Certificate with unique ID", "Verifiable by its certificate ID.", "#4338CA"), ("link", "A DOI for your abstract", "Prefix 10.65838, resolvable at doi.org.", "#0891B2"),
             ("badge-check", "CPD credit", "Accredited through PACE Council.", "#059669"), ("globe", "Zero travel, zero visa", "Join from your campus or home.", "#EA580C")], 4, "compact")
    + h3("How students get there from the dashboard", "route")
    + steps([("Research Studio", "Eight units teach the method.", "book-open"), ("Start a project", "Plan back from a conference date.", "flag"), ("Mentor check", "7 items scored 1–4.", "clipboard-check"),
             ("Spotlight", "Submit your abstract.", "send")], cols=4),
    section=S)

mark("The OneGrasp Scientific Committee")
members = [("Dr Santosh Kumar Mishra", "SNDT Women's University", "India"), ("Dr Sudarshan Rao K", "SMVITM Bantakal", "India"), ("Dr Farid Khallouki", "Moulay Ismail University", "Morocco"),
           ("Dr Fatiha Hakimi", "Hassan II Institute (IAV)", "Morocco"), ("Dr Rahmatullah Pashtoon", "Kandahar University", "Afghanistan"), ("Dr Bishnu Pada Bose", "Invosystems", "Singapore"),
           ("Dr Rudrarup Gupta", "Business & Economics", "India"), ("Dr Rohan Singh", "Chandigarh University", "India"), ("Dr Pradip Das", "Jagannath Kishore College", "India"),
           ("Dr Nalanda Roy", "Georgia Southern University", "USA"), ("Dr Ganesh Adhikari", "Nepal Engineering College", "Nepal"), ("Dr Jamiu Adetola Odugbesan", "Royal Docks School of Business", "United Kingdom"),
           ("Dr Nazrul Islam", "Independent University", "Bangladesh"), ("Dr Maatouk Khoukhi", "UAE University", "UAE"), ("Dr Tareq Nael Hashem", "Business & Economics", ""),
           ("Dr G. Vikram", "Karunya Institute", "India"), ("Dr Subhash Desai", "Sabarmati University", "India"), ("Dr Maria Cecilia Colautti", "UNPSJB", "Argentina"),
           ("Dr Ahmed M. Saqr", "TH Köln", "Germany"), ("Dr Chintan Patel", "CVM University", "India"), ("Dr Hadi Erfani", "Islamic Azad University", "Iran"),
           ("Dr S. Satish", "Hindustan Institute (HITS)", "India"), ("Dr Subhash Ghimre", "Kathmandu University", "Nepal"), ("Dr Nilesh Charankar", "Industry researcher", "USA"),
           ("Dr Sai Suman Singamsetty", "Centurion University", "India"), ("Dr Srikanth V", "Acharya Bangalore B School", "India"), ("Dr Sanjay G. Patel", "Nirma University", "India"),
           ("Dr Vijay Anant Athavale", "Walchand Institute of Tech.", "India"), ("Dr Maha Fawzy Anber", "El Shorouk Academy", "Egypt"), ("Prof D.K. Chaturvedi", "Dayalbagh Educational Inst.", "India"),
           ("Dr Praneetha Kotla", "Northern Illinois University", "USA"), ("Dr Bright Keswani", "Poornima University", "India"), ("Dr David Wortley", "ISDM · IORMA", "United Kingdom"),
           ("Dr Manjunath G N", "Sri Siddhartha Medical College", "India"), ("Prof Heba Afify", "Cairo University", "Egypt"), ("Dr Ju Lee Kim", "RedGene", "Republic of Korea"),
           ("Dr C. Bindu Ashwini", "RV College of Engineering", "India"), ("Dr Luisa Maria Arvide Cambra", "University of Almería", "Spain"), ("Dr Jahanavee", "Uka Tarsadia University", "India")]
pal = ["#4338CA", "#0891B2", "#DB2777", "#EA580C", "#059669", "#7C3AED", "#DC2626", "#0D9488"]


def initials(n):
    w = [x for x in n.replace("Dr ", "").replace("Prof ", "").replace(".", " ").split() if x]
    return (w[0][0] + w[-1][0]).upper()


add(head("Scientific committee", "The OneGrasp", "Scientific Committee.",
         "A 50-member committee of professors, researchers and industry experts reviews abstracts, chairs sessions and delivers keynotes across 11 disciplines. Featured here: 39 members from 15 countries.")
    + grid([f'<div class="person"><span class="avatar" style="background:{pal[i % 8]}">{initials(n)}</span><div><b>{n}</b><span>{u}</span>{f"<em class=flag>{c}</em>" if c else ""}</div></div>' for i, (n, u, c) in enumerate(members)], 3, gap="1.8mm 2.4mm")
    + band("India · USA · UK · Germany · Spain · Argentina · Singapore · Korea · UAE · Egypt · Morocco · Iran · Afghanistan · Nepal · Bangladesh", "15 countries:", "globe", "mt push"),
    section=S)

mark("Keynotes, awards and the conference day")
add(head("Conferences", "Keynotes from", "leading experts.", "Committee members and invited experts open each day with keynotes that bridge research and practice.")
    + grid([f'<div class="kn" style="--kc:{c}"><span class="avatar" style="background:{c};width:16mm;height:16mm;line-height:16mm;font-size:12pt">{initials(n)}</span><b>{n}</b><em>{r}</em><p>{t}</p></div>' for n, r, t, c in [
        ("Dr Manjunath G N", "Professor & Head, Pharmacology, Sri Siddhartha Medical College, India", "Mental health & psychological stress in athletes · Brain–computer interfaces", "#4338CA"),
        ("Dr Bishnu Pada Bose", "Professor, Partner & Advisor, Invosystems, Singapore", "Outcome-based vs traditional education · Greenhouse gases & global warming", "#0891B2"),
        ("Dr Ju Lee Kim", "Senior Researcher, R&D Center, RedGene, Republic of Korea", "Organoids and gene circuits in stem-cell research", "#DB2777")]], 3, gap="4mm")
    + h3("Two evenings, one clear format (IST)", "clock")
    + two(table(["Day 1", ""], [["6:00", "Inaugural ceremony & welcome"], ["6:30", "Keynote I"], ["7:15", "Keynote II"], ["8:00", "Networking & Q&A"], ["8:15", "Paper session I"], ["9:00", "Paper session II"], ["9:45", "Panel & open Q&A"]], "dense", widths=["22%", "78%"]),
          table(["Day 2", ""], [["6:00", "Welcome & Day 1 recap"], ["6:30", "Keynote III"], ["7:15", "Keynote IV"], ["8:00", "Open networking"], ["8:15", "Paper sessions III & IV"], ["9:00", "Award ceremony"], ["9:45", "Valedictory & certificates"]], "dense", widths=["22%", "78%"]), gap="4mm")
    + h3("Awards at every conference", "trophy")
    + cards([("trophy", "Best Paper Award", "For the strongest paper in each discipline.", "#F5B700"), ("star", "Young Researcher Award", "Recognising early-career excellence.", "#4338CA"), ("mic", "Outstanding Presenter", "For clarity and impact on stage.", "#DB2777")], 3, "compact")
    + callout("try", "Students: start with the <b>Research Studio</b> this term, aim for a student conference next term, and a OneGrasp international conference after that.", cls="push"),
    section=S)
