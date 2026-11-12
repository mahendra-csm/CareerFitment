# Security Audit Report — OneGrasp Career Fitment

**Scope:** `mahendrabella1/careerfitment` at commit `bb0c7d8` (default branch, 2026‑11‑12), all 215 commits of history (for secrets).
**Method:** Manual code review of every API route (78 `route.ts` files) and every auth, data-access and payment module, review of `firestore.rules` and the Supabase migration, automated secret scan of the working tree and the history's file list, `npm audit`, a production build, and tests (unit tests plus Firestore rules on the local emulator).
**Not done:** No testing against production, no live login attempts, no dynamic scanning (DAST) of the deployed site, and no review of Firebase, Vercel, Razorpay or SMTP console settings. I could not see those settings, so findings that depend on them are marked **conditional**.
**Standards:** OWASP Top 10 (2021), OWASP API Security Top 10 (2023).

Secret values are never reproduced in this report. Findings list only the file, the line and the type of secret.

---

## Severity summary

| ID | Title | Severity | Status |
|---|---|---|---|
| C-01 | Hardcoded admin password in public repo and client bundle | **Critical** | Code fixed. **Password rotation is still required** |
| C-02 | Default `ADMIN_TOKEN` exposes all leads (PII) | **Critical** (conditional) | Fixed and tested |
| C-03 | Payment status is written by the browser (`paid` flag) | **Critical** | Partly fixed. Rule lock-down awaits approval |
| H-01 | Open email relay on the company SMTP account (2 routes) | High | Fixed and tested |
| H-02 | Unauthenticated, unmetered LLM proxy with system-prompt injection | High | Fixed and tested |
| H-03 | Public 100%-off coupon code, and the fallback turned it on during an outage | High | Partly fixed. The code must be retired |
| H-04 | One payment signature could be replayed across any number of accounts | High | Fixed and tested (needs admin credentials set) |
| H-05 | `users/{uid}` create rule allows privileged fields (forged certificates, forged parent consent, pre-paid) | High | Fixed in rules and emulator-tested. **Must be deployed** |
| H-06 | Vulnerable framework and dependencies (Next.js 14.2.35 and others) | High | Open. Needs a major upgrade (approval) |
| H-07 | Storage rules for identity-document vaults not in the repo; no upload type/size limits | High (conditional) | Recommended `storage.rules` written and emulator-tested. **Must be compared and deployed** |
| M-01 | Missing HTTP security headers / no CSP | Medium | Partly fixed (no CSP yet) |
| M-02 | Institution membership is self-declared | Medium | Open (design change) |
| M-03 | Admin = an email string; no verified-email check, no MFA, no role claim | Medium | Open (approval) |
| M-04 | No rate limiting on public endpoints | Medium | Open (infrastructure) |
| M-05 | Certificates and assessment results come from client-written data | Medium | Open (design change) |
| M-06 | No email verification at sign-up | Medium | Open |
| M-07 | Legacy assessment/lead API is open and keeps data in `/tmp` on serverless | Medium | Open |
| M-08 | No Firebase App Check | Medium | Open |
| L-01 | Internal error details returned to clients | Low | Partly fixed (AI search) |
| L-02 | Research source links rendered without a scheme check (self-XSS) | Low | Open |
| L-03 | Protocol-relative open redirect in institution message links | Low | Fixed and tested |
| L-04 | Two lockfiles, and an invalid pnpm workspace config | Low | Open |
| L-05 | `xlsx` (dev only) has unfixed prototype pollution | Low | Open |
| L-06 | ID tokens cached by value for 5 minutes, so revocation is delayed | Low | Open (accepted) |
| L-07 | No CI; `npm run typecheck` was failing | Low | Fixed |
| L-08 | Firebase config is logged to the console on every page load | Low | Open |
| I-01…I-05 | Informational / things done well | Info | — |

---

## Critical

### C-01 — Hardcoded admin password in a public repository and the production JS bundle
- **File:** `app/admin/layout.tsx:27` (original). It held a `DEV_ADMIN` object with an email and a plaintext password; lines 40‑75 held the sign-in, auto-create and bypass logic.
- **Explanation:** The admin login form shipped a hardcoded password for `support@onegrasp.com`. When sign-in failed with "user not found", the code called `createUserWithEmailAndPassword` with that password. This *creates the real Firebase admin account* in whatever project the client is configured for, and `lib/firebase/client.ts` hardcodes the **production** project (`careerfitment`). A UI-only bypass then showed the admin shell. The bypass is disabled when `NODE_ENV === "production"`, but:
  1. the repository is **public**, so the password is public;
  2. `DEV_ADMIN` is referenced outside the guarded branch, so the string is also compiled into the production client bundle;
  3. if the production admin was ever bootstrapped through this path (for example by running `next dev` locally, which talks to production Firebase), **the live admin password is the public one**.
- **Exploitation:** Anyone can sign in at `/admin` as `support@onegrasp.com`. Firestore rules then grant `isAdmin()`: read and write every `users/*` document (names, phones, emails, assessment results), every coupon, payment settings and institutional link. The server routes `requireAdmin` and `send-report` also accept the account.
- **Business impact:** Full breach of student PII (minors included). The attacker could turn payments off, mint free coupons, and email reports anywhere. Under the DPDP Act this would be a reportable personal-data breach.
- **Remediation (done in code):** Removed the credential, the auto-create path and the bypass. The login is now real Firebase sign-in only.
- **Remediation (operator, required, NOT done by me):**
  1. **Immediately change the password** of `support@onegrasp.com` in Firebase Authentication. Then revoke its sessions (Firebase console → Users → disable/enable, or set `validSince`).
  2. Turn on MFA for the account (Identity Platform) and use a dedicated admin mailbox.
  3. Check Firebase Auth logs and Firestore usage for admin-scope reads from unknown IPs since the commit that added `DEV_ADMIN`.
  4. Removing the password from code does **not** remove it from git history or forks. Rotation is the only real fix.
- **Test:** `tests/security/security.test.mjs` → "C-01 …". This asserts there is no credential, no `createUserWithEmailAndPassword` and no bypass in the file. It fails on the original code.

### C-02 — Default admin token exposes every lead (conditional on `ADMIN_TOKEN` being unset)
- **File:** `lib/adminAuth.ts:4` (original) — `process.env.ADMIN_TOKEN || "<public default>"`. Used by `GET /api/leads` (`app/api/leads/route.ts:23`).
- **Explanation:** If `ADMIN_TOKEN` is not set on the deployment, the expected token is a string published in the repository. `ADMIN_TOKEN` is **not** listed in `.env.example`, which makes it likely that it is unset.
- **Exploitation:** `curl -H "Authorization: Bearer <public default>" https://<site>/api/leads` returns every lead: name, email, phone, city, age and UTM data (from Firestore `leads` when admin credentials are configured).
- **Fix (done):** The guard fails closed. It needs `ADMIN_TOKEN` set to at least 24 characters and compares tokens in constant time via SHA‑256 digests. With the variable unset, every request is refused.
- **Test:** "C-02 …". This checks that the old default is refused, an unset or short token is refused, and the correct token is accepted. It fails on the original code.
- **Operator action:** If `GET /api/leads` is needed, set `ADMIN_TOKEN` to a random value of 32 or more characters. Review whether this endpoint has been called (Vercel logs).

### C-03 — Payment state is controlled by the browser
- **Files:** `app/PaymentGate.tsx:214-221` (`markPaid` → `setDoc(users/{uid}, { paid: true … })`); `firestore.rules:45-49` (a TODO that admits it); `app/assessment-experience.tsx:1096` (the gate checks `profile.paid` client-side); `app/api/payment/verify/route.ts` (originally stored nothing).
- **Explanation:** `paid` is a field the student can write on their own profile, and the paid assessment is gated only in the browser.
- **Exploitation:** In the devtools console on any signed-in page: `setDoc(doc(db,"users",uid),{paid:true},{merge:true})`. The paid assessment and report then unlock. Emulator test "KNOWN GAP (C-03)" shows the rule allows this today.
- **Impact:** Direct revenue loss, and payment records in Firestore and the CRM can't be trusted.
- **Fix (done, additive, non-breaking):** `lib/payments/claim.ts` plus `app/api/payment/verify/route.ts`. After the Razorpay HMAC check, the server binds the payment to the signed-in uid in a transaction (`payments/{paymentId}`). It writes `paid` and the related fields with the Admin SDK and sets `paymentVerifiedBy: "server"`.
- **Fix (pending your approval, could break things):**
  1. Add `paid`, `paymentStatus`, `paidAt`, `paymentId`, `amountPaid` and `couponCode` to `adminOnlyUserFields()` in `firestore.rules`.
  2. Make `/api/payment/redeem` write the waiver with the Admin SDK, as `/api/institutional/redeem` already does.
  3. Remove the client `markPaid` writes and have the gate re-read the profile.
  4. Ideally, also check `paid` server-side in `/api/new-assessment/score`.

  **Why approval is needed:** these steps make payment depend on `FIREBASE_*` admin credentials being set in production. Without them, paying students would be locked out. Confirm the credentials are present before deploying.

---

## High

### H-01 — Open email relay (`/api/exams/send-alert`, `/api/scholarships/send-alert`)
- **Files (original):** `app/api/exams/send-alert/route.ts:10-20`, `app/api/scholarships/send-alert/route.ts:5-15`. The comment said "no server-side auth check (this app has none anywhere)".
- **Explanation:** Unauthenticated POST with `to`, `message` and `officialUrl` taken from the body, sent with the company SMTP account as "OneGrasp", reply-to support@.
- **Exploitation:** `POST {to:"victim@x", examName:"Your account", message:"Verify your payment", officialUrl:"https://phish.example"}` sends a phishing mail from OneGrasp's real mailbox, which passes SPF and DKIM. It can be scripted for spam.
- **Impact:** Brand-damaging phishing, the domain blacklisted, the SMTP provider suspending the account (which breaks every transactional email), and legal exposure.
- **Fix (done):** A Firebase ID token is required. The recipient is the verified account email. The exam or scholarship is looked up by slug in server data, which supplies the name and link. The message is plain text capped at 200 characters. The two client callers were updated to send `Authorization: Bearer`, the slug and the message.
- **Tests:** "H-01 …" checks that unauthenticated requests get 401, that `body.to` is never read, and covers URL and text sanitisation. Both fail on the original code.

### H-02 — Unauthenticated LLM proxy (`/api/ai/search`)
- **File:** `app/api/ai/search/route.ts:51-108` (original).
- **Explanation:** No sign-in. The quota was a hardcoded `7` that was never decremented. The client's `messages` array, including `role:"system"` entries, was forwarded to Groq after the server's system prompt. Upstream error text was echoed back.
- **Exploitation:** A loop of POSTs uses OneGrasp's Groq account as a free general-purpose LLM, and injected system messages remove the guardrails.
- **Impact:** Unbounded API cost or quota exhaustion, which takes down the Communication Lab and interview features that share the key. Abuse is also attributed to OneGrasp.
- **Fix (done):** A signed-in caller is required (`caller()`). Each user gets 20 calls a day via `chargeDaily` in a transaction. Only `user` and `assistant` turns are forwarded (the last 10, at most 2,000 characters each). The question is capped at 1,000 characters. The client gets a generic error. (The UI component `AIEducationAssistant` isn't mounted anywhere, so no user flow changes; it now sends the token anyway.)
- **Tests:** "H-02 …".

### H-03 — Public 100%-off coupon; the fallback failed open
- **Files:** `lib/offer.ts:47` (`freeCouponCode`, imported by client components `app/PaymentGate.tsx` and `app/OfferBanner.tsx`, so it is in the bundle); `lib/coupons.ts:47-62, 88-91`.
- **Explanation:** When the `coupons` collection is empty, unreadable, or there are no admin credentials, `FALLBACK_COUPONS` (which includes the 100% code) is used. The code is public in the repo and in the JS bundle.
- **Exploitation:** Enter the code during any Firestore incident (or on a deployment without admin creds) to get the paid assessment free via `/api/payment/redeem`. Combined with C-03 this works anyway.
- **Fix (done):** A Firestore **error** no longer falls back to any 100%-off code (test "H-03 …", which fails on the original code).
- **Still to do (operator):** Rotate or retire the published free code. Keep real codes only in `/admin/coupons`. Remove `freeCouponCode` from `lib/offer.ts` once the admin-managed coupons are confirmed in production.

### H-04 — Payment signature replay across accounts
- **File:** `app/api/payment/verify/route.ts` (original lines 41-81).
- **Explanation:** A valid `(order_id, payment_id, signature)` triple proved that *a* payment happened, but it wasn't tied to an account or recorded. With C-03 in place, one real payment could unlock any number of accounts, and each replay fired CRM "paid" events.
- **Fix (done):** `claimPayment` creates `payments/{paymentId}` once. The same uid retrying gets an idempotent success. A **different** uid gets `409 "This payment has already been used."` The IDs are format-validated. Test "C-03 claimPayment …" uses a fake transactional DB.
- **Limit:** This runs only where `FIREBASE_*` admin credentials are configured. Elsewhere behaviour is unchanged.

### H-05 — `users/{uid}` create rule allowed privileged fields
- **File:** `firestore.rules:58-59` (original).
- **Explanation:** `adminOnlyUserFields()` was enforced on *update* only. On *create*, a student could write `certificates` (forged certificate references), `decision.parentResponse` (a forged "parents agree"), `testDrives`, `boosterRequests`, `institutionalLinkCode`, `paid:true`, or a `uid` field naming someone else.
- **Fix (done in `firestore.rules`):** On create, `paid` must be false or absent, `uid` must match, and the server-only fields are forbidden. `institution` stays allowed because the sign-up form sets it. **The rules must be deployed** (`firebase deploy --only firestore:rules` or the console). Editing this file changes nothing in production on its own.
- **Tests:** `tests/rules/firestore.rules.spec.mjs` runs on the Firestore emulator: 14 tests, all passing. Three of them fail against the original rules, and the registration payload still succeeds (no regression).

### H-06 — Vulnerable framework and dependencies
`npm audit` on `package-lock.json`: **1 critical, 10 high, 10 moderate, 1 low**.

| Package (installed) | Severity | Advisories (examples) | Fix |
|---|---|---|---|
| `next` 14.2.35 | Critical | GHSA-ggv3-7p47-pfv8 (request smuggling in rewrites), GHSA-h25m-26qc-wcjf (RSC deserialization DoS), GHSA-9g9p-9gw9-jx7f (image optimizer DoS) | Major upgrade (npm suggests 16.x). Breaking: App Router API changes, async `params`, React 19 |
| `nodemailer` 9.x | High | GHSA-wmmp-3585-3rmp (IDN allow-list bypass), GHSA-2x7j-588g-ccc2 (address-parser DoS), GHSA-8m3c-c648-2xjj | Upgrade to the patched line; low risk because the API is stable |
| `postcss`, `source-map-js`, `brace-expansion`, `re2js`, `@grpc/grpc-js` | High | DoS and info-disclosure classes | Transitive. Mostly fixed by upgrading `next` and `firebase-admin` |
| `xlsx` 0.18.5 (dev) | High | GHSA-4r6h-8v6p-xvw6 (prototype pollution), ReDoS | No npm fix. Only used by local scripts. Switch to the SheetJS CDN build or drop it |
| `firebase` / `@firebase/firestore` | High (flagged) | npm proposes "fix: firebase@9.14.0", a *downgrade* | Likely an advisory-range artefact. **Do not downgrade.** Re-check after updating `firebase` |
| `firebase-admin` ≤14.3 | Moderate | via `@google-cloud/storage`, `gaxios`, `uuid` | Minor update |

Not applied: framework upgrades are breaking and need a full regression pass and your approval. A plan is in `REMEDIATION_TRACKER.md`.

### H-07 — Identity-document vaults with no Storage rules in source control (conditional)
- **Files:**
  - `lib/scholarships/clientVault.ts:33-38` — `scholarshipVault/{uid}/…` holds marksheets, the Aadhaar-seeded bank passbook, income and domicile certificates and photos.
  - `lib/studyAbroad/clientVault.ts:29-31` — `studyAbroadVault/{uid}/…` holds passports, transcripts and financial documents.
  - `lib/studyAbroad/clientReviews.ts:60` — `reviewVerification/{uid}/…`.

  `lib/firebase/client.ts:86-91` says the rules "must be set on the Firebase console". The repository has no `storage.rules`. The upload inputs accept any file type and size.
- **Risk:** If the deployed rules are the default test-mode rules, or simply `request.auth != null`, any signed-in user can list and download every student's identity documents. That is a severe DPDP breach involving minors' data. I **could not check the deployed rules**.
- **Fix (done, needs deploying):** A new `storage.rules`:
  - owner-only read and create on each vault folder;
  - admins can read review proofs;
  - files must be PDF, image or Word, under 10 MB;
  - no overwrites;
  - everything else denied.

  Also new: `firebase.json` (so `firebase deploy --only storage` uses it), and `accept` filters on both vault inputs. Emulator tests: `tests/rules/storage.rules.spec.mjs`, 5 of 5 pass.
- **Operator:** Compare the console rules with this file today, deploy, and check Cloud Storage access logs if the old rules were permissive. `getDownloadURL` links already handed out keep working until each file's token is revoked.

---

## Medium

### M-01 — Missing HTTP security headers
- `next.config.js` set only cache headers.
- **Done:** `Strict-Transport-Security` (2 years, includeSubDomains), `X-Content-Type-Options`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy`, a `Permissions-Policy` that keeps camera and microphone for this origin (voice features), and `poweredByHeader: false`. Test "M-01".
- **Open:** Content-Security-Policy. The app loads the Meta Pixel, Razorpay Checkout, Vercel Analytics, Firebase, YouTube embeds, and uses inline `<style>`. Roll the CSP out as `Content-Security-Policy-Report-Only` first; a draft is in the deployment checklist.

### M-02 — Institution membership is self-declared
- `lib/auth/AuthProvider.tsx:349` stores the free-text `institution` at sign-up. `lib/institution/server.ts:142-152` (`studentsOf`) links any user whose `institution` matches a school's name or alias.
- **Impact:** Anyone can register as "<School name>". They then get that school's broadcast messages and opportunity links (`/api/student/messages`), and they appear in the school's portal and analytics. A school also sees the profile data of anyone who typed its name.
- **Fix:** Link students only via `institutionalLinkCode` (the redeem flow already writes it server-side) or school approval, and store an `institutionId`. That also fixes the performance problem in `PERFORMANCE_AUDIT.md` P-02.

### M-03 — Admin authorisation is an email string
- `firestore.rules:13-16` and `lib/auth/admins.ts`. There is no `email_verified` check (emulator test "KNOWN GAP (M-03)"), no MFA, no role claim, and a single shared mailbox.
- **Fix:** Use a custom claim `admin:true` set via the Admin SDK, require `request.auth.token.email_verified == true` and MFA. **Needs approval:** this locks admins out if the admin account's email isn't verified. Check that first.

### M-04 — No rate limiting
Unauthenticated, unthrottled endpoints:
- `POST /api/crm-lead` sends a CRM push and an internal email per call, so it can flood the CRM and the team inbox.
- `POST /api/leads`
- `POST /api/payment/coupon` allows coupon guessing.
- `GET /api/institutional/check` allows guessing institutional codes (4–32 characters `[A-Z0-9-]`).
- `POST /api/new-assessment/score` (CPU)
- `POST /api/money/grade-scam` and `/api/startups/grade`

Serverless instances make in-memory limits useless. **Fix:** Vercel WAF rate-limit rules, or Upstash/Redis sliding-window limits on these paths. Require an ID token on `/api/crm-lead`; the client has one straight after sign-up.

### M-05 — Results and certificates trust client-written progress
- `lib/certificates/server.ts:32-55` issues a public certificate from `users/{uid}.progress.courses.*` and the `startups*Progress` collections. The owner writes these (`firestore.rules:166-187`; `users` update allows `progress`).
- `latestAssessment` (the scores schools and parents see) is also written by the browser (`AuthProvider.tsx:416`).
- **Impact:** Forged "verified" certificates and assessment results.
- **Fix:** Write completion and assessment results server-side (the scoring route already computes them), and add `progress` and `latestAssessment` to the admin-only fields.

### M-06 — No email verification at sign-up
`register()` never calls `sendEmailVerification`, and `/api/assessment/completion-email` sends to any unverified address. **Fix:** Send a verification email, and enable *Email enumeration protection* in Firebase Auth. (I can't see whether that setting is on.)

### M-07 — Legacy assessment and lead API
`/api/assessment/*`, `/api/report/[sessionId]` and `PATCH /api/leads` are unauthenticated. The session UUID is the only key, and the report returns the lead's name and email. Locally the data is kept in `os.tmpdir()` JSON files on serverless (`lib/localMode/service.ts:162`), so it is lost and inconsistent across instances. **Fix:** Retire the legacy flow if `NewExam` has replaced it, or require sign-in.

### M-08 — No Firebase App Check
Any script holding the public web config can call Firebase Auth and Firestore directly. Rules are the only barrier. **Fix:** Enable App Check (reCAPTCHA Enterprise) for Firestore, Storage and Auth, monitor first, then enforce.

---

## Low

- **L-01 Error detail leakage.**
  - `app/api/assessment/*` returns raw `err.message` and Supabase error text.
  - `lib/institution/server.ts:63-67` puts project IDs in 503 messages.
  - `app/api/admin/seed/route.ts:31` returns the error message.
  - Fixed for `/api/ai/search`. Recommend generic messages plus server-side logging.
- **L-02 Self-XSS via `href`.** `app/account/research/projects/[id]/sources/page.tsx:38` renders a user-entered `s.url` as an `href` with no scheme check (`javascript:` executes on click). Only the owner sees it today. Validate with `safeHttpUrl`.
- **L-03 Open redirect (fixed).** `app/api/institution/messages/route.ts:75` accepted `//evil.example`. It now uses `safeInternalPath` (test "L-03").
- **L-04 Lockfiles.** `package-lock.json` and `pnpm-lock.yaml` both exist, so the build tool picks one and they can drift. `pnpm-workspace.yaml` contains placeholder text (`set this to true or false`). Keep one package manager.
- **L-05 `xlsx`.** See H-06.
- **L-06 Token cache.** `lib/firebase/adminAuth.ts:28-51` caches verified tokens for up to 5 minutes per instance, so a disabled account keeps access for up to 5 minutes. Accepted trade-off; document it.
- **L-07 No CI / failing typecheck (fixed).** Added `.github/workflows/ci.yml` (typecheck, tests, audit; `contents: read`). `tsconfig.json` now excludes the orphaned Jest-style `*.test.ts`, which had 237 type errors.
- **L-08 Console logging.** `lib/firebase/client.ts:52` logs the Firebase configuration on every page load. Remove it.

## Informational / done well
- **I-01** Firebase web API key, Razorpay **key ID** and the Supabase anon key in the code are public by design. They are not secrets. Restrict the web API key to your domains in Google Cloud.
- **I-02** Newer routes are written well. Portfolio, milestones, student messages, institution portal, certificates and Communication Lab verify tokens, derive the uid server-side (no IDOR found), validate input lengths and use per-user AI quotas.
- **I-03** Razorpay HMAC and the cron secret use `timingSafeEqual`. The institutional-link redemption is a race-safe transaction.
- **I-04** The Supabase job tables have RLS enabled, with a single public `select` policy on active jobs. Job URLs are forced to `https:`.
- **I-05** No credential files (`.env`, service-account JSON, keys) appear anywhere in git history. The `GROQ_API_KEY` value in `.env.example` history is a placeholder.
