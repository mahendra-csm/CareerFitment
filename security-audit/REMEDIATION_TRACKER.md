# Remediation Tracker

**Status key:**
- **Fixed** — code changed in this branch
- **Partial** — part of the fix is done; the rest is listed
- **Open** — not changed
- **Ops** — needs an action in a console or dashboard, which I can't do from code

**Verification key:**
- **Tested** — automated test, which also fails on the original code
- **Emulator** — Firestore rules test on the local emulator
- **Build** — production build succeeds
- **—** — not verified

Branch: `security/audit-remediation` (delivered as `security-audit/remediation.patch`).

| ID | Sev | Issue | Status | Verification | Owner action / next step |
|---|---|---|---|---|---|
| C-01 | Critical | Hardcoded admin password + auto-create/bypass | **Fixed** (code) / **Ops pending** | Tested, Build | **Rotate the `support@onegrasp.com` password now**, revoke its sessions, enable MFA, review access logs |
| C-02 | Critical | Default `ADMIN_TOKEN` → leads PII | **Fixed** | Tested | Set `ADMIN_TOKEN` (32+ random characters) only if `GET /api/leads` is needed |
| C-03 | Critical | Browser writes `paid` | **Partial** | Tested (claim logic), Emulator (gap documented) | **Approval needed:** lock the payment fields in the rules, make `/api/payment/redeem` write server-side, remove client `markPaid`. Precondition: `FIREBASE_*` admin credentials set in production |
| H-01 | High | Open email relay (2 routes) | **Fixed** | Tested, Build | Check whether the SMTP account sent unexpected mail (provider logs) |
| H-02 | High | Unauthenticated LLM proxy | **Fixed** | Tested | Review the Groq usage dashboard for abuse |
| H-03 | High | Public 100% coupon; fail-open fallback | **Partial** | Tested | **Ops:** retire or rotate the published free code; confirm the `coupons` collection is populated; then delete `freeCouponCode` from `lib/offer.ts` |
| H-04 | High | Payment replay across accounts | **Fixed** (where admin creds exist) | Tested | Confirm `FIREBASE_*` env vars are set in production |
| H-05 | High | `users` create allows privileged fields | **Fixed** (rules file) | Emulator (14/14; 3 fail on old rules) | **Ops: deploy `firestore.rules`** — the file alone changes nothing |
| H-06 | High | Vulnerable `next` 14.2.35, `nodemailer`, transitive deps | **Open** | `npm audit` | **Approval needed:** (1) `nodemailer` upgrade (low risk), (2) `firebase-admin` minor, (3) Next.js major upgrade on its own branch with full QA. Do not apply npm's `firebase@9.14.0` downgrade |
| H-07 | High | Storage rules for document vaults unknown / unversioned | **Fixed** (new `storage.rules`) / **Ops pending** | Emulator (5/5) | **Compare with console rules and deploy `firebase deploy --only storage` today** |
| M-01 | Medium | Security headers / CSP | **Partial** | Tested | Deploy, then add CSP in Report-Only (draft in checklist) |
| M-02 | Medium | Self-declared institution membership | **Open** | — | Design: link via code or school approval, store `institutionId` (also fixes P-02) |
| M-03 | Medium | Admin by email, no verified-email check or MFA | **Open** | Emulator (gap documented) | **Approval needed:** check the admin email is verified, then require `email_verified` + a custom claim |
| M-04 | Medium | No rate limiting | **Open** | — | Vercel WAF / Upstash on public POST routes; require an ID token on `/api/crm-lead` |
| M-05 | Medium | Certificates and results from client-written progress | **Open** | — | Server-side completion and assessment writes; lock `progress`/`latestAssessment` |
| M-06 | Medium | No email verification | **Open** | — | `sendEmailVerification`; enable email-enumeration protection |
| M-07 | Medium | Legacy assessment/lead API open; `/tmp` store | **Open** | — | Retire it if unused by the current exam flow |
| M-08 | Medium | No App Check | **Open** | — | Enable in monitor mode, then enforce |
| L-01 | Low | Error detail leakage | **Partial** | Tested (AI search) | Generic errors in the legacy routes |
| L-02 | Low | `javascript:` href in research sources | **Open** | — | Validate with `safeHttpUrl` on save and render |
| L-03 | Low | Protocol-relative open redirect | **Fixed** | Tested | — |
| L-04 | Low | Two lockfiles, invalid pnpm config | **Open** | — | Pick one package manager |
| L-05 | Low | `xlsx` (dev) vulnerable | **Open** | — | Replace or remove |
| L-06 | Low | 5-minute token cache | Accepted | — | Document |
| L-07 | Low | No CI; red typecheck | **Fixed** | `tsc` exit 0, CI file | Enable branch protection requiring the `CI / check` job |
| L-08 | Low | Config logged to the console | **Open** | — | Remove the line |
| P-01 | Perf | Admin downloads all users | **Open** | — | Paginated server API |
| P-02 | Perf | Portal full scan per request | **Open** | — | `institutionId` index |
| P-04 | Perf | Hot counter on bulk sign-up | **Open** | — | Sharded counter |
| P-08 | Perf | SMTP limits | **Open** | — | Transactional provider + queue |
| P-09 | Perf | LLM provider limits | **Open** | — | Global AI concurrency limit |

## Proposed order of the remaining work
1. **Today (ops):** C-01 rotation, H-05 Firestore rules deploy, H-07 Storage rules check and deploy, H-03 code retirement, check that `FIREBASE_*` and `ADMIN_TOKEN` are set.
2. **This week (approval):** C-03 lock-down, M-03, `nodemailer`/`firebase-admin` updates, M-04 rate limits on the listed routes.
3. **Before scaling to large schools:** M-02 + P-02, P-01, P-04, M-05.
4. **Planned upgrade:** Next.js major (H-06), CSP enforcement, App Check.
