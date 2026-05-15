# Category & Tag Map — arahkaii.com

Live taxonomy IDs. **Rebuilt by Routine 6 quarterly from `arahkaii:wp_get_terms`.** This file is initially a placeholder; the first Routine 6 run replaces it with live data.

---

## How routines use this file

When a routine needs to assign a category or tag, it:
1. Looks up the term name in this file
2. Gets the term ID
3. Calls `arahkaii:wp_add_post_terms` with the ID

If the term isn't in this file, the routine calls `arahkaii:wp_get_terms` to look it up live, then either uses the result or (for missing categories) flags for manual creation.

---

## Categories (top-level)

*Placeholder — Routine 6 will populate with live data on first quarterly run.*

| ID | Slug | Name | Description |
|---|---|---|---|
| TBD | fashion | Fashion | Asian designers, runway, luxury industry |
| TBD | beauty | Beauty | K/J/C-beauty, skincare science, heritage practices |
| TBD | culture | Culture | Heritage craft, cultural criticism, designer profiles |
| TBD | travel | Travel | Insider Asia-Pacific luxury guides |
| TBD | lifestyle | Lifestyle | Wellness, fasting, slow living |
| TBD | sustainability | Sustainability | Quiet luxury, craft preservation, sustainable design |

---

## Tags — recurring set

*Routines reference these by name; IDs resolved at runtime via `wp_get_terms`.*

### Geographic tags (always lowercase, hyphenated)
- `singapore`, `jakarta`, `kuala-lumpur`, `bangkok`, `tokyo`, `seoul`, `shanghai`, `hong-kong`, `hanoi`, `bali`, `kyoto`

### Brand tags (lowercase, hyphenated)
- `bottega-veneta`, `the-row`, `loewe`, `gucci`, `saint-laurent`, `hermes`, `chanel`, `prada`, `dior`, `lemaire`
- `songzio`, `wooyoungmi`, `juun-j`, `lee-sang-bong`, `yohji-yamamoto`, `issey-miyake`, `comme-des-garcons`
- `sulwhasoo`, `tatcha`, `hada-labo`, `florasis`, `flower-knows`, `joocyee`, `decorte`, `three-cosmetics`

### Concept tags (always lowercase)
- `quiet-luxury`, `heritage-craft`, `future-vintage`, `modest-fashion`, `slow-hotel`, `decompression-stay`
- `k-beauty`, `j-beauty`, `c-beauty`, `skinflu`, `glass-skin`
- `creative-director-era`, `paris-fashion-week`, `milan-fashion-week`, `seoul-fashion-week`

### Trend tags (rotated quarterly)
- Set fresh by Routine 6 based on what's actually trending in the data

---

## Casing discipline

**Hard rule:** All tags are **lowercase, hyphenated**. Always.

`korean-heritage-brands` ✓
`Korean Heritage Brands` ✗ (creates a duplicate tag)
`korean_heritage_brands` ✗ (underscores not allowed)
`koreanheritagebrands` ✗ (unreadable)

Routines must check via `wp_get_terms` before creating any new tag. If a casing-variant exists, use the existing ID.

---

## Category vs tag — the rule

**Use a category when:** the topic is one of the six pillars
**Use a tag when:** the topic is a brand, place, designer, or concept that could appear in multiple pillars

Example: a piece on Bottega Veneta's Andiamo bag → category: Fashion. Tags: `bottega-veneta`, `quiet-luxury`, `future-vintage`, `investment-handbags`, `intrecciato`.

---

## Pages (non-post taxonomy)

| Slug | Purpose |
|---|---|
| `/about` | Editorial mission, masthead |
| `/contact` | Editor contact |
| `/privacy` | Privacy policy |
| `/terms` | Terms of service |
| `/editorial-standards` | Public-facing version of brand-voice |

---

*This file is rebuilt by Routine 6. Manual edits between runs are okay — they'll be preserved if the routine sees them as additions, not conflicts.*

*Last refresh: PENDING (awaiting first Routine 6 run)*
