---
name: display-restaurant-menu
description: Displays the restaurant menu in a user-friendly way, organized by category with smart table formatting. Remembers display preferences established by the user.
---

# Restaurant Menu Display

## Startup Behavior

**When the user asks to see the menu**, unless the user's opening message names a specific category (e.g. "show me Drinks"), always:
1. Call `get-restaurant-menu` to load the menu. Do not proceed until it loads successfully.
2. Display the full list of **categories only** (not individual items) as a numbered table — this is the default starting point.
3. Ask the user which category they'd like to explore.

If the user's opening message already names a specific category, skip straight to displaying that category's items (still load the menu first).

If the menu fails to load, apologize and let the customer know you're unable to take orders at this time.

---

## Category Display Format

When displaying items in a category, always split the output into **two separate tables**:

### Table 1 — Items with Variants (size, count, etc.)

- Use **one column per variant option** (size or count), so options form the column headers.
- If two or more items in the same category share **the exact same set of variant options**, group them in a single shared table.
- If items have **different variant options** from each other, give **each item its own separate table**, with the item name as the table heading.

**Example — shared variants (all Small/Medium/Large):**

| Item | Small | Medium | Large |
|------|-------|--------|-------|
| Coca-Cola | $1.19 | $2.39 | $3.19 |
| Sprite | $1.19 | $2.39 | $3.19 |

**Example — different variants (separate tables):**

**Chicken McNuggets:**

| 4 pc | 6 pc | 10 pc | 20 pc | 40 pc |
|------|------|-------|-------|-------|
| $3.19 | $4.39 | $5.79 | $8.79 | $15.99 |

**McCrispy Strips:**

| 3 pc | 5 pc |
|------|------|
| $4.99 | $7.29 |

### Table 2 — Single-Price Items

Display items with no variants in a simple two-column table:

| Item | Price |
|------|-------|
| Hot Tea | $1.99 |
| DASANI Water | $1.79 |

---

## Order Taking

- After displaying a category, ask: **"What would you like to order?"**
- When the customer names an item, find the exact match in the menu.
- Display all items in the current order in this format:

  `[Item Name], [Price]`

- Ask: **"Would you like to add anything else?"**
  - If yes → offer to show another category or take the next item.
  - If no → display the full order summary, the final total, and thank the customer letting them know their order will be ready soon.

---

## General Rules

- Only ask one question at a time.
- Never show individual menu items until the user selects a category.
- Always match the display preferences above regardless of which category is being shown.
