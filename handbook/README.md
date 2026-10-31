# OneGrasp Career Fitment Handbook (2026–27)

A 120-page, full-colour A4 handbook for the Career Fitment Assessment, for students, parents and schools.

| File | Use |
|---|---|
| `out/OneGrasp-Career-Fitment-Handbook-print.pdf` | Print edition: high-resolution images |
| `out/OneGrasp-Career-Fitment-Handbook-digital.pdf` | Digital edition: smaller file for download and sharing |

## What's inside (10 colour-coded parts)

A practical **do-it workbook**: every dashboard tool has its own 3-page chapter (opener, how it works with real screenshots, and a mission card with tick boxes and a fill-in worksheet).

1. **Meet OneGrasp**: who we are, services, why choices go wrong, future of work, campus days and photos
2. **The Assessment**: what it is, editions, the science, registering, the exam screen, question types, trust
3. **The 8 Dimensions**: one page per dimension with a chart and a fill-in box, plus the 8 undergraduate areas
4. **Your Report**: page-by-page anatomy, a worked example, every class's report, how to read it
5. **Dashboard: Explore**: home, navigation, then tool chapters: Career Library, Entrance Exams, Scholarships, Study Abroad, Internships & Jobs; quick map
6. **Skills for Life & Work**: Financial Literacy, Law & Rights, AI & Certifications, Communication Lab, Resume & Interview, Proof & Progress, Spotlight
7. **Startups & Funding**: the Startups course chapter with an idea canvas, Spot–Build–Pitch, all 311 funding programmes
8. **Research & Conferences**: the Research Studio chapter, conferences, researcher journey, scientific committee, keynotes
9. **Parents & Schools**: guide-not-decide, ten questions, the Institution Portal, FAQ and glossary
10. **Your Action Plan**: 30-day kickstart challenge, month-by-month plans per stage, profile on one page, trackers, achievements log

## Rebuild

```
python3 build.py --html
python3 editions.py
```

Content lives in `p0_front.py` … `p8_family.py`, components in `lib.py`, styles in `style.css`.
Screenshots in `assets/shots` were taken from the live app with a demo student (Ananya Rao).
Partner and school logos come from the OneGrasp Canva designs; icons are Lucide (ISC licence).
