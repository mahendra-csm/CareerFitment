# OneGrasp Career Fitment Handbook (2026–27)

A 120-page A4 print handbook for the Career Fitment Assessment: what OneGrasp is, the assessment, the 8 dimensions, the report for every class, every dashboard tool, the startup funding directory, research and conferences, and pages for parents and schools.

- `out/handbook.pdf`: 113 print-ready pages
- `out/canva-inserts.json`: 7 pages that come from existing Canva designs (partner logos, partner schools, campus photos, the scientific committee, keynotes). They are merged in at these page numbers, for 120 in all.

| Book page | Canva page |
|---|---|
| 6 | Main brochure (DAHXfhMiiR0) p48: international collaborations |
| 7 | Conferences brochure (DAHXidPDcII) p2: accreditation, DOI and indexing partners |
| 8 | Main brochure p2: partner schools |
| 15 | Main brochure p3: on campus with students |
| 16 | Main brochure p4: assessment day in pictures |
| 112 | Conferences brochure p9: the scientific committee |
| 113 | Conferences brochure p8: keynotes |

## Rebuild

```
python3 build.py
```

Content lives in `part1_front.py` … `part8_back.py`; layout in `lib.py` and `style.css`. Screenshots in `assets/shots` were taken from the live app with a sample student (Ananya Rao).
