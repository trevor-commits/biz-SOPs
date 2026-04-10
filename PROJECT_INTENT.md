# PROJECT_INTENT

## Purpose
Maintain a durable, searchable, Obsidian-native SOP and equipment system for Gillette Window & Solar Cleaning, backed by the `biz-SOPs` Git repository.

## Problem Statement
Operational knowledge is otherwise scattered across chats, bookmarks, emails, and memory. That makes it harder to repeat processes consistently, maintain equipment on time, and reuse prior decisions without reopening the same research.
Service definitions are also trapped inside the CRM export unless they are promoted into a durable, searchable catalog inside the same Obsidian system.

## Target Users and Top Jobs
- Primary users: Trevor Gillette as owner-operator.
- Secondary users: future assistants, contractors, or AI helpers who need to understand past decisions and current operating procedures.
- Top jobs:
  - Capture, clean up, and reuse customer-facing service descriptions without leaving them trapped in the CRM.
  - Capture and retrieve the exact way recurring field work should be done.
  - Track equipment, maintenance cadence, and supporting checklists in one place.
  - Track what must be bought now, what can wait, and what should be reordered routinely.
  - Compare tools, vendors, and process decisions before spending money or changing workflow.

## In-Scope Outcomes
- Document repeatable business processes in plain language.
- Maintain a service catalog that is traceable back to CRM source data but readable as Obsidian notes.
- Track equipment and maintenance schedules with enough structure to review due work quickly.
- Track urgent purchases, deferred purchases, and consumable restock needs without a separate system.
- Preserve process and purchasing decisions with enough context to reuse later.
- Reduce repeated research and repeated "how do I do this?" thinking on the same operational questions.

## Non-Goals
- This repo is not the operational system of record for scheduling, invoicing, CRM, or accounting.
- This repo is not a dumping ground for unsorted raw notes with no retained value.
- This repo is not intended to store secrets, credentials, or customer-sensitive information.

## Success Metrics and Guardrails
- Leading metrics:
  - New SOPs, equipment notes, and maintenance schedules are captured in the preferred Obsidian working copy instead of living only in chat history or memory.
  - Active buy-now, soon, later, and consumable restock items are visible from the same Obsidian project used for SOPs.
  - Important process or tool decisions include recommendation, reasoning, and source context.
- Lagging metrics:
  - Less repeated research on the same operational question.
  - More consistent execution of recurring business tasks.
  - Fewer missed maintenance tasks or forgotten equipment setup details.
- Guardrails:
  - No secrets or customer PII in tracked files.
  - Prefer concise Markdown over heavyweight systems unless scale clearly demands more.
  - Keep notes practical and decision-oriented rather than academic.

## Primary Journeys and Navigation Model
- SOP creation: convert a working process into a step-by-step procedure plus a short field checklist.
- Service catalog management: convert CRM rows into durable Markdown notes, flag weak copy, and link approved service notes to future SOPs and add-ons.
- Equipment management: document an asset, link it to related SOPs, and keep recurring maintenance tasks in the equipment note.
- Purchasing management: capture urgent buys, replacements, and restock needs in dedicated purchase notes that can be grouped by service, category, and urgency.
- Decision capture: compare options, note tradeoffs, record the current best choice, and track follow-up questions.

## Content and Wording Principles
- Use plain, practical wording oriented around business decisions and real field work.
- Prefer direct titles such as "Best CRM follow-up workflow" or "Solar panel cleaning ladder setup SOP".
- Separate facts, observations, and recommendations clearly.
- Include source context when the note depends on outside research.

## Technical Strategy and Stack Rationale
- Current project type: `docs`
- Why this stack now: a dedicated Git repository cloned directly into the Obsidian vault gives low-overhead editing, local portability, version history, and a clean boundary around the business SOP system without making the entire mixed personal vault the source of truth.

## Constraints, Assumptions, Risks, and Invalidation Triggers
- Constraints:
  - Must stay easy to update without adding admin burden.
  - Must have one canonical repo identity and one preferred operational working copy to avoid split-brain edits.
  - Secondary local clones should stay subordinate to the preferred working copy and should not be treated as separate live-edit surfaces or automatic mirrors.
  - Should remain easy to reference from Obsidian on desktop and mobile.
- Assumptions:
  - Most content will be Markdown notes plus lightweight frontmatter.
  - Equipment metadata can stay lightweight while recurring maintenance due-state lives in Tasks inside equipment notes.
  - Active purchasing state can live in purchase notes and Bases views without needing a separate database.
- Risks:
  - Content becomes inconsistent or duplicated if notes are edited in multiple local copies without a declared primary working copy.
  - Maintenance state drifts if due dates are stored in more than one place.
  - Purchase state drifts if active shopping items are duplicated across reference notes, daily notes, and equipment notes.
  - Unattended backup automation can push a destructive edit too quickly if major deletions are not reviewed first.
  - Over-structuring too early could slow down capture.
- Invalidation triggers:
  - If retrieval becomes difficult across many notes, refine the folder structure, indexes, or templates.
  - If collaboration grows materially, add clearer ownership/review conventions.
  - If richer metadata is required, evaluate a structured system beyond plain Markdown.

## Operability and Quality Bar
- Reliability/diagnosability: notes should be versioned, readable in plain text, and easy to diff.
- Security/privacy: never store secrets, payment data, or customer PII in this repo.
- Accessibility/mobile/responsive needs: content should stay concise, scan-friendly, and readable on mobile GitHub or editor views.

## Open Questions and Decision Records
- Add a retention and archive rule for Daily Notes, photos, and maintenance logs before the pilot system scales.
- Decide which `.obsidian` files belong in the dedicated SOP repo versus local-only machine state.
- Add decision-record links here if the repo later adopts ADRs or dedicated decision logs.
