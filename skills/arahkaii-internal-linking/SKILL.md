---
name: arahkaii-internal-linking
description: Internal linking optimisation + live URL database for arahkaii.com — Muslim-owned, 8-pillar architecture. Use when drafting a new article, updating an existing piece, or auditing link structure. Maintains the URL database under references/url-database.md (rebuilt quarterly by Routine 6). Enforces 5–8 contextual links per article, anchor text that reads naturally, no full-title-verbatim anchors, no "click here". Loads VOICE.md to ensure anchor style matches the pillar voice. Provides cross-linking rules tying clusters together (Halal Fine Dining cluster, Modest Style cluster, Evening Edit cluster, etc.).
---

# Arahkaii Internal Linking

Build a tight internal-link graph that compounds Arahkaii's topical authority — without ever reading like SEO spam.

## Step 0 — Load the foundation

1. `_shared/VOICE.md` (for anchor-text style)
2. `_shared/EDITORIAL_PILLARS.md` (for the cluster graph)
3. `references/url-database.md` (live URL inventory, in the repo)

## Step 1 — Find the article's pillar + cluster

Map the current article to:
- One of the 8 pillars
- One or more keyword clusters (from the gameplan):
  - Cluster A — Halal Fine Dining
  - Cluster B — Arahkaii Evening Edit
  - Cluster C — Asian Travel Guides
  - Cluster D — Modest Luxury Style
  - Cluster E — Beauty & Wellness
  - Cluster F — People & Profiles
  - Cluster G — Living & Interiors
  - Cluster H — Watches & Quiet Luxury

## Step 2 — Select 5–8 contextual links

For each cluster, prioritise links in this order:

1. **Anchor article in the same cluster** (the "best of" pillar piece — e.g. "Best Halal Fine Dining Singapore 2026")
2. **Sister pillar article** (Dining → Travel for cross-border guides; Beauty → People for founder profiles)
3. **Related cluster article** (Halal Fine Dining → Evening Edit dessert bars)
4. **People profile** that humanises a brand mentioned in the article
5. **Guides article** that contextualises (e.g. "Things to Do in [city] at Night" links to the dessert bars guide)

## Step 3 — Anchor-text rules

| Rule | Bad | Good |
|---|---|---|
| Never use the full article title verbatim | "Read our article '12 Hidden Dessert Bars in Singapore Only Insiders Know' for more." | "…the same wave that spawned [Singapore's hidden dessert bars](url)." |
| Never use "click here", "read more", "this article" | "Click here to read more." | "…a pattern we traced [in the modest-luxury movement](url) last month." |
| Match the pillar voice | (varies) | (see VOICE.md §4) |
| Anchor inside a clause, never standalone | "**Read this:** url" | "…[Lyn Lee's founder story](url) makes the same point." |
| Anchor length 2–6 words usually | "Click here to read about how the modest fashion economy is being redefined by a new generation of Asian designers" | "[the modest fashion economy](url)" |
| Use the surrounding sentence's natural phrasing | (varies) | (varies) |

## Step 4 — Distribution rules

- 5–8 links per article (8 max — beyond that, dilution kicks in)
- Distribute throughout the article, never stacked at the end
- At least one link in the first 200 words (high-equity placement)
- At least one link in the last 300 words (closes the loop)
- Never two links in the same sentence
- Never link to the same destination URL twice

## Step 5 — The URL database

`references/url-database.md` (in the repo) is the source of truth. Format:

```markdown
| URL | Pillar | Cluster | Primary keyword | Word count | Published | Anchor suggestions |
|---|---|---|---|---:|---|---|
| /dining/best-halal-fine-dining-singapore-2026/ | Dining | A | halal fine dining singapore | 2200 | 2026-05-25 | "halal fine dining in Singapore", "Arahkaii's halal dining edit", "the city's halal-certified restaurants" |
| /guides/things-to-do-at-night-singapore-no-bars/ | Guides | B | things to do at night singapore | 1900 | 2026-05-29 | "the Arahkaii Evening Edit", "things to do after dark in Singapore", "alcohol-free nights out" |
```

Each row carries 2–3 pre-written anchor text suggestions a writer can drop into a sentence.

## Step 6 — Cluster cross-linking rules

Every published article in a cluster gets at least one inbound link from every other article in that cluster. This is the "topic moat" that compounds rankings.

| Cluster | Cross-link target |
|---|---|
| A — Halal Fine Dining | All halal-dining pieces link to "Best Halal Fine Dining Singapore 2026" (anchor pillar) and at least 2 sibling pieces |
| B — Evening Edit | All evening-edit pieces link to "Things to Do in Singapore at Night That Don't Involve Bars" and at least 2 sibling pieces |
| C — Asian Travel | City guides link to the "Modest Traveller" sidebar pieces and to dining pieces in the same city |
| D — Modest Style | All modest-style pieces link to "The Rise of Modest Luxury in Asian Fashion" anchor |
| E — Beauty & Wellness | Treatment explainers link to "Best Halal-Certified Skincare Brands" and to the relevant clinic guide |
| F — People & Profiles | Profiles link to the brand's pillar article + to one other profile in the same vertical |
| G — Living & Interiors | Home tours link to design-hotel pieces and to people-profile pieces of the designer / owner |
| H — Watches & Quiet Luxury | Watch / jewellery pieces link to the modest-style anchor and to relevant founder profiles |

## Step 7 — Output format

```markdown
## Suggested internal links for [article title]

| # | Anchor text (in context) | Destination URL | Reason |
|---|---|---|---|
| 1 | "...the same wave that spawned [Singapore's hidden dessert bars](url)..." | /guides/hidden-dessert-bars-singapore/ | Same cluster (B), cross-link |
| 2 | "[Lyn Lee's founder story](url) makes the same point" | /people/lyn-lee-awfully-chocolate/ | Sister-pillar (F), humanises brand |
| ... | ... | ... | ... |

**Total: [N] links**
**Distribution:** [first 200 words: N · middle: N · last 300 words: N]
**Pillar coverage:** [Style: N · Dining: N · etc.]
```

## Rules

1. Never link to a draft / unpublished URL.
2. Never use the exact same anchor text twice across the site.
3. Never link to alcohol/nightlife competitor content (even for "context").
4. Always cross-link within the cluster — that's where topical authority lives.
5. Always verify the destination URL is live via `arahkaii:wp_get_post_snapshot` before publishing.

## Quarterly maintenance (Routine 6)

Routine 6 rebuilds `references/url-database.md` by:
1. Calling `arahkaii:wp_get_posts` to list all published posts
2. Extracting pillar / cluster / keyword / word count from each post's meta
3. Generating 2–3 pre-written anchor text suggestions per URL using VOICE.md voice rules
4. Committing the updated file with a "Routine 6: URL database refresh" commit

---

*Loaded by: arahkaii-editorial-writer (during drafting), arahkaii-editorial-reviewer (to validate link density), arahkaii-publisher (to ensure links resolve), and Routine 6 (to rebuild quarterly).*
