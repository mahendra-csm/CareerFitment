# OneGrasp Career Fitment Handbook (2026–27)

A 120-page, full-colour A4 handbook for the Career Fitment Assessment, for students, parents and schools.

| File | Use |
|---|---|
| `out/OneGrasp-Career-Fitment-Handbook-print.pdf` | Print edition: high-resolution images |
| `out/OneGrasp-Career-Fitment-Handbook-digital.pdf` | Digital edition: smaller file for download and sharing |

## What's inside (8 colour-coded parts)

1. **Meet OneGrasp** (red): who we are, services, the three traps, myths vs facts, the future of work, campus days and photos
2. **The Assessment** (blue): what it is, four editions, the science, the 90 minutes, registering, the exam screen, question types, trust and privacy
3. **The 8 Dimensions** (violet): two pages per dimension with charts, plus the 8 undergraduate readiness areas
4. **Your Report** (green): every class's report, a worked example (sample student Ananya), the 15 domains, how to read it, a 90-day plan
5. **Your Dashboard** (orange): every tool, with real screenshots, steps, tasks and a quick map
6. **Startups & Funding** (magenta): Spot–Build–Pitch and all 311 funding programmes
7. **Research & Conferences** (indigo): conferences, the researcher journey, the 39 featured scientific committee members, keynotes
8. **Parents & Schools** (sky): guide-not-decide, ten questions, the Institution Portal, benefits, FAQ and glossary

## Rebuild

```
python3 build.py --html
python3 editions.py
```

Content lives in `p0_front.py` … `p8_family.py`, components in `lib.py`, styles in `style.css`.
Screenshots in `assets/shots` were taken from the live app with a demo student (Ananya Rao).
Partner and school logos come from the OneGrasp Canva designs; icons are Lucide (ISC licence).
