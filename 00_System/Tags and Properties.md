# Tags and Properties

## Purpose
Use a small, stable property set so notes stay queryable without turning maintenance into data entry work.

## Global Rules
- Use `YYYY-MM-DD` for all dates.
- Keep `owner` as `Trevor` unless responsibility actually changes.
- Use lowercase values for `type` and `status`.
- Only add new properties if they will be reviewed, filtered, or reported on later.

## Shared Properties

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

## Status Values
- `draft` = still being built
- `active` = approved and in use
- `needs-review` = usable but due for update
- `archived` = no longer active, kept for history

## SOP Properties

```yaml
---
type: sop
status: draft
owner: Trevor
created:
last_reviewed:
next_review:
service:
task:
equipment_ids: []
ppe: []
estimated_duration:
season:
tags:
  - sop
---
```

## Equipment Properties

```yaml
---
type: equipment
status: active
owner: Trevor
created:
last_reviewed:
next_review:
asset_id:
category:
brand:
model:
serial_number:
purchase_date:
warranty_until:
storage_location:
related_sops: []
tags:
  - equipment
---
```

Note:
- Do not store recurring maintenance due dates in frontmatter.
- The canonical due-state lives in recurring Tasks inside the equipment note.

## Maintenance Log Properties

```yaml
---
type: maintenance-log
status: active
owner: Trevor
created:
asset_id:
maintenance_type:
performed_on:
performed_by:
cost:
tags:
  - maintenance-log
---
```

## Checklist Properties

```yaml
---
type: checklist
status: draft
owner: Trevor
created:
last_reviewed:
next_review:
service:
task:
tags:
  - checklist
---
```

## Decision Note Properties

```yaml
---
type: decision
status: draft
owner: Trevor
created:
decision_topic:
decision_status:
review_date:
tags:
  - decision
---
```

## Suggested Tag Use
- Use properties first.
- Use tags only for cross-cutting themes that are helpful in search.

Good examples:
- `safety`
- `seasonal`
- `vendor`
- `training`
- `troubleshooting`
