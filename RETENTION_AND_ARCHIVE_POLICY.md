# Retention and Archive Policy

## Purpose
Keep the SOP system readable and useful by separating permanent operating knowledge from temporary capture noise.

## Canonical rules
- Permanent instructions, standards, equipment records, decision notes, and high-value maintenance history stay in live folders.
- Temporary field capture for this system belongs in repo-scoped Daily Notes under `00_System/Daily Notes/`, not in a vault-global personal Daily Notes folder.
- If a capture note produces a durable lesson, promote that lesson into the correct SOP, equipment, checklist, reference, or decision note and link back if needed.
- If a note or attachment no longer has current operational value, archive it by moving it. Do not keep duplicate live and archived copies.

## What stays live
- Active SOPs, checklists, equipment notes, and reference notes.
- Maintenance log notes that contain repair detail, costs, warranty history, incident evidence, or troubleshooting value.
- Current and upcoming seasonal preparation notes.
- Final decision notes that explain why a tool, process, or material was approved, rejected, or deferred.

## What gets archived
- Reviewed Daily Notes after durable takeaways have been promoted.
- Superseded SOP drafts once a current version is established.
- Stale vendor research, clipped manuals, or comparison notes after the final decision is captured elsewhere.
- Detailed maintenance logs for retired equipment once the equipment note contains the final disposition summary.
- Redundant photos or attachments that no longer add evidence, troubleshooting, or training value.

## Retention rules

### Daily Notes
- Review at least weekly.
- Keep actionable job-day capture in `00_System/Daily Notes/`.
- Move reviewed notes older than 30 days to `90_Archive/Daily Notes/YYYY/`.
- Delete empty or no-value Daily Notes instead of archiving them.

### Photos and attachments
- Keep only photos that support maintenance proof, damage history, warranty claims, training examples, or troubleshooting.
- Store attachments next to the note they support whenever practical.
- Move obsolete but still useful evidence into the matching archive folder with the archived note.
- Delete duplicate or context-free media that has no operational value.

### Maintenance logs
- Routine recurring maintenance stays as completed Tasks inside the equipment note unless more detail is needed.
- Create a maintenance log note when the work involves repairs, replacements, cost tracking, photos, or unusual troubleshooting.
- Keep maintenance logs for active equipment live.
- When equipment is retired, move detailed logs to `90_Archive/Maintenance/<asset-id>/` after the equipment note records the retirement summary.

### Research and decision support
- Keep the final decision note live.
- Move rejected, superseded, or stale comparison inputs to `90_Archive/Reference/` once the final decision note captures the rationale.
- Archive clipped manuals only when the manual is no longer tied to active equipment or procedures.

## Archive conventions
- Archive by move, not by copy.
- Preserve the original asset ID or service name in the filename.
- Add `status: archived` and `archived_on:` properties when practical.
- If an archived note is replaced by a new live note, link the replacement from the archived note.
- Never archive the only current copy of an active SOP or equipment record.

## Review cadence
- Weekly: review repo-scoped Daily Notes and promote durable lessons.
- Monthly: archive reviewed Daily Notes and stale reference clutter.
- Quarterly: archive superseded SOP drafts, retired-equipment maintenance detail, and stale research inputs.
- Seasonally: archive completed seasonal prep notes when the next season's version is ready.

## Do not do
- Do not leave permanent lessons only inside Daily Notes.
- Do not keep maintenance due dates in both Tasks and separate frontmatter date fields.
- Do not keep duplicate live and archived copies of the same note.
- Do not keep standalone photos with no note context.
