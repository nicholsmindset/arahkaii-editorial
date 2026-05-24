---
name: arahkaii-seo-optimizer
description: SEO + AI Overview optimisation for arahkaii.com — keyword clusters validated against May 2026 Ahrefs data, Rank Math meta, schema, GEO targeting (Singapore / KL / Jakarta / Dubai), AI Overview eligibility. Use whenever optimising meta for a new draft, refreshing a published article's SEO, planning a keyword cluster, scoring a draft for AI Overview surfaces, or generating schema markup. Loads VOICE.md (meta writing in pillar voice), EDITORIAL_PILLARS.md (cluster structure), HALAL_SUBSTITUTIONS.md (keyword redirects). Refuses to optimise for alcohol / nightlife keywords — applies the substitution table instead.
---

# Arahkaii SEO Optimizer

Make every Arahkaii article rank, get cited by AI Overviews, and pull through to *Singapore / KL / Jakarta / Dubai* local SERPs — without ever compromising voice or values.

## Step 0 — Load the foundation

1. `_shared/VOICE.md` (meta is written in pillar voice)
2. `_shared/EDITORIAL_PILLARS.md` (cluster structure)
3. `_shared/HALAL_SUBSTITUTIONS.md` (keyword redirect table)
4. `_shared/IMAGE_SYSTEM.md` (alt-text style)
5. The validated keyword clusters from the gameplan

## Step 1 — Verify the topic is on-brand

Run the keyword through HALAL_SUBSTITUTIONS.md. If the topic naturally pulls toward alcohol or nightlife, switch to the halal substitute keyword cluster before doing any optimisation. Surface the swap to Robert.

## Step 2 — The validated keyword clusters (from May 2026 Ahrefs data)

| Cluster | Primary keyword | Volume signal | Pillar |
|---|---|---|---|
| A — Halal Fine Dining | halal fine dining singapore | High | Dining |
| A — Halal Fine Dining | mother's day halal dining singapore | Very high (validated 8.5k on CNA Luxury) | Dining |
| A — Halal Fine Dining | muslim owned restaurant singapore | Medium-high | Dining |
| A — Halal Fine Dining | halal omakase singapore | Medium, low competition | Dining |
| A — Halal Fine Dining | halal restaurants jb | High | Dining |
| B — Evening Edit | things to do at night singapore | High | Guides |
| B — Evening Edit | best dessert places singapore | High | Dining/Guides |
| B — Evening Edit | late night cafes singapore | Medium-high | Dining/Guides |
| B — Evening Edit | specialty coffee bar singapore | Medium | Dining |
| C — Asian Travel | things to do in johor bahru | Very high | Travel |
| C — Asian Travel | canggu travel guide | High | Travel |
| C — Asian Travel | muslim friendly bali | Medium-high, low competition | Travel |
| C — Asian Travel | things to do in penang | High | Travel |
| C — Asian Travel | halal food tokyo | Surging | Travel |
| D — Modest Style | modest luxury fashion | Growing | Style |
| D — Modest Style | modest fashion brands | High | Style |
| D — Modest Style | quiet luxury asia | Medium | Style |
| D — Modest Style | hijab styles 2026 | Seasonal | Style |
| E — Beauty & Wellness | pdrn facial singapore | Validated on CNA | Beauty |
| E — Beauty & Wellness | halal skincare brands | Growing | Beauty |
| E — Beauty & Wellness | scalp treatment singapore | Validated on CNA | Beauty |
| E — Beauty & Wellness | spa massage jb | Validated on CNA | Beauty |
| F — People | [founder/brand name] interview | Long-tail | People |
| G — Living | modern luxury home interior design | CNA Luxury ranks | Living |
| G — Living | design hotels asia | Medium-high | Living/Travel |
| H — Watches & Quiet Luxury | asian watch brands | Growing | Style |
| H — Watches & Quiet Luxury | fine jewellery singapore | Seasonal (Eid) | Style |

## Step 3 — Generate Rank Math meta

Canonical Rank Math keys (always write to `meta_input` on create, or `wp_update_post_meta` after):

| Key | Rule |
|---|---|
| `rank_math_title` | ≤60 chars total. Pattern: `[Primary keyword phrased naturally] | arahkaii`. End with " | arahkaii". |
| `rank_math_description` | 150–160 chars. Hook + value + soft pull (NO CTA verb). Never "click", "discover", "find out". |
| `rank_math_focus_keyword` | lowercase, single phrase, exact match to primary keyword |
| `rank_math_robots` | `["index", "follow"]` |
| `rank_math_advanced_robots` | `{"max-snippet": "-1", "max-image-preview": "large", "max-video-preview": "-1"}` |

### Meta description template

```
[Specific hook]. [What the piece argues or offers]. [Implicit promise].
```

### Examples

| Type | Meta description |
|---|---|
| Halal Dining listicle | "The halal fine dining restaurants Singapore's stylish set actually book — from Tanjong Pagar omakase to Bugis modern Malay. Halal status declared for every entry." |
| Modest Travel | "Where to eat, pray, and walk in Canggu without a cocktail in sight. A modest traveller's edit of Bali's quietest cluster — by stay, by lunch, by sunset." |
| Founder Profile | "Lyn Lee built Awfully Chocolate from a kitchen in Katong. Twenty-six years in, she is still tasting every batch. A profile from Arahkaii." |

## Step 4 — Schema markup

| Article type | Schema |
|---|---|
| Standard feature | `Article` + `BreadcrumbList` |
| Listicle | `Article` + `ItemList` (each entry as `ListItem`) |
| Restaurant guide | `Article` + `Restaurant` per entry (with `servesCuisine`, `priceRange`, `address`) — add `"hasMenu": false` if no online menu |
| Recipe (rare for us) | `Recipe` |
| FAQ (in service guides) | `FAQPage` |
| How-to (in beauty / styling explainers) | `HowTo` |
| Profile | `Person` + `Article` |

**Always include** `Article.author`, `Article.publisher.name = "Arahkaii"`, `Article.publisher.logo` (full URL).

**Halal-friendly schema additions** for Dining articles:

```json
{
  "@type": "Restaurant",
  "name": "[Name]",
  "address": { ... },
  "servesCuisine": "[cuisine]",
  "priceRange": "$$",
  "knowsAbout": ["halal"],
  "specialty": "halal-certified"
}
```

This helps Arahkaii's listicles appear in halal-specific local search.

## Step 5 — AI Overview optimisation

Run the checklist for any article aiming at AI Overview surfaces:

- [ ] Question-format H2s where natural ("What is halal omakase?", "Why is PDRN trending in Singapore?")
- [ ] Lead sentence of each H2 is a standalone, self-contained answer
- [ ] Definition pattern present at least once ("PDRN refers to polydeoxyribonucleotide, a regenerative skincare actor…")
- [ ] Table or comparison present where natural (e.g. restaurant comparison)
- [ ] FAQ block (4–6 Q&As) at the bottom of service-guide articles
- [ ] Numbers, dates, prices clustered (AI Overviews favour these)
- [ ] Named entities introduced with one sentence of context

## Step 6 — Local / GEO targeting

For city-specific content, ensure:

- City name in H1, first paragraph, ≥2 H2s, meta title, meta description, URL slug
- Neighbourhood names at locals' granularity (Tanjong Pagar, Holland Village, Bukit Bintang)
- Currency in local + SGD where the audience is split
- Local terminology preserved (kopitiam, kedai makan, warung, izakaya)
- `Restaurant` / `LocalBusiness` schema with full address + geo coordinates where verifiable

**Priority cities for Arahkaii:** Singapore · Kuala Lumpur · Johor Bahru · Jakarta · Penang · Bali (Canggu / Ubud / Seminyak) · Bangkok · Tokyo · Istanbul · Dubai · Doha.

## Step 7 — Internal link signals

5–8 internal links per article (matches `arahkaii-internal-linking`). At least one link from within the first 200 words and one from the last 300 words — both are high-equity placements for ranking signals.

## Step 8 — Image SEO

For every image attached via `arahkaii-publisher`:

- File name: `[primary-keyword]-[descriptor].webp` (lowercase, hyphenated)
- Alt text: Plain English description of what is in the image, including the primary keyword if natural — never keyword-stuffed
- Title attribute: Same as alt text
- WebP format, ≤200KB

## Step 9 — Output format

```markdown
# SEO Optimisation — [Article title]

## Keyword strategy
- **Primary:** [keyword] (Cluster [letter], pillar [name])
- **Secondary:** [list]
- **Long-tail:** [list]
- **GEO:** [city — local pack target Y/N]

## Rank Math meta
- `rank_math_title` ([X]/60 chars): "[title]"
- `rank_math_description` ([X]/160 chars): "[description]"
- `rank_math_focus_keyword`: "[keyword]"

## Schema
- Type(s): [Article + ...]
- JSON-LD block: [inline JSON]

## AI Overview score
[Checklist with pass/fail per item]

## Image SEO
- File name: [...]
- Alt text: [...]

## Internal link checks (pulled from arahkaii-internal-linking)
- [N] links · first-200-words placement: ✅/❌ · last-300-words placement: ✅/❌

## Recommended improvements (if any)
[Actionable list]
```

## Hard rules

1. Never optimise for alcohol / nightlife keywords. Apply HALAL_SUBSTITUTIONS.md.
2. Never keyword-stuff meta or alt text — Rank Math will flag and Google will discount.
3. Never write a meta description with a CTA verb ("click", "discover", "find out").
4. Always end `rank_math_title` with ` | arahkaii`.
5. Always declare halal status in `Restaurant` schema for Dining articles.
6. Never optimise above the voice — if "SEO-friendly" wording violates VOICE.md, the voice wins.

---

*Pairs with: arahkaii-editorial-writer (drafting), arahkaii-publisher (meta writes), arahkaii-content-auditor (refresh sweeps), arahkaii-internal-linking (link signals).*
