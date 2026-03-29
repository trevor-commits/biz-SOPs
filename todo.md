# TODO

## Active Next Steps
Goal: stand up a field-usable SOP, equipment, and maintenance knowledge system that runs in Markdown/Git and is practical inside Obsidian.
- [ ] P1 | Owner: Trevor | Target: 2026-04-02 | Verify the end-to-end mobile edit path from Obsidian phone capture into the preferred SOP working copy and document the exact sync path plus recovery steps if edits have not landed before Codex automation runs.
- [ ] P1 | Owner: Trevor | Target: 2026-04-03 | Build the first two complete pilot systems: window cleaning and pressure washing, including SOPs, checklists, equipment notes, and recurring maintenance Tasks.
- [ ] P2 | Owner: Trevor | Target: 2026-04-04 | Build the initial Obsidian dashboards for SOP review, equipment register, maintenance due items, and purchasing queues using live pilot notes.
- [ ] P2 | Owner: Trevor | Target: 2026-04-05 | Reduce dedicated SOP repo noise by deciding which `.obsidian` files belong in the SOP repo if any local vault config is later introduced.
- [ ] P2 | Owner: Trevor | Target: 2026-04-07 | Run a friction review after the pilots and remove any fields, sections, or automation that add overhead without operational value.

## Completed
- [x] 2026-03-27 | Bootstrapped the repository with `AGENTS.md`, `PROJECT_INTENT.md`, `todo.md`, and `README.md` for business research and SOP tracking.
- [x] 2026-03-28 | Remediated the repo governance records so branch lifecycle and next-steps wording match the current documentation standard.
- [x] 2026-03-28 | Added `SOP_SYSTEM_PLAN.md` and reprioritized the repo around an Obsidian-backed SOP, equipment, and maintenance rollout plan.
- [x] 2026-03-28 | Resolved the canonical source-of-truth decision: the `biz-SOPs` repo remains canonical and its preferred operational working copy lives at `/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs`.
- [x] 2026-03-28 | Resolved the maintenance-state model: recurring Tasks inside equipment notes are the canonical due-state for scheduled maintenance.
- [x] 2026-03-28 | Isolated the preferred Obsidian working copy into its own ignored subtree inside the parent vault and added a dedicated Git backup lane for the SOP repo.
- [x] 2026-03-28 | Stopped tracking parent-vault Obsidian plugin installation payloads so the shared vault backup keeps stable configuration, not third-party plugin binaries.
- [x] 2026-03-28 | Added `RETENTION_AND_ARCHIVE_POLICY.md` and aligned the SOP plan so repo-scoped Daily Notes, maintenance logs, and supporting media have explicit archive rules.
- [x] 2026-03-28 | Built the initial folder structure in the preferred Obsidian working copy, including system, service, equipment, maintenance, checklist, reference, decision, and archive directories.
- [x] 2026-03-28 | Added the first core system notes and reusable templates for SOP, equipment, maintenance log, checklist, and decision notes in `00_System/Templates/`.
- [x] 2026-03-28 | Updated the equipment and maintenance templates so tools and parts can carry buy links, replacement-part links, and repair-prep notes.
- [x] 2026-03-28 | Added a dedicated purchasing layer with `25_Purchasing/`, a reusable purchase template, a Bases-powered purchasing dashboard, and sync-safety guidance that preserves phone edits without introducing a separate Codex database.

## Suggested Recommendation Log
- 2026-03-27 | status: open | reasoning level: `medium` | Create a reusable note template for research and tool comparisons after 3-5 entries reveal the right common fields.
- 2026-03-27 | status: open | reasoning level: `medium` | Add a lightweight decision log once the first major tool or equipment choice is finalized in this repo.
- 2026-03-28 | status: open | reasoning level: `medium` | Add the first live truck inventory / consumables purchase notes with reorder thresholds using the new purchasing template once the first equipment notes exist so supplies do not become a separate untracked system.
- 2026-03-28 | status: open | reasoning level: `medium` | Add a chemical and materials reference note with approved uses, storage rules, and restrictions once pressure washing and window cleaning pilots are in place.
- 2026-03-28 | status: open | reasoning level: `medium` | Add a preferred-vendors note once repeated suppliers emerge so buy links can be standardized and maintained in one place when useful.
- 2026-03-28 | status: open | reasoning level: `medium` | Add QR-code or ID labels for major equipment after the asset register stabilizes so physical gear can be matched to notes faster in the field.
- 2026-03-28 | status: open | reasoning level: `medium` | Add a mobile field-capture workflow using Daily Notes, phone shortcuts, or QuickAdd after the core note templates are working so field lessons make it back into the system quickly.
- 2026-03-28 | status: open | reasoning level: `medium` | Add a web-clipping template for manuals, vendor pages, and equipment research after the decision-note pattern is stable so outside research lands in a consistent format.
- 2026-03-28 | status: completed | reasoning level: `medium` | Added `RETENTION_AND_ARCHIVE_POLICY.md` and linked the archive rules into the SOP system plan before pilot notes begin to accumulate clutter.

## Active Branch Ledger
### `main`
- status: active
- created: 2026-03-27
- base: `main`
- worktree: `/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs`
- source chat: 2026-03-27 "Bootstrap repository governance and starter docs"
- last refreshed by chat: 2026-03-28 "Add purchasing layer, purchase dashboard, and sync-safety guidance"
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
- 2026-03-28 | type: targeted remediation | scope: close the open architecture findings from the 2026-03-28 full audit | repo fingerprint: `Equipment & SOPs` `main` at `e8f8eba` before remediation commit | supporting implementation fingerprint: `Systems Command Center` `main` at `a1f1415` plus preferred Obsidian working copy on `main` | prior audit reference: 2026-03-28 full audit | source/work chat: current remediation chat | audit chat: same chat | implementation chat: same chat | separate follow-up audit: no, remediation and verification executed together | commands / evidence: `git diff --check`; `git -C '/Users/gillettes/Coding Projects/Systems Command Center' ls-files '.obsidian/plugins/**'`; `launchctl print gui/$(id -u)/com.gillettes.biz-sops-git-backup`; `tail -n 80 /Users/gillettes/.codex/log/biz-sops-git-backup.out.log`; direct repo-scoped run of `obsidian-vault-git-backup.sh`; `git status -sb` on canonical and parent repos | tested: canonical working-copy split, dedicated SOP backup lane, parent-vault plugin payload ignore cleanup, and archive-policy documentation | not tested: long-duration scheduled backup behavior over multiple days, pilot SOP template usability, or live Obsidian Tasks/Bases dashboards | findings opened or updated: overbroad whole-vault auto-push boundary closed; plugin payload churn closed; missing retention/archive rule closed | fixes closed / verified: dedicated SOP repo cloned into the preferred Obsidian path; parent vault ignores the SOP subtree and no longer tracks plugin install payload files; retention/archive policy documented and linked into the operating plan; dedicated SOP launch agent exits cleanly with code `0` | declined / deferred findings: dedicated SOP repo `.obsidian` policy remains deferred until local repo-specific config exists | better-path challenge: keep the dedicated SOP repo config-light and only add repo-local `.obsidian` files when a concrete field workflow needs them | references: current remediation chat, `RETENTION_AND_ARCHIVE_POLICY.md`, parent vault `.gitignore`, `a1f1415`, and the `biz-sops-git-backup` launch-agent logs
- 2026-03-28 | type: targeted implementation verification | scope: initial folder scaffold, system notes, and reusable templates in the preferred Obsidian working copy | repo fingerprint: `main` at `feb27f2` before scaffold commit | prior audit reference: 2026-03-28 targeted remediation | source/work chat: current template-build chat | audit chat: same chat | implementation chat: same chat | separate follow-up audit: no, implementation and verification executed together | commands / evidence: `find -maxdepth 3` on the preferred working copy; `git status -sb`; `git diff --check` | tested: folder scaffold creation, tracked empty-directory placeholders, core system notes, maintenance dashboard placeholder, and reusable SOP/equipment/maintenance/checklist/decision templates | not tested: actual Obsidian template insertion behavior, Tasks recurrence behavior inside live equipment notes, or pilot SOP usability in the field | findings opened or updated: none; execution matched the planned structure step | fixes closed / verified: initial folder structure created and tracked; naming/property/review notes created; reusable templates created in `00_System/Templates/` | declined / deferred findings: dashboard automation remains intentionally deferred until pilot notes exist | better-path challenge: keep dashboards lightweight until real pilot notes reveal which views are genuinely useful | references: current template-build chat
- 2026-03-28 | type: targeted implementation verification | scope: improve equipment and maintenance templates for vendor links, replacement parts, and repair-prep capture | repo fingerprint: `main` at `89bfdf3` before template refinement commit | prior audit reference: 2026-03-28 targeted implementation verification | source/work chat: current buy-link and repair-notes chat | audit chat: same chat | implementation chat: same chat | separate follow-up audit: no, template refinement and verification executed together | commands / evidence: `sed -n` on updated templates and system notes; `git status -sb`; `git diff --check` | tested: equipment template purchase-link sections, replacement-parts property, repair/failure-prep sections, maintenance-log repair capture sections, and plan/property documentation alignment | not tested: real vendor-link population in pilot notes or live field use of the repair sections | findings opened or updated: none; user-directed structure refinement | fixes closed / verified: equipment and maintenance templates now support multiple buy links, parts links, known-failure capture, and prevention notes | declined / deferred findings: no dedicated vendor index note yet; deferred until repeated suppliers justify it | better-path challenge: keep buy links primarily in note bodies until repeated use proves they need a more centralized system | references: current buy-link and repair-notes chat
- 2026-03-28 | type: targeted implementation verification | scope: add a dedicated purchasing layer, Bases dashboard, equipment procurement metadata, and sync-safety guidance for the preferred Obsidian working copy | repo fingerprint: `main` at `048f171` before purchasing-layer commit | prior audit reference: 2026-03-28 targeted implementation verification | source/work chat: current purchasing-system chat | audit chat: same chat | implementation chat: same chat | separate follow-up audit: no, user requested direct implementation in the same chat | commands / evidence: `sed -n` on updated system docs and templates; YAML parse of `25_Purchasing/Purchasing.base`; `git status -sb`; `git diff --check` | tested: purchasing folder and dashboard creation, purchase template and properties, equipment procurement metadata, README/plan/governance alignment, and repo formatting sanity | not tested: live Obsidian render of the embedded Bases views on desktop or phone, real phone-to-Mac sync timing, or pilot note usability in the field | findings opened or updated: active shopping state needed its own layer and sync guidance needed to prefer pull-before-edit over append-only restrictions | fixes closed / verified: dedicated `25_Purchasing/` added; active purchase state separated from reference notes; purchase metadata, templates, and dashboard views documented; sync safety clarified around the preferred working copy | declined / deferred findings: exact mobile sync transport remains unverified and is tracked as an active next step | better-path challenge: use dedicated purchase notes plus derived views instead of a single tracker note so service/category sorting stays queryable without maintaining duplicate lists | references: current purchasing-system chat

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
- 2026-03-28 | command(s): `git diff --check`; `git -C '/Users/gillettes/Coding Projects/Systems Command Center' ls-files '.obsidian/plugins/**'`; `launchctl print gui/$(id -u)/com.gillettes.biz-sops-git-backup`; `tail -n 80 /Users/gillettes/.codex/log/biz-sops-git-backup.out.log`; direct repo-scoped run of `obsidian-vault-git-backup.sh`; `git status -sb` on the parent vault, preferred Obsidian working copy, and coordination clone | result: pass; plugin payload tracking is empty in the parent vault, the dedicated SOP backup lane exits cleanly with code `0`, and both repos are in a clean synced state | log/PR reference: current remediation chat and parent vault commit `a1f1415`
- 2026-03-28 | command(s): `find '/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs' -maxdepth 3`; `git -C '/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs' status -sb`; `git -C '/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs' diff --check` | result: pass; the folder scaffold and template files exist in the preferred working copy and the resulting diff is formatting-clean | log/PR reference: current template-build chat
- 2026-03-28 | command(s): `sed -n` on `00_System/Templates/Equipment Template.md`, `00_System/Templates/SOP Template.md`, `00_System/Templates/Maintenance Log Template.md`, `00_System/Tags and Properties.md`, and `SOP_SYSTEM_PLAN.md`; `git -C '/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs' diff --check` | result: pass; template and system docs now include multiple buy-link support plus repair/failure-prep capture without introducing duplicate maintenance date fields | log/PR reference: current buy-link and repair-notes chat
- 2026-03-28 | command(s): `sed -n` on updated README, intent, AGENTS, plan, templates, and dashboard files; `ruby -e 'require "yaml"; YAML.load_file("25_Purchasing/Purchasing.base")'`; `git -C '/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs' status -sb`; `git -C '/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs' diff --check` | result: pass; purchasing docs/templates align, the `.base` file is valid YAML, and the preferred working copy diff is formatting-clean | log/PR reference: current purchasing-system chat

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
- 2026-03-28 | feedback source: Claude | feedback summary: use a single `50_Reference/Purchase Tracker.md`, add `purchase_status` on equipment notes, and make automation append-only so phone edits are never overwritten | evaluation chat: current purchasing-system chat | reasoning response: accepted the need for a dedicated purchasing layer and secondary equipment procurement metadata, but rejected `50_Reference/` as the active queue location and rejected append-only editing in favor of preferred-working-copy plus sync-before-edit safety rules | decision status: partial | implementation/disposition chat: current purchasing-system chat | linked branch / audit / suggestion / test evidence: 2026-03-28 targeted implementation verification entry, updated Active Next Steps, and 2026-03-28 purchasing-layer test evidence
