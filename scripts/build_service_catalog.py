#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
CATALOG_ROOT = ROOT / "15_Service Catalog"
NORMALIZED_CSV = (
    ROOT
    / "50_Reference/CRM Service Descriptions/GilletteWindowSolarCleaning_pricebook_template_compatible.csv"
)
OVERRIDES_CSV = CATALOG_ROOT / "service_catalog_overrides.csv"
DASHBOARD_MD = CATALOG_ROOT / "Dashboard.md"
BASE_FILE = CATALOG_ROOT / "Service Catalog.base"
SOURCE_FILE_LABEL = "GilletteWindowSolarCleaning_pricebook_template_compatible.csv"
TODAY = date.today().isoformat()

SERVICE_FOLDERS = [
    "Window Cleaning",
    "Pressure Washing",
    "Solar Cleaning",
    "Gutters",
    "Roof and Soft Wash",
    "Repairs and Specialty",
    "Estimates and Internal Review",
]

PILOT_UUIDS = [
    "olit_2ef08e0a44d040959da46888b3973cca",
    "olit_cb16209a93e0437e939dd219b9b64ec1",
    "olit_430277d614fb4da1bba8bd01556f070a",
    "olit_44cadddaa78d44aabf6f348f08b1b809",
    "olit_1b1d4e8b26814404b58a8b5c898e0d2f",
]

STANDARD_SERVICE_CATEGORIES = {
    "Premium Window Cleaning",
    "Commercial Window Cleaning",
    "Pressure Washing",
    "Gutter Cleaning",
    "Gutter Guards",
    "Gutter Repairs",
    "Solar Panel Maintenance",
    "Roof cleaning",
    "Soft Washing",
}

WINDOW_KEYWORDS = (
    "window",
    "screen",
    "mirror",
    "blind",
    "skylight",
    "glass",
    "tint",
)
GUTTER_KEYWORDS = (
    "gutter",
    "downspout",
    "drip edge",
    "hanger",
    "outlet",
)
SOLAR_KEYWORDS = ("solar",)
ROOF_KEYWORDS = ("roof", "tile", "moss", "soft wash", "vent", "house wash")
PRESSURE_KEYWORDS = (
    "pressure",
    "concrete",
    "driveway",
    "sidewalk",
    "walkway",
    "patio",
    "paver",
    "porch",
    "garage",
    "carpet cleaning",
)
SUSPECT_TITLE_TERMS = (
    "exploitation",
    "general work",
)


@dataclass
class SourceRecord:
    industry: str
    category: str
    source_name: str
    description: str
    price: float
    cost: float
    taxable: bool
    unit_of_measure: str
    online_booking_enabled: bool
    source_uuid: str
    source_industry_uuid: str
    title: str = ""
    service_line: str = ""
    service_type: str = ""
    customer_visibility: str = ""
    review_status: str = ""
    target_folder: str = ""
    filename: str = ""
    audit_notes: list[str] | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the Obsidian service catalog from the CRM export.")
    parser.add_argument(
        "--mode",
        choices=["pilot", "full"],
        default="full",
        help="Generate the five-note pilot set or the full catalog.",
    )
    return parser.parse_args()


def clean_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def sanitize_filename(value: str) -> str:
    value = clean_whitespace(value)
    value = re.sub(r"\bw/", "with ", value)
    value = value.replace("/hour", " per hour")
    value = value.replace("/", " - ")
    value = value.replace(":", " -")
    value = re.sub(r'[<>|"?*]', "", value)
    return clean_whitespace(value)


def money_to_float(value: str) -> float:
    value = value.strip()
    if not value:
        return 0.0
    return float(value)


def bool_from_csv(value: str) -> bool:
    return value.strip().lower() == "true"


def split_description_and_metadata(value: str) -> tuple[str, dict[str, str]]:
    marker = "Source metadata (preserved from HCP export):\n"
    if marker not in value:
        return value.strip(), {}
    body, metadata_block = value.split(marker, 1)
    metadata: dict[str, str] = {}
    for line in metadata_block.splitlines():
        if not line.startswith("- "):
            continue
        key, raw_value = line[2:].split(":", 1)
        metadata[key.strip()] = raw_value.strip()
    return body.rstrip().strip(), metadata


def load_overrides() -> dict[str, dict[str, str]]:
    overrides: dict[str, dict[str, str]] = {}
    if not OVERRIDES_CSV.exists():
        return overrides
    with OVERRIDES_CSV.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            source_uuid = row["source_uuid"].strip()
            normalized_row: dict[str, str] = {}
            for key, value in row.items():
                if isinstance(value, list):
                    normalized_row[key] = " | ".join(item.strip() for item in value if item)
                elif value is None:
                    normalized_row[key] = ""
                else:
                    normalized_row[key] = value.strip()
            overrides[source_uuid] = normalized_row
    return overrides


def load_records() -> list[SourceRecord]:
    records: list[SourceRecord] = []
    with NORMALIZED_CSV.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            source_copy, metadata = split_description_and_metadata(row["description"])
            records.append(
                SourceRecord(
                    industry=clean_whitespace(row["industry"]),
                    category=clean_whitespace(row["category"]),
                    source_name=row["name"],
                    description=source_copy,
                    price=money_to_float(row["price"]),
                    cost=money_to_float(row["cost"]),
                    taxable=bool_from_csv(row["taxable"]),
                    unit_of_measure=clean_whitespace(row["unit_of_measure"]),
                    online_booking_enabled=bool_from_csv(row["online_booking_enabled"]),
                    source_uuid=metadata.get("source_uuid", ""),
                    source_industry_uuid=metadata.get("industry_uuid", ""),
                )
            )
    return records


def contains_any(value: str, keywords: Iterable[str]) -> bool:
    lowered = value.lower()
    return any(keyword in lowered for keyword in keywords)


def infer_service_line(record: SourceRecord) -> str:
    category = record.category
    title = clean_whitespace(record.source_name)
    combined = f"{category} {title}"
    if category in {"Premium Window Cleaning", "Commercial Window Cleaning"}:
        return "Window Cleaning"
    if category == "Pressure Washing":
        return "Pressure Washing"
    if category in {"Gutter Cleaning", "Gutter Guards", "Gutter Repairs"}:
        return "Gutters"
    if category == "Solar Panel Maintenance":
        return "Solar Cleaning"
    if category in {"Roof cleaning", "Soft Washing"}:
        return "Roof and Soft Wash"
    if category in {"Window Screen Mesh Replacement", "Window Screen Frame/Assembly Maintenance", "Window Tint Installation"}:
        return "Window Cleaning"
    if category == "Estimates":
        if contains_any(combined, GUTTER_KEYWORDS):
            return "Gutters"
        if contains_any(combined, SOLAR_KEYWORDS):
            return "Solar Cleaning"
        if contains_any(combined, WINDOW_KEYWORDS):
            return "Window Cleaning"
        return "Estimates and Internal Review"
    if category == "Warranty Work":
        return "Estimates and Internal Review"
    if category == "Bird Proofing":
        if contains_any(combined, SOLAR_KEYWORDS):
            return "Solar Cleaning"
        if contains_any(combined, ROOF_KEYWORDS):
            return "Roof and Soft Wash"
        return "Repairs and Specialty"
    if category == "Satellite Dish Removal":
        return "Repairs and Specialty"
    if category == "Repairs":
        if contains_any(combined, WINDOW_KEYWORDS):
            return "Window Cleaning"
        if contains_any(combined, ROOF_KEYWORDS):
            return "Roof and Soft Wash"
        if contains_any(combined, GUTTER_KEYWORDS):
            return "Gutters"
        return "Repairs and Specialty"
    if category == "Custom Services":
        if contains_any(combined, WINDOW_KEYWORDS):
            return "Window Cleaning"
        if contains_any(combined, GUTTER_KEYWORDS):
            return "Gutters"
        if contains_any(combined, SOLAR_KEYWORDS):
            return "Solar Cleaning"
        if contains_any(combined, ROOF_KEYWORDS):
            return "Roof and Soft Wash"
        if contains_any(combined, PRESSURE_KEYWORDS):
            return "Pressure Washing"
        return "Repairs and Specialty"
    return "Repairs and Specialty"


def infer_service_type(record: SourceRecord) -> str:
    category = record.category
    title = clean_whitespace(record.source_name).lower()
    if any(term in title for term in SUSPECT_TITLE_TERMS):
        return "internal-review"
    if category == "Estimates":
        return "estimate"
    if category == "Warranty Work":
        return "warranty"
    if category in {"Repairs", "Window Screen Mesh Replacement", "Window Screen Frame/Assembly Maintenance"}:
        return "repair"
    if category in {"Gutter Repairs"}:
        return "repair"
    if any(keyword in title for keyword in ("repair", "replacement", "diagnosis", "restore", "restoration", "seal", "leak")):
        return "repair"
    if category in {"Bird Proofing", "Gutter Guards", "Window Tint Installation", "Satellite Dish Removal", "Custom Services"}:
        return "add-on"
    return "core-service"


def infer_review_status(
    record: SourceRecord,
    duplicate_title_counts: Counter,
    duplicate_filename_counts: Counter,
) -> tuple[str, list[str]]:
    title = clean_whitespace(record.source_name)
    lowered_title = title.lower()
    notes: list[str] = []
    review_status = "clean"

    if any(term in lowered_title for term in SUSPECT_TITLE_TERMS):
        review_status = "suspect"
        notes.append("Suspicious CRM row name; do not use customer-facing until the service intent is verified.")

    if not record.description:
        if review_status == "clean":
            review_status = "needs-review"
        notes.append("CRM description field is empty. Add customer-facing copy before operational use.")

    if record.price == 0:
        if review_status == "clean":
            review_status = "needs-review"
        notes.append("CRM price is $0.00. Treat this as quoted, complimentary, or incomplete until pricing is verified.")

    if duplicate_title_counts[record.title] > 1 or duplicate_filename_counts[record.filename] > 1:
        if review_status == "clean":
            review_status = "duplicate-candidate"
        notes.append("This title appears more than once in the export. Verify whether the rows should remain distinct.")

    if not record.online_booking_enabled and record.category in STANDARD_SERVICE_CATEGORIES and record.service_type == "core-service":
        notes.append("Core service is not currently online-bookable in the CRM. Confirm whether that is intentional.")

    return review_status, notes


def infer_customer_visibility(record: SourceRecord) -> str:
    if record.review_status == "suspect" or record.service_type == "internal-review":
        return "review-needed"
    if record.service_type in {"estimate", "warranty"}:
        return "internal-only"
    return "customer-facing"


def infer_target_folder(record: SourceRecord) -> str:
    if record.service_type in {"estimate", "warranty", "internal-review"}:
        return "Estimates and Internal Review"
    if record.review_status == "suspect":
        return "Estimates and Internal Review"
    if record.service_line in SERVICE_FOLDERS:
        return record.service_line
    return "Repairs and Specialty"


def pricing_note(record: SourceRecord) -> str:
    if record.price == 0:
        return "CRM stores this as $0.00. Treat as quoted, complimentary, or incomplete until verified."
    if record.unit_of_measure:
        return "Fixed CRM price and unit are present."
    return "Fixed CRM price is present; confirm the pricing basis before using it externally."


def split_description_sections(description: str) -> dict[str, list[str]]:
    sections = {
        "summary": [],
        "included": [],
        "best_fit": [],
        "not_included": [],
        "notes": [],
    }
    current = "summary"
    heading_map = {
        "what we do": "included",
        "why it’s worth it": "best_fit",
        "why it's worth it": "best_fit",
        "what’s not included": "not_included",
        "what's not included": "not_included",
        "just so you know": "notes",
    }

    for raw_line in description.splitlines():
        line = raw_line.strip()
        if not line:
            sections[current].append("")
            continue
        normalized = line.rstrip(":").lower()
        if normalized in heading_map:
            current = heading_map[normalized]
            continue
        sections[current].append(line)
    return sections


def markdownize_lines(lines: list[str]) -> str:
    output: list[str] = []
    for line in lines:
        if not line:
            if output and output[-1] != "":
                output.append("")
            continue
        if line.startswith("•"):
            output.append(f"- {line[1:].strip()}")
        else:
            output.append(line)
    return "\n".join(output).strip()


def build_summary(record: SourceRecord, sections: dict[str, list[str]]) -> str:
    if record.review_status == "suspect":
        return "Review-needed CRM row. Verify what this item is supposed to represent before using it in the service catalog or customer-facing materials."
    summary = markdownize_lines(sections["summary"])
    if summary:
        return summary
    if record.description:
        first_paragraph = record.description.split("\n\n", 1)[0].strip()
        if first_paragraph:
            return first_paragraph
    return f"TODO: verify the customer-facing summary for {record.title}."


def build_internal_notes(record: SourceRecord) -> list[str]:
    notes = [
        f"CRM category: {record.category}.",
    ]
    if record.customer_visibility != "customer-facing":
        notes.append("Do not treat this note as approved customer-facing copy until the flagged issues are resolved.")
    if record.price == 0:
        notes.append("Pricing is not ready for public use without verification.")
    if not record.description:
        notes.append("Add cleaned customer-facing copy before treating this as an approved service note.")
    if record.online_booking_enabled:
        notes.append("This row is currently marked as online-bookable in the CRM.")
    else:
        notes.append("This row is not currently marked as online-bookable in the CRM.")
    notes.append("Link related SOPs, checklists, equipment, and purchase notes here as those notes are created.")
    return notes


def should_use_compact_shape(record: SourceRecord, sections: dict[str, list[str]]) -> bool:
    if record.service_type in {"estimate", "warranty", "internal-review"}:
        return True
    if record.review_status == "suspect":
        return True
    if not record.description:
        return True
    if not markdownize_lines(sections["included"]) and len(record.description) < 220:
        return True
    return False


def format_callout(title: str, body_lines: list[str]) -> list[str]:
    lines = [title]
    for line in body_lines:
        if line == "":
            lines.append(">")
        else:
            lines.append(f"> {line}")
    return lines


def build_related_links(record: SourceRecord, records: list[SourceRecord]) -> list[str]:
    candidates = [
        candidate
        for candidate in records
        if candidate.source_uuid != record.source_uuid
        and candidate.service_line == record.service_line
        and candidate.customer_visibility == "customer-facing"
        and candidate.review_status != "suspect"
    ]
    candidates.sort(
        key=lambda candidate: (
            candidate.category != record.category,
            candidate.service_type != "add-on",
            candidate.title,
        )
    )
    links: list[str] = []
    for candidate in candidates[:3]:
        link_target = f"15_Service Catalog/{candidate.target_folder}/{candidate.filename[:-3]}"
        links.append(f"- [[{link_target}|{candidate.title}]]")
    return links


def to_yaml_list(values: list[str]) -> list[str]:
    if not values:
        return ["aliases: []"]
    lines = ["aliases:"]
    for value in values:
        lines.append(f"  - {value}")
    return lines


def format_frontmatter(record: SourceRecord, aliases: list[str]) -> list[str]:
    lines = [
        "---",
        "type: service-description",
        "status: draft",
        "owner: Trevor",
        f"created: {TODAY}",
        "last_reviewed:",
        "next_review:",
        f"service_line: {record.service_line}",
        f"service_type: {record.service_type}",
        f"customer_visibility: {record.customer_visibility}",
        f"review_status: {record.review_status}",
        f"source_uuid: {record.source_uuid}",
        f"price: {record.price:g}",
        f"unit_of_measure: {record.unit_of_measure}",
        f"cost: {record.cost:g}",
        f"taxable: {str(record.taxable).lower()}",
        f"online_booking_enabled: {str(record.online_booking_enabled).lower()}",
    ]
    lines.extend(to_yaml_list(aliases))
    lines.extend(
        [
            "tags:",
            "  - service-description",
            "---",
        ]
    )
    return lines


def render_note(record: SourceRecord, all_records: list[SourceRecord]) -> str:
    sections = split_description_sections(record.description)
    compact = should_use_compact_shape(record, sections)
    aliases: list[str] = []
    source_name_clean = clean_whitespace(record.source_name)
    if record.title != source_name_clean:
        aliases.append(source_name_clean)

    lines: list[str] = []
    lines.extend(format_frontmatter(record, aliases))
    lines.extend(["", f"# {record.title}", ""])

    summary = build_summary(record, sections)
    lines.extend(
        format_callout(
            "> [!summary] Quick Summary",
            summary.splitlines() if summary else ["TODO: verify summary."],
        )
    )
    lines.append("")

    pricing_lines = [
        f"- CRM price: ${record.price:,.2f}",
        f"- Unit: {record.unit_of_measure or 'Quoted / not specified'}",
        f"- Taxable: {'Yes' if record.taxable else 'No'}",
        f"- Online booking enabled: {'Yes' if record.online_booking_enabled else 'No'}",
        f"- Pricing note: {pricing_note(record)}",
    ]
    lines.extend(format_callout("> [!info] Pricing", pricing_lines))
    lines.append("")

    included = markdownize_lines(sections["included"])
    not_included = markdownize_lines(sections["not_included"])
    best_fit_parts = [markdownize_lines(sections["best_fit"]), markdownize_lines(sections["notes"])]
    best_fit = "\n\n".join(part for part in best_fit_parts if part).strip()
    related_links = build_related_links(record, all_records)
    internal_notes = [f"- {note}" for note in build_internal_notes(record)]

    if not compact:
        if included:
            lines.extend(["## Included", included, ""])
        if not_included:
            lines.extend(["## Not Included", not_included, ""])
        if best_fit:
            lines.extend(["## Best Fit / When To Offer", best_fit, ""])
        if related_links:
            lines.extend(["## Upsells and Related Services", *related_links, ""])

    lines.extend(["## Internal Notes", *internal_notes, ""])

    source_copy = record.description or "TODO: verify original source copy; the CRM description field was empty in the export."
    lines.extend(
        format_callout(
            "> [!note]- Source Copy",
            source_copy.splitlines() if source_copy else ["TODO: verify original source copy."],
        )
    )
    lines.append("")

    source_meta_lines = [
        f"- Industry: {record.industry}",
        f"- CRM category: {record.category}",
        f"- Source UUID: {record.source_uuid}",
        f"- Industry UUID: {record.source_industry_uuid}",
        f"- Source file: 50_Reference/CRM Service Descriptions/{SOURCE_FILE_LABEL}",
    ]
    lines.extend(format_callout("> [!note]- Source Metadata", source_meta_lines))
    lines.append("")

    audit_notes = record.audit_notes or ["No auto-detected issues during import."]
    lines.extend(format_callout("> [!warning]- Audit Notes", [f"- {note}" for note in audit_notes]))
    lines.append("")

    if not compact:
        review_history = [
            f"- {TODAY} - Imported from the CRM pricebook export with `scripts/build_service_catalog.py`.",
        ]
        lines.extend(format_callout("> [!abstract]- Review History", review_history))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_base_file() -> None:
    content = """filters:
  and:
    - 'file.inFolder("15_Service Catalog")'
    - 'file.ext == "md"'
    - 'type == "service-description"'
properties:
  file.name:
    displayName: Service
  service_line:
    displayName: Service Line
  service_type:
    displayName: Type
  customer_visibility:
    displayName: Visibility
  review_status:
    displayName: Review
  price:
    displayName: Price
  unit_of_measure:
    displayName: Unit
  online_booking_enabled:
    displayName: Booking
  file.mtime:
    displayName: Updated
views:
  - type: table
    name: All Services
    order:
      - service_line
      - service_type
      - file.name
  - type: table
    name: Customer-Facing
    filters:
      and:
        - 'customer_visibility == "customer-facing"'
    order:
      - service_line
      - file.name
  - type: table
    name: Booking Enabled
    filters:
      and:
        - 'online_booking_enabled == true'
    order:
      - service_line
      - file.name
  - type: table
    name: Estimates and Internal Review
    filters:
      and:
        - 'service_type == "estimate" || service_type == "warranty" || service_type == "internal-review"'
    order:
      - review_status
      - file.name
  - type: table
    name: Needs Review Queue
    filters:
      and:
        - 'review_status == "needs-review" || review_status == "suspect" || review_status == "duplicate-candidate"'
    order:
      - review_status
      - service_line
      - file.name
  - type: table
    name: Duplicate Title / Collision Review
    filters:
      and:
        - 'review_status == "duplicate-candidate"'
    order:
      - service_line
      - file.name
  - type: table
    name: Quoted / Variable Pricing
    filters:
      and:
        - 'price == 0'
    order:
      - service_type
      - file.name
  - type: table
    name: By Service Line
    groupBy:
      property: service_line
      direction: ASC
    order:
      - service_line
      - service_type
      - file.name
"""
    BASE_FILE.write_text(content, encoding="utf-8")


def write_dashboard() -> None:
    content = """# Service Catalog Dashboard

Use this as the main browsing and cleanup surface for CRM-derived service descriptions.

## How To Use
- Treat `15_Service Catalog/` as the curated working home for service descriptions.
- Keep the raw and normalized CSV source files in `50_Reference/CRM Service Descriptions/`.
- Use the review views first when cleaning weak, duplicate, quoted, or suspicious services.
- Add links to SOPs, checklists, equipment notes, and purchase notes directly inside service notes as those notes are created.

## All Services
![[Service Catalog.base#All Services]]

## Customer-Facing
![[Service Catalog.base#Customer-Facing]]

## Booking Enabled
![[Service Catalog.base#Booking Enabled]]

## Estimates and Internal Review
![[Service Catalog.base#Estimates and Internal Review]]

## Needs Review Queue
![[Service Catalog.base#Needs Review Queue]]

## Duplicate Title / Collision Review
![[Service Catalog.base#Duplicate Title / Collision Review]]

## Quoted / Variable Pricing
![[Service Catalog.base#Quoted / Variable Pricing]]

## By Service Line
![[Service Catalog.base#By Service Line]]
"""
    DASHBOARD_MD.write_text(content, encoding="utf-8")


def ensure_directories() -> None:
    CATALOG_ROOT.mkdir(parents=True, exist_ok=True)
    for folder in SERVICE_FOLDERS:
        (CATALOG_ROOT / folder).mkdir(parents=True, exist_ok=True)


def clear_existing_catalog_notes() -> None:
    for folder in SERVICE_FOLDERS:
        for path in (CATALOG_ROOT / folder).glob("*.md"):
            path.unlink()


def build_records(overrides: dict[str, dict[str, str]]) -> list[SourceRecord]:
    records = load_records()
    for record in records:
        override = overrides.get(record.source_uuid, {})
        override_title = clean_whitespace(override.get("title_override", ""))
        record.title = override_title or clean_whitespace(record.source_name)
        base_filename = sanitize_filename(f"{record.category} - {record.title}")
        record.filename = f"{base_filename}.md"

    duplicate_title_counts = Counter(record.title for record in records)
    duplicate_filename_counts = Counter(record.filename for record in records)

    for record in records:
        override = overrides.get(record.source_uuid, {})
        auto_service_line = infer_service_line(record)
        auto_service_type = infer_service_type(record)
        record.service_line = override.get("service_line") or auto_service_line
        record.service_type = override.get("service_type") or auto_service_type
        auto_review_status, auto_audit_notes = infer_review_status(
            record,
            duplicate_title_counts,
            duplicate_filename_counts,
        )
        record.review_status = override.get("review_status") or auto_review_status
        record.customer_visibility = override.get("customer_visibility") or infer_customer_visibility(record)
        record.target_folder = record.service_line if record.service_line in SERVICE_FOLDERS else infer_target_folder(record)
        if record.service_type in {"estimate", "warranty", "internal-review"} or record.review_status == "suspect":
            record.target_folder = "Estimates and Internal Review"
        if duplicate_filename_counts[record.filename] > 1:
            short_uuid = record.source_uuid.replace("olit_", "")[:8]
            base_filename = sanitize_filename(f"{record.category} - {record.title} - {short_uuid}")
            record.filename = f"{base_filename}.md"

        record.audit_notes = []
        initial_override_note = override.get("initial_audit_note", "")
        if initial_override_note:
            record.audit_notes.append(initial_override_note)
        record.audit_notes.extend(auto_audit_notes)
        if not record.audit_notes:
            record.audit_notes.append("No auto-detected issues during import.")
    return records


def write_notes(records: list[SourceRecord], mode: str) -> list[Path]:
    selected_records = records
    if mode == "pilot":
        selected_records = [record for record in records if record.source_uuid in PILOT_UUIDS]

    written_paths: list[Path] = []
    for record in selected_records:
        output_path = CATALOG_ROOT / record.target_folder / record.filename
        output_path.write_text(render_note(record, records), encoding="utf-8")
        written_paths.append(output_path)
    return written_paths


def main() -> None:
    args = parse_args()
    ensure_directories()
    clear_existing_catalog_notes()
    overrides = load_overrides()
    records = build_records(overrides)
    write_base_file()
    write_dashboard()
    written_paths = write_notes(records, args.mode)
    print(f"mode={args.mode}")
    print(f"notes_written={len(written_paths)}")
    for path in written_paths:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
