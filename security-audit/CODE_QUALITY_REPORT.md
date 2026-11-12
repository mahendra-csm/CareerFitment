# Code Quality & Architecture Report

## Architecture summary
- **Stack:** Next.js 14 App Router (React 18, TypeScript strict), Firebase Auth and Firestore (client SDK under rules plus Admin SDK in API routes), Supabase Postgres for the job portal, Razorpay, Groq/DeepSeek LLMs, SMTP via nodemailer, Vercel hosting and cron.
- **Size:** about 720 TS/TSX files, 78 API routes, roughly 2,900 JSON data files, and 102 MB of `public/` assets.
- **Two generations of code live side by side:**
  - **Newer modules** (institution portal, portfolio, certificates, Communication Lab, jobs, aptitude) are consistent. They use server-verified identity (`caller()`/`requireInstitution()`), input normalisation, small pure modules, and unit tests.
  - **Older modules** (legacy assessment engine, `/api/ai/search`, alerts, payment gate) trust the client. Comments even claim "this app has no server-side auth anywhere", which is no longer true.

## Findings

| ID | Issue | Evidence | Recommendation | Priority |
|---|---|---|---|---|
| Q-01 | Inconsistent trust model | Client writes `paid`, `progress`, `latestAssessment` while newer features write server-side | Adopt one rule: **anything another party relies on is written by the server**. Track the migration in REMEDIATION_TRACKER | High |
| Q-02 | Duplicated identity code with a hardcoded API key | Token lookup is implemented 3 times: `lib/firebaseIdentity.ts`, `lib/firebase/adminAuth.ts`, and inline in `app/api/admin/send-report/route.ts:14-35`. The web API key is hardcoded in 3 files | One `lib/security/requestAuth.ts`-style helper (started in this audit); read the key from `NEXT_PUBLIC_FIREBASE_API_KEY` | Medium |
| Q-03 | Duplicated SMTP setup | `createTransport` appears in 8 files with slightly different host parsing | One `lib/mail.ts` with a pooled transporter and one send function | Medium |
| Q-04 | Probably dead data modules | `lib/data/careerLibrary930{Accurate,Complete,Full,Verified}.ts`, `lib/careers/CAREER_LIBRARY_930_COMPLETE.ts`, `internships150Plus.ts`, `industryCareerData.ts`, `careerCompatibilityMatrix.ts` have no direct importers (grep) | Confirm with `ts-prune`/`knip`, then delete. This shrinks the repo, the typecheck and the cognitive load | Medium |
| Q-05 | Very large components | `app/assessment-experience.tsx` (2,320 lines), `app/account/Dashboard.tsx` (2,014), `Class6Report.tsx`/`Class7Report.tsx` (1,939 each, near-duplicates), `FullReport.tsx` (1,674) | Split by section; share one report shell between Class 6/7 | Medium |
| Q-06 | No error boundaries | No `app/error.tsx`, `app/global-error.tsx` or `app/not-found.tsx` | Add them, so a render error shows a recoverable screen and is reported (Sentry) | Medium |
| Q-07 | Inconsistent API response shapes | `{success,message,statusCode,data}` in legacy routes, `{error}` in newer ones, `{success,error}` in others | Standardise on one shape (the newer `ApiError`/`fail()` pattern) | Low |
| Q-08 | Raw error messages returned | See SECURITY L-01 | Log server-side; return generic text | Low |
| Q-09 | Inline CSS via `dangerouslySetInnerHTML` (about 40 places) | Static strings (safe today), but it blocks a strict CSP (`style-src` would need `'unsafe-inline'`) | Move to CSS modules or `globals.css` over time | Low |
| Q-10 | Repository hygiene | 21 status/summary `.md` files at the root (some stale, e.g. `DEPLOYMENT_READY.md`), `server-manual.js` (a stray HTTP server), `scratch/`, `DASHBOARD_PREVIEW.html`, `.xlsx` source sheets and a `.ps1` script at the root | Move docs to `docs/`, delete the stray server and scratch files, keep data sources in `data/raw/` | Low |
| Q-11 | Two package managers | `package-lock.json` and `pnpm-lock.yaml`; `pnpm-workspace.yaml` holds placeholder text | Choose one; delete the other lockfile | Low |
| Q-12 | Typecheck was red | An orphaned Jest test (`lib/newAssessment/class8Scoring.test.ts`) with no Jest installed: 237 errors | **Fixed** (excluded). Either port it to `node:test` or delete it | Done |
| Q-13 | No CI | No `.github/` | **Fixed**: `.github/workflows/ci.yml` | Done |
| Q-14 | Outdated or misleading security comments | `app/api/startups/grade/route.ts:5`, `app/api/exams/send-alert` (old), `app/api/payment/verify/route.ts:10-13` | Updated where code changed; update the rest | Low |
| Q-15 | Production `console.log` | `lib/firebase/client.ts:52` | Remove | Low |

## What is good
- `strict` TypeScript and a clean typecheck (after Q-12).
- Clear module comments explaining *why*.
- Pure, testable scoring and logic modules with 106 existing tests.
- Consistent input normalisation in the newer server modules (`lib/portfolio/server.ts`, `lib/boosters/catalog.ts`).
- Transactions where they matter (certificate issuance, institutional redeem, AI quota).

## Suggested order
Q-01 (with C-03 and M-05), Q-02/Q-03 (small, reduce attack surface), Q-06, Q-04, Q-05, then the rest.
