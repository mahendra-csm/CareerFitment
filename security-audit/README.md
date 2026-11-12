# Security audit of `mahendrabella1/careerfitment`

This folder holds the audit of the **Career Fitment web application** (`github.com/mahendrabella1/careerfitment`, commit `bb0c7d8`) and its fixes. The application lives in a different repository from this one, and this session could not push to it, so the fixes are delivered here as a patch.

| File | Contents |
|---|---|
| `EXECUTIVE_SUMMARY.md` | Start here: overall verdict, architecture, top risks, readiness |
| `SECURITY_AUDIT_REPORT.md` | Every finding, with file and line, exploitation scenario, impact and fix |
| `PERFORMANCE_AUDIT.md` | Bundle measurements, bottlenecks, scalability estimates |
| `CODE_QUALITY_REPORT.md` | Architecture and maintainability issues |
| `REMEDIATION_TRACKER.md` | Status and verification of every item, and what needs your approval |
| `PRODUCTION_DEPLOYMENT_CHECKLIST.md` | Launch, environment, monitoring, backup, rollback and DPDP checklist |
| `SECURITY_TEST_REPORT.md` | Tests run, results, mutation checks, remaining risks |
| `remediation.patch` | All code changes **except** `app/admin/layout.tsx` |
| `files/app/admin/layout.tsx` | The fixed admin layout, as a whole file |

**Why one file is shipped whole:** a normal diff of `app/admin/layout.tsx` would contain the leaked admin password in its removed lines. Publishing the patch would then leak it again.

## Applying the fixes (in the application repository)
```bash
git checkout -b security/audit-remediation bb0c7d8
```
```bash
git apply /path/to/security-audit/remediation.patch
```
```bash
cp /path/to/security-audit/files/app/admin/layout.tsx app/admin/layout.tsx
```
```bash
mkdir -p security-audit && cp /path/to/security-audit/*.md security-audit/
```
```bash
npm ci && npm run typecheck && npm test
```

## Do these first, whatever happens to the patch
1. Change the password of `support@onegrasp.com` in Firebase Authentication, revoke its sessions, and enable MFA (C-01).
2. Compare the live Firestore and Storage rules with `firestore.rules` and `storage.rules` from the patch, then deploy them (H-05, H-07).
3. Retire the published 100%-off coupon code (H-03).
