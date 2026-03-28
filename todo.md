# TODO

## Active Next Steps
Goal: build a reliable business knowledge base for research, tool comparisons, and SOPs without adding overhead.
- [ ] P1 | Owner: Trevor | Target: 2026-03-31 | Add the first real research note for a current business question or tool decision.
- [ ] P1 | Owner: Trevor | Target: 2026-03-31 | Add the first SOP draft for a recurring operational task that should become repeatable.
- [ ] P2 | Owner: Trevor | Target: 2026-04-03 | Revisit the repo structure after a handful of notes exist and decide whether folders/templates are needed.

## Completed
- [x] 2026-03-27 | Bootstrapped the repository with `AGENTS.md`, `PROJECT_INTENT.md`, `todo.md`, and `README.md` for business research and SOP tracking.

## Suggested Recommendation Log
- 2026-03-27 | status: open | reasoning level: `medium` | Create a reusable note template for research and tool comparisons after 3-5 entries reveal the right common fields.
- 2026-03-27 | status: open | reasoning level: `medium` | Add a lightweight decision log once the first major tool or equipment choice is finalized in this repo.

## Active Branch Ledger
- `main`
  - `source chat`: 2026-03-27 repo bootstrap
  - `last refreshed by chat`: 2026-03-27 repo bootstrap
  - `purpose`: initialize the repository governance and starter docs
  - `merge expectation`: none; this is the primary branch
  - `exit checklist`: initial files committed; remote connected when ready
  - `retain after close`: yes
  - `retain reason`: default branch

## Branch History
- No closed branch entries recorded yet.

## Audit Record Convention
- Record each audit, ship-check, or substantial verification-driven review in an easy-to-find project audit log entry.
- Each entry should capture:
  - `date`
  - `type` (for example `full audit`, `targeted audit`, `ship-check`, `governance review`)
  - `scope`
  - `repo fingerprint` (branch + commit when available)
  - `prior audit reference`
  - `source/work chat`
  - `audit chat`
  - `implementation chat` or `disposition chat`
  - `separate follow-up audit` (`yes` / `no` plus reason when `no`)
  - `commands / evidence`
  - `tested`
  - `not tested`
  - `findings opened or updated`
  - `fixes closed / verified`
  - `declined / deferred findings`
  - `better-path challenge`
  - `references` (issue, PR, commit, or log path)
- When a finding is later implemented, deferred, declined, or superseded, update the existing audit trail instead of deleting the history.

## Audit Record Log
- 2026-03-27 | type: governance review | scope: initial repository bootstrap | repo fingerprint: `main` before first commit | prior audit reference: none | source/work chat: repo bootstrap chat | audit chat: same chat | implementation chat: same chat | separate follow-up audit: no, bootstrap-only setup | commands / evidence: `bootstrap-project-governance.sh`, `verify-project-agents-compliance.sh`, `git diff --check` | tested: governance scaffold creation, AGENTS marker compliance, diff formatting sanity | not tested: remote push, future docs lint/spellcheck workflow, real content note capture | findings opened or updated: none | fixes closed / verified: initial governance scaffold verified | declined / deferred findings: publish/export workflow still `TODO: verify` | better-path challenge: keep the repo docs-first until actual usage proves a need for more structure | references: local bootstrap chat

## Test Evidence Convention
- Testing is required delivery evidence. If a check is skipped, blocked, or only partially run, record the reason and the remaining risk.
- Record each verification run as:
  - `date` (YYYY-MM-DD)
  - `command(s)` executed
  - `result` (pass/fail + short note)
  - `log/PR reference` (commit SHA, CI URL, or local log path)
- When a verification run closes or updates an audit finding, cross-reference the matching audit record entry and the chat or commit that performed the work.

## Test Evidence Log
- 2026-03-27 | command(s): `bootstrap-project-governance.sh`, `verify-project-agents-compliance.sh`, `git diff --check` | result: pass; governance files created, required AGENTS markers present, no diff formatting issues | log/PR reference: local bootstrap chat

## Testing Cadence Matrix
| Trigger | Command(s) | Cadence | Gate Criteria |
|---|---|---|---|
| Documentation/process change | `git diff --check` plus repo-specific docs lint/spellcheck once configured | Per change | Formatting is clean and any missing docs automation is documented |
| Template/policy change | `bootstrap-project-governance.sh` or template output review, plus `git diff --check` | Per change | Generated output reviewed or blocker documented |
| Release/readiness review | `TODO: verify whether publish/export workflow is needed for this repo` | Pre-release | Distribution approach is confirmed or explicitly deferred |

## Feedback Decision Log
Record outside feedback and the resulting reasoning once, then update the same entry as the decision evolves.
- Each entry should capture:
  - `date`
  - `feedback source`
  - `feedback summary`
  - `evaluation chat`
  - `reasoning response`
  - `decision status` (`accepted`, `partial`, `deferred`, `rejected`, or `superseded`)
  - `implementation/disposition chat`
  - `linked branch / audit / suggestion / test evidence`
- Reuse or update an existing entry when the same feedback thread comes back instead of opening duplicate records.
