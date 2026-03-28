# TODO

## Active Next Steps
Goal: build a reliable business knowledge base for research, tool comparisons, and SOPs without adding overhead.
- [ ] P1 | Owner: Trevor | Target: 2026-03-31 | Add the first real research note for a current business question or tool decision.
- [ ] P1 | Owner: Trevor | Target: 2026-03-31 | Add the first SOP draft for a recurring operational task that should become repeatable.
- [ ] P2 | Owner: Trevor | Target: 2026-04-03 | Revisit the repo structure after a handful of notes exist and decide whether folders/templates are needed.

## Completed
- [x] 2026-03-27 | Bootstrapped the repository with `AGENTS.md`, `PROJECT_INTENT.md`, `todo.md`, and `README.md` for business research and SOP tracking.
- [x] 2026-03-28 | Remediated the repo governance records so branch lifecycle and next-steps wording match the current documentation standard.

## Suggested Recommendation Log
- 2026-03-27 | status: open | reasoning level: `medium` | Create a reusable note template for research and tool comparisons after 3-5 entries reveal the right common fields.
- 2026-03-27 | status: open | reasoning level: `medium` | Add a lightweight decision log once the first major tool or equipment choice is finalized in this repo.

## Active Branch Ledger
### `main`
- status: active
- created: 2026-03-27
- base: `main`
- worktree: `/Users/gillettes/Coding Projects/Equipment & SOPs`
- source chat: 2026-03-27 "Bootstrap repository governance and starter docs"
- last refreshed by chat: 2026-03-28 "Verify repo setup matches documented standards"
- purpose: default branch for the repository bootstrap and subsequent small documentation/governance updates
- merge expectation: `no merge`
- merge target: `main`
- exit checklist:
  - [x] Initial governance/docs scaffold created
  - [x] Remote connected and `main` pushed
  - [x] Branch ledger updated to current documentation standard
  - [ ] Re-evaluate whether `main` should stay in the active ledger once a non-trivial feature branch exists
- delete when: never; retained as the default branch
- cleanup command: `none`
- retain after close: yes
- retain reason: default branch
- linked issue/PR/audit record: `Audit Record Log` entries dated 2026-03-27 and 2026-03-28

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
- 2026-03-28 | type: governance review | scope: repo setup alignment against current bootstrap documentation | repo fingerprint: `main` at `8164e021f24cfba94bc6527b634fdcc9863d8249` before remediation commit | prior audit reference: 2026-03-27 governance review | source/work chat: repo setup conformance chat | audit chat: same chat | implementation chat: same chat | separate follow-up audit: no, direct remediation in same chat | commands / evidence: `verify-project-agents-compliance.sh`, `ensure-project-todo-audit-sections.sh`, `git diff --check` | tested: AGENTS marker compliance, required todo sections, branch ledger completeness, diff formatting sanity | not tested: future docs lint/spellcheck workflow, real note capture workflow, publish/export workflow | findings opened or updated: branch ledger fields and AGENTS next-steps wording needed refresh | fixes closed / verified: branch ledger normalized and AGENTS wording updated to current standard | declined / deferred findings: publish/export workflow remains `TODO: verify` until the repo needs one | better-path challenge: keep the setup minimal and standards-compliant instead of adding speculative structure too early | references: local conformance chat

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
- 2026-03-28 | command(s): `verify-project-agents-compliance.sh`, `ensure-project-todo-audit-sections.sh`, `git diff --check` | result: pass; AGENTS markers verified, required todo governance sections present, and no diff formatting issues | log/PR reference: local conformance chat

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
