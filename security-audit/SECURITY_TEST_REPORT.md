# Security Test Report

**Environment:** a cloud sandbox with Node 22.23.4, npm 10.9.9 and Java (for the Firestore emulator v1.19.8).
**Not tested against:** any production system. No real accounts, payments or emails were used.

## 1. Baseline (original code, commit `bb0c7d8`)
| Check | Result |
|---|---|
| `npm run typecheck` | **FAIL**: 237 errors, all from `lib/newAssessment/class8Scoring.test.ts` (Jest globals, no Jest installed) |
| Existing unit suites (11) | **106 / 106 pass** (jobs 32, stress 14, progress 4, certificates 4, ai 3, commLab 8, startups 4, boosters 6, institution 3, jobready 14, aptitude 14) |
| `next build` | Pass. 257 routes; `/account` first-load JS 747 kB |
| `npm audit` (lockfile) | 1 critical, 10 high, 10 moderate, 1 low |
| Secret scan, working tree | 1 hardcoded admin password (`app/admin/layout.tsx:27`), plus public-by-design keys: Firebase web key ×3, Razorpay key ID ×1 |
| Secret scan, history (file names, 215 commits) | No `.env`, service-account, key or PEM files ever committed |

## 2. After remediation (branch `security/audit-remediation`)
| Check | Result |
|---|---|
| `npx tsc --noEmit` | **Pass** (exit 0) |
| `npm test` (all unit suites + security) | **122 / 122 pass** |
| `npm run test:security` | **16 / 16 pass** |
| Firestore rules on the emulator (`tests/rules/firestore.rules.spec.mjs`) | **14 / 14 pass** |
| Storage rules on the emulator (`tests/rules/storage.rules.spec.mjs`) | **5 / 5 pass** (owner-only, cross-user and anonymous denied, type and size limits, admin reads review proofs, default deny) |
| `next build` | **Pass**. Bundle sizes unchanged. The admin chunks no longer contain the account auto-create path |
| Existing behaviour | All 106 pre-existing tests still pass; the registration payload is still accepted by the rules |

### Proof that the tests detect the vulnerabilities (mutation check)
I reverted the fixed files to the original code and re-ran the security suite. **8 tests failed**: C-01, C-02, H-01 ×2, H-02 ×2, H-03, M-01. The scholarships route wasn't reverted in that run, so its tests correctly passed. I then restored the fixes.

I re-ran the rules tests against the **original** `firestore.rules`. **3 failed** (H-05 paid-on-create, privileged fields on create, forged uid on create). The other 11 passed, which confirms the existing protections work.

## 3. Test inventory
| Test | Covers | Type |
|---|---|---|
| C-01 admin layout has no hardcoded credential | Credential removal | Static |
| C-02 ADMIN_TOKEN guard | Fail-closed, old default refused, short token refused, constant-time compare accepts the right token | Unit |
| H-01 ×2 routes refuse unauthenticated callers | 401 with no token, even with `to` in the body | Route handler |
| H-01 ×2 recipient never from body | `to: who.email` only | Static |
| H-01 bearerIdentity | Scheme required, invalid token, verifier error fails closed | Unit |
| H-01 safeHttpUrl / plainText | `javascript:`/`data:` dropped; CRLF header-injection characters removed; length caps | Unit |
| H-02 AI search refuses unauthenticated callers | 401/503 with no token | Route handler |
| H-02 role filter + quota | Only user/assistant forwarded; `chargeDaily` called | Static |
| C-03 claimPayment | First claim writes `payments/` and `users.paid`; retry is idempotent; a replay from another uid is refused and doesn't mark the replayer paid | Unit (fake transactional DB) |
| C-03 ID formats | Path-like IDs rejected | Unit |
| H-03 coupon outage | Configured but failing Firestore → no 100% code offered | Unit (own process) |
| L-03 safeInternalPath | `//host`, `/\host`, absolute URLs, `javascript:` rejected | Unit |
| M-01 headers | All 5 headers on `/:path*`; microphone kept; `poweredByHeader` off | Config |
| H-05 static rules check | Create clause contains the new conditions | Static |
| Rules (emulator) ×14 | Registration OK; no paid-on-create; no privileged fields on create; no cross-user create/read/write (IDOR); no institution change after sign-up; coupons/settings closed; server-only collections closed; admin read; research profiles get vs list; reviews can't self-publish; owner-only records | Emulator |

## 4. Known gaps, deliberately asserted as current behaviour
These tests pass *because the gap exists*. They should be flipped to `assertFails` when the approved fix lands:
- **KNOWN GAP (C-03):** a student can update their own `paid` to `true`.
- **KNOWN GAP (M-03):** the admin rule accepts a token whose `email_verified` is false.

## 5. Not tested / remaining risk
- **No dynamic testing of the deployed site** (DAST, TLS configuration, live headers, rate limits). Run OWASP ZAP baseline against **staging**.
- **No load test.** Scalability figures are estimates (PERFORMANCE_AUDIT.md).
- **Deployed Firebase Storage rules** were not visible. A tested recommended `storage.rules` is now in the repo (H-07), but what is live today is unknown.
- **Console settings** were not visible: Auth providers, email enumeration protection, App Check, API key restrictions, Vercel env vars, Razorpay webhooks.
- Whether the production admin password equals the leaked one is **unknown**. I did not attempt a login, which would have been an unauthorised access attempt. Treat it as compromised.
- The `next` 14.x advisories remain until the framework upgrade.

## 6. How to re-run
```bash
npm ci
npm run typecheck
npm test
npm run test:security
# Rules (needs Java):
npm i -D firebase-tools@13 @firebase/rules-unit-testing@3 firebase@10
npm run test:rules
```
