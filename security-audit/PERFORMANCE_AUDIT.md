# Performance & Scalability Audit

**Measured** means taken from the production build (`next build`, Next 14.2.35, 2026‑11‑12) or from reading the code.
**Estimated** means reasoning about load. **No load test was run.** I was not authorised to load-test production, and a local `next start` says little about Vercel serverless behaviour. Every concurrency figure below is theoretical.

## Architecture as it affects performance
- **Hosting:** Next.js 14 App Router on Vercel. Pages are mostly static (`○`) and served from the CDN. 78 API routes run as serverless functions, some with `maxDuration` of 20–60 s.
- **Data:** Firebase Auth and Firestore. The browser uses the client SDK under rules; the server uses the Admin SDK. Supabase Postgres holds the job portal only.
- **External calls in the request path:**
  - Google Identity Toolkit (token check, cached for 5 minutes per instance)
  - Groq and DeepSeek (LLM, 2–20 s)
  - Razorpay
  - the SMTP server (one connection per email)
  - the CRM webhook

## Measured: client bundles (baseline build)
| Metric | Value |
|---|---|
| Routes in build | 257 |
| Shared first-load JS | 88.1 kB |
| Median first-load JS per route | 151 kB |
| Routes with first-load JS > 300 kB | **78** |
| Largest | `/account` **747 kB**, `/admin/report/[uid]` 691 kB, `/institution/report/[uid]` 690 kB, `/account/communication/*` 387 kB |

My fixes did not change bundle sizes (post-fix build: `/account` 747 kB, `/admin` 287 kB).

## Findings

| ID | Bottleneck | Evidence | Effect at scale | Recommendation |
|---|---|---|---|---|
| P-01 | **The admin dashboard downloads the whole `users` collection to the browser** | `app/admin/(dashboard)/page.tsx:100`, `archives/page.tsx:31` use `getDocs(collection(db,"users"))` and fetch full documents (assessment, exam session, progress, activity) | Reads per load = number of users. At 10k users with 20–50 kB documents that is 200–500 MB to the browser, so the page will not load. Firestore read cost grows linearly | Server-side, paginated admin API (`limit`/`startAfter`) with `select()` field masks. Precompute counts with aggregation queries (`count()`) |
| P-02 | **Every institution-portal request scans every user** | `lib/institution/server.ts:142` `studentsOf()` runs `db.collection("users").select("institution").get()`. It is used by 18 route call sites | Each portal click costs N document reads plus latency. At 20k users: about 20k reads and several seconds per request, multiplied by every teacher clicking | Store a normalised `institutionId` on the user when they link (see M-02) and query `where("institutionId","==",id)` with an index |
| P-03 | All institutions are read for each student lookup | `institutionForStudent()` (`server.ts:162`) reads the whole `institutions` collection on every passport and milestone call | Small N today, but it grows | The same `institutionId` fix, or an in-memory cache with a TTL |
| P-04 | Hot single document under bulk sign-up | `/api/institutional/redeem` increments `institutional_links/{code}.usedCount` in a transaction | Firestore sustains about 1 write/s per document. If a school registers 300 students at once, transactions contend, retry and fail (students fall back to the payment gate) | Distributed counters (N shards) or a `redemptions` subcollection with `count()`; enforce `maxStudents` with sharded counters |
| P-05 | Big client bundles | Table above. Class 6/7 assessments import whole question JSON client-side (`app/Class6Assessment.tsx:7`). Large data modules (`lib/careers/careerLibrary930Plus.ts`, 1.7 MB) are imported by pages | Slow first load on mid-range Android over 4G, the main audience. Every 100 kB of JS adds roughly 0.3–1 s of parse and execute time on low-end phones (estimate) | `next/dynamic` for report, chart (`recharts`) and `three` sections. Move catalogues behind API routes or static JSON fetched on demand. Run `@next/bundle-analyzer` |
| P-06 | Stress benchmark reads up to 20k documents | `app/api/stress/benchmarks/route.ts:41`, cached 10 minutes **per instance** | Each cold instance re-reads up to 20k documents | Keep precomputed deciles in one document, updated on write or by a scheduled job |
| P-07 | Legacy local-mode store is not concurrency-safe | `lib/localMode/service.ts:162-408` does read-modify-write of JSON files in `os.tmpdir()` | Lost updates under concurrency. Data lives on one instance and disappears | Retire it, or move it to Firestore (it already falls through to Firestore when configured) |
| P-08 | SMTP for transactional mail | A new `nodemailer` transporter per call in 8 files. Mailbox-provider SMTP (Hostinger-style) has hourly send caps | Completion and alert mails get throttled or dropped in spikes (e.g. a school of 1,000 finishing in an hour) | A transactional provider (SES, Postmark, Resend) via a queue, with retries |
| P-09 | LLM provider limits | `lib/ai/llm.ts`. Per-user daily quotas exist (25/40/20), but nothing global | Groq and DeepSeek tokens-per-minute limits are hit long before Vercel limits. The result is 429s and 60 s function timeouts | A global concurrency limit and queue for AI calls, plus graceful "busy" responses and caching of identical prompts |
| P-10 | No error/latency monitoring | No Sentry or OTel. `@vercel/speed-insights` is present (client side only) | Regressions go unnoticed | See the deployment checklist |
| P-11 | Token verification is a network hop | `verifySignIn` → Identity Toolkit `accounts:lookup` | Adds roughly 100–300 ms to the first call per token per instance (estimate) | Acceptable. The alternative is local JWT verification with `jose` once runtime constraints allow |

## Scalability estimate (theoretical, not measured)
"Concurrent users" means users active at the same moment, doing student flows such as the assessment, dashboard and features.

| Concurrent users | Student flows | Institution / admin | Main risks |
|---|---|---|---|
| **100** | Comfortable: static pages on the CDN, functions autoscale, Firestore is far from its limits | Fine while total registered users are under ~5k | None significant |
| **500** | Expected OK | Portal slows linearly with total users (P-02). Admin dashboard degrades past ~5–10k registered users (P-01) | SMTP throttling in spikes (P-08) |
| **1,000** | OK for browsing and taking assessments. AI features start returning 429s at provider limits (P-09) | The admin dashboard is likely unusable with a large user base. Bulk school sign-up contends on one link document (P-04) | LLM limits, institutional hot doc, no rate limiting (M-04) leaves room for abuse |
| **5,000** | Needs P-01, P-02, P-04, P-08 and P-09 fixed plus rate limiting and the Next.js upgrade (DoS CVEs) | Not viable without P-01/P-02 | Firestore cost from full scans; provider limits; Vercel concurrency limits on the plan in use (check the plan) |

**Verdict:** For hundreds of concurrent students the architecture is basically sound. The serverless/CDN design scales well. The parts that **don't** scale are the admin and institution views and the bulk-registration counter. These do full collection scans or hit one document, so they degrade with *total registered users*, not with concurrency. Fix P-01, P-02 and P-04 before onboarding large schools.

## Recommended next measurements
1. `ANALYZE=true next build` with `@next/bundle-analyzer` to attribute the 747 kB on `/account`.
2. A k6 or Artillery test against a **staging** project, not production: the sign-up, assessment-scoring and portal flows at 100/500/1,000 virtual users.
3. Firestore usage dashboard: reads per day, attributed to `users` collection scans.
