# OneGrasp Career Fitment Handbook: Design System v3 ("Premium colour")

v3 replaces both earlier directions. It keeps the colour and visual engagement of the original book and the typography and discipline of the v2 preview.

- **Prototype:** `out/OneGrasp-Handbook-v3-Prototype.pdf`
- **Source:** `proto.py` + `v3.css` (+ `fonts.css`)

## Phase 1: Audit of the two earlier designs

| | Original (v1) | v2 preview | v3 response |
|---|---|---|---|
| Colour | Bright and engaging, but 10 unrelated chapter palettes and gradients | One navy/red palette; felt plain | 6 brand accents, one per chapter; 2–3 per page; flat fills, no gradients |
| Icons | Many, mixed with 3D clip art | None | Lucide only, 1.75 stroke, in 2 mm-radius tinted tiles; each one labels content |
| Illustration | Cartoon 3D objects, floating art | Removed | Real photos (OneGrasp school sessions), real logos, real screenshots |
| Type | Poppins everywhere | Poppins titles + Inter body | Poppins Bold for display; Inter Medium for sub-heads and labels; Inter Regular for body |
| Density | Crowded; some pages auto-shrunk to 60 % | Large empty areas; long paragraphs | Every page filled to the margins at 100 % scale. Text broken into cards, steps, sliders and tables. |
| Hierarchy | Many competing boxes | Weak: everything looked the same | Kicker → title → lead → tinted panels. Numbers and markers are in the accent colour. |
| Screenshots | Large laptop mock-ups | Laptop mock-ups | Flat browser frames, red numbered pins with a key alongside |
| Worksheets | Plain tables | Plain tables | Colour-coded phases, writing lines, weekly tick strip, signature row |
| Print | RGB, Type 3 fonts | Inter embedded as Type 3 fonts | Static TTF Inter + Poppins, fully embedded (the PDF contains no Type 3 fonts) |

## Phase 2: Design system

**Colour**

| Token | Hex | Text-safe tone | Role |
|---|---|---|---|
| OneGrasp Red | `#C72D35` | `#B0262E` | Identity, key highlights, pins |
| Deep Navy | `#17243A` | n/a | Headings, type card, cover |
| Blue | `#2196C8` | `#1672A0` | Assessment, report, research, parent notes |
| Purple | `#7754B8` | `#6243A3` | 8 Dimensions, personality, intelligence |
| Green | `#279B70` | `#1F7D5A` | Strengths, skills, progress, examples |
| Orange | `#F09A24` | `#B76A06` | Dashboard, activities, action steps |
| Gold | `#E5B73B` | `#8C6A0C` | Insights ("In simple words"), startups, edition badge |
| Light grey | `#F3F4F6` | n/a | Neutral panels |
| Warm neutral | `#F5F4F1` | n/a | Alternate panels |

The pale accent colours (e.g. gold, orange) are never used for body text; the text-safe tone is used instead. Tints are 8–13 % of the accent on white.

**Chapter identities**

| Part | Chapter | Accent | Icon |
|---|---|---|---|
| 01 | Meet OneGrasp | red | building-2 |
| 02 | The Assessment | blue | clipboard-check |
| 03 | The 8 Dimensions | purple | brain |
| 04 | Your Report at a Glance | blue | file-chart-column |
| 05 | Your Dashboard: Explore | orange | layout-dashboard |
| 06 | Skills for Life & Work | green | sprout |
| 07 | Startups & Funding | gold | rocket |
| 08 | Research & Conferences | blue | microscope |
| 09 | Parents & Schools | red | heart-handshake |
| 10 | Your Action Plan | orange | flag |

**Type scale (A4)**

| Element | Style |
|---|---|
| Cover title | Poppins Bold 40 pt |
| Page title | Poppins Bold 23 pt; the second phrase in the chapter accent |
| Section heading | Poppins SemiBold 10.6 pt, with an icon tile |
| Card heading | Inter SemiBold 9.6 pt |
| Lead | Inter Regular 10.4 pt / 1.55 |
| Body | Inter Regular 9.6 pt; cards 8.1–8.4 pt (minimum 7.7 pt for secondary notes) |
| Labels | Inter SemiBold 7.4–7.8 pt, tracked caps (short labels only) |

**Grid:** A4 with mirrored margins. Inner (binding) margin 22 mm, outer 16 mm, top 22 mm, bottom 18 mm. 4.5 mm gutters. A running header carries the chapter-number chip, chapter name and book title. A coloured edge tab on the outer edge helps you find chapters with your thumb. The footer has the folio and a chapter-colour dot.

**Components (all in `v3.css`)**
- **Cards:** `.card.t` (tinted), `.card.line` (outlined), `.card.top` (accent bar).
- **Callouts:** `.callout`, in four kinds: `.insight` (gold), `.action` (orange), `.parent` (blue) and `.grow-c` (green, used for examples).
- **Process:** `.flow` (numbered steps with arrows), `.phases` (time-boxed plan), `.rhythm` (weekly routine).
- **Data:** `.sl` (preference slider), `.typecard`, and `.tbl` (colour-coded header, zebra rows).
- **Dimension pages:** `.dimhero` (dimension header with progress strip), `.pr` (preference pair with slider), `.ages` (Class 6–8 / 9–10 / 11–12 / family tiles).
- **Screenshots:** `.shot` (flat browser frame), `.pin` and `.key` (numbered annotations).
- **Worksheets:** `.field`, `.wl`, `.box` (checkbox), `.timeline` (weekly tick strip).

**Images:** real photos only, cropped with `object-fit` and never stretched. There are no drop shadows, gradients or 3D art.

## Phase 3: Prototype (5 pages)

| Page in book | Sample | Shows |
|---|---|---|
| 1 | Cover | Navy panel and OneGrasp school-session photo, six-colour chapter bar, required cover text, the four partner-school logos |
| 2 | Contents | Two columns, colour-coded chapter chips, page numbers from the live 120-page build |
| 24 | 01 Personality | Dimension header, three explainer cards, preference sliders, type card, example, 4-column career table, age tiles, fill-in |
| 45 | How to use your dashboard | Six-step flow, annotated screenshot with 8-point key, My Progress screenshot, weekly-routine grid, mission |
| 116 | Your 90-day plan | Four "my report" fields, Explore/Do/Build phases with writing space, 12-week tick strip, signature row |

All text on these pages comes verbatim from the book's source modules. The Example and Why-it-matters text on page 24 was already in the source but was not printed in v2.

**Prototype QA:**
- Overflow: 0 on all pages, and every page prints at 100 %.
- Fonts: Inter (4 weights) and Poppins (2 weights), all embedded. There are no Type 3 or fallback fonts.
- Text is selectable.

## Canva

- **What I checked:** the Canva connector is connected. Its upload endpoint (`www.canva.com/_blob/upload…`) is blocked by this cloud environment's network policy (HTTP 403 at the proxy). Canva's URL import needs a public URL, and publishing generated files publicly for that is not allowed.
- **Result:** no Canva design has been created from this prototype yet.
- **Canva-compatible route:** in Canva, use *Create a design → Import file* and choose the PDF. Canva converts each page into editable text, shapes and images. The fonts are standard Google Fonts (Poppins, Inter), so Canva maps them natively.
- **To let me upload directly:** add `www.canva.com` to Allowed domains in the environment's network settings.

## Still open (Phase 5–6, after approval)

- Roll v3 out to all 120 pages, chapter by chapter, with per-page QA (overflow, blank areas, contrast, page refs).
- Chapter-opener template: large number, accent field, real photo, overview and in-this-part list.
- 3 mm bleed version for the cover, chapter openers and back cover. CMYK conversion (FOGRA39) to be done at prepress; Chromium writes RGB.
- Photo resolution: school photos are 1050 × 1400 px, which is about 250 dpi at the cover crop. Higher-resolution originals would be needed for 300 dpi.
- The factual-verification list in `DESIGN-SYSTEM.md` still applies.
