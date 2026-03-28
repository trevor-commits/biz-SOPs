# PROJECT_INTENT

## Purpose
Maintain a durable, searchable knowledge base for business research, equipment decisions, software/tool evaluations, and SOPs for Gillette Window & Solar Cleaning.

## Problem Statement
Operational knowledge is otherwise scattered across chats, bookmarks, emails, and memory. That makes it harder to compare tools, repeat processes consistently, and reuse prior research when making business decisions.

## Target Users and Top Jobs
- Primary users: Trevor Gillette as owner-operator.
- Secondary users: future assistants, contractors, or AI helpers who need to understand past decisions and current operating procedures.
- Top jobs:
  - Capture and retrieve research on the best way to do recurring business tasks.
  - Compare tools, vendors, and equipment before spending money or changing workflow.
  - Turn proven ways of working into repeatable SOPs.

## In-Scope Outcomes
- Document repeatable business processes in plain language.
- Preserve research findings with enough context to reuse later.
- Track equipment and software decisions with rationale.
- Reduce repeated research on the same business questions.

## Non-Goals
- This repo is not the operational system of record for scheduling, invoicing, CRM, or accounting.
- This repo is not a dumping ground for unsorted raw notes with no retained value.
- This repo is not intended to store secrets, credentials, or customer-sensitive information.

## Success Metrics and Guardrails
- Leading metrics:
  - New research or SOP notes are captured in this repo instead of being left only in chat history.
  - Important tool decisions include recommendation, reasoning, and source links.
- Lagging metrics:
  - Less repeated research on the same question.
  - Faster decision-making for equipment and software purchases.
  - More consistent execution of recurring business tasks.
- Guardrails:
  - No secrets or customer PII in tracked files.
  - Prefer concise Markdown over heavyweight systems unless scale clearly demands more.
  - Keep notes practical and decision-oriented rather than academic.

## Primary Journeys and Navigation Model
- Research capture: identify a business question, create or update a note, summarize findings, and record the recommendation.
- Tool evaluation: compare options, note tradeoffs, record the current best choice, and track follow-up questions.
- SOP creation: convert a working process into a step-by-step procedure that can be reused or handed off.

## Content and Wording Principles
- Use plain, practical wording oriented around business decisions and real field work.
- Prefer direct titles such as "Best CRM follow-up workflow" or "Solar panel cleaning ladder setup SOP".
- Separate facts, observations, and recommendations clearly.
- Include source context when the note depends on outside research.

## Technical Strategy and Stack Rationale
- Current project type: `docs`
- Why this stack now: Markdown in git is lightweight, searchable, versioned, and easy to maintain as a solo operator without adding tool overhead.

## Constraints, Assumptions, Risks, and Invalidation Triggers
- Constraints:
  - Must stay easy to update without adding admin burden.
  - Should remain useful from a laptop-first workflow and still be easy to reference quickly.
- Assumptions:
  - Most content will be short Markdown notes rather than structured database records.
  - The repo will grow gradually and taxonomy can evolve from actual usage.
- Risks:
  - Notes become inconsistent or duplicated if no simple capture pattern is followed.
  - Research can go stale if decisions are not revisited when tools or pricing change.
  - Over-structuring too early could slow down capture.
- Invalidation triggers:
  - If retrieval becomes difficult across many notes, introduce folders, indexes, or templates.
  - If collaboration grows materially, add clearer ownership/review conventions.
  - If richer metadata is required, evaluate a structured system beyond plain Markdown.

## Operability and Quality Bar
- Reliability/diagnosability: notes should be versioned, readable in plain text, and easy to diff.
- Security/privacy: never store secrets, payment data, or customer PII in this repo.
- Accessibility/mobile/responsive needs: content should stay concise, scan-friendly, and readable on mobile GitHub or editor views.

## Open Questions and Decision Records
- Decide the eventual top-level taxonomy once a first set of real notes exists.
- Decide whether tool evaluations and SOPs should live in separate folders or remain mixed until scale requires separation.
- Add decision-record links here if the repo later adopts ADRs or dedicated decision logs.
