# TODO

## Active Next Steps
Goal: stand up a field-usable SOP, equipment, and maintenance knowledge system that runs in Markdown/Git and is practical inside Obsidian.
- [ ] P1 | Owner: Trevor | Target: 2026-03-30 | Resolve and document the canonical source-of-truth decision: the live SOP system should either move fully into `/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs` or this planning repo should remain canonical, but not both.
- [ ] P1 | Owner: Trevor | Target: 2026-03-31 | Choose one single maintenance-tracking model for the SOP system: property-driven schedule fields or Tasks-driven recurring maintenance, then update `SOP_SYSTEM_PLAN.md` and templates to remove duplicate state.
- [ ] P1 | Owner: Trevor | Target: 2026-04-01 | Decide whether the entire mixed personal/business Obsidian vault should continue auto-pushing to GitHub or whether the SOP/business subtree should be isolated into a narrower backup boundary.
- [ ] P1 | Owner: Trevor | Target: 2026-04-02 | Create the initial vault structure, naming convention, and note property standard described in `SOP_SYSTEM_PLAN.md` after the canonical path and maintenance model are finalized.
- [ ] P1 | Owner: Trevor | Target: 2026-04-03 | Create reusable templates for SOP, equipment, maintenance log, checklist, and decision notes after the schema is simplified.
- [ ] P1 | Owner: Trevor | Target: 2026-04-05 | Build the first two complete pilot systems: window cleaning and pressure washing, including SOPs, checklists, equipment notes, and maintenance schedules.
- [ ] P2 | Owner: Trevor | Target: 2026-04-06 | Reduce Obsidian vault Git noise by deciding which `.obsidian` files are real configuration worth tracking and which plugin installation files should be ignored.
- [ ] P2 | Owner: Trevor | Target: 2026-04-07 | Build the initial Obsidian dashboards for SOP review, equipment register, and maintenance due items.
- [ ] P2 | Owner: Trevor | Target: 2026-04-08 | Run a friction review after the pilots and remove any fields, sections, or automation that add overhead without operational value.

## Completed
- [x] 2026-03-27 | Bootstrapped the repository with `AGENTS.md`, `PROJECT_INTENT.md`, `todo.md`, and `README.md` for business research and SOP tracking.
- [x] 2026-03-28 | Remediated the repo governance records so branch lifecycle and next-steps wording match the current documentation standard.
- [x] 2026-03-28 | Added `SOP_SYSTEM_PLAN.md` and reprioritized the repo around an Obsidian-backed SOP, equipment, and maintenance rollout plan.

## Suggested Recommendation Log
- 2026-03-27 | status: open | reasoning level: `medium` | Create a reusable note template for research and tool comparisons after 3-5 entries reveal the right common fields.
- 2026-03-27 | status: open | reasoning level: `medium` | Add a lightweight decision log once the first major tool or equipment choice is finalized in this repo.
- 2026-03-28 | status: open | reasoning level: `medium` | Add a truck inventory / consumables note with reorder thresholds once the first equipment notes exist so supplies do not become a separate untracked system.
- 2026-03-28 | status: open | reasoning level: `medium` | Add a chemical and materials reference note with approved uses, storage rules, and restrictions once pressure washing and window cleaning pilots are in place.
- 2026-03-28 | status: open | reasoning level: `medium` | Add QR-code or ID labels for major equipment after the asset register stabilizes so physical gear can be matched to notes faster in the field.
- 2026-03-28 | status: open | reasoning level: `medium` | Add a mobile field-capture workflow using Daily Notes, phone shortcuts, or QuickAdd after the core note templates are working so field lessons make it back into the system quickly.
- 2026-03-28 | status: open | reasoning level: `medium` | Add a web-clipping template for manuals, vendor pages, and equipment research after the decision-note pattern is stable so outside research lands in a consistent format.
- 2026-03-28 | status: open | reasoning level: `medium` | Add an explicit retention and archive policy for maintenance logs, photos, and Daily Notes before the pilot systems generate operational clutter.

## Active Branch Ledger
### `main`
- status: active
- created: 2026-03-27
- base: `main`
- worktree: `/Users/gillettes/Coding Projects/Equipment & SOPs`
- source chat: 2026-03-27 "Bootstrap repository governance and starter docs"
- last refreshed by chat: 2026-03-28 "Full audit of SOP system plan and Obsidian implementation approach"
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
- 2026-03-28 | type: full audit | scope: SOP system plan in `SOP_SYSTEM_PLAN.md` plus the current Obsidian vault backup implementation used to support it | repo fingerprint: `Equipment & SOPs` `main` at `4ab38cbdf24736696ef2e6f4b73bbd72cf0e541d`; supporting implementation fingerprint: `Systems Command Center` `main` at `43538d8cfe258c82d417bb714e40f2ffb4839045` | prior audit reference: 2026-03-28 governance review | source/work chat: SOP planning and Obsidian backup setup chats | audit chat: current thorough audit chat | implementation chat: none yet; findings-only audit | separate follow-up audit: no, pending remediation work not yet started | commands / evidence: `sed -n` and `nl -ba` on `SOP_SYSTEM_PLAN.md`, `todo.md`, `.gitignore`, `obsidian-vault-git-backup.sh`, `com.gillettes.obsidian-vault-git-backup.plist`; `git rev-parse HEAD` on both repos | tested: planning document structure, current execution queue, backup automation scope, and repo-boundary assumptions | not tested: real SOP template usability in Obsidian, Bases views, Tasks queries, mobile capture flow, or long-term backup behavior under real daily usage | findings opened or updated: canonical source-of-truth drift; duplicate maintenance-state model risk; overbroad whole-vault auto-push boundary; Obsidian plugin payload churn still tracked | fixes closed / verified: none in this audit pass | declined / deferred findings: none yet | better-path challenge: if starting today, prefer a single canonical business SOP location with a narrower backup boundary before scaling automation, because mixed-vault auto-push and split planning truth will create avoidable overhead | references: current audit report plus supporting implementation files

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
- 2026-03-28 | command(s): `git diff --check` | result: pass; `SOP_SYSTEM_PLAN.md` and the updated rollout plan in `todo.md` are formatting-clean | log/PR reference: current SOP planning chat
- 2026-03-28 | command(s): `sed -n`, `nl -ba`, and `git rev-parse HEAD` against `SOP_SYSTEM_PLAN.md`, `todo.md`, `.gitignore`, `obsidian-vault-git-backup.sh`, and `com.gillettes.obsidian-vault-git-backup.plist` | result: pass; audit evidence collected for planning/implementation review with reproducible file-line references | log/PR reference: current full audit chat

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
