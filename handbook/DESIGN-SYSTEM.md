# OneGrasp Career Fitment Handbook — Design Audit & System (v2)

## Stage 1 — Design audit (v1, before redesign)

| # | Finding | Effect | v2 action |
|---|---------|--------|-----------|
| 1 | 10 different chapter colours plus a bright 8-colour dimension palette | Brochure / AI look, no identity | One brand palette; muted navy–red chart scale |
| 2 | Icons, chips, pills, rounded cards, shadows, gradients | "Generated" appearance | All removed; hairline rules and typographic hierarchy |
| 3 | 3D illustrations and cartoon art | Undermines credibility | Hidden; real photos, logos and screenshots only |
| 4 | Poppins used for everything incl. body | Tiring to read in long text | Poppins SemiBold titles; Inter for headings, labels, body |
| 5 | Shouty uppercase labels | Noisy | Sentence-case labels, Inter Medium |
| 6 | Auto-shrink on 9 pages (one at 60 %) | Unreadable small text | Contents fixed; remaining pages listed below for Stage 4 |
| 7 | Symmetric margins | Text lost in binding | Mirrored grid, 24 mm inner / 17 mm outer |
| 8 | Handwriting font, purple text on 90-day plan | Off-brand | Inter, navy |
| 9 | Committee directory duplicated the wall | Redundant | Removed; replaced by featured page for Dr Rudrarup Gupta |
| 10 | Photo-heavy cover | Read as brochure | Typographic book cover with the specified text |

## Stage 2 — Design system

**Colour**

| Token | Hex | Use |
|-------|-----|-----|
| Red | `#B92B32` | Numbers, markers, kickers, cover edge — sparingly |
| Navy | `#17243A` | Titles, headings, rules, chapter openers |
| White | `#FFFFFF` | Paper |
| Stone | `#F4F3EF` | Quiet panels |
| Body | `#333B46` | Running text |
| Muted | `#747C87` | Captions, running heads, folios |
| Rule | `#E3E5E8` | Hairlines |

Chart scale (grayscale-distinct): `#17243A #B92B32 #3D4F66 #7A2A30 #5E7189 #9C5A5E #8A97A8 #C2A3A5`.

**Type**

| Role | Font | Size |
|------|------|------|
| Page title | Poppins SemiBold | 24 pt / 1.15 |
| Chapter opener | Poppins SemiBold | 34 pt |
| Cover title | Poppins SemiBold | 50 pt |
| Section heading | Inter SemiBold | 10.6 pt |
| Lead | Inter Regular | 10.8 pt / 1.62 |
| Body | Inter Regular | 9.8 pt / 1.6 |
| Labels / captions | Inter Medium | 7.6–8 pt |

Fonts are embedded in the PDF; text stays selectable.

**Grid (A4 210 × 297 mm)** — top 25 mm, bottom 22 mm, inner 24 mm, outer 17 mm, mirrored by page parity. Running head (book · section) at 12 mm; folio bottom outer corner.

**Layout systems** — editorial text · assessment (dimension pages) · workbook (fill-in tables, write lines, checkboxes) · dashboard documentation (framed screenshots + numbered steps) · research/startup (directories, two-column tables) · parents/schools · chapter openers (navy, red part number).

## Stage 3 — Preview pages

`out/OneGrasp-Handbook-Design-Preview.pdf`: cover (1), contents (2), assessment dimension (24), dashboard documentation (45), action-plan worksheet (116), plus featured member page (103).

## Stage 4 — Open items for full implementation

- Pages still auto-scaled below 100 %: 5, 22, 25, 26, 36, 41, 102 — to be re-laid out (split content or re-grid), never shrunk.
- 3 mm bleed for full-bleed pages (cover, chapter openers, back cover).
- Funding donut charts → muted scale.
- Print limits: Chromium exports RGB; a CMYK (FOGRA39) conversion must be done by the printer or in Acrobat/Ghostscript. Images are 300 DPI where the source allows; some logos came only as screen-resolution thumbnails.

## Factual claims needing human verification (not changed in the book)

1. Brochure figures: 3,000+ students, 10+ schools, 1,000+ parents, 500+ sessions, 2 states — source marked "to be confirmed".
2. Conflicting figures: "2,500+" vs "3,000+" career roadmaps.
3. Committee: only 39 of the stated 50 members were supplied with photos and details.
4. Dr Pradip Kumar Das appeared twice with different photos — confirm the correct one.
5. Dr Tareq Nael Hashem — country not supplied (currently grouped with India).
6. Dr Rudrarup Gupta — name of the organisation he founded, and BCCI commentator role wording, to be confirmed.
7. Assessment question counts and the 90-minute duration are taken from the app code — confirm against the live test.
8. Typical entrance-exam months in the Class 11–12 plan — confirm for 2026–27.
9. "Ananya" is a demo student; her report uses generated answers — label as sample in print.
10. 311 funding programmes listed from the app's data file — amounts and eligibility change; add an "as of" date.
