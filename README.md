# Equipment & SOPs

This repository backs the SOP, equipment, and maintenance system for Gillette Window & Solar Cleaning.

Preferred operational working copy:
- `/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs`

Secondary coordination clone:
- `/Users/gillettes/Coding Projects/Equipment & SOPs`

The Git repo identity is the source of truth. The preferred Obsidian working copy is where live SOP content should be edited.

## What belongs here
- SOP drafts and finalized process docs.
- Equipment notes with recurring maintenance tasks.
- Checklists, maintenance logs, and decision notes that support those SOPs.
- Supporting vendor/tool/process references that have durable operational value.

## What does not belong here
- Secrets, tokens, passwords, or customer PII.
- Raw exports that can be regenerated elsewhere unless they are needed as evidence.
- One-off scratch notes that have no decision, instruction, or reference value.

## Suggested content pattern
Use Markdown files and keep each note focused on one topic. Keep equipment metadata in properties and keep recurring maintenance due-state in Tasks inside the equipment note.

Recommended sections for new notes:
1. Goal
2. Current options or process
3. Findings
4. Recommendation
5. Evidence or source links
6. Next action

## Practical starting categories
- SOPs
- Equipment
- Maintenance logs
- Checklists
- Decision notes

## Working conventions
- Prefer plain, scannable filenames.
- If Daily Notes are used for this system, point them at `00_System/Daily Notes/` inside the SOP repo so field capture stays inside the same Git-backed project boundary.
- Include the date and source context when capturing research.
- When a decision is made, record the reason so the same research does not need to be repeated later.
- When an SOP becomes stable, keep it action-oriented and ordered step by step.
- Apply `RETENTION_AND_ARCHIVE_POLICY.md` so Daily Notes, maintenance logs, and supporting media do not turn into long-term clutter.

## Core project files
- `PROJECT_INTENT.md`: canonical statement of repo purpose and scope.
- `todo.md`: active next steps, recommendations, audit history, and test evidence.
- `AGENTS.md`: repository-local execution rules for AI-assisted work.
- `RETENTION_AND_ARCHIVE_POLICY.md`: archive and retention rules for Daily Notes, maintenance logs, research inputs, and media.
