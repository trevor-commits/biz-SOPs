# Purchasing Dashboard

Use this as the active buying surface for phone checks, store runs, and restock reviews.

## How To Use
- Create one note per item in `25_Purchasing/` with `00_System/Templates/Purchase Template.md`.
- Use `urgency` for `now`, `soon`, or `later`.
- Use `purchase_kind` for `one-time`, `consumable`, `replacement`, or `upgrade`.
- Use both `service_lines` and `category` when an item belongs to a service lane and a tool family such as `truck`, `ladders`, or `water-fed`.
- Link back to equipment or decision notes when the purchase is tied to a known asset or tool comparison.

## Buy Now
![[Purchasing.base#Buy Now]]

## Buy Soon
![[Purchasing.base#Buy Soon]]

## Later / Wishlist
![[Purchasing.base#Later]]

## Consumables and Replacements
![[Purchasing.base#Restock and Replacement]]

## By Category
![[Purchasing.base#By Category]]

## Phone Capture Rule
- If you are on your phone and know the item belongs in the live queue, create or update the purchase note directly in `25_Purchasing/`.
- If you only have a partial thought, capture it in `00_System/Daily Notes/` and promote it into a purchase note during the next review.

## Sync Safety
- The preferred working copy is the live source of truth.
- Automation should sync before editing and preserve unrelated note changes instead of rewriting whole files.
