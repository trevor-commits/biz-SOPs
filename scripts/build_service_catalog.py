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
RAW_EXPORT_CSV = (
    ROOT
    / "50_Reference/CRM Service Descriptions/GilletteWindowSolarCleaning_pricebook_export.csv"
)
OVERRIDES_CSV = CATALOG_ROOT / "service_catalog_overrides.csv"
DASHBOARD_MD = CATALOG_ROOT / "Dashboard.md"
BASE_FILE = CATALOG_ROOT / "Service Catalog.base"
SOURCE_FILE_LABEL = "GilletteWindowSolarCleaning_pricebook_export.csv"

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

CATEGORY_SERVICE_LINE_MAP = {
    "Premium Window Cleaning": "Window Cleaning",
    "Commercial Window Cleaning": "Window Cleaning",
    "Pressure Washing": "Pressure Washing",
    "Gutter Cleaning": "Gutters",
    "Gutter Guards": "Gutters",
    "Gutter Repairs": "Gutters",
    "Solar Panel Maintenance": "Solar Cleaning",
    "Roof cleaning": "Roof and Soft Wash",
    "Soft Washing": "Roof and Soft Wash",
    "Window Screen Mesh Replacement": "Window Cleaning",
    "Window Screen Frame/Assembly Maintenance": "Window Cleaning",
    "Window Tint Installation": "Window Cleaning",
    "Warranty Work": "Estimates and Internal Review",
    "Satellite Dish Removal": "Repairs and Specialty",
}

BIRD_PROOFING_SERVICE_LINE_BY_TITLE = {
    "Roof Bird Waste Cleaning and Removal": "Roof and Soft Wash",
    "Bird Spike Installation": "Roof and Soft Wash",
    "Solar Panel Bird Proofing": "Solar Cleaning",
    "Plastic Bird Spike Installation": "Roof and Soft Wash",
    "Metal Bird Spike Installation": "Roof and Soft Wash",
}

REPAIR_SERVICE_LINE_BY_TITLE = {
    "Window Screen Replacement": "Window Cleaning",
    "Roof Tile Repair/Replacement": "Roof and Soft Wash",
    "Roof Leak Diagnosis – $50/hour": "Roof and Soft Wash",
    "Seal Leaky Roof Vent": "Roof and Soft Wash",
    "Large Sliding Screen Door Mesh Replacement – Premium Pet Resistant Mesh": "Window Cleaning",
    "Window Screen Frame Repair w/ Mesh Replacement": "Window Cleaning",
}

CUSTOM_SERVICE_LINE_BY_TITLE = {
    "Exterior String Light Removal": "Repairs and Specialty",
    "Cobweb Removal": "Repairs and Specialty",
    "General Work": "Repairs and Specialty",
    "Paint Touch up": "Repairs and Specialty",
    "Home Bird Proofing": "Repairs and Specialty",
    "Plastic Installation on skylight": "Window Cleaning",
    "Window Blind Removal": "Window Cleaning",
    "Tree Trimming": "Repairs and Specialty",
    "Tree Trimming Removal": "Repairs and Specialty",
    "Downspout Extension Installation": "Gutters",
    "Parental Exploitation": "Repairs and Specialty",
    "Second Story Exterior Window Film Application (Customer Supplied)": "Window Cleaning",
    "Leaf Raking": "Repairs and Specialty",
    "Bruning Exploitation": "Repairs and Specialty",
    "Under Roof Tile Cleaning - Bird Droppings": "Roof and Soft Wash",
    "Window Screen Mesh Replacement – Premium High Visibility Mesh (UltraVue)": "Window Cleaning",
    "Satellite Dish Removal – Two-Story Apartment Buildings": "Repairs and Specialty",
    "Penetration Sealing / Surface Closure After Removal of Satellite Dishes": "Repairs and Specialty",
    "Haul-Off and Disposal of Removed Satellite Dishes": "Repairs and Specialty",
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
INCLUDED_BOOKING_PATTERNS = (
    "included at no extra charge",
    "included as part of",
    "included with",
    "included for site cleanup",
    "included because",
    "comes with",
)
RISKY_PROMISE_TERMS = ("guarantee", "guarantees", "guaranteed")

SUMMARY_BLOCK = "> [!summary] Quick Summary"
PRICING_BLOCK = "> [!info] Pricing"
SOURCE_COPY_BLOCK = "> [!note]- Source Copy"
SOURCE_METADATA_BLOCK = "> [!note]- Source Metadata"
AUDIT_BLOCK = "> [!warning]- Audit Notes"
REVIEW_HISTORY_BLOCK = "> [!abstract]- Review History"
LOCAL_NOTES_HEADING = "## Local Notes and Links"
JUST_SO_YOU_KNOW_HEADING = "## Just So You Know"

PRESERVE_ALWAYS_BLOCKS = {
    LOCAL_NOTES_HEADING,
    REVIEW_HISTORY_BLOCK,
}
PRESERVE_WHEN_REVIEWED_BLOCKS = {
    SUMMARY_BLOCK,
    "## Included",
    "## Not Included",
    "## Best Fit / When To Offer",
    JUST_SO_YOU_KNOW_HEADING,
    "## Upsells and Related Services",
    "## Internal Notes",
}
STATUS_SEVERITY = {
    "clean": 0,
    "duplicate-candidate": 1,
    "needs-review": 2,
    "suspect": 3,
}


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
    title_collision: bool = False


@dataclass
class ExistingNote:
    path: Path
    frontmatter: dict[str, str | list[str]]
    blocks: dict[str, str]


@dataclass(frozen=True)
class CopyOverride:
    summary: tuple[str, ...] | None = None
    included: tuple[str, ...] | None = None
    not_included: tuple[str, ...] | None = None
    best_fit: tuple[str, ...] | None = None
    notes: tuple[str, ...] | None = None


COPY_OVERRIDES: dict[tuple[str, str], CopyOverride] = {
    (
        "Premium Window Cleaning",
        "Interior Only",
    ): CopyOverride(
        summary=(
            "Interior-only window cleaning for homeowners who want the inside glass cleaned without the exterior work.",
            "We hand-clean the interior panes to remove fingerprints, dust, and everyday buildup for a clear, streak-free finish.",
        ),
        included=(
            "- Hand-clean interior glass using a professional window-cleaning solution",
            "- Detail normal fingerprints, smudges, and everyday interior buildup",
            "- Finish with a squeegee and detailing towels for a clear, streak-free result",
            "- Work carefully around normal access points; please move fragile or high-value items before arrival",
        ),
        not_included=(
            "- Exterior glass cleaning",
            "- Hard-water stain removal, paint, adhesive, or heavy post-construction debris",
            "- Screens, tracks, sills, blinds, or other detail add-ons unless they are listed in the quote",
        ),
        best_fit=(
            "- Good when the inside glass needs attention but the exterior work is not needed yet",
            "- Helps brighten rooms and improve how the glass looks from inside the home",
            "- Pairs well with tracks and sills, blinds, mirrors, or full interior-and-exterior window cleaning",
        ),
        notes=(
            "- Pricing depends on pane count, interior access, and layout.",
            "- Please have fragile or valuable items moved before arrival.",
        ),
    ),
    (
        "Premium Window Cleaning",
        "Exterior Only",
    ): CopyOverride(
        summary=(
            "Exterior-only window cleaning for homeowners who want the outside glass cleaned without interior work.",
            "We hand-clean the exterior panes to remove weather buildup and leave the glass clear and streak-free.",
        ),
        included=(
            "- Hand-clean exterior glass using a professional window-cleaning solution",
            "- Remove normal dust, pollen, cobwebs, and surface grime from the outside glass",
            "- Finish with a squeegee and detailing towels for a clear, streak-free result",
            "- Light rinse or detail prep as needed for normal exterior buildup",
        ),
        not_included=(
            "- Interior glass cleaning",
            "- Hard-water stain removal, paint, adhesive, or heavy post-construction debris",
            "- Screens, tracks, sills, or other detail add-ons unless they are listed in the quote",
        ),
        best_fit=(
            "- Good when you want the curb-appeal improvement without paying for interior work",
            "- Removes the weather buildup that makes exterior glass look dull",
            "- Pairs well with screen cleaning, hard-water/detail work, or full interior-and-exterior window cleaning",
        ),
        notes=(
            "- Pricing depends on pane count, exterior access, and layout.",
            "- Ladder or second-story access can change the final price or scope.",
        ),
    ),
    (
        "Premium Window Cleaning",
        "Interior & Exterior",
    ): CopyOverride(
        summary=(
            "Full window cleaning for both sides of the glass.",
            "We hand-clean the interior and exterior panes for a clear, streak-free finish and a more complete result than a one-side-only service.",
        ),
        included=(
            "- Hand-clean both the interior and exterior glass using a professional window-cleaning solution",
            "- Detail normal fingerprints, smudges, dust, pollen, and everyday buildup",
            "- Finish with a squeegee and detailing towels for a clear, streak-free result on both sides",
            "- Work carefully around normal access points; please move fragile or high-value items before arrival",
        ),
        not_included=(
            "- Hard-water stain removal, paint, adhesive, or heavy post-construction debris",
            "- Screens, tracks, sills, blinds, or other detail add-ons unless they are listed in the quote",
            "- Specialty ladder work or unusually difficult access beyond the approved scope",
        ),
        best_fit=(
            "- Best when you want the most complete visual improvement from the service",
            "- Brightens the home while improving both the interior and exterior view",
            "- Pairs well with screens, tracks and sills, skylights, mirrors, or other detail add-ons",
        ),
        notes=(
            "- Pricing depends on pane count, access, and layout.",
            "- Please have fragile or valuable items moved before arrival.",
        ),
    ),
    (
        "Premium Window Cleaning",
        "Premium Window Cleaning – Exterior Only (Second-Story Feature Window)",
    ): CopyOverride(
        summary=(
            "Exterior-only cleaning for a second-story feature window that needs dedicated ladder access.",
            "We hand-clean the exterior glass and price it separately because of the additional setup, height, and access requirements.",
        ),
        included=(
            "- Hand-clean exterior glass using a professional window-cleaning solution",
            "- Remove normal dust, pollen, cobwebs, and surface grime from the outside glass",
            "- Use ladder access and careful positioning as needed for safe second-story service",
        ),
        not_included=(
            "- Interior glass cleaning",
            "- Hard-water stain removal, paint, adhesive, or heavy post-construction debris",
            "- Screens, tracks, sills, or other detail add-ons unless they are listed in the quote",
        ),
        best_fit=(
            "- Good for isolated feature windows that need separate second-story access",
            "- Improves the appearance of hard-to-reach glass without bundling the full home",
            "- Pairs well with exterior-only or full window cleaning on the rest of the property",
        ),
        notes=(
            "- Pricing is higher than standard lower-story exterior panes because of the extra height, ladder work, and setup time.",
            "- Final scope depends on safe access at the time of service.",
        ),
    ),
    (
        "Premium Window Cleaning",
        "Screen Cleaning",
    ): CopyOverride(
        summary=(
            "Window screen cleaning removes loose dirt, pollen, and cobweb buildup from removable screens so they do not keep blowing debris back onto cleaned glass.",
        ),
        included=(
            "- Brush or lightly rinse removable screens to remove loose dirt, pollen, and cobwebs",
            "- Gently scrub the screen material and frame with safe cleaning tools",
            "- Reinstall screens once they are ready to go back in place",
        ),
        not_included=(
            "- Screen repair, mesh replacement, or frame restoration",
            "- Cleaning screens that are too brittle, torn, or unsafe to handle",
            "- Window glass cleaning unless it is also part of the approved quote",
        ),
        best_fit=(
            "- Best when you want freshly cleaned windows to stay cleaner longer",
            "- Helps improve airflow and the overall finished look of the window service",
            "- Pairs well with exterior-only or full window cleaning",
        ),
        notes=(
            "- This line currently behaves like an add-on or bundle item, not a clean standalone published price. Keep it quote-based until the CRM pricing rule is cleaned up.",
            "- If screens are brittle or damaged, repair or replacement may be the better recommendation.",
        ),
    ),
    (
        "Premium Window Cleaning",
        "Tracks & Sill Cleaning",
    ): CopyOverride(
        summary=(
            "Tracks and sill cleaning removes the dirt and debris that collect around the glass so the finished window service looks more complete.",
        ),
        included=(
            "- Brush out accessible tracks to loosen built-up dust and debris",
            "- Vacuum and wipe accessible tracks and sills to remove remaining buildup",
            "- Clean the visible frame areas that most affect the finished appearance",
        ),
        not_included=(
            "- Deep restoration for mold, damaged caulking, or weatherstripping issues",
            "- Disassembly-based cleaning or repair work",
            "- Window glass cleaning unless it is also part of the approved quote",
        ),
        best_fit=(
            "- Best when you want the windows to look finished beyond the glass alone",
            "- Helps reduce dust and grime that collect in the frames over time",
            "- Pairs well with interior-only or full window cleaning",
        ),
        notes=(
            "- This line currently behaves like an add-on or bundle item, not a clean standalone published price. Keep it quote-based until the CRM pricing rule is cleaned up.",
            "- Final scope depends on how accessible the tracks and sills are without disassembly.",
        ),
    ),
    (
        "Solar Panel Maintenance",
        "Solar Panel Cleaning",
    ): CopyOverride(
        notes=(
            "- Pricing depends on panel count, system layout, roof access, and the amount of buildup on the array.",
            "- We use solar-safe methods only. Bird proofing, electrical repairs, and roofing repairs are separate unless listed in the quote.",
        ),
    ),
    (
        "Gutter Cleaning",
        "Gutter Cleaning (Roof & Downspouts)",
    ): CopyOverride(
        notes=(
            "- Pricing depends on building size, story height, debris volume, downspout condition, and safe roof access.",
            "- Nearby windows or siding can get splashed during cleanup. Exterior gutter face washing and window cleaning are separate unless they are listed in the quote.",
        ),
    ),
    (
        "Gutter Cleaning",
        "Gutter Cleaning w/Patio Cover (Roof & Downspouts)",
    ): CopyOverride(
        notes=(
            "- Pricing depends on building size, patio-cover scope, story height, debris volume, downspout condition, and safe roof access.",
            "- Nearby windows or siding can get splashed during cleanup. Exterior gutter face washing and window cleaning are separate unless they are listed in the quote.",
        ),
    ),
    (
        "Soft Washing",
        "Low Pressure House Wash (Single Story)",
    ): CopyOverride(
        notes=(
            "- Please make sure all windows and doors are closed before the wash begins. Weak seals can allow solution or water intrusion.",
            "- Pricing depends on treated square footage, siding type, buildup severity, and how much setup or plant protection is needed.",
        ),
    ),
    (
        "Soft Washing",
        "Low Pressure House Wash (Two Story)",
    ): CopyOverride(
        notes=(
            "- Please make sure all windows and doors are closed before the wash begins. Weak seals can allow solution or water intrusion.",
            "- Pricing depends on treated square footage, siding type, buildup severity, story height, and how much setup or plant protection is needed.",
        ),
    ),
    (
        "Roof cleaning",
        "Tile Roof Moss Treatment",
    ): CopyOverride(
        notes=(
            "- Pricing depends on roof size, moss severity, access, and how much of the roof needs treatment.",
            "- Roof treatments kill and loosen organic growth over time. The roof usually looks better gradually rather than instantly the same day.",
        ),
    ),
    (
        "Roof cleaning",
        "Asphalt Roof Moss Treatment",
    ): CopyOverride(
        notes=(
            "- Pricing depends on roof size, moss severity, access, and how much of the roof needs treatment.",
            "- Roof treatments kill and loosen organic growth over time. The roof usually looks better gradually rather than instantly the same day.",
        ),
    ),
}

CATEGORY_FALLBACK_NOTES: dict[str, tuple[str, ...]] = {
    "Commercial Window Cleaning": (
        "- Pricing depends on glass count, access requirements, and service frequency.",
        "- On-site conditions, safety requirements, and timing can affect the final scope or quote.",
    ),
    "Pressure Washing": (
        "- Pricing depends on treated square footage, surface condition, buildup severity, and layout.",
        "- Some stains or discoloration can improve significantly without disappearing completely; specialized stain treatment may need separate quoting.",
    ),
    "Solar Panel Maintenance": (
        "- Pricing depends on panel count, system layout, roof access, and debris severity.",
        "- We use solar-safe methods only. Bird proofing, electrical repairs, and roofing repairs are separate unless they are listed in the quote.",
    ),
    "Soft Washing": (
        "- Pricing depends on treated square footage, surface type, access, and buildup severity.",
        "- Soft washing is designed to clean safely, but existing staining, oxidation, or surface damage can still limit the final cosmetic result.",
    ),
    "Roof cleaning": (
        "- Pricing depends on treated roof area, access, and the severity of moss or organic growth.",
        "- Roof treatment results develop over time, and pre-existing wear or staining can still limit the final cosmetic result.",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the Obsidian service catalog from the CRM export.")
    parser.add_argument(
        "--mode",
        choices=["pilot", "full"],
        default="full",
        help="Update the five-note pilot set or the full catalog.",
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
    value = value.strip().replace("$", "").replace(",", "")
    if not value:
        return 0.0
    return float(value)


def bool_from_csv(value: str) -> bool:
    return value.strip().lower() == "true"


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
    with RAW_EXPORT_CSV.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            records.append(
                SourceRecord(
                    industry=clean_whitespace(row["industry"]),
                    category=clean_whitespace(row["category"]),
                    source_name=row["name"],
                    description=row["description"].strip(),
                    price=money_to_float(row["price"]),
                    cost=money_to_float(row["cost"]),
                    taxable=bool_from_csv(row["taxable"]),
                    unit_of_measure=clean_whitespace(row["unit_of_measure"]),
                    online_booking_enabled=bool_from_csv(row["online_booking_enabled"]),
                    source_uuid=clean_whitespace(row["uuid"]),
                    source_industry_uuid=clean_whitespace(row["industry_uuid"]),
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
    explicit_category_route = CATEGORY_SERVICE_LINE_MAP.get(category)
    if explicit_category_route and category not in {"Bird Proofing", "Repairs", "Custom Services", "Estimates"}:
        return explicit_category_route
    if category == "Estimates":
        if contains_any(combined, GUTTER_KEYWORDS):
            return "Gutters"
        if contains_any(combined, SOLAR_KEYWORDS):
            return "Solar Cleaning"
        if contains_any(combined, WINDOW_KEYWORDS):
            return "Window Cleaning"
        return "Estimates and Internal Review"
    if category == "Bird Proofing":
        explicit_title_route = BIRD_PROOFING_SERVICE_LINE_BY_TITLE.get(title)
        if explicit_title_route:
            return explicit_title_route
        if contains_any(combined, SOLAR_KEYWORDS):
            return "Solar Cleaning"
        if contains_any(combined, ROOF_KEYWORDS):
            return "Roof and Soft Wash"
        return "Repairs and Specialty"
    if category == "Repairs":
        explicit_title_route = REPAIR_SERVICE_LINE_BY_TITLE.get(title)
        if explicit_title_route:
            return explicit_title_route
        if contains_any(combined, WINDOW_KEYWORDS):
            return "Window Cleaning"
        if contains_any(combined, ROOF_KEYWORDS):
            return "Roof and Soft Wash"
        if contains_any(combined, GUTTER_KEYWORDS):
            return "Gutters"
        return "Repairs and Specialty"
    if category == "Custom Services":
        explicit_title_route = CUSTOM_SERVICE_LINE_BY_TITLE.get(title)
        if explicit_title_route:
            return explicit_title_route
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


def escalate_status(current: str, candidate: str) -> str:
    if STATUS_SEVERITY[candidate] > STATUS_SEVERITY[current]:
        return candidate
    return current


def description_contains_heading(description: str, heading: str) -> bool:
    pattern = rf"(?mi)^{re.escape(heading)}:\s*$"
    return re.search(pattern, description) is not None


def infer_review_status(
    record: SourceRecord,
    duplicate_title_counts: Counter,
    duplicate_category_title_counts: Counter,
    duplicate_filename_counts: Counter,
    records_by_line: dict[str, list[SourceRecord]],
) -> tuple[str, bool, list[str]]:
    title = clean_whitespace(record.source_name)
    lowered_title = title.lower()
    lowered_description = record.description.lower()
    notes: list[str] = []
    review_status = "clean"
    title_collision = duplicate_title_counts[record.title] > 1 or duplicate_filename_counts[record.filename] > 1

    if any(term in lowered_title for term in SUSPECT_TITLE_TERMS):
        review_status = "suspect"
        notes.append("Suspicious CRM row name; do not use customer-facing until the service intent is verified.")

    if not record.description:
        review_status = escalate_status(review_status, "needs-review")
        notes.append("CRM description field is empty. Add customer-facing copy before operational use.")

    if record.price == 0:
        review_status = escalate_status(review_status, "needs-review")
        notes.append("CRM price is $0.00. Treat this as quoted, complimentary, or incomplete until pricing is verified.")

    if title_collision:
        if review_status == "clean":
            review_status = "duplicate-candidate"
        if duplicate_category_title_counts[(record.category, record.title)] > 1:
            notes.append(
                "This exact title appears more than once in the same CRM category. Treat it as a likely source duplicate until the CRM rows are reviewed and either merged or intentionally differentiated."
            )
        else:
            notes.append(
                "This title appears more than once across CRM categories. Verify whether the rows should remain distinct or be renamed for clearer catalog routing."
            )

    if record.online_booking_enabled and any(pattern in lowered_description for pattern in INCLUDED_BOOKING_PATTERNS):
        review_status = escalate_status(review_status, "needs-review")
        notes.append(
            "Description says this work is included with another service, but the CRM row is also online-bookable. Confirm whether it should stay as a separate bookable item."
        )

    if any(term in lowered_description for term in RISKY_PROMISE_TERMS):
        review_status = escalate_status(review_status, "needs-review")
        notes.append("Source copy uses guarantee language. Confirm that the promise is operationally and legally safe before publishing it.")

    has_primary_structure = any(
        description_contains_heading(record.description, heading)
        for heading in ("What we do", "Why it’s worth it", "Why it's worth it", "What’s not included", "What's not included")
    )
    has_secondary_structure = any(
        description_contains_heading(record.description, heading)
        for heading in ("Includes", "Benefits", "Note")
    )
    if has_primary_structure and has_secondary_structure:
        review_status = escalate_status(review_status, "needs-review")
        notes.append("Description contains multiple structure styles stitched together. Consolidate it into one customer-facing format.")

    if "pavers" in lowered_description and "paver" not in lowered_title:
        line_records = records_by_line.get(record.service_line, [])
        if any("paver" in other.title.lower() for other in line_records if other.source_uuid != record.source_uuid):
            review_status = escalate_status(review_status, "needs-review")
            notes.append(
                "Description mentions pavers even though a separate paver-specific service exists. Clarify the scope so staff and customers do not confuse the offerings."
            )

    if not record.online_booking_enabled and record.category in STANDARD_SERVICE_CATEGORIES and record.service_type == "core-service":
        notes.append("Core service is not currently online-bookable in the CRM. Confirm whether that is intentional.")

    return review_status, title_collision, notes


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


def normalize_override_lines(lines: tuple[str, ...] | None) -> str:
    if not lines:
        return ""
    return "\n".join(lines).strip()


def copy_override_for(record: SourceRecord) -> CopyOverride | None:
    override = COPY_OVERRIDES.get((record.category, record.title))
    if override:
        return override
    lowered_description = record.description.lower()
    if (
        record.online_booking_enabled
        and record.price == 0
        and any(pattern in lowered_description for pattern in INCLUDED_BOOKING_PATTERNS)
    ):
        return CopyOverride(
            notes=(
                "- This line currently behaves like an add-on or bundle item, not a clean standalone published price. Keep it quote-based until the CRM pricing rule is cleaned up.",
                "- Use the approved quote to decide whether it is bundled or separately charged on a given job.",
            )
        )
    return None


def build_summary(record: SourceRecord, sections: dict[str, list[str]]) -> str:
    override = copy_override_for(record)
    if override and override.summary:
        return normalize_override_lines(override.summary)
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
    notes.append("Use the Local Notes and Links section for approved SOP, checklist, equipment, and purchase-note links.")
    return notes


def build_notes_text(record: SourceRecord, sections: dict[str, list[str]]) -> str:
    override = copy_override_for(record)
    if override and override.notes:
        return normalize_override_lines(override.notes)
    notes = markdownize_lines(sections["notes"])
    if notes:
        return notes
    fallback = CATEGORY_FALLBACK_NOTES.get(record.category)
    if fallback:
        return normalize_override_lines(fallback)
    return normalize_override_lines(
        (
            "- Final pricing and scope depend on the approved quote, site conditions, and access at the time of service.",
            "- If the job conditions are different from the original assumption, the scope or price may need to be updated before work begins.",
        )
    )


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


def block_from_lines(lines: list[str]) -> str:
    return "\n".join(lines).rstrip()


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


def to_yaml_list(key: str, values: list[str]) -> list[str]:
    if not values:
        return [f"{key}: []"]
    lines = [f"{key}:"]
    for value in values:
        lines.append(f"  - {value}")
    return lines


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    remainder = text[4:]
    marker = "\n---\n"
    end_index = remainder.find(marker)
    if end_index == -1:
        return "", text
    return remainder[:end_index], remainder[end_index + len(marker) :]


def parse_frontmatter(text: str) -> dict[str, str | list[str]]:
    frontmatter: dict[str, str | list[str]] = {}
    if not text:
        return frontmatter
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        raw_line = lines[index]
        if not raw_line.strip():
            index += 1
            continue
        if ":" not in raw_line:
            index += 1
            continue
        key, raw_value = raw_line.split(":", 1)
        key = key.strip()
        value = raw_value.lstrip()
        if value == "[]":
            frontmatter[key] = []
            index += 1
            continue
        if value == "":
            items: list[str] = []
            next_index = index + 1
            while next_index < len(lines) and lines[next_index].startswith("  - "):
                items.append(lines[next_index][4:])
                next_index += 1
            if items:
                frontmatter[key] = items
                index = next_index
                continue
            frontmatter[key] = ""
            index += 1
            continue
        frontmatter[key] = value
        index += 1
    return frontmatter


def parse_body_blocks(body: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    lines = body.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not (line.startswith("## ") or line.startswith("> [!")):
            index += 1
            continue
        block_start = line
        next_index = index + 1
        while next_index < len(lines) and not (
            lines[next_index].startswith("## ") or lines[next_index].startswith("> [!")
        ):
            next_index += 1
        block_text = "\n".join(lines[index:next_index]).rstrip()
        blocks[block_start] = block_text
        index = next_index
    return blocks


def load_existing_note(path: Path) -> ExistingNote:
    text = path.read_text(encoding="utf-8")
    frontmatter_text, body = split_frontmatter(text)
    return ExistingNote(
        path=path,
        frontmatter=parse_frontmatter(frontmatter_text),
        blocks=parse_body_blocks(body),
    )


def build_existing_note_index() -> dict[str, ExistingNote]:
    existing_notes: dict[str, ExistingNote] = {}
    for folder in SERVICE_FOLDERS:
        for path in sorted((CATALOG_ROOT / folder).glob("*.md")):
            note = load_existing_note(path)
            source_uuid = str(note.frontmatter.get("source_uuid", "")).strip()
            if not source_uuid:
                continue
            existing_notes[source_uuid] = note
    return existing_notes


def unique_list(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        cleaned = clean_whitespace(value)
        if not cleaned or cleaned in seen:
            continue
        seen.add(cleaned)
        ordered.append(cleaned)
    return ordered


def preserved_scalar(existing_note: ExistingNote | None, key: str, default: str) -> str:
    if existing_note is None:
        return default
    value = existing_note.frontmatter.get(key, "")
    if isinstance(value, list):
        return default
    cleaned = value.strip()
    return cleaned or default


def preserved_list(existing_note: ExistingNote | None, key: str, default: list[str]) -> list[str]:
    if existing_note is None:
        return default
    value = existing_note.frontmatter.get(key, default)
    if isinstance(value, list):
        merged = unique_list([*value, *default])
        return merged or default
    return default


def reviewed_existing_note(existing_note: ExistingNote | None) -> bool:
    if existing_note is None:
        return False
    status = preserved_scalar(existing_note, "status", "draft").lower()
    last_reviewed = preserved_scalar(existing_note, "last_reviewed", "")
    return bool(last_reviewed) or status != "draft"


def should_preserve_block(existing_note: ExistingNote | None, block_key: str) -> bool:
    if existing_note is None:
        return False
    if block_key in PRESERVE_ALWAYS_BLOCKS and block_key in existing_note.blocks:
        return True
    if reviewed_existing_note(existing_note) and block_key in PRESERVE_WHEN_REVIEWED_BLOCKS and block_key in existing_note.blocks:
        return True
    return False


def preserved_block(existing_note: ExistingNote | None, block_key: str) -> str | None:
    if should_preserve_block(existing_note, block_key):
        return existing_note.blocks[block_key]
    return None


def format_frontmatter(record: SourceRecord, aliases: list[str], existing_note: ExistingNote | None, run_date: str) -> list[str]:
    created = preserved_scalar(existing_note, "created", run_date)
    status = preserved_scalar(existing_note, "status", "draft")
    owner = preserved_scalar(existing_note, "owner", "Trevor")
    last_reviewed = preserved_scalar(existing_note, "last_reviewed", "")
    next_review = preserved_scalar(existing_note, "next_review", "")
    tags = preserved_list(existing_note, "tags", ["service-description"])
    lines = [
        "---",
        "type: service-description",
        f"status: {status}",
        f"owner: {owner}",
        f"created: {created}",
        f"last_reviewed: {last_reviewed}" if last_reviewed else "last_reviewed:",
        f"next_review: {next_review}" if next_review else "next_review:",
        f"service_line: {record.service_line}",
        f"service_type: {record.service_type}",
        f"customer_visibility: {record.customer_visibility}",
        f"review_status: {record.review_status}",
        f"title_collision: {str(record.title_collision).lower()}",
        f"source_uuid: {record.source_uuid}",
        f"price: {record.price:g}",
        f"unit_of_measure: {record.unit_of_measure}" if record.unit_of_measure else "unit_of_measure:",
        f"cost: {record.cost:g}",
        f"taxable: {str(record.taxable).lower()}",
        f"online_booking_enabled: {str(record.online_booking_enabled).lower()}",
    ]
    lines.extend(to_yaml_list("aliases", aliases))
    lines.extend(to_yaml_list("tags", tags))
    lines.append("---")
    return lines


def build_summary_block(record: SourceRecord, sections: dict[str, list[str]]) -> str:
    summary = build_summary(record, sections)
    return block_from_lines(
        format_callout(
            SUMMARY_BLOCK,
            summary.splitlines() if summary else ["TODO: verify summary."],
        )
    )


def build_pricing_block(record: SourceRecord) -> str:
    pricing_lines = [
        f"- CRM price: ${record.price:,.2f}",
        f"- Unit: {record.unit_of_measure or 'Quoted / not specified'}",
        f"- Taxable: {'Yes' if record.taxable else 'No'}",
        f"- Online booking enabled: {'Yes' if record.online_booking_enabled else 'No'}",
        f"- Pricing note: {pricing_note(record)}",
    ]
    return block_from_lines(format_callout(PRICING_BLOCK, pricing_lines))


def build_internal_notes_block(record: SourceRecord) -> str:
    internal_notes = [f"- {note}" for note in build_internal_notes(record)]
    return block_from_lines(["## Internal Notes", *internal_notes])


def build_local_notes_block(existing_note: ExistingNote | None) -> str:
    existing_block = preserved_block(existing_note, LOCAL_NOTES_HEADING)
    if existing_block:
        return existing_block
    return block_from_lines(
        [
            LOCAL_NOTES_HEADING,
            "- Add approved SOP, checklist, equipment, and purchase-note links here.",
        ]
    )


def build_source_copy_block(record: SourceRecord) -> str:
    source_copy = record.description or "TODO: verify original source copy; the CRM description field was empty in the export."
    return block_from_lines(
        format_callout(
            SOURCE_COPY_BLOCK,
            source_copy.splitlines() if source_copy else ["TODO: verify original source copy."],
        )
    )


def build_source_metadata_block(record: SourceRecord) -> str:
    source_meta_lines = [
        f"- Industry: {record.industry}",
        f"- CRM category: {record.category}",
        f"- Source UUID: {record.source_uuid}",
        f"- Industry UUID: {record.source_industry_uuid}",
        f"- Source file: 50_Reference/CRM Service Descriptions/{SOURCE_FILE_LABEL}",
    ]
    return block_from_lines(format_callout(SOURCE_METADATA_BLOCK, source_meta_lines))


def build_audit_notes_block(record: SourceRecord) -> str:
    audit_notes = record.audit_notes or ["No auto-detected issues during import."]
    return block_from_lines(format_callout(AUDIT_BLOCK, [f"- {note}" for note in audit_notes]))


def build_review_history_block(existing_note: ExistingNote | None, created: str) -> str:
    existing_block = preserved_block(existing_note, REVIEW_HISTORY_BLOCK)
    if existing_block:
        return existing_block
    history = [
        f"- {created} - Imported from the CRM pricebook export with `scripts/build_service_catalog.py`.",
    ]
    return block_from_lines(format_callout(REVIEW_HISTORY_BLOCK, history))


def render_note(record: SourceRecord, all_records: list[SourceRecord], existing_note: ExistingNote | None, run_date: str) -> str:
    sections = split_description_sections(record.description)
    compact = should_use_compact_shape(record, sections)
    override = copy_override_for(record)
    generated_aliases: list[str] = []
    source_name_clean = clean_whitespace(record.source_name)
    if record.title != source_name_clean:
        generated_aliases.append(source_name_clean)
    aliases = preserved_list(existing_note, "aliases", generated_aliases)
    created = preserved_scalar(existing_note, "created", run_date)

    lines: list[str] = []
    lines.extend(format_frontmatter(record, aliases, existing_note, run_date))
    lines.extend(["", f"# {record.title}", ""])

    summary_block = preserved_block(existing_note, SUMMARY_BLOCK) or build_summary_block(record, sections)
    lines.extend(summary_block.splitlines())
    lines.append("")

    lines.extend(build_pricing_block(record).splitlines())
    lines.append("")

    included = normalize_override_lines(override.included) if override and override.included else markdownize_lines(sections["included"])
    not_included = normalize_override_lines(override.not_included) if override and override.not_included else markdownize_lines(sections["not_included"])
    best_fit = normalize_override_lines(override.best_fit) if override and override.best_fit else markdownize_lines(sections["best_fit"])
    notes = build_notes_text(record, sections)
    related_links = build_related_links(record, all_records)

    if not compact:
        included_block = preserved_block(existing_note, "## Included")
        if included_block:
            lines.extend(included_block.splitlines())
            lines.append("")
        elif included:
            lines.extend(["## Included", included, ""])

        not_included_block = preserved_block(existing_note, "## Not Included")
        if not_included_block:
            lines.extend(not_included_block.splitlines())
            lines.append("")
        elif not_included:
            lines.extend(["## Not Included", not_included, ""])

        best_fit_block = preserved_block(existing_note, "## Best Fit / When To Offer")
        if best_fit_block:
            lines.extend(best_fit_block.splitlines())
            lines.append("")
        elif best_fit:
            lines.extend(["## Best Fit / When To Offer", best_fit, ""])

        notes_block = preserved_block(existing_note, JUST_SO_YOU_KNOW_HEADING)
        if notes_block:
            lines.extend(notes_block.splitlines())
            lines.append("")
        elif notes:
            lines.extend([JUST_SO_YOU_KNOW_HEADING, notes, ""])

        related_block = preserved_block(existing_note, "## Upsells and Related Services")
        if related_block:
            lines.extend(related_block.splitlines())
            lines.append("")
        elif related_links:
            lines.extend(["## Upsells and Related Services", *related_links, ""])

    internal_notes_block = preserved_block(existing_note, "## Internal Notes") or build_internal_notes_block(record)
    lines.extend(internal_notes_block.splitlines())
    lines.append("")

    lines.extend(build_local_notes_block(existing_note).splitlines())
    lines.append("")

    lines.extend(build_source_copy_block(record).splitlines())
    lines.append("")

    lines.extend(build_source_metadata_block(record).splitlines())
    lines.append("")

    lines.extend(build_audit_notes_block(record).splitlines())
    lines.append("")

    review_history_block = build_review_history_block(existing_note, created)
    lines.extend(review_history_block.splitlines())
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
  title_collision:
    displayName: Duplicate Title
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
        - 'title_collision == true'
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
- Keep both CRM CSV reference files in `50_Reference/CRM Service Descriptions/`.
- Treat the raw HCP export as the generator source of truth so UUIDs and categories stay first-class fields instead of being re-parsed from note copy.
- Treat the template-compatible CSV as a downstream import/reference derivative, not the identity source for note generation.
- Use the review views first when cleaning weak, duplicate, quoted, or suspicious services.
- Put approved SOP, checklist, equipment, and purchase-note links in each service note's `Local Notes and Links` section so reruns preserve them.

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


def dedupe_notes(notes: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for note in notes:
        cleaned = clean_whitespace(note)
        if cleaned in seen:
            continue
        seen.add(cleaned)
        output.append(cleaned)
    return output


def build_records(overrides: dict[str, dict[str, str]]) -> list[SourceRecord]:
    records = load_records()
    for record in records:
        override = overrides.get(record.source_uuid, {})
        override_title = clean_whitespace(override.get("title_override", ""))
        record.title = override_title or clean_whitespace(record.source_name)
        record.service_line = override.get("service_line") or infer_service_line(record)
        record.service_type = override.get("service_type") or infer_service_type(record)
        base_filename = sanitize_filename(f"{record.category} - {record.title}")
        record.filename = f"{base_filename}.md"

    duplicate_title_counts = Counter(record.title for record in records)
    duplicate_category_title_counts = Counter((record.category, record.title) for record in records)
    duplicate_filename_counts = Counter(record.filename for record in records)
    records_by_line: dict[str, list[SourceRecord]] = defaultdict(list)
    for record in records:
        records_by_line[record.service_line].append(record)

    for record in records:
        override = overrides.get(record.source_uuid, {})
        auto_review_status, title_collision, auto_audit_notes = infer_review_status(
            record,
            duplicate_title_counts,
            duplicate_category_title_counts,
            duplicate_filename_counts,
            records_by_line,
        )
        record.title_collision = title_collision
        record.review_status = override.get("review_status") or auto_review_status
        record.customer_visibility = override.get("customer_visibility") or infer_customer_visibility(record)
        record.target_folder = record.service_line if record.service_line in SERVICE_FOLDERS else infer_target_folder(record)
        if record.service_type in {"estimate", "warranty", "internal-review"} or record.review_status == "suspect":
            record.target_folder = "Estimates and Internal Review"
        if duplicate_filename_counts[record.filename] > 1:
            short_uuid = record.source_uuid.replace("olit_", "")[:8]
            base_filename = sanitize_filename(f"{record.category} - {record.title} - {short_uuid}")
            record.filename = f"{base_filename}.md"

        initial_override_note = override.get("initial_audit_note", "")
        notes = []
        if initial_override_note:
            notes.append(initial_override_note)
        notes.extend(auto_audit_notes)
        record.audit_notes = dedupe_notes(notes) or ["No auto-detected issues during import."]
    return records


def select_records(records: list[SourceRecord], mode: str) -> list[SourceRecord]:
    if mode == "pilot":
        pilot_order = {uuid: index for index, uuid in enumerate(PILOT_UUIDS)}
        selected = [record for record in records if record.source_uuid in pilot_order]
        selected.sort(key=lambda record: pilot_order[record.source_uuid])
        return selected
    return records


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp")
    tmp_path.write_text(content, encoding="utf-8")
    tmp_path.replace(path)


def sync_notes(records: list[SourceRecord], mode: str) -> list[Path]:
    existing_notes = build_existing_note_index()
    selected_records = select_records(records, mode)
    selected_uuids = {record.source_uuid for record in selected_records}
    run_date = date.today().isoformat()

    written_paths: list[Path] = []
    old_paths_to_remove: list[Path] = []

    for record in selected_records:
        existing_note = existing_notes.get(record.source_uuid)
        output_path = CATALOG_ROOT / record.target_folder / record.filename
        content = render_note(record, records, existing_note, run_date)
        atomic_write(output_path, content)
        written_paths.append(output_path)
        if existing_note is not None and existing_note.path != output_path:
            old_paths_to_remove.append(existing_note.path)

    if mode == "full":
        current_uuids = {record.source_uuid for record in records}
        for source_uuid, existing_note in existing_notes.items():
            if source_uuid not in current_uuids:
                old_paths_to_remove.append(existing_note.path)

    for old_path in old_paths_to_remove:
        if old_path.exists():
            old_path.unlink()

    return written_paths


def main() -> None:
    args = parse_args()
    ensure_directories()
    overrides = load_overrides()
    records = build_records(overrides)
    write_base_file()
    write_dashboard()
    written_paths = sync_notes(records, args.mode)
    print(f"mode={args.mode}")
    print(f"notes_written={len(written_paths)}")
    for path in written_paths:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
