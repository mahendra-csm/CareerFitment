# Print QA report: Career Fitment Handbook v3 (full book)

Checked file: `out/OneGrasp-Career-Fitment-Handbook-print.pdf`. A digital edition and a 5-page preview were exported alongside it.

| Check | Result |
|---|---|
| Page count | **120**, A4 portrait (210 × 297 mm) |
| Page references and contents | All `{{REF}}` links resolved; none left unresolved. Contents and opener page numbers are generated from the build. |
| Fonts | Inter (4 weights) and Poppins (6 weights), all embedded as TrueType. No Type 3 or fallback fonts. The symbols ₹ → ☐ ✓ ✎ ✂ were added to the fonts (from DejaVu Sans) so they embed too. |
| Text | Selectable and searchable on every page. |
| Margins | Mirrored margins: 22 mm inner (binding), 16 mm outer, 22 mm top, 18 mm bottom. |
| Text size | Pages print at 92–100 % scale. Nine pages are slightly scaled to fit (lowest 90 %, so body text is never below about 8.6 pt). |
| Colour | Chapter accents follow the v3 system. There are no gradients and no shadows. |
| Overflow | None. The build shrinks any page that would overflow, and every page fits at 90 % or more. |

**Pages slightly scaled to fit**

| Page | Scale |
|---|---|
| 5 | 94 % |
| 9 | 91 % |
| 15 | 92 % |
| 16 | 94 % |
| 21 | 95 % |
| 26 | 91 % |
| 37 | 92 % |
| 102 | 94 % |
| 104 | 90 % |

## Images

| Item | Effective resolution | Action |
|---|---|---|
| Dr Rudrarup Gupta photo (p. 103) | ~86 dpi | **Need a higher-resolution photo** (at least 900 px wide) before printing |
| Chapter-opener photos (school sessions) | 125–140 dpi | Fine on screen. Supply original camera files for 300 dpi print. |
| School gallery (p. 13) | 110–190 dpi | Same as above |
| Dashboard screenshots | ≥ 200 dpi | OK |
| Logos and committee portraits | Small placements | OK at their printed size |

## Not done by this pipeline (prepress)

- **CMYK:** Chromium writes RGB PDFs. Convert to CMYK (FOGRA39 or the printer's profile) at prepress.
- **Bleed:** pages are exact A4 without bleed. The cover, chapter openers and back cover need 3 mm added at prepress, or a bleed export.
- **Canva:** this cloud environment's network policy blocks uploads to `www.canva.com`. The PDF can be imported into Canva with Create a design → Import file. Icons are Lucide (open source, consistent 1.75 stroke) rather than Canva's library for the same reason.

## Content changes in this round (as requested)

- **Cover:** full red, with the logo in a white circle in the centre.
- **Funding directory:** cut from 4 pages to 2. It now lists the **121 programmes open at idea, proof-of-concept or prototype stage**. All 311 remain in the dashboard, and the source and date are printed on both pages.
- **Two new visual pages** (they keep the book at 120 pages):
  - "Your journey with OneGrasp" (roadmap, Part 1)
  - "Your dashboard at a glance" (mind map, Part 5)
- **Restyled pages:** these became mind maps, roadmaps and comparison panels. The wording is unchanged.
  - What is OneGrasp
  - Is it just another exam
  - Your roadmap and next steps
  - every tool chapter's "What's inside"
- **Dimension pages:** rebuilt in the prototype layout. The example and "why it matters" text from the source now appear on each page.

## Factual items still to verify

See the list at the end of `DESIGN-SYSTEM.md`.
