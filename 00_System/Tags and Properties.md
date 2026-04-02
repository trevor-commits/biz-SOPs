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
service_lines: []
procurement_status: owned
brand:
model:
serial_number:
purchase_date:
warranty_until:
storage_location:
related_sops: []
replacement_parts: []
tags:
  - equipment
---
```

Note:
- Do not store recurring maintenance due dates in frontmatter.
- The canonical due-state lives in recurring Tasks inside the equipment note.
- Keep purchase links and vendor options in the note body, not in frontmatter, unless a specific query later proves they need to be promoted to properties.
- Use `procurement_status` only as a secondary inventory signal such as `owned`, `need-to-buy`, `wishlist`, or `replace-soon`. The active shopping queue still lives in purchase notes.

## Purchase Properties

```yaml
---
type: purchase
status: active
owner: Trevor
created:
last_reviewed:
next_review:
purchase_stage: need-to-buy
urgency: now
purchase_kind: one-time
service_lines: []
category:
linked_asset_id:
quantity_needed:
reorder_min:
target_vendor:
estimated_cost:
purchased_date:
actual_cost:
next_action:
tags:
  - purchase
---
```

Suggested values:
- `purchase_stage`: `need-to-buy`, `researching`, `ordered`, `received`, `deferred`, `cancelled`
- `urgency`: `now`, `soon`, `later`
- `purchase_kind`: `one-time`, `consumable`, `replacement`, `upgrade`
- Set `status: archived` when `purchase_stage` reaches `received` or `cancelled`, unless there is still an active follow-up reason to keep the note in the working queue.

Suggested `category` values:
- `truck`
- `ladders`
- `water-fed`
- `pressure-washing`
- `hand-tools`
- `ppe`
- `chemicals`
- `solar`
- `gutters`
- `multi-service`

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
replacement_parts: []
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
- `repair`

## Service Description Properties

```yaml
---
type: service-description
status: draft
owner: Trevor
created:
last_reviewed:
next_review:
service_line:
service_type:
customer_visibility:
review_status:
source_uuid:
price:
unit_of_measure:
cost:
taxable:
online_booking_enabled:
aliases: []
tags:
  - service-description
---
```

Suggested values:
- `service_type`: `core-service`, `add-on`, `estimate`, `repair`, `warranty`, `internal-review`
- `customer_visibility`: `customer-facing`, `internal-only`, `review-needed`
- `review_status`: `clean`, `needs-review`, `suspect`, `duplicate-candidate`

Note:
- Keep `source_uuid` in frontmatter as the stable sync key for reruns and traceability.
- Keep `source_category`, `industry_uuid`, source file path, and other archival details in the note body unless a Bases view later proves they need to move into properties.
