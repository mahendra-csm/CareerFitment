# Fix All Audit Issues: Instructions for Claude Code (VS Code)

> **How to use this file**
> 1. Open the **application repository** (`mahendrabella1/careerfitment`) in VS Code.
> 2. Copy this whole `security-audit/` folder (this file, the reports, `remediation.patch` and `files/`) into the root of that repository.
> 3. Open Claude Code and say:
>    **"Read `security-audit/FIX_ALL_ISSUES.md` and follow it step by step."**
>
> Claude stops at every 🛑 **APPROVAL GATE** and waits for you to answer.

---

## 0. Instructions to Claude: read these first

You are fixing the issues found in a security, performance and code-quality audit of this Next.js 14 + Firebase app. The full findings are in `security-audit/SECURITY_AUDIT_REPORT.md`, `PERFORMANCE_AUDIT.md`, `CODE_QUALITY_REPORT.md` and `REMEDIATION_TRACKER.md`. Read those and the repo's own `CLAUDE.md` before changing code.

**Rules for the whole task:**
- Work on a branch: `git checkout -b security/audit-remediation`. Never commit to `main` and never push without being asked.
- Preserve existing behaviour and business logic. Change the minimum needed for each fix.
- After **every** phase, run:
  ```bash
  npm run typecheck
  ```
  ```bash
  npm test
  ```
  Both must pass before you continue. Never skip, disable or weaken a test to make it pass.
- Every security fix needs a regression test in `tests/security/` (node:test, same style as the existing ones). Where possible, confirm the test **fails** on the old code.
- **Never** print, copy or commit secrets. In particular, never search for or reproduce the old admin password from git history.
- **Never** run anything against production. No `firebase deploy`, no live API calls, no real payments or emails, unless the user explicitly says so in this chat.
- Stop at each 🛑 APPROVAL GATE, explain what will change and what could break, and wait.
- After each phase, tick the boxes in this file and update `security-audit/REMEDIATION_TRACKER.md` (Status and Verification columns).
- If something in the code doesn't match what this file describes, stop and tell the user. Don't guess.

---

## Phase 1: Apply the already-verified fixes

These fixes were written and tested during the audit (122 of 122 tests and 19 of 19 emulator rule tests passed).

- [ ] **1.1** Check the repo is at, or close to, commit `bb0c7d8`:
  ```bash
  git log --oneline -3
  ```
- [ ] **1.2** Try applying the patch:
  ```bash
  git apply --check security-audit/remediation.patch && git apply security-audit/remediation.patch
  ```
  ```bash
  cp security-audit/files/app/admin/layout.tsx app/admin/layout.tsx
  ```
  If `git apply --check` fails (the code has moved on since the audit), **don't force it**. Implement items 1.3 to 1.13 by hand from the descriptions below, and use the patch only as a reference (`git apply --reject` and inspect the `.rej` files).
- [ ] **1.3 C-01: hardcoded admin credential.** `app/admin/layout.tsx` must contain no `DEV_ADMIN`, `DEV_BYPASS_ENABLED`, `bypass` state or `createUserWithEmailAndPassword`. The login is plain `signIn(email, password)`, and the password field starts empty.
- [ ] **1.4 C-02: admin token.** `lib/adminAuth.ts` has no hardcoded fallback. It refuses every request when `ADMIN_TOKEN` is unset or shorter than 24 characters, and compares SHA-256 digests with `timingSafeEqual`.
- [ ] **1.5 H-01: email relay.**
  - `app/api/exams/send-alert/route.ts` and `app/api/scholarships/send-alert/route.ts` require `Authorization: Bearer <Firebase ID token>`, through `bearerIdentity()` in the new `lib/security/requestAuth.ts`.
  - The recipient is the verified token email, never `body.to`.
  - The exam or scholarship is looked up by `examSlug` / `scholarshipSlug` in server data (`data/exams/exams.ts`, `data/scholarships/scholarships.ts`). The link goes through `safeHttpUrl()`, and the message through `plainText(…, 200)`.
  - Callers in `components/exams/ExamsHomeClient.tsx` and `components/scholarships/ScholarshipsHomeClient.tsx` send the ID token, the slug and the message.
- [ ] **1.6 H-02: AI search.** `app/api/ai/search/route.ts`:
  - requires `caller(request)` and uses the verified uid, not `studentId`;
  - calls `chargeDaily(db, uid, "search", 20, …)`;
  - forwards only `user`/`assistant` messages (the last 10, at most 2,000 characters each) and caps the question at 1,000 characters;
  - returns a generic error message.

  `app/account/components/AIEducationAssistant.tsx` sends the ID token.
- [ ] **1.7 H-03 (part): coupon outage.** In `lib/coupons.ts`, the `catch` in `getCoupons()` returns `FALLBACK_COUPONS.filter(c => c.percentOff < 100)`.
- [ ] **1.8 H-04 / C-03 (part): payments.**
  - New `lib/payments/claim.ts` with `claimPayment()`. In one transaction it creates `payments/{paymentId}` with the uid, and writes `paid` and related fields to `users/{uid}` with `paymentVerifiedBy: "server"`. The same uid retrying gets `already_yours`; a different uid gets `claimed_by_other`.
  - `app/api/payment/verify/route.ts` validates the `order_` and `pay_` ID formats and calls `claimPayment` when `isFirestoreConfigured()` and the token has a uid. It returns 409 on `claimed_by_other`.
- [ ] **1.9 H-05: Firestore create rule.** In `firestore.rules`, `match /users/{uid}` → `allow create` also requires:
  - `paid` to be false or absent;
  - `uid` (if present) to equal the doc id;
  - none of `institutionalLinkCode`, `archivedAt`, `testDrives`, `decision`, `certificates`, `boosterRequests`.

  `institution` stays allowed, because the sign-up form sets it.
- [ ] **1.10 H-07: Storage rules.**
  - New `storage.rules`: owner-only on `scholarshipVault/{uid}/*`, `studyAbroadVault/{uid}/*` and `reviewVerification/{uid}/*` (admins can read review proofs); PDF, image or Word files only, under 10 MB; no overwrites; everything else denied.
  - New `firebase.json` pointing at both rule files, plus emulator ports.
  - `accept=".pdf,.doc,.docx,image/png,image/jpeg,image/webp,image/heic,image/heif"` on the file inputs in `components/scholarships/DocumentVaultClient.tsx` and `components/studyAbroad/AbroadDocumentVaultClient.tsx`.
- [ ] **1.11 M-01: headers.** `next.config.js` has `poweredByHeader: false` and a `{ source: "/:path*" }` rule setting `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy` and `Permissions-Policy` (with `camera=(self), microphone=(self)` kept, because the voice features need them).
- [ ] **1.12 L-03: open redirect.** `app/api/institution/messages/route.ts` validates `body.link` with `safeInternalPath()`, which rejects `//host` and `/\host`.
- [ ] **1.13 L-07: CI and typecheck.**
  - `tsconfig.json` excludes `**/*.test.ts`.
  - `package.json` has `test`, `test:security` and `test:rules` scripts.
  - `tests/jobs/ts-hooks.mjs` maps `next/server` to `next/server.js`.
  - `.github/workflows/ci.yml` runs typecheck, tests and a non-blocking `npm audit`, with `permissions: contents: read`.
- [ ] **1.14** Check the tests exist: `tests/security/security.test.mjs`, `tests/security/coupons-outage.test.mjs`, `tests/rules/firestore.rules.spec.mjs` and `tests/rules/storage.rules.spec.mjs`.
- [ ] **1.15** Verify:
  ```bash
  npm ci
  ```
  ```bash
  npm run typecheck
  ```
  ```bash
  npm test
  ```
  ```bash
  npm run test:security
  ```
  If Java is installed, also run the rule tests on the **emulator**:
  ```bash
  npm i -D firebase-tools@13 @firebase/rules-unit-testing@3 firebase@10
  ```
  ```bash
  npm run test:rules
  ```
- [ ] **1.16** Commit: `Apply verified audit fixes (C-01, C-02, H-01..H-05, H-07, M-01, L-03, L-07)`.

---

## Phase 2: Safe fixes (no approval needed)

These are low-risk and don't change how anything is stored or deployed.

- [ ] **2.1 L-02: `javascript:` links in research sources.** Find where research sources are saved (`lib/research/clientProgress.ts`, the `Source.url` field) and rendered (`app/account/research/projects/[id]/sources/page.tsx`). Clean the URL with `safeHttpUrl()` on save, and only render the `<a href>` when the cleaned value is not empty. Do the same for any other user-entered URL rendered as `href`; search for `href={` that uses user data. Add a test.
- [ ] **2.2 L-08: console logging.** Remove the `console.log("Firebase client config…")` line in `lib/firebase/client.ts`.
- [ ] **2.3 L-01: internal error details.**
  - In the legacy routes `app/api/assessment/**`, `app/api/report/[sessionId]`, `app/api/leads` and `app/api/admin/seed`, return generic messages to the client and keep `console.error` for the details.
  - In `lib/institution/server.ts` `caller()`, keep the detailed project-mismatch text in the server log only, and return a generic 503 message.
  - Keep the HTTP status codes the same.
- [ ] **2.4 Q-02: one token-verification helper.**
  - `app/api/admin/send-report/route.ts` should use `verifySignIn` from `lib/firebase/adminAuth.ts` plus `isAdmin()` instead of its own inline lookup.
  - Replace the hardcoded web API key in `lib/firebaseIdentity.ts` and `send-report` with `process.env.NEXT_PUBLIC_FIREBASE_API_KEY`, falling back to the existing public value so nothing breaks.
- [ ] **2.5 Q-03: one mail helper.** Create `lib/mail.ts`: one cached, pooled nodemailer transporter with the same host clean-up as `lib/exams/alertEmail.ts`, plus `sendMail()`. Move the 8 `createTransport` call sites onto it without changing any email content.
- [ ] **2.6 M-04 (part): lead-capture spam.**
  - `app/api/crm-lead/route.ts`: require a Firebase ID token, and take the email from the verified token, not the body. Update the caller in the registration flow (search `"/api/crm-lead"`) to send `Authorization: Bearer`; the user is signed in at that point.
  - Add `lib/security/rateLimit.ts` with a simple interface: `limit(key, max, windowSec) → boolean`. If `UPSTASH_REDIS_REST_URL` and `UPSTASH_REDIS_REST_TOKEN` are set, use Upstash's REST API through `fetch`; add no new dependency. Otherwise allow the request (no-op), and log a warning once.
  - Apply it by IP plus route to these public endpoints: `/api/crm-lead`, `/api/leads` (POST), `/api/payment/coupon`, `/api/institutional/check`, `/api/new-assessment/score`, `/api/money/grade-scam`, `/api/startups/grade`. Return 429 with a friendly message.
  - Add tests with a fake limiter.
- [ ] **2.7 M-06: email verification.** After `register()` in `lib/auth/AuthProvider.tsx` creates the profile, call `sendEmailVerification(cred.user)` best-effort (never block or fail registration). Don't block unverified users yet; just send the email.
- [ ] **2.8 Q-06: error boundaries.** Add `app/error.tsx` (client component, a "Try again" button calling `reset()`), `app/global-error.tsx` and `app/not-found.tsx`, in the app's existing visual style. Don't show the error message or stack in the UI.
- [ ] **2.9 Dependencies (non-major).** Do not upgrade `next`, `react` or `firebase` majors here.
  - Upgrade `nodemailer` to the latest version that fixes GHSA-wmmp-3585-3rmp, GHSA-2x7j-588g-ccc2 and GHSA-8m3c-c648-2xjj. Check its changelog for breaking changes. Upgrade `@types/nodemailer` to match.
  - Run `npm update firebase-admin` within the current major.
  - **Do not** apply npm's suggestion to downgrade `firebase` to 9.14.0.
  - Re-run `npm audit` and record the before and after numbers in `REMEDIATION_TRACKER.md`.
- [ ] **2.10 L-04: two lockfiles.** Ask the user which package manager Vercel uses. Keep that lockfile and delete the other. Fix or remove the placeholder `allowBuilds` text in `pnpm-workspace.yaml`.
- [ ] **2.11 P-03 / P-06: small performance fixes.**
  - Cache `institutionForStudent()`'s full read of the `institutions` collection in memory for 60 seconds.
  - For stress benchmarks: store precomputed deciles in `stressBenchmarks/_summary_{band}`, update them on POST, and read that one document on GET (fall back to the current scan if it's missing).
- [ ] **2.12 Q-14: stale comments.** Remove comments claiming "no server-side auth check (this app has none anywhere)", for example in `app/api/startups/grade/route.ts`.
- [ ] **2.13** Run typecheck, `npm test` and `npm run build`, then commit: `Audit phase 2: safe hardening, rate limiting, error boundaries, dependency updates`.

---

## Phase 3: 🛑 Changes that need approval (stop before each one)

For each item: explain the change and what could break, ask the user, and implement **only** after a "yes". Use one commit per item.

### 🛑 3.1 C-03: payment status written only by the server
**Precondition:** ask the user to confirm that `FIREBASE_PROJECT_ID`, `FIREBASE_CLIENT_EMAIL` and `FIREBASE_PRIVATE_KEY` are set in **Vercel production**. Without them, paying students would be locked out.
- [ ] Add `'paid', 'paymentStatus', 'paidAt', 'paymentId', 'amountPaid', 'couponCode', 'paymentVerifiedBy'` to `adminOnlyUserFields()` in `firestore.rules`. Remove the TODO comment there.
- [ ] `app/api/payment/redeem/route.ts`: require a valid ID token (401 otherwise) and write the waiver to `users/{uid}` with the Admin SDK, as `app/api/institutional/redeem/route.ts` does.
- [ ] `app/PaymentGate.tsx`: remove the browser `setDoc(… paid: true …)` in `markPaid`. After `/api/payment/verify` or `/redeem` succeeds, call `refreshProfile()` from `AuthProvider`. Keep the UI flow the same.
- [ ] `app/api/payment/verify/route.ts`: when `claimPayment` throws, return an error so the client can retry, instead of silently succeeding.
- [ ] Server-side gate: in `app/api/new-assessment/score/route.ts` (the paid paper), when payment is active (`isPaymentActive()`), require a signed-in caller whose `users/{uid}.paid === true` (Admin SDK read). Return 402 otherwise. Confirm with the user which exam categories are free (the demo test) and leave those open.
- [ ] Flip the emulator test `KNOWN GAP (C-03)` to `assertFails`, and add a test that the server write path still works.

### 🛑 3.2 H-03: retire the public free coupon
**Precondition:** the user confirms the `coupons` collection is populated through `/admin/coupons` in production.
- [ ] Remove `freeCouponCode` from `lib/offer.ts` and drop the 100% entry from `FALLBACK_COUPONS` in `lib/coupons.ts`. Search for other uses and update them.

### 🛑 3.3 M-03: stronger admin authorisation
**Precondition:** the user confirms that `support@onegrasp.com` has a **verified** email in Firebase Auth.
- [ ] In `firestore.rules` `isAdmin()` and in `storage.rules`, add `&& request.auth.token.email_verified == true`. In `lib/firebase/adminAuth.ts` `verifySignIn`, also return `emailVerified` from the lookup, and make `requireAdmin` and `send-report` require it.
- [ ] Optional (ask): move to a custom claim `admin: true`, set by a one-off script `scripts/set-admin-claim.mjs` that the **user** runs. Rules then check `request.auth.token.admin == true`. Keep the email check as well during the switch-over.
- [ ] Flip the emulator test `KNOWN GAP (M-03)`.

### 🛑 3.4 M-05: certificates and results only from server-written data
- [ ] Move course and lesson completion writes behind an API route that checks the lesson exists and records completion with the Admin SDK. Add `progress` (or at least `progress.courses`) to the admin-only user fields, and make the startups progress collections server-written.
- [ ] Have `/api/new-assessment/score` save `latestAssessment` server-side for the signed-in caller. Lock `latestAssessment` in the rules.
- [ ] Explain the migration impact (existing documents stay valid). Add tests showing a student can't write a completed course and then get a certificate.

### 🛑 3.5 M-02 + P-02: real school membership and fast portal queries
- [ ] Add `institutionId` to `users/{uid}`, written only by the server (institutional-link redeem, or school/admin approval).
- [ ] Write a migration script `scripts/backfill-institution-id.mjs`, dry run by default, which **the user runs**. It matches existing `institution` names with the current `belongsTo()` logic.
- [ ] Change `studentsOf()` to `where("institutionId","==",inst.id)`, keeping the old name match behind a flag until the backfill is verified. Add the Firestore index.
- [ ] Decide with the user whether students who typed a school name without a code still get that school's messages.

### 🛑 3.6 P-01: admin dashboard without downloading every user
- [ ] Add `app/api/admin/users/route.ts` (`requireAdmin`) with cursor pagination (`limit` ≤ 100, `startAfter`), a `select()` of only the list fields, and `count()` aggregates for the totals. Switch `app/admin/(dashboard)/page.tsx` and `archives/page.tsx` to it.

### 🛑 3.7 P-04: bulk school sign-up hot spot
- [ ] Replace the single `usedCount` increment in `/api/institutional/redeem` with a sharded counter (10 shards) or a `redemptions` subcollection plus `count()`. Keep the `maxStudents` check correct under concurrency, and test it with a fake DB.

### 🛑 3.8 M-07: legacy assessment API
- [ ] Show the user whether `app/assessment-experience.tsx` (which calls `/api/assessment/*`, `/api/leads` and `/api/report/*`) is still reachable from any page. If not, propose deleting the legacy routes and `lib/localMode`. If it is, require sign-in on them.

### 🛑 3.9 M-01 (part): Content-Security-Policy
- [ ] Add `Content-Security-Policy-Report-Only`, using the draft in `PRODUCTION_DEPLOYMENT_CHECKLIST.md` §5. **Do not enforce.** Tell the user to watch the browser console and reports for a week before switching to enforcing.

### 🛑 3.10 H-06: Next.js major upgrade (separate branch)
- [ ] Only on a new branch `chore/next-upgrade`, and only after everything above is merged.
- [ ] Follow the official upgrade guides step by step: 14 → 15 (async `params`/`searchParams`/`headers()`, React 19, caching defaults), then to a current patched release. Run `npx @next/codemod` where it applies.
- [ ] Fix type errors and run the full test suite and `next build`. List every route that needs manual QA, and leave production deployment to the user.

---

## Phase 4: Final verification

- [ ] `npm run typecheck`: no errors.
- [ ] `npm test`: everything passes. Report the counts.
- [ ] `npm run test:rules`: everything passes on the emulator.
- [ ] `npm run build`: succeeds. Compare the `/account` first-load JS with the baseline (747 kB).
- [ ] `npm audit --omit=dev`: record the remaining issues in `REMEDIATION_TRACKER.md` with a reason for each.
- [ ] Secret scan of the working tree (show the file and line only, never the value):
  ```bash
  git grep -nE "AIza[0-9A-Za-z_-]{35}|rzp_(live|test)_|BEGIN [A-Z ]*PRIVATE KEY|gsk_[A-Za-z0-9]{20,}"
  ```
  Only the public-by-design Firebase web key and Razorpay key ID may remain.
- [ ] Update `security-audit/REMEDIATION_TRACKER.md` and `SECURITY_TEST_REPORT.md` with what changed and how it was verified.
- [ ] Give the user a short summary: done, skipped (with the reason), and what is waiting for them (§5).

---

## 5. Things only the user can do (Claude: remind them; don't attempt these)

These need console access or a decision Claude must not make.

| # | Action | Where |
|---|---|---|
| 1 | **Change the `support@onegrasp.com` password, revoke its sessions and enable MFA** (C-01). Review sign-in logs | Firebase console → Authentication |
| 2 | Deploy the rules after reviewing them: `firebase deploy --only firestore:rules,storage` | Your terminal, with your Firebase login |
| 3 | Compare the **current live Storage rules** with `storage.rules` *before* deploying. If they were open, review access logs | Firebase console → Storage → Rules |
| 4 | Retire the published 100%-off coupon | `/admin/coupons` |
| 5 | Set `FIREBASE_*`, `RAZORPAY_*`, `CRON_SECRET`, `SMTP_*`, and `ADMIN_TOKEN` (only if `GET /api/leads` is needed); leave `ADMIN_SEED_KEY` unset | Vercel → Settings → Environment Variables |
| 6 | Restrict the Firebase web API key to your domains | Google Cloud console → Credentials |
| 7 | Turn on email enumeration protection and App Check (monitor first) | Firebase console |
| 8 | Turn on Firestore point-in-time recovery and daily exports; test one restore | Google Cloud console |
| 9 | Branch protection on `main` (require the `CI / check` job), Dependabot, secret scanning; consider making the repo private | GitHub → Settings |
| 10 | Spending caps on Groq and DeepSeek; set up Sentry | Provider dashboards |
| 11 | DPDP Act: parental consent for under-18s, privacy notice, data deletion, review of the Meta Pixel | Your lawyer |
