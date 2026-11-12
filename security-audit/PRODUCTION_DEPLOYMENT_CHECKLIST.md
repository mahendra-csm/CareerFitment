# Production Deployment Checklist

Tick every item before a public launch. Items marked **BLOCKER** must be done first.

## 1. Immediate security actions
- [ ] **BLOCKER** Rotate the password of `support@onegrasp.com` in Firebase Auth, revoke its sessions and enable MFA (C-01).
- [ ] **BLOCKER** Review Firebase Auth sign-in logs and Firestore usage for unexpected admin access since the `DEV_ADMIN` commit.
- [ ] **BLOCKER** Deploy the updated `firestore.rules` with `firebase deploy --only firestore:rules`. Run `npm run test:rules` against the emulator first (H-05).
- [ ] **BLOCKER** Compare the live Storage rules (console → Storage → Rules) with `storage.rules` and deploy with `firebase deploy --only storage` (H-07). If the old rules were permissive, review the access logs.
- [ ] **BLOCKER** Retire or rotate the published 100%-off coupon in `/admin/coupons` (H-03).
- [ ] Review SMTP provider logs for mail sent through `/api/*/send-alert` that you didn't expect (H-01).
- [ ] Review Groq and DeepSeek usage for abuse of `/api/ai/search` (H-02).
- [ ] Restrict the Firebase web API key in Google Cloud Console to your production domains (HTTP referrer restriction).
- [ ] Turn on *Email enumeration protection* in Firebase Auth settings.

## 2. Environment configuration (Vercel → Project → Settings → Environment Variables)

Production and Preview should use **separate** Firebase projects. Today the client code hardcodes the production project as its fallback, so set the `NEXT_PUBLIC_FIREBASE_*` variables per environment.

| Variable | Required | Notes |
|---|---|---|
| `FIREBASE_PROJECT_ID`, `FIREBASE_CLIENT_EMAIL`, `FIREBASE_PRIVATE_KEY` | **Yes** | Server-side payment recording, admin and institution routes, AI quotas. Use a least-privilege service account (Firestore User + Firebase Auth Admin), not Owner |
| `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET` | Yes | Production values only in Production. Rotate the secret if it was ever shared |
| `ADMIN_TOKEN` | Only if `GET /api/leads` is used | 32+ random characters. Unset means the endpoint is disabled (fail-closed) |
| `CRON_SECRET` | Yes (job sync) | 16+ characters; Vercel cron sends it automatically |
| `GROQ_API_KEY`, `DEEPSEEK_API_KEY` | For AI features | Set provider-side spend limits |
| `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS` | Yes | Prefer a transactional provider (P-08) |
| `NEXT_PUBLIC_SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY` | Jobs | The service role key must **never** have a `NEXT_PUBLIC_` prefix |
| `JOB_REPORT_SALT` | Recommended | So report hashing doesn't fall back to `CRON_SECRET` |
| `TEAM_NOTIFY_EMAIL` | Recommended | Point it somewhere else on Preview |
| `ADMIN_SEED_KEY` | **Leave unset** in production | Disables `/api/admin/seed` |

- [ ] No `serviceAccountKey.json` in the deployed bundle. It is gitignored; keep it that way.
- [ ] Mark secrets as *Sensitive* in Vercel so they can't be read back from the dashboard.

## 3. Build and release
- [ ] CI (`.github/workflows/ci.yml`) is green: typecheck + `npm test`.
- [ ] `npm audit --omit=dev` reviewed. The Next.js major upgrade is planned (H-06).
- [ ] Use one package manager and lockfile (L-04).
- [ ] `next build` succeeds locally with the production env shape.
- [ ] Source maps are not public. (Next disables browser source maps by default; keep `productionBrowserSourceMaps` unset.)

## 4. GitHub hardening
- [ ] Branch protection on `main`: require a PR, 1 review, the `CI / check` status, and no force-push.
- [ ] Turn on Dependabot alerts and security updates, plus secret scanning with push protection.
- [ ] Consider making the repository **private**. The full business logic, coupon codes and admin email are public today.
- [ ] Restrict the Vercel GitHub integration to the production branch for production deploys.

## 5. HTTPS and headers
- [x] HSTS, `nosniff`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy` (this branch).
- [ ] Verify them after deploying: `curl -sI https://<domain>/ | grep -iE "strict|x-frame|x-content|referrer|permissions"`.
- [ ] Add a CSP in **Report-Only** mode, watch for violations for a week, then enforce. Starting draft:
  ```
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://checkout.razorpay.com https://connect.facebook.net https://va.vercel-scripts.com https://apis.google.com;
  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
  font-src 'self' https://fonts.gstatic.com data:;
  img-src 'self' data: blob: https:;
  media-src 'self' blob:;
  connect-src 'self' https://*.googleapis.com https://*.firebaseio.com https://firestore.googleapis.com https://api.razorpay.com https://lumberjack.razorpay.com https://*.supabase.co https://vitals.vercel-insights.com https://www.facebook.com;
  frame-src https://api.razorpay.com https://checkout.razorpay.com https://www.youtube.com https://www.youtube-nocookie.com https://careerfitment.firebaseapp.com;
  frame-ancestors 'self'; base-uri 'self'; form-action 'self'; object-src 'none'
  ```
  Adjust it to the actual violations; don't enforce it without the report-only period.

## 6. Monitoring and alerting
- [ ] Error tracking (Sentry for Next.js) on both client and server, with PII scrubbing on.
- [ ] Vercel log drain to a searchable store. Alert on 5xx rate, `[payment]` errors and `claimed_by_other` warnings.
- [ ] Firebase budget alerts and Google Cloud billing alerts; Groq/DeepSeek spend caps.
- [ ] Uptime check on `/`, `/api/payment/status` and `/api/jobs/stats`.
- [ ] Alert on Firestore read spikes (P-01/P-02 scans).

## 7. Backup and disaster recovery
- [ ] Firestore **Point-in-Time Recovery** enabled, plus scheduled exports (`gcloud firestore export gs://<bucket>`) daily, kept 30 days, in a bucket with separate IAM.
- [ ] Supabase daily backups (plan-dependent) checked, and a restore tested once.
- [ ] Restore runbook written and tested on a staging project.
- [ ] Firebase Auth users exported periodically (`firebase auth:export`) and stored encrypted.

## 8. Rollback strategy
- **App:** Vercel → Deployments → *Promote* the previous deployment (instant). Keep the last known-good deployment noted in the release log.
- **Firestore rules:** Firebase console → Rules → *History* → restore the previous version. Keep `firestore.rules` in git as the source of truth.
- **Data migrations:** Run them only as idempotent scripts, after an export taken immediately beforehand.
- **Feature kill switches:** `FORCE_PAYMENT_OFF` (`lib/paymentSettings.ts`), the admin payment toggle, and the AI provider env vars (unset one to disable the feature).

## 9. Privacy and compliance (India — DPDP Act 2023; this is not legal advice)
- [ ] A privacy notice in clear language (and in Indian languages where the audience needs it) listing the data collected, purposes, retention, processors (Firebase/Google, Vercel, Razorpay, Groq/DeepSeek, CRM, Meta Pixel) and the grievance contact.
- [ ] **Verifiable parental consent for users under 18.** Many users are Class 6–12 students. The Act requires verifiable consent from a parent or guardian before processing a child's data, and prohibits tracking, behavioural monitoring and targeted advertising directed at children. **The Meta Pixel (`app/MetaPixel.tsx`) on pages used by minors needs a legal review.** Consult counsel on how the DPDP Rules, 2025 apply and when their provisions commence.
- [ ] Consent records (who, when, which notice version) stored server-side.
- [ ] Data principal rights: an access, correction and erasure flow. Today there is no self-service account deletion, and the `users` delete rule is admin-only.
- [ ] A retention policy, with deletion of inactive accounts and old leads.
- [ ] A breach-response plan: notify the Data Protection Board and affected users. CERT-In directions (April 2022) require reporting certain incidents within 6 hours and keeping logs for 180 days.
- [ ] Data processing agreements with every processor, including LLM providers that receive student text and audio transcripts.
