import p0_front
import p1_meet
import p2_test
import p3_dims
import p4_report
import p5_explore
import p6_skills
import p7_startup
import p8_research
import p9_family
import p10_action

# ---- motivational quote bands on pages that have room (attributions listed for verification in DESIGN-SYSTEM-v4.md)
import lib
QB = [('<div class="kicker">Your dream career</div>', "The only way to do great work is to love what you do.", "Steve Jobs, Stanford, 2005", "#C72D35"),
      ('<div class="kicker">Choosing your stream</div>', "Dream, dream, dream. Dreams transform into thoughts and thoughts result in action.", "A. P. J. Abdul Kalam", "#F09A24"),
      ('<div class="kicker">Your results</div>', "Take up one idea. Make that one idea your life; think of it, dream of it, live on that idea.", "Swami Vivekananda", "#7754B8"),
      ('<div class="kicker">Study Abroad · How it works</div>', "If you want to shine like a sun, first burn like a sun.", "A. P. J. Abdul Kalam", "#2196C8"),
      ('<div class="kicker">Internships & Jobs · Do it now</div>', "For the things we have to learn before we can do them, we learn by doing them.", "Aristotle, Nicomachean Ethics", "#F09A24"),
      ('<div class="kicker">AI & Certifications · How it works</div>', "The illiterate of the 21st century will not be those who cannot read and write, but those who cannot learn, unlearn, and relearn.", "Alvin Toffler, Future Shock", "#7754B8"),
      ('<div class="kicker">Research Studio · Do it now</div>', "Research is to see what everybody else has seen, and to think what nobody else has thought.", "Albert Szent-Györgyi", "#2196C8"),
      ('<div class="kicker">For parents</div><h1 class="title">Ten questions', "There are two lasting bequests we can hope to give our children. One of these is roots, the other, wings.", "Hodding Carter", "#2196C8"),
      ('<div class="kicker">For schools and colleges</div>', "The function of education is to teach one to think intensively and to think critically.", "Martin Luther King Jr.", "#C72D35"),
      ('<div class="kicker">Your year</div><h1 class="title">Class 6–10', "Start where you are. Use what you have. Do what you can.", "Arthur Ashe", "#279B70"),
      ('<div class="kicker">Workbook</div><h1 class="title">My weekly', "We are what we repeatedly do. Excellence, then, is not an act, but a habit.", "Will Durant", "#F09A24")]
for key, text, who, col in QB:
    hits = [pg for pg in lib.PAGES if key in pg["body"]]
    if len(hits) != 1:
        print("quote target not unique:", key, len(hits)); continue
    hits[0]["body"] += lib.qband(text, who, col)
