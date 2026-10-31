from lib import *

theme("brand")

# ---------------------------------------------------------------- 1. cover
add(f'''<div class="cv">
<div class="cv-bg"></div><div class="cv-dots"></div>
<div class="cv-logo">{img("art/logo.png")}</div>
<div class="cv-chip">{icon("book-open", "4mm", "#E5383B")} Handbook · 2026–27 Edition</div>
<div class="cv-photos">
  <div class="cvp p1">{img("gallery/new1.webp")}</div>
  <div class="cvp p2">{img("gallery/old12.webp")}</div>
  <div class="cvp p3">{img("gallery/new5.webp")}</div>
  <div class="cvp p4">{img("gallery/old02.webp")}</div>
</div>
{img("brochure/c11-i-001.png", "cv-girl")}
<div class="cv-text">
  <div class="cv-kick">OneGrasp Career Fitment Assessment</div>
  <h1 class="cv-title">The Complete<br><span>Career Fitment</span><br>Handbook</h1>
  <p class="cv-sub">Know yourself. Choose your path. Build your future.<br>The step-by-step guide to the assessment, the 8 dimensions, your report and all 20+ tools in your dashboard.</p>
  <div class="cv-for"><span>{icon("graduation-cap", "4mm", "#fff")} Students</span><span>{icon("heart-handshake", "4mm", "#fff")} Parents</span><span>{icon("school", "4mm", "#fff")} Schools & colleges</span></div>
</div>
<div class="cv-band">
  <div><b>8</b><span>dimensions<br>of you</span></div><div><b>4</b><span>editions, Class 6<br>to degree</span></div>
  <div><b>930</b><span>careers<br>explained</span></div><div><b>20+</b><span>tools in one<br>dashboard</span></div><div><b>311</b><span>startup funding<br>programmes</span></div>
  <div class="cv-url">{img("art/qr.png", "cv-qr")}<span>Take the assessment<br><b>careerfitment.onegrasp.com</b></span></div>
</div></div>''', kind="cover")

# ---------------------------------------------------------------- 2. belongs to + how to use
mark("How to use this handbook")
add(head("Before you begin", "This handbook", "belongs to…")
    + two(box('<div class="own">' + "".join(f'<div class="ownf"><label>{l}</label><div class="wline"></div></div>' for l in
                                           ["My name", "Class / year", "School or college", "Date I took the assessment", "My personality type", "My interest code", "My top career field"]) + "</div>", "soft"),
          box(h3("How to use this book", "compass")
              + p("You do not need to read it cover to cover. Each part has its own colour, so you can find your way by the edge of the page.")
              + "".join(f'<div class="route" style="--rc:{c}"><span class="rdot"></span><div><b>{t}</b><br><span class="small">{x}</span></div></div>' for c, t, x in [
                  ("#E5383B", "Part 1 · Meet OneGrasp", "Who we are and why this matters"),
                  ("#0EA5E9", "Part 2 · The Assessment", "Read before you take the test"),
                  ("#8B5CF6", "Part 3 · The 8 Dimensions", "What each part of you means"),
                  ("#10B981", "Part 4 · Your Report", "Read with your report open"),
                  ("#F97316", "Part 5 · Your Dashboard", "Keep next to your screen"),
                  ("#D946EF", "Part 6 · Startups & Funding", "311 programmes to fund an idea"),
                  ("#6366F1", "Part 7 · Research & Conferences", "Present your work to the world"),
                  ("#0284C7", "Part 8 · Parents & Schools", "How the adults can help")])),
          ratio="0.9fr 1.1fr")
    + h3("Look out for these boxes")
    + grid([callout("simple", "The idea explained the way a friend would."), callout("example", "A real situation that shows how it works."),
            callout("ananya", "Follow Ananya, a sample Class 11 student, through her real report."), callout("try", "A small action you can do this week."),
            callout("parent", "Advice for mothers, fathers and guardians."), callout("warn", "Mistakes and scams to avoid.")], 3, gap="0 3mm"),
    section="How to use this book")

# ---------------------------------------------------------------- 3. welcome letter
mark("A welcome from OneGrasp")
add(head("Welcome", "Every child is good at", "something.")
    + two(quote("Most career decisions are made on marks, peer pressure or guesswork. OneGrasp replaces guesswork with self-knowledge and a clear, honest plan the whole family can see.", "The OneGrasp Team")
          + p("Dear student, parent and teacher,", "mt")
          + p("A career is rarely one decision. It is a chain of them: which subjects to take, which stream, which entrance exam, which degree, which college, which first job. Each choice shapes the next. When the first link is chosen on marks alone, or because a cousin did the same course, the whole chain can pull in the wrong direction.")
          + p("The Career Fitment Assessment starts with <b>you</b>: how you think, what you enjoy, how you learn, what drives you and what you are naturally good at. It then connects that picture to <b>real</b> careers, exams, colleges and money (scholarships, funding and salaries), so the next step is clear."),
          photo("gallery/new1.webp", "A OneGrasp session: “Which career fits me?”", style="height:78mm") + p("", "mt")
          + p("After the report, the real work begins. Your dashboard turns the report into lessons, tools and weekly tasks, and this handbook walks you through every one of them, page by page.")
          + p("Read it slowly. Read it together. Come back to it whenever a big decision arrives.")
          + '<div class="sign"><span class="hand">With warm wishes,</span><b>The OneGrasp Team</b><span class="small">OneGrasp Education Pvt. Ltd., Hyderabad</span></div>', ratio="1.05fr 0.95fr", gap="7mm")
    + h3("Start in three steps", "rocket")
    + steps([("Scan or visit", "careerfitment.onegrasp.com on any phone, tablet or laptop.", "qr-code"),
             ("Register in 2 minutes", "Sign up yourself, or join through your school or college link.", "user-plus"),
             ("Take the test", "Answer honestly. Your report is ready the moment you finish.", "file-check")]),
    section="Welcome")

# ---------------------------------------------------------------- 4. contents
add(head("Contents", "What's inside", "this handbook.") + "{{TOC}}", section="Contents")

# ---------------------------------------------------------------- 5. partners
mark("Our partners and collaborations")
logos = [("crossref", "Crossref", "DOI registration"), ("doi", "DOI 10.65838", "Permanent citable links"), ("pace", "PACE Council", "CPD accreditation"), ("jci", "Journal Citation Index", "Citation indexing"),
         ("intellimind", "IntelliMindEd", "Academic partner"), ("metaspectra", "metaSpectra", "Indexing partner"), ("rmetahub", "RMetaHub", "Indexing partner"), ("kvrss", "KVRSS Group", "Partner")]
schools = [("school-shanthinikethan", "Sree Shanthinikethan English Medium School"), ("school-dps", "Delhi Public School"), ("school-oxford", "Oxford Grammar High School"), ("school-excellencia", "Excellencia Junior College")]
add(head("Working together", "Our partners and", "collaborations.", "International organisations, partner schools and learning platforms that OneGrasp works with.")
    + h3("International collaborations", "globe")
    + grid([f'<div class="logo-card">{img("logos/" + f + ".png")}<span>{n}<br><span class="small">{d}</span></span></div>' for f, n, d in logos], 4)
    + h3("Schools that chose OneGrasp for their students", "school")
    + grid([f'<div class="logo-card" style="height:34mm">{img("logos/" + f + ".png", style="max-height:19mm")}<span>{n}</span></div>' for f, n in schools], 4)
    + h3("Free courses and tools in the dashboard come from", "graduation-cap")
    + grid([f'<div class="logo-card" style="height:16mm">{img("logos/" + f + ".svg", style="max-height:8mm")}</div>' for f in ("google", "microsoft", "ibm", "harvard")], 4)
    + two(box(h3("Media partners", "megaphone") + pills(["All Conference Alert", "Conference Alerts India", "Conference Alerts", "All International Conference", "ConferenceAlerts.com", "10times", "Conference2go", "Events Notification"]), "soft"),
          box(h3("Researchers from 70+ countries", "map") + pills(["India", "USA", "United Kingdom", "Germany", "Spain", "Argentina", "Singapore", "Korea", "UAE", "Egypt", "Morocco", "Iran", "Afghanistan", "Nepal", "Bangladesh"]), "soft"), "mt", gap="4mm")
    + p("All logos and trademarks belong to their respective owners.", "small center push"),
    section="Partners")

# ---------------------------------------------------------------- 6. at a glance
mark("OneGrasp at a glance")
nums = [("3,000+", "Students assessed", "users", "#E5383B"), ("10+", "Schools and colleges", "school", "#4C5FD5"), ("8", "Dimensions measured", "radar", "#F5B700"),
        ("2,500+", "Career roadmaps", "route", "#16A34A"), ("2", "States reached", "map", "#7048E8"), ("1,000+", "Parents engaged", "heart-handshake", "#0EA5E9"), ("500+", "Counselling sessions", "messages-square", "#E64980")]
add(head("The big picture", "OneGrasp", "at a glance.", center=True)
    + photo("gallery/old08.webp", style="height:62mm", tape=False)
    + '<div class="glance">' + "".join(f'<div class="gl" style="--g:{c}"><span class="gln">{i + 1}</span>{icon(ic, "6mm", c)}<b>{v}</b><span>{l}</span></div>' for i, (v, l, ic, c) in enumerate(nums)) + "</div>"
    + h3("Inside the dashboard", "layout-dashboard")
    + stats([("930", "careers explained", "briefcase"), ("29", "entrance exams", "clipboard-list"), ("40", "scholarships", "award"), ("209", "free internships", "laptop"), ("24", "legal guides", "scale")])
    + '<div class="grid push" style="grid-template-columns:repeat(4,1fr);gap:3mm">' + "".join(photo(f"gallery/{g}", style="height:30mm", tape=False) for g in ("old10.webp", "new2.webp", "old03.webp", "g13.jpg")) + "</div>",
    section="At a glance")
