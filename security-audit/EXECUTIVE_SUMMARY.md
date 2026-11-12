# Executive Summary — Security, Performance & Production-Readiness Audit

**Application:** OneGrasp Career Fitment (`mahendrabella1/careerfitment`, commit `bb0c7d8`)
**Date:** 2026‑11‑12
**Scope:** The full repository. Frontend, 78 API routes, Firestore and Storage rules, Supabase schema, payments, AI integrations, email, dependencies, build and CI, and git history (for secrets).
**Not in scope / not possible:** Production consoles (Firebase, Vercel, Razorpay, SMTP), live testing of the deployed site, and load testing. Findings that depend on those are marked *conditional*.

## Overall assessment
**Not ready for a public launch yet.** It can be made ready in days, not months.

The newer half of the codebase is well engineered: server-verified identity, no IDOR found, input normalisation and transactions. The older half trusts the browser for things that matter: payment status, results, certificates and outbound email. On top of that, one critical **operational** exposure has to be handled in the Firebase console today.

## Architecture overview
```
Browser (Next.js 14 App Router, React 18)
  ├─ Firebase Auth (email/password)  ──►  ID token
  ├─ Firestore client SDK  ──(firestore.rules)──►  users/*, owner-only feature data
  ├─ Firebase Storage      ──(storage rules: NOT in repo before this audit)──►  document vaults
  └─ fetch /api/*  ─────────────►  Vercel serverless functions (78 routes)
                                     ├─ token check: Identity Toolkit accounts:lookup
                                     ├─ Firestore Admin SDK (bypasses rules)
                                     ├─ Supabase (job portal; RLS on)
                                     ├─ Razorpay (orders + HMAC verify)
                                     ├─ Groq / DeepSeek LLMs (resume, interview, comm-lab, AI search)
                                     ├─ SMTP (nodemailer) + CRM webhook
                                     └─ Vercel Cron → /api/jobs/sync (CRON_SECRET)
```
**Sensitive data:** personal data of students, many of them **minors** (Class 6–12): name, phone, email, school, psychometric results, voice transcripts, and identity documents (marksheets, bank passbook, passport) in Storage. Payment metadata.
**Trust boundaries:** browser ↔ Firestore rules; browser ↔ API routes; the server ↔ third parties (LLMs receive student text and audio).

## Most dangerous issues
1. **C-01 — The admin password is public.** A plaintext admin credential for `support@onegrasp.com` sat in this **public** repo and in the production JS bundle, and the code created the real production admin account with it. If the live password matches it, anyone can sign in as admin and read every student's data. **Change it now.**
2. **C-03 — Anyone can mark themselves "paid"** from the browser console. Payment is client-controlled.
3. **H-01 — Open email relay.** Two unauthenticated routes sent OneGrasp-branded mail with any text and link to any address. This was a ready-made phishing tool.
4. **H-07 — Identity-document vault rules are unknown.** The Storage rules were never in source control.
5. **C-02 / H-02 / H-03** — the default admin token on the leads API, a free unmetered LLM proxy on your API key, and a public 100%-off coupon that also switched on during database outages.

## What was fixed in this engagement (all verified by tests)
| Fixed | How it was verified |
|---|---|
| Hardcoded admin credential, auto-create and bypass removed (C-01, code side) | Test fails on old code; build |
| `ADMIN_TOKEN` fails closed, constant-time compare (C-02) | Unit test |
| Email relays closed: sign-in required, recipient = verified email, server-side content (H-01) | Route tests (401), static tests |
| AI search requires sign-in, has a daily quota, and rejects client-supplied system messages (H-02) | Route + static tests |
| Payments recorded server-side and bound to one account; replays refused (H-04, part of C-03) | Transactional unit test |
| Coupon outage no longer enables the free code (H-03, part) | Unit test |
| Firestore create rule hardened (H-05) | **Emulator** tests 14/14; 3 fail on old rules; sign-up unaffected |
| Recommended Storage rules for the vaults, plus upload type filters (H-07) | **Emulator** tests 5/5 |
| Security headers: HSTS, nosniff, frame, referrer, permissions (M-01, part) | Config test |
| Protocol-relative open redirect (L-03) | Unit test |
| Typecheck green (it was red), CI workflow added (L-07) | `tsc` exit 0 |

**Totals:** 122/122 unit and security tests and 19/19 rules tests pass. The production build succeeds. All 106 pre-existing tests still pass.

## Production readiness
| Area | Rating | Notes |
|---|---|---|
| Authentication | Amber | Firebase Auth is solid. Admin is identified by an email string with no MFA; no email verification |
| Authorisation / IDOR | Green (APIs) / Amber (rules) | No IDOR found in server routes. Rules gaps remain on payment and progress fields |
| Payments | **Red → Amber** | Server-side record added. The lock-down needs approval |
| Data protection | **Red** until the C-01 rotation and Storage rules deploy |
| Dependencies | Amber | Next.js 14.2.35 has critical advisories; a major upgrade is needed |
| Performance (students) | Green | Static/CDN plus serverless scales |
| Performance (admin / schools) | Amber/Red | Full-collection scans grow with the user count |
| Observability / DR | Red | No error tracking, alerting or verified backups |
| Privacy (DPDP) | Red | No verifiable parental consent; Meta Pixel on a minors' site; no deletion flow. Needs legal review |

## Required before public launch (summary)
1. Rotate the admin password, enable MFA, review the logs (C-01).
2. Deploy `firestore.rules` and `storage.rules` (H-05, H-07).
3. Approve and complete the payment lock-down (C-03). Retire the public free coupon (H-03).
4. Rate-limit public endpoints (M-04). Set provider spend caps.
5. Error tracking, alerting, Firestore PITR and exports, and a tested restore.
6. DPDP: parental consent for minors, privacy notice, deletion and retention, and a review of the Meta Pixel. Get legal sign-off.
7. Schedule the Next.js upgrade (H-06).

See `REMEDIATION_TRACKER.md` for every item, `PRODUCTION_DEPLOYMENT_CHECKLIST.md` for the launch steps, and `SECURITY_TEST_REPORT.md` for the evidence.

> **Limitations.** This is a code-level assessment. It does not certify the application as secure or legally compliant. Console configuration, deployed rules and live behaviour were not visible. Residual risks are listed in `SECURITY_TEST_REPORT.md` §5.
