# Phase 1 — Homepage Rebuild Spec

**For:** Robert Nichols, executing in wp-admin · **Page:** `page-id-13` · **Theme:** Soledad v8.7.3 (Penci) · **Builder:** Elementor · **Time estimate:** 2-3 hours

This spec is written to be executed step-by-step without further consultation. Each step has a verification check.

---

## The problem (one sentence)

The homepage is an Elementor static page using 11 hand-curated Penci background-image tiles — it renders **zero `<article>` elements**, **zero `<h1>`**, and **zero dynamic post loops**. New articles only surface in the dynamic mega-menu header, never in the body. We're going to replace the static tiles with Elementor Posts widgets that pull the latest posts from each pillar, while keeping the editorial aesthetic.

---

## Backup procedure (do this BEFORE any edit)

1. In wp-admin → Elementor → **Tools** → **Import / Export Kit** → **Export Kit**
2. Select only **Templates** → **Pages** → check `Homepage` (page-id-13)
3. Download the `.zip` and save to `/Users/robertnichols/Desktop/arahkaii_site/audit/homepage-v1-backup-2026-05-26.zip`
4. Also commit the file to the editorial repo for version history:
   ```bash
   cd /tmp/arahkaii-editorial
   git checkout -b homepage-rebuild-2026-05-26
   mkdir -p references/homepage-snapshots
   cp /Users/robertnichols/Desktop/arahkaii_site/audit/homepage-v1-backup-2026-05-26.zip references/homepage-snapshots/
   git add references/homepage-snapshots/
   git commit -m "snapshot: homepage v1 Elementor export before 2026-05-26 rebuild"
   ```

**Restore (if needed):** Elementor → Tools → Import/Export Kit → Import → upload the zip → restores page-id-13 to current state.

---

## Step 1 — Verify pillar categories exist

The Posts widgets filter by category. Before building, confirm all 8 pillar slugs exist:

In wp-admin → Posts → **Categories**, confirm these slugs:

| Required slug | Pillar | Current status to check |
|---|---|---|
| `style` | Style | likely missing (legacy was `fashion`) |
| `beauty` | Beauty | exists (live posts use it) |
| `dining` | Dining | exists (halal-fine-dining post is published) |
| `travel` | Travel | exists |
| `living` | Living | exists |
| `people` | People | likely missing (legacy posts may be under `culture`) |
| `culture` | Culture | exists |
| `guides` | Guides | likely missing |

**If `style`, `people`, or `guides` are missing:**

1. In wp-admin → Posts → Categories → **Add New Category**
2. Set Name, Slug exactly as above, leave Parent = None
3. Description (helps SEO + the Posts widget's category description display):
   - **Style:** "Modest luxury and Asian designers — investment-grade clothing, modest swimwear, hijab styling, and the houses we cover from Tatler Asia + Vogue Arabia register."
   - **People:** "Founders, tastemakers, and creator-CEOs. Especially Muslim-owned brands and the Southeast Asian designers shaping how modern luxury looks."
   - **Guides:** "Service journalism — what to buy, where to eat, how to dress. Includes the Arahkaii Evening Edit."

4. **Do NOT auto-create from the Posts widget** (per `arahkaii-editorial/CLAUDE.md` §6, categories are read-only; creating them is a deliberate one-time step).

**Verification:**
```bash
curl -s "https://www.arahkaii.com/wp-json/wp/v2/categories?per_page=20&_fields=id,name,slug,count" | python3 -m json.tool
```
Confirm all 8 slugs present with `count >= 1`.

---

## Step 2 — Add new pillar categories to existing posts

Most existing posts live under legacy `/fashion/`, `/culture/`, `/beauty/` etc. To make the homepage Posts widgets find them under the new pillar names, we ADD the new category (don't migrate URLs — that creates more redirect chains).

Strategy: dual-category every post. Example: a post in `fashion` gets `style` added; a post in `culture` that's about a designer gets `people` added.

**Manual mapping** (the safe path):
1. Posts → All Posts → filter by Category = Fashion
2. Bulk-select → Bulk Actions → Edit → **Add** Categories: `style`
3. Repeat for Culture → add `people` for designer/founder profiles, `guides` for service pieces

**OR via the WP MCP** (faster, requires `ARAHKAII_TOKEN`):
```python
# Get all posts in Fashion category and add Style:
arahkaii:wp_get_posts(category_slug="fashion", per_page=50)
# For each post:
arahkaii:wp_add_post_terms(post_id=X, taxonomy="category", term_ids=[STYLE_CAT_ID])
```

(This is one of the few places where running the WP MCP saves real time — but it's optional. Manual works fine for ~30-40 posts.)

---

## Step 3 — Edit page-id-13 in Elementor

### 3.1 Open the page

wp-admin → Pages → All Pages → Homepage → **Edit with Elementor**

### 3.2 Remove the existing static tile sections

There are likely 2-3 Elementor sections containing the Penci `penci-bgitem` tiles. For each:

1. Click the section's blue handle → **Save as Template** (name it `Homepage v1 Static Tiles`, save to template library — extra safety on top of the Kit export)
2. Then **Delete** the section

**Keep:** the site header/menu, the footer, and any newsletter capture form (those are already dynamic or static-and-fine).

### 3.3 Add Section 1 — Hero strip (sticky/editor's pick)

1. Add a new section → 1 column, full width, no padding
2. Drop in an **Elementor Heading** widget
   - Text: **Living beautifully, with intention.**
   - HTML tag: **H1** (this fixes the homepage's `<h1>` count from 0 → 1)
   - Alignment: left
   - Typography: match the Soledad H1 default (the theme will inherit if you don't override)
   - Custom CSS class: `arahkaii-tagline`
3. Below it, drop a **Posts widget** (Elementor free) OR **Loop Grid** (Elementor Pro — preferred if you have it)

**Posts widget config (hero):**
- Skin: **Cards** (or **Classic** if cards too heavy)
- Columns: **5** (1 large featured + 4 below) — Elementor's Pro Posts widget supports this; if free version, use a 4-col grid
- Posts Per Page: **5**
- Source: **Posts**
- Include By: **Term** → select `Editor's Pick` tag (create this tag in wp-admin first if needed) OR **Sticky Posts** (use WP's built-in Sticky for the 1-2 editor's pick at the top)
- Order By: **Date** Order **DESC**
- Show: **Image**, **Title**, **Excerpt** (15 words), **Date**, **Author**
- Image size: medium_large
- Read More: hidden

### 3.4 Add Section 2 — The Evening Edit (Guides pillar)

1. New section → 1 column, full width
2. **Heading widget**: text `The Evening Edit`, HTML tag **H2**, wrap in a link to `/guides/` (Elementor: paste `/guides/` into Heading Link field)
3. Optional sub-heading: `Service journalism, modestly considered.` (Text Editor widget, small grey text)
4. **Posts widget**:
   - Skin: Classic, 4 columns
   - Posts Per Page: **4**
   - Source: Posts → Include By Term → category `guides`
   - Order By: Date DESC

### 3.5 Section 3 — Dining (★ highest-ROI pillar)

1. New section, 1 column
2. **Heading** `Dining` → H2 → link `/dining/`
3. Optional eyebrow text: `Halal-conscious. Editorially uncompromising.`
4. **Posts widget**:
   - Skin: Cards
   - Posts Per Page: **6** (this pillar gets more real estate)
   - Source: category `dining`
   - Order By: Date DESC
5. Add a CTA below: text `View all of Dining →` linked to `/dining/`

### 3.6 Section 4 — Style

1. New section
2. **Heading** `Style` → H2 → link `/style/`
3. **Posts widget**: 4 cols, 4 posts, category `style`, Date DESC

### 3.7 Section 5 — Beauty

Same pattern, category `beauty`.

### 3.8 Section 6 — Travel

Same pattern, category `travel`.

### 3.9 Section 7 — People & Culture (2-column row)

1. New section → **2 columns** (50/50)
2. Left column:
   - Heading `People` → H2 → link `/people/`
   - Posts widget: 1 col, 3 posts, category `people`, Date DESC
3. Right column:
   - Heading `Culture` → H2 → link `/culture/`
   - Posts widget: 1 col, 3 posts, category `culture`, Date DESC

### 3.10 Section 8 — Living

Same pattern as Style/Beauty/Travel, 4 cols, 4 posts, category `living`.

### 3.11 Section 9 — Newsletter capture

Keep the existing newsletter form if it exists. If not, add a Contact Form 7 form (the plugin is already active per the homepage HTML inspection).

Suggested copy above the form (Text Editor widget):
- **Heading H3:** *Join the Arahkaii circular.*
- **Subtext:** *A short weekly note from the editors — the four pieces we kept reading, one room worth booking, one thing worth wearing.*

### 3.12 Save the Elementor page

Hit **Update**. Elementor commits the layout.

---

## Step 4 — Update Rank Math meta on page-id-13

The current homepage meta predates the 8-pillar revamp. Update it.

### Via wp-admin (manual):

1. wp-admin → Pages → Homepage → **Edit** (Block Editor or Classic)
2. Scroll to the **Rank Math SEO** meta box (below the content)
3. Set:
   - **Focus Keyword:** `asian modern luxury`
   - **SEO Title:** `Arahkaii | Asian modern luxury, modestly lived` (45 chars)
   - **Meta Description:** `Style, Dining, Travel and Culture for the modern Asian woman. Editorial standards from Singapore, KL, Jakarta and Dubai — modest by design.` (155 chars)
4. **Update**

### Via WP MCP (if `ARAHKAII_TOKEN` is set):

```python
arahkaii:wp_update_post_meta(
    id=13,
    meta={
        "rank_math_focus_keyword": "asian modern luxury",
        "rank_math_title": "Arahkaii | Asian modern luxury, modestly lived",
        "rank_math_description": "Style, Dining, Travel and Culture for the modern Asian woman. Editorial standards from Singapore, KL, Jakarta and Dubai — modest by design.",
        "rank_math_robots": ["index", "follow"],
        "rank_math_advanced_robots": {"max-snippet": "-1", "max-image-preview": "large", "max-video-preview": "-1"}
    }
)
# Round-trip verify
arahkaii:wp_get_post_snapshot(id=13, include=["meta"])
```

---

## Step 5 — Add ItemList schema (for the 8 pillars)

Rank Math doesn't auto-emit `ItemList` for static homepages. Add it via Rank Math → **Titles & Meta** → **Homepage** → **Schema** → **Custom Schema**.

Paste this JSON-LD (it tells Google the homepage is an ordered list of 8 pillar pages — helps with sitelink box generation):

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Arahkaii editorial pillars",
  "itemListOrder": "https://schema.org/ItemListOrderAscending",
  "numberOfItems": 8,
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Style",   "url": "https://www.arahkaii.com/style/"},
    {"@type": "ListItem", "position": 2, "name": "Beauty",  "url": "https://www.arahkaii.com/beauty/"},
    {"@type": "ListItem", "position": 3, "name": "Dining",  "url": "https://www.arahkaii.com/dining/"},
    {"@type": "ListItem", "position": 4, "name": "Travel",  "url": "https://www.arahkaii.com/travel/"},
    {"@type": "ListItem", "position": 5, "name": "Living",  "url": "https://www.arahkaii.com/living/"},
    {"@type": "ListItem", "position": 6, "name": "People",  "url": "https://www.arahkaii.com/people/"},
    {"@type": "ListItem", "position": 7, "name": "Culture", "url": "https://www.arahkaii.com/culture/"},
    {"@type": "ListItem", "position": 8, "name": "Guides",  "url": "https://www.arahkaii.com/guides/"}
  ]
}
```

---

## Step 6 — Purge LSCWP cache

After save, the LiteSpeed plugin auto-purges on `save_post`. To force a global purge:

- wp-admin → **LiteSpeed Cache** → **Toolbox** → **Purge All**

Or via WP MCP:
```python
arahkaii:wp_update_post(id=13, fields={})  # re-fires save_post, triggers global purge
```

---

## Step 7 — Verification (run all four checks)

### 7.1 Article element count

```bash
curl -sL -A "Mozilla/5.0" --max-time 12 https://www.arahkaii.com/ | grep -c '<article'
```
**Expected:** ≥25 (one `<article>` per post card across all sections). **Was 0 before.**

### 7.2 H1 count

```bash
curl -sL -A "Mozilla/5.0" --max-time 12 https://www.arahkaii.com/ | python3 -c "import sys, re; html=sys.stdin.read(); h1s=re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I|re.S); print(f'H1 count: {len(h1s)}'); [print(' ', re.sub(r\"<[^>]+>\",\"\",h).strip()[:80]) for h in h1s[:3]]"
```
**Expected:** Exactly 1, content = `Living beautifully, with intention.`

### 7.3 First 6 internal post links match newest posts

```bash
# Get the 6 newest posts from WP REST
curl -s "https://www.arahkaii.com/wp-json/wp/v2/posts?per_page=6&orderby=date&order=desc&_fields=id,slug,link" | python3 -m json.tool
# Compare against what curl sees on the homepage:
curl -sL -A "Mozilla/5.0" --max-time 12 https://www.arahkaii.com/ | python3 -c "
import sys, re
html = sys.stdin.read()
links = re.findall(r'<a[^>]+href=[\"\\'](https://www\\.arahkaii\\.com/[^/\"\\'#?]+/[^/\"\\'#?]+/)', html)
seen = []
for l in links:
    if l not in seen and '/category/' not in l and '/author/' not in l and '/tag/' not in l:
        seen.append(l)
print('First 10 post links on homepage:')
for l in seen[:10]: print(' ', l)
"
```
**Expected:** First 6 post links on the homepage match (or include) the 6 newest posts from the REST API.

### 7.4 ItemList schema parses

```bash
curl -sL -A "Mozilla/5.0" --max-time 12 https://www.arahkaii.com/ | python3 -c "
import sys, json, re
html = sys.stdin.read()
blocks = re.findall(r'<script type=[\"\\']application/ld\\+json[\"\\']>([\s\\S]*?)</script>', html)
print(f'JSON-LD blocks: {len(blocks)}')
for b in blocks:
    try:
        d = json.loads(b)
        t = d.get('@type') or (d.get('@graph',[{}])[0].get('@type') if isinstance(d.get('@graph'),list) else None)
        print(f'  Type: {t}')
    except Exception as e:
        print(f'  PARSE ERROR: {e}')
"
```
**Expected:** Block count ≥ 4 (WebSite, Person, Organization, **ItemList**, BreadcrumbList).

---

## Step 8 — Re-submit to GSC

1. Open Google Search Console → **URL Inspection** → paste `https://www.arahkaii.com/`
2. If the cached version is the old static page, click **Request Indexing**
3. Within 24h Google should recrawl. The next sitemap report should also show updated link discovery.

---

## Step 9 — Commit the change

```bash
cd /tmp/arahkaii-editorial
# The Phase 1 work itself doesn't change repo files (Elementor changes live in WP DB),
# but document the rebuild in references/
cat > references/homepage-v2-layout.md << 'EOF'
# Homepage v2 Layout (deployed 2026-05-26)

Replaces the v1 static Penci tile layout. See REVAMP_NOTES.md for context.

## Section structure

| # | Section | Source | Posts shown | Category filter |
|---|---|---|---:|---|
| 1 | Hero — Editor's Picks + H1 | Sticky / Editor's Pick tag | 5 | (Sticky) |
| 2 | The Evening Edit | Posts widget | 4 | guides |
| 3 | Dining ★ | Posts widget | 6 | dining |
| 4 | Style | Posts widget | 4 | style |
| 5 | Beauty | Posts widget | 4 | beauty |
| 6 | Travel | Posts widget | 4 | travel |
| 7 | People & Culture | 2-col Posts widgets | 3+3 | people, culture |
| 8 | Living | Posts widget | 4 | living |
| 9 | Newsletter capture | Contact Form 7 | — | — |
| 10 | Footer | (theme default) | — | — |

## Brand H1: "Living beautifully, with intention."

From brand-voice.md §0 — the master tagline.

## ItemList schema present on homepage

8 pillars listed as itemListElement, ordered per editorial-pillars.md output-share allocation.

## v1 backup

Stored at `references/homepage-snapshots/homepage-v1-backup-2026-05-26.zip`.
Elementor Tools → Import Kit to restore.
EOF
git add references/homepage-v2-layout.md
git commit -m "homepage v2: dynamic Posts widgets per pillar, H1 fix, ItemList schema"
```

---

## Estimated impact (if executed cleanly)

| Signal | Before | After |
|---|---:|---:|
| `<article>` elements on homepage | 0 | ≥ 25 |
| `<h1>` on homepage | 0 | 1 |
| New posts surfacing within 24h of publish | No (manual edit required) | Yes (auto via Posts widgets) |
| Internal links from homepage | 15 (curated, stale) | 30-40 (dynamic, fresh) |
| PageRank flow to recent posts | Low | High (homepage is highest-PR page) |
| Schema breadth | WebSite + Person + Organization | + ItemList + BreadcrumbList |
| Brand position in `<title>` | "Southeast Asian Fashion, Beauty & Lifestyle" (pre-revamp) | "Asian modern luxury, modestly lived" (8-pillar aligned) |

**SEO Health Index expected delta:** +25-30 in Technical Foundations subscore.

---

## What to watch in the first 7 days

1. **GSC URL Inspection on `/`:** verify the new content is crawled
2. **GSC Performance → Pages → homepage:** impressions should rise within 14 days as the homepage internal-linking PageRank redistribution helps deeper pages get crawled
3. **Sitemaps report:** the `indexed: 0` issue should start resolving as Google reprocesses the site structure
4. **GA4 (once scope-fixed):** track homepage engagement_rate, session duration, scroll depth — expect 30-50% improvement vs the static layout (users scroll farther when there's content below the fold)
