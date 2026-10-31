from lib import *

S = "Research & Conferences"

divider(7, "Research & Conferences", "From a student's first research question to an international stage: OneGrasp's peer-reviewed conferences and the scientific committee behind them.",
        ["International scientific conferences", "The researcher journey", "The OneGrasp Scientific Committee", "Keynotes from leading experts"],
        image="shots/research-conf.jpg")

mark("International scientific conferences")
add(head("Conferences", "Where global research", "gets presented.",
         "Present. Publish. Get recognised. Two-evening online conferences across 11 disciplines, with a DOI for every accepted abstract, CPD-accredited certificates and a 50-member international scientific committee.")
    + stats([("500+", "conferences held online"), ("70+", "countries represented"), ("50", "committee members"), ("11", "disciplines"), ("10,000+", "researchers reached")])
    + two(box(h3("11 disciplines, one global calendar") + '<ol class="num small">' + "".join(f"<li>{d}</li>" for d in [
        "Business & Economics", "Engineering & Technology", "Sports & Physical Education", "Agriculture & Food Sciences", "Interdisciplinary & Emerging", "Social Sciences & Humanities",
        "Education", "Physical & Life Sciences", "Health & Medical Sciences", "Mathematics & Data Science", "Arts, Culture & Communication"]) + "</ol>"),
          box(h3("The OneGrasp conference model") + kv([("Format", "Live online, two evenings"), ("Review", "Committee peer review"), ("Publication", "DOI via Crossref, prefix 10.65838"),
                                                       ("Accreditation", "CPD via PACE Council"), ("Recognition", "Three awards per event"), ("Indexing", "Listed in 10+ directories")]), "tint"))
    + h3("Who presents at OneGrasp")
    + '<div>' + "".join(f'<span class="pill">{x}</span>' for x in ["Faculty and professors", "PhD and research scholars", "Postgraduate students", "Industry professionals", "Policy makers", "School and college students (through the Research Studio)"]) + "</div>"
    + note("Find it:", "the calendar and call for papers are at onegrasp.com/events. In the dashboard: Spotlight › Submit an abstract.", "blue push"),
    section=S)

mark("The researcher journey")
add(head("Conferences", "From research paper", "to global recognition.",
         "A clear eight-step path takes every presenter from first submission to a published, indexed and certified contribution, and for the best, a future keynote.")
    + '<div class="grid g4">' + "".join(f'<div class="card"><div class="cnum">STEP {i}</div><h4>{t}</h4><p>{x}</p></div>' for i, (t, x) in enumerate([
        ("Submit your abstract", "Online, before the abstract deadline."), ("Committee review", "Reviewed by experts in your discipline."), ("Register", "Early, standard or late registration."),
        ("Present live", "In your discipline's paper session."), ("DOI assigned", "A permanent, citable link via Crossref."), ("Indexed", "Listed across 10+ directories."),
        ("Certificate issued", "CPD-accredited, with a unique, verifiable ID."), ("Keynote invitation", "Strong presenters keynote future editions.")], 1)) + "</div>"
    + h3("Awards at every conference")
    + cards([("Best Paper Award", "For the strongest paper in each discipline."), ("Young Researcher Award", "Recognising early-career excellence."), ("Outstanding Presenter", "For clarity and impact on stage.")], 3, "compact")
    + h3("How students get there from the dashboard")
    + steps([("Research Studio", "Eight short units teach the method, from a good question to Q&A (Part 5)."), ("Start a project", "Pick a conference first and plan backwards from its date."),
             ("Mentor check", "Seven items scored 1–4 before your abstract goes forward."), ("Spotlight", "Submit your abstract to a OneGrasp conference and get writing help.")], "row")
    + p("Every certificate carries the conference edition and code, the participant's name, discipline, date and authorised signatures. Accreditation: Crossref member, DOI prefix 10.65838 (resolvable at doi.org); CPD via PACE Council.", "small push"),
    section=S)

mark("The OneGrasp Scientific Committee")
placeholder("canva:DAHXidPDcII:9")   # scientific committee: 39 featured members of 50, 15 countries
mark("Keynotes from leading experts")
placeholder("canva:DAHXidPDcII:8")   # keynotes and moments from recent conferences
