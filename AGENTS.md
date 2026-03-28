# AGENTS.md (Equipment & SOPs)

## Scope
Repository-local execution policy for `/Users/gillettes/Coding Projects/Equipment & SOPs`.
Use this with global policy in `/Users/gillettes/.codex/AGENTS.md`.

## Repository Lineage
- Lineage status: `canonical`.
- Authoritative repo path: `/Users/gillettes/Coding Projects/Equipment & SOPs`.
- If project scope/runtime changes materially, refresh this file, `PROJECT_INTENT.md`, and the root `todo.md` testing cadence in the same change.

## Stack and Runtime
[MANDATORY_STACK_RUNTIME] stack/runtime profile, risk areas, release gates, boundaries, rollback/ops checks

- Stack/runtime profile:
  - Documentation-first repository for business research, tool evaluations, equipment notes, and SOPs.
  - Primary release surface is the readability, accuracy, and long-term usefulness of the Markdown knowledge base plus any helper automation added later.
- Primary risk areas:
  - stale or conflicting recommendations across research notes and SOPs
  - tool comparisons that omit rationale, date context, or source evidence
  - SOP drift where documented steps no longer match the real workflow
- Release gates:
  - run `git diff --check` for formatting sanity on doc-only changes
  - run the repo-specific docs lint/spellcheck/render command once configured
  - record example/template output checks when templates or automation change
  - keep policy and helper-script changes small, scoped, and verifiable
- Boundaries:
  - keep changes scoped to this project unless the user explicitly widens the scope
  - prefer no-new-dependency solutions unless the new dependency materially improves reliability or delivery
  - do not change deployment, infrastructure, or secret-handling behavior without explicit intent and verification evidence
- Rollback/ops checks:
  - uncommitted rollback: `git restore -- <path>`
  - committed rollback: `git revert <sha>`
  - document any project-specific smoke, health, or deploy rollback path when release behavior changes

## Operating Principles
[MANDATORY_OPERATING_PRINCIPLES] operating principles aligned to `OPERATING_PRINCIPLES.md`

- Apply `/Users/gillettes/.codex/policies/OPERATING_PRINCIPLES.md` hierarchy first.
- Prefer evidence-first changes and reversible edits.
- Keep solutions reliable, scoped, and easy to verify.

## Intent Alignment
[MANDATORY_PROJECT_INTENT] canonical project intent documentation + behavior aligned to `PROJECT_INTENT_ALIGNMENT.md`

- Canonical intent doc: `/Users/gillettes/Coding Projects/Equipment & SOPs/PROJECT_INTENT.md`.
- Refresh this AGENTS runtime profile, release gates, risk areas, docs map, and testing cadence when scope/runtime changes materially.

## Docs Map
- `/Users/gillettes/Coding Projects/Equipment & SOPs/README.md`.
- `/Users/gillettes/Coding Projects/Equipment & SOPs/PROJECT_INTENT.md`.
- `/Users/gillettes/Coding Projects/Equipment & SOPs/todo.md`.
- Add research notes, comparison templates, SOP folders, and decision logs here as they become canonical.

## Todo Governance
[MANDATORY_TODO_ADD] add follow-up work to project `todo.md`
[MANDATORY_TODO_SUGGESTIONS] maintain a persistent `Suggested Recommendation Log` in `todo.md`; record every materially new suggested action there, avoid duplicate entries by reusing matching items, keep history instead of deleting entries, and check items off when completed
[MANDATORY_TODO_CHECKOFF] auto-check completed verified `todo.md` items
[MANDATORY_PLAN_TRACKING] capture durable chat-created plans in `todo.md` by recording the overall goal plus concrete steps, then mark them complete in the same file/log when verified
[MANDATORY_FEEDBACK_DECISIONS] maintain a durable `Feedback Decision Log` in root `todo.md`; record outside feedback, the reasoning response, final decision, and any linked implementation/audit/test evidence there; update existing entries instead of duplicating the same feedback thread
[MANDATORY_TESTING_GOVERNANCE] testing is required delivery evidence; keep `Test Evidence Convention`, `Test Evidence Log`, and `Testing Cadence Matrix` in root `todo.md`, and document what ran or what remains untested
[MANDATORY_BRANCH_LIFECYCLE] maintain `Active Branch Ledger` and `Branch History` in root `todo.md`; every non-trivial branch must record purpose, responsible/source chat, last refreshed by chat, merge expectation, exit checklist, delete-vs-retain outcome, retain reason when applicable, and delete/cleanup trigger

- Track actionable work in `/Users/gillettes/Coding Projects/Equipment & SOPs/todo.md` with priority, owner, and target date.
- When an audit creates actionable execution work, put those items at the top of `Active Next Steps` in dependency order; keep deferred, optional, or not-yet-execution-ready audit recommendations in `Suggested Recommendation Log`.
- Keep audit records durable: show source/work chat, audit chat, implementation/disposition chat, tested scope, not-tested scope, findings, disposition, and verification evidence.
- Keep outside feedback decisions durable in `Feedback Decision Log` so the same reasoning trail can be reused later.

## Worktree and Concurrency
[MANDATORY_WORKTREE] one-worktree-per-chat rule for concurrent chats in same repo

- Use one worktree per concurrent non-trivial chat.
- For non-trivial work, record branch purpose and expected merge/delete conditions in `todo.md` before deep implementation.
- Stay on the current checkout by default when scope is clear and rollback is straightforward; create a feature branch and usually a dedicated worktree only when risk, concurrency, or separate merge timing justifies isolation.

## Pragmatic Delivery
[MANDATORY_PRAGMATIC] pragmatic improvement mindset

- Favor small, reversible reliability improvements over broad rewrites.

## Audit and Planning
[MANDATORY_FULL_AUDIT] full-audit behavior aligned to `FULL_AUDIT.md`
[MANDATORY_NEXT_STEPS] next-steps behavior aligned to `NEXT_STEPS_ORCHESTRATION.md`, including `todo.md`-grounded and independently inferred recommendations with a reasoning level for every suggested item; when an audit or the current chat creates or discovers more urgent execution-ready work, move those items to the top of `Active Next Steps` and reserve `Suggested Recommendation Log` for deferred, optional, or not-yet-execution-ready items; if none remain, explicitly state `No further steps required.`

- Full audits follow `/Users/gillettes/.codex/policies/FULL_AUDIT.md`.
- Non-trivial implementation should receive a separate follow-up audit chat unless explicitly waived; if waived or blocked, record that in the audit trail.

## Clarification and Safety
[MANDATORY_CLARIFY] ask focused clarifying question(s), explain the conflict/misalignment, and pause risky changes until clarified

- Ask clarifying questions only when scope, conflict, or risk prevents safe execution.

## Credit and Verification Posture
[MANDATORY_CREDIT_IMPACT] prioritize correctness/reliability and flag significant low-upside credit waste with efficient reliable alternatives
[MANDATORY_NO_COMMIT_BLOCK] verification commands provide evidence and do not block commits/pushes unless the user explicitly requests strict gates

- Verification evidence is mandatory in handoff notes for repository changes.
- For research docs, verification should usually include source review, date context when relevant, and a quick sanity check for contradictory guidance in related notes.

## Execution Defaults
[MANDATORY_NO_APPROVAL_PROMPTS] execute requested actions end-to-end without repeated approval prompts; ask only when blocked by platform constraints or missing requirements
[MANDATORY_IGNORE_UNRELATED_CHANGES] treat unrelated tracked edits as valid concurrent work; do not block execution/cleanup, and never revert them unless explicitly requested
[MANDATORY_COMMIT_OWN_CHANGES] commit every file edited in the current task before completion unless the user explicitly says not to; never let unrelated dirty state prevent committing task files
[MANDATORY_AUTO_PUSH] after edits in a git repository, automatically commit and push every task-touched file that remains changed unless the user explicitly says not to push; if push fails, stop and report the exact failing command/output
[MANDATORY_TASK_CLASSIFICATION] classify task tier per `TASK_CLASSIFICATION.md`; match verification depth and playbook loading to tier

- Execute directly for implementation requests.
- Keep unrelated tracked changes intact.
