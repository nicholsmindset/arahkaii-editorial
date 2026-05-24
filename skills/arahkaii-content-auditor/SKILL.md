---
name: arahkaii-content-auditor
description: Audit existing arahkaii.com content against the new 8-pillar architecture, halal-substitution framework, anti-AI-slop standards, and voice rules. Use to analyse content performance, identify refresh candidates, score thin content, flag alcohol/nightlife violations from legacy posts, audit category distribution, surface gap clusters, and plan refresh sprints. Loads VOICE.md, EDITORIAL_PILLARS.md, HALAL_SUBSTITUTIONS.md. Produces a prioritised audit report with per-article actions: keep, refresh, halal-fix, or unpublish.
---

# Arahkaii Content Auditor

Score every published article on Arahkaii.com against the revamped brand standard. Output is a prioritised action list — not a vibe check.

## Step 0 — Load the foundation

1. `_shared/VOICE.md`
2. `_shared/EDITORIAL_PILLARS.md`
3. `_shared/HALAL_SUBSTITUTIONS.md`
4. `_shared/IMAGE_SYSTEM.md`
5. Ahrefs / Search Console data for traffic per URL
6. `arahkaii:wp_get_posts` for current published inventory

## Step 1 — Inventory

Pull every published post via `arahkaii:wp_get_posts`. For each: URL, title, published date, primary category, tag list, word count, current organic traffic (last 90 days), backlinks, top keyword + position.

## Step 2 — Score each article (0–100, 10 points per dimension)

| Dimension | Pass condition | Points |
|---|---|---|
| Pillar alignment | Maps cleanly to one of the 8 new pillars | 10 |
| Halal compliance | No alcohol / bar references; halal status declared if Dining/Travel/Guides | 10 |
| Voice fidelity | Holds the pillar's micro-voice from VOICE.md §4 | 10 |
| Banned-phrase scan | Zero Tier-1 hits | 10 |
| Specificity | Named subjects, prices, dates, neighbourhoods | 10 |
| Opening 100 words | Scene-anchored, not adjective-stacked | 10 |
| Length floor | ≥ 800 words | 10 |
| Internal links | 5–8 contextual, naturally placed | 10 |
| SEO meta | Rank Math fields complete + within length | 10 |
| Featured image | Inside palette, no slop, no banned subjects | 10 |

## Step 3 — Categorise by action

| Score | Action |
|---|---|
| 90–100 | **Keep** — production-grade, leave as-is |
| 70–89 | **Light refresh** — voice polish, image swap, internal-link top-up |
| 50–69 | **Heavy refresh** — rewrite lede, restructure, add halal status, regenerate images |
| 30–49 | **Major rebuild** — likely a halal violation or off-pillar; rewrite end-to-end |
| 0–29 | **Unpublish** — or fully replace with a halal-aligned substitute article |

## Step 4 — Special audits

### Audit 1 — Halal violation scan

Search every post for alcohol terms (wine, beer, cocktail, champagne, whisky, gin, rum, cognac, sake, vodka, liqueur, bar, speakeasy, nightclub).

For each hit, classify:
- **Direct violation** (article is about alcohol) → Unpublish, replace with halal substitute from HALAL_SUBSTITUTIONS.md
- **Tangential mention** (restaurant happens to serve alcohol) → Apply the "tangential" rule (state halal position plainly, remove tasting notes, remove imagery)
- **Historic / cultural reference** (e.g. "sake brewing in Kyoto" as cultural context) → Soften per voice rules; never glamorise

### Audit 2 — Pillar distribution

Compare current published mix to the target ratios in EDITORIAL_PILLARS.md:

| Pillar | Target | Current | Action |
|---|---:|---:|---|
| Style | 25% | ? | ? |
| Dining | 20% | ? | ? |
| Beauty | 15% | ? | ? |
| Travel | 15% | ? | ? |
| People | 8% | ? | ? |
| Living | 7% | ? | ? |
| Culture | 7% | ? | ? |
| Guides | 3% | ? | ? |

Any pillar more than 5pp off target = calendar adjustment in next 30 days.

### Audit 3 — Decaying content

Pull pages with ≥30% traffic decline vs 90 days ago. Sort by:
- Refreshable (still relevant cluster) → re-publish with current data, new images, voice polish
- Replaced (topic now obsolete or out-of-scope) → 301 to closest sibling article, then unpublish

### Audit 4 — Thin content

Pull pages with <500 words OR with a quality score <60 (per SEO testing tools). Either rebuild to ≥1,500 words OR consolidate / 301.

### Audit 5 — Image audit

For every featured image:
- Inside the locked palette (IMAGE_SYSTEM.md §1)?
- Free of banned subjects (§5)?
- No AI sheen, no extra fingers, no symmetrical perfection?

Schedule batch image regeneration for any failures via `arahkaii-featured-image-prompt`.

### Audit 6 — Internal-link graph

For each cluster, check cross-link density. Every article in a cluster should have ≥3 inbound links from other articles in the same cluster. Surface broken links.

## Step 5 — Output: the audit report

```markdown
# Arahkaii Content Audit — [ISO date]

## Headline numbers
- Total published: [N]
- Production-grade (90+): [N] · [%]
- Light refresh (70–89): [N] · [%]
- Heavy refresh (50–69): [N] · [%]
- Major rebuild (30–49): [N] · [%]
- Unpublish recommended (0–29): [N] · [%]

## Halal violation scan
- Direct violations: [N] — [list with URLs]
- Tangential mentions: [N] — [list with URLs]
- Recommended action: [unpublish / rewrite / 301]

## Pillar distribution vs target
| Pillar | Target | Current | Delta | Action |
|---|---:|---:|---:|---|

## Decaying content (top 20 by traffic loss)
| URL | -% | Action |
|---|---:|---|

## Thin content (under 500 words)
| URL | Word count | Action |
|---|---:|---|

## Image audit failures
[List of URLs needing new featured images]

## Internal-link orphans
[List of articles with <2 inbound links from same cluster]

## Recommended refresh sprint (next 30 days)
| Priority | URL | Action | Owner | ETA |
|---|---|---|---|---|

## Cluster gap recommendations
[Pillars / clusters under-served — suggested new articles to commission]
```

## Hard rules

1. Never auto-unpublish — surface the recommendation, let Robert approve.
2. Halal violations always rank top-priority regardless of traffic.
3. Pillar audit always uses the 8-pillar architecture (not the legacy 6-pillar).
4. Image audit always uses the IMAGE_SYSTEM.md palette as the source of truth.
5. Never recommend deletion if the URL has ≥5 backlinks — recommend rewrite + redirect instead.

---

*Pairs with: arahkaii-publisher (executes the refresh writes), arahkaii-editorial-writer (drafts the rebuilt content), arahkaii-seo-optimizer (rewrites meta during refresh), arahkaii-featured-image-prompt (regenerates failed images).*
