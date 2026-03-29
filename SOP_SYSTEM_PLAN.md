# SOP, Equipment, and Maintenance System Plan

## Objective
Build a low-overhead operating system for Gillette Window & Solar Cleaning that makes it easy to:
- document exactly how work should be done
- track what equipment exists and where it is used
- track maintenance schedules and completed maintenance
- keep the information readable in Git and practical inside Obsidian
- add new procedures without rebuilding the system each time

## Recommended Operating Model

### Source of truth
- Treat the `biz-SOPs` Git repository as the canonical project identity.
- Preferred operational working copy: `/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs`.
- Secondary local clones may exist for coordination or tooling, but they are not separate sources of truth.
- Use Obsidian as the primary editing, browsing, and dashboard interface.
- Do not maintain a second separate copy of the same SOPs outside clones of the same Git repo.

### Recommended Obsidian setup
Recommended default:
1. Keep the preferred working copy inside the existing `Systems Command Center` vault at `/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs`.
2. Treat that folder as the live content location inside Obsidian.
3. Point any SOP-specific Daily Notes workflow at `00_System/Daily Notes/` inside this repo so field capture stays inside the same Git-backed project boundary.
4. Let Git history provide versioning and backup for the dedicated SOP repo without making the entire mixed personal vault the canonical SOP store.

## Design Principles
- One note, one purpose. Do not mix SOP steps, maintenance logs, and purchase research in the same file unless there is a strong reason.
- Keep capture fast. Required metadata should be minimal and useful.
- Separate "master SOP" from "job checklist". The SOP explains the full process. The checklist is the field-use quick reference.
- Link everything. SOPs should link to equipment notes, and equipment notes should link back to the SOPs that use them.
- Record maintenance once. Avoid duplicate maintenance trackers in notes, spreadsheets, and reminders unless one is explicitly read-only.
- Standardize names and IDs early. This prevents later cleanup pain.
- Prefer official/core Obsidian features first. Add community plugins only when they clearly reduce workload.

## Recommended Folder Structure
Use a small, stable folder taxonomy so the vault remains easy to scan on desktop and mobile.

```text
00_System/
  Dashboard.md
  Daily Notes/
  Naming Conventions.md
  Tags and Properties.md
  Review Cadence.md
  Templates/

10_SOPs/
  Window Cleaning/
  Pressure Washing/
  Solar Cleaning/
  Gutters/
  Truck and Shop/

20_Equipment/
  Water Fed/
  Pressure Washing/
  Ladders/
  Hand Tools/
  PPE/
  Vehicle/

30_Maintenance/
  Dashboard.md
  Logs/
  Seasonal/

40_Checklists/
  Daily/
  Service Specific/
  Safety/

50_Reference/
  Chemicals and Materials/
  Safety Rules/
  Vendor Notes/
  Troubleshooting/

60_Decisions/
  Equipment/
  Process/

90_Archive/
```

## Core Note Types

### 1. SOP notes
Use for the full start-to-finish process for one repeatable task.

Examples:
- `Window Cleaning - Exterior Residential SOP`
- `Pressure Washing - Driveway SOP`

Mandatory sections:
- Purpose
- When to use this SOP
- Required equipment and consumables
- PPE and safety warnings
- Pre-job checks
- Step-by-step procedure
- Quality standard / definition of done
- Post-job cleanup and reset
- Equipment care after use
- Job interruption / repair response
- Dos and don'ts
- Common mistakes and troubleshooting
- Review history

### 2. Equipment notes
Use for one physical asset, tool family, or standardized kit.

Examples:
- `EQ-PW-001 - Pressure Washer`
- `EQ-WC-003 - Unger Squeegee Kit`

Mandatory sections:
- Asset summary
- Where it is used
- Required accessories / consumables
- Purchase and replacement links
- Operating notes
- Routine maintenance schedule
- Repair and failure prep
- Troubleshooting
- Storage instructions
- Retirement / replacement triggers
- Maintenance history

### 3. Maintenance log notes
Use for completed maintenance events that are more important than a quick checkbox.

Best for:
- repairs
- oil changes
- hose replacements
- pump servicing
- recurring maintenance with notes or photos
- documenting the actual failure symptoms, suspected cause, and prevention notes after a problem

Small per-use maintenance can stay inline on the equipment note. Larger work should get its own log note and be linked back to the equipment note.

### 4. Checklist notes
Use for quick field execution.

Examples:
- `Pressure Washing - Pre-Job Checklist`
- `Truck - End of Day Reset Checklist`

These should be short, scannable, and usable from a phone.

### 5. Reference notes
Use for support information that is not itself a procedure.

Examples:
- dilution ratios
- stain treatment reference
- ladder safety reminders
- Sacramento seasonal maintenance notes

### 6. Decision notes
Use for purchase or process decisions.

Examples:
- why one surface cleaner was chosen over another
- why a chemical was approved, rejected, or deferred

## Standard Properties
Use Obsidian properties/frontmatter to keep notes queryable.

Common properties for most note types:

```yaml
---
type:
status:
owner: Trevor
created:
last_reviewed:
next_review:
tags:
---
```

Recommended note-type-specific properties:

### SOP properties

```yaml
---
type: sop
status: draft
service:
task:
equipment_ids:
ppe:
estimated_duration:
season:
last_reviewed:
next_review:
---
```

### Equipment properties

```yaml
---
type: equipment
asset_id:
category:
brand:
model:
serial_number:
status: active
purchase_date:
warranty_until:
storage_location:
related_sops:
---
```

### Maintenance log properties

```yaml
---
type: maintenance-log
asset_id:
maintenance_type:
performed_on:
performed_by:
cost:
---
```

## Naming and ID Conventions
- Use stable asset IDs for physical equipment. Example: `EQ-PW-001`, `EQ-WC-004`, `EQ-VEH-001`.
- Put the asset ID at the start of equipment note titles so search results stay predictable.
- Keep SOP titles written in plain language around the job being performed, not internal shorthand.
- Keep checklist names short and field-oriented.

## Recommended SOP Format
Each SOP should answer four questions:
1. What is the job?
2. What do I need?
3. What do I do, in order?
4. What does "done right" look like?

Recommended SOP body:

```md
# Pressure Washing - Driveway SOP

## Purpose

## Scope / When To Use

## Required Equipment

## PPE and Safety

## Pre-Job Checks

## Procedure
### 1. Arrival and setup
### 2. Site prep
### 3. Cleaning pass
### 4. Detail work
### 5. Rinse and finish

## Quality Standard

## Post-Job Cleanup and Equipment Care

## Dos and Don'ts

## Common Problems and Fixes

## Review History
```

## Recommended Equipment Note Format

```md
# EQ-PW-001 - Pressure Washer

## Summary

## Used For

## Required Accessories

## Operating Notes

## Maintenance Schedule
- Per use:
- Weekly:
- Monthly:
- Quarterly:
- Annual:

## Troubleshooting

## Storage

## Replacement Criteria

## Maintenance History
```

## Maintenance Tracking Model
Use a three-layer model so maintenance is clear without becoming over-administered. Canonical due-state lives in recurring Tasks inside the equipment note, not in duplicate frontmatter date fields.

### Layer 1: Equipment note = canonical maintenance home
Each equipment note should contain:
- the equipment metadata
- the maintenance instructions
- purchase links for the main tool and common replacement parts
- known failure points, spare parts to keep, and repair-prep notes
- recurring Tasks for each scheduled maintenance action
- links to any maintenance log notes that add detail

### Layer 2: Maintenance dashboard = what needs attention now
The maintenance dashboard should be built from Tasks queries and should show:
- overdue maintenance tasks
- due in next 7 days
- due in next 30 days
- recently completed maintenance tasks

### Layer 3: Maintenance logs = proof and details
Create a maintenance log note when the work needs detail, cost, photos, or repair notes.

## Obsidian Workflow

### Recommended minimum stack
Start with the lowest-overhead toolset that still gives structure and automation.

Core Obsidian features:
- Properties
- Templates
- Daily Notes
- Bases
- Obsidian Web Clipper

Recommended community plugin:
- Tasks

Optional later:
- QuickAdd
- Templater

Why this stack:
- Obsidian Properties provide typed metadata in Markdown notes.
- Bases is now a core plugin for database-like views over note properties.
- Templates reduce note-creation friction.
- Daily Notes give a place to capture same-day observations that can later be promoted into SOP, equipment, or maintenance notes. For this system, keep that Daily Notes folder inside the SOP repo so it stays within the same backup and archive boundary.
- Obsidian Web Clipper can save vendor pages, manuals, and product research into structured Markdown notes using templates.
- Tasks supports recurring tasks, due dates, filtering, and updating the source task from query views.
- QuickAdd can make mobile capture faster, but it is not required on day one.
- Templater is powerful, but it can execute arbitrary JavaScript and system commands, so it should be added only when the simpler template flow becomes limiting.

## Automation Approach
Do not start with custom scripts. Start with structured notes plus dashboard automation.

### Day-one automation
- Templates create standardized notes.
- Bases views create equipment registers and SOP indexes from note properties.
- Tasks queries create overdue and upcoming maintenance views from recurring Tasks embedded in equipment notes.
- Daily Notes plus phone capture shortcuts create a low-friction path to capture field observations without opening a full SOP note.
- Keep any repo-specific Daily Notes in `00_System/Daily Notes/` so capture, review, archive, and backup all stay inside the same project.

### Later automation if needed
- QuickAdd for one-tap note creation from phone.
- Templater for more dynamic note creation or auto-filled frontmatter.
- Web Clipper templates for manuals, vendor pages, and research capture if the basic decision-note flow becomes repetitive.
- Optional script-generated dashboards if built-in views become insufficient.

## Recommended Dashboards

### 00_System/Dashboard.md
Should surface:
- recently updated SOPs
- SOPs due for review
- equipment recently added or changed
- open decision notes

### 30_Maintenance/Dashboard.md
Should surface:
- overdue maintenance
- due this week
- due this month
- recently completed maintenance
- equipment notes missing recurring maintenance Tasks

## Pilot Rollout
Do not try to document everything at once. Start with two service lanes and prove the pattern.

### Pilot 1: Window cleaning
Create:
- one full window cleaning SOP
- one field checklist
- equipment notes for the main kit
- maintenance schedules for the main kit

### Pilot 2: Pressure washing
Create:
- one full pressure washing SOP
- one field checklist
- equipment notes for the pressure washer and core accessories
- maintenance schedules for those assets

After the pilots, review friction:
- Which properties were actually used?
- Which sections stayed empty?
- Which notes were annoying to update?
- Which dashboards helped in practice?

Then simplify before scaling.

## Review Cadence
- Daily or job-day: capture issues, mistakes, or improvements in Daily Notes.
- Weekly: review maintenance dashboard and promote any important field learnings into permanent notes.
- Monthly: review high-use equipment and restock/repair needs.
- Quarterly: review active SOPs and update anything that drifted.
- Seasonally: review service-specific SOPs before the relevant demand season.

## Retention and Archive Rules
- Keep current SOPs, equipment notes, active reference notes, and final decision notes live.
- Keep recurring maintenance due-state in Tasks inside equipment notes. Use maintenance log notes only when detail, cost, photos, or incident history matters.
- Review repo-scoped Daily Notes weekly and move reviewed notes older than 30 days into `90_Archive/Daily Notes/YYYY/`.
- Move detailed logs for retired equipment into `90_Archive/Maintenance/<asset-id>/` after the equipment note records the retirement summary.
- Move stale comparison notes, clipped manuals, and superseded SOP drafts into the appropriate `90_Archive/` area once the durable live note captures the final conclusion.
- Delete empty Daily Notes, duplicate media, and context-free photos instead of archiving them.
- Canonical detailed policy lives in `RETENTION_AND_ARCHIVE_POLICY.md`.

## What This System Should Contain

### Service execution
- master SOPs for each recurring service
- quick field checklists
- quality standards
- safety rules
- common failure modes

### Equipment management
- asset register
- accessories and consumables
- maintenance schedules
- repair history
- replacement criteria

### Operations support
- truck loadout and reset checklists
- restock thresholds
- seasonal prep and shutdown notes
- vendor references
- purchasing decisions

## High-Value Additions To Consider
- A photo standard note for before/after documentation.
- A chemical and materials reference with approved uses, storage rules, and restrictions.
- A truck inventory note with reorder thresholds for common consumables.
- A "new tool evaluation" template so purchases are compared consistently.
- A preferred-vendors note so repeated buy links can be standardized if the same suppliers keep coming up.
- A web-clipping template for saving manuals, vendor pages, and comparison research into the correct note type automatically.
- A training/readiness checklist for any future helper or contractor.
- A safety incident / near-miss log for anything worth learning from.
- QR labels on major equipment that point to the matching equipment note title or ID.

## Anti-Headache Rules
- Avoid one giant "everything" SOP. Split by job type or phase.
- Avoid duplicate maintenance trackers in both notes and spreadsheets unless one is explicitly a derived reporting view.
- Avoid overloading frontmatter with fields you never query.
- Avoid custom automation before the basic note pattern proves useful.
- Avoid hiding critical knowledge in daily notes only. Promote durable information into permanent notes.

## Implementation Sequence
1. Work from the preferred Obsidian clone at `/Users/gillettes/Coding Projects/Systems Command Center/Gillette Window & Solar Cleaning/SOPs`.
2. Create folder structure and templates.
3. Define note properties and naming standards.
4. Build the two pilot SOP systems: window cleaning and pressure washing.
5. Build the equipment register and maintenance dashboard.
6. Review friction and simplify before scaling to other services.

## Source Notes
- Obsidian Help: https://help.obsidian.md/
- Obsidian for iOS and iPadOS: https://help.obsidian.md/ios
- Obsidian Tasks plugin: https://github.com/obsidian-tasks-group/obsidian-tasks
- QuickAdd: https://quickadd.obsidian.guide/
- Templater: https://github.com/SilentVoid13/Templater
