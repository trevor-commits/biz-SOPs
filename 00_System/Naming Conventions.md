# Naming Conventions

## Goals
- Keep names easy to scan on mobile.
- Keep search results stable.
- Make file names descriptive without being long.

## General Rules
- Use title case for note titles.
- Prefer full service names over unclear abbreviations.
- Keep dates in `YYYY-MM-DD` format.
- Do not put version numbers in filenames. Track changes in the note body instead.
- Do not use customer names, addresses, or other sensitive job-specific details in reusable SOP notes.

## Note Naming Standards

### SOPs
Pattern:
- `<Service> - <Task> SOP`

Examples:
- `Window Cleaning - Exterior Residential SOP`
- `Pressure Washing - Driveway SOP`

### Equipment
Pattern:
- `<Asset ID> - <Common Name>`

Examples:
- `EQ-WC-001 - Water Fed Pole`
- `EQ-PW-001 - Pressure Washer`
- `EQ-VEH-001 - Work Truck`

### Checklists
Pattern:
- `<Scope> - <Purpose> Checklist`

Examples:
- `Truck - End of Day Reset Checklist`
- `Pressure Washing - Pre-Job Checklist`

### Maintenance Logs
Pattern:
- `YYYY-MM-DD - <Asset ID> - <Maintenance Event>`

Examples:
- `2026-03-28 - EQ-PW-001 - Pump Oil Change`
- `2026-03-28 - EQ-WC-001 - Hose Fitting Replacement`

### Decision Notes
Pattern:
- `YYYY-MM-DD - <Decision Topic>`

Examples:
- `2026-03-28 - Surface Cleaner Evaluation`
- `2026-03-28 - Soft Wash Chemical Approval`

### Daily Notes
Pattern:
- `YYYY-MM-DD`

Example:
- `2026-03-28`

## Asset ID Standard
- `EQ` = equipment
- second segment = service/category code
- third segment = three-digit sequence

Current category codes:
- `WC` = window cleaning
- `PW` = pressure washing
- `SC` = solar cleaning
- `GU` = gutters
- `VEH` = vehicle
- `PPE` = personal protective equipment

## Folder Placement Rules
- SOPs go in the matching service folder under `10_SOPs/`.
- Equipment notes go in the most specific category folder under `20_Equipment/`.
- Maintenance logs go in `30_Maintenance/Logs/`.
- Checklists go in `40_Checklists/`.
- Decision notes go in `60_Decisions/`.
- Archived material moves to the matching area under `90_Archive/`.
