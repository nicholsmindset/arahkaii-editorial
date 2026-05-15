# URL Database — arahkaii.com

Live inventory of every published post on arahkaii.com. **Rebuilt by Routine 6 quarterly from `arahkaii:wp_get_posts` + `wp_get_post_terms`.**

This file is the source of truth for internal linking. Routines reference it to insert 5–10 contextual links per article.

---

## How routines use this file

The `arahkaii-internal-linking` skill reads this file at the start of every drafting session. When inserting internal links, it:
1. Identifies relevant clusters based on the article's topic and tags
2. Selects 5–10 candidate URLs from those clusters
3. Inserts them with natural anchor text matching the surrounding sentence

---

## Schema

Each post is listed under its primary category, with metadata for linking decisions:

```
### [Post Title]
- URL: <permalink>
- Slug: <post_name>
- Tags: tag1, tag2, tag3
- Modified: <YYYY-MM-DD>
- Word count: <int>
- Primary keyword: <focus_keyword>
- Pillar: <fashion|beauty|culture|travel|lifestyle|sustainability>
```

---

## Categories

*This file is initially a placeholder. The first Routine 6 quarterly run will populate it with live data from arahkaii.com.*

### Fashion

*Awaiting first Routine 6 run.*

### Beauty

*Awaiting first Routine 6 run.*

### Culture

*Awaiting first Routine 6 run.*

### Travel

*Awaiting first Routine 6 run.*

### Lifestyle

*Awaiting first Routine 6 run.*

### Sustainability

*Awaiting first Routine 6 run.*

---

## Topic clusters (cross-pillar linking)

These clusters span categories and are used by the internal-linking skill to identify thematically-related pieces:

- **Quiet luxury cluster:** posts tagged `quiet-luxury`, `heritage-craft`, `future-vintage`, `the-row`, `bottega-veneta`, `lemaire`
- **Korean fashion cluster:** posts tagged `k-fashion`, `korean-heritage-brands`, `songzio`, `wooyoungmi`, `juun-j`, `seoul`, `paris-fashion-week`
- **C-beauty cluster:** posts tagged `c-beauty`, `florasis`, `flower-knows`, `joocyee`, `chinese-makeup`
- **K-beauty cluster:** posts tagged `k-beauty`, `sulwhasoo`, `beauty-of-joseon`, `anua`, `hada-labo`, `glass-skin`, `skinflu`
- **J-beauty cluster:** posts tagged `j-beauty`, `tatcha`, `hada-labo`, `decorte`, `three-cosmetics`
- **Investment fashion cluster:** posts tagged `future-vintage`, `investment-handbags`, `birkin`, `andiamo`, `jackie-1961`
- **Slow luxury travel cluster:** posts tagged `slow-hotel`, `decompression-stay`, `aman`, `six-senses`, `capella`
- **Modest fashion cluster:** posts tagged `modest-fashion`, `buttonscarves`, `vivi-zubedi`, `indonesian-designers`, `malaysian-fashion`
- **Designer profiles cluster:** posts tagged with any specific designer name

---

## Internal linking rules

**Per article:** 5–10 contextual links inserted naturally in body. Stack 2-3 in the intro section, 2-3 mid-article, 2-3 in conclusion or recap.

**Anchor text:** descriptive, natural to the sentence. Never "click here", never the article's full title verbatim. 3-7 words ideal.

**Distribution:**
- 3–4 links from the same pillar (deep topical authority)
- 2–3 links from adjacent pillars (lateral browsing)
- 1–2 links from a category archive (e.g., `/category/fashion/`)

**Reciprocity:** when this article links to others, Routine 6's next run will note candidates for the linked-to articles to link back (when contextually relevant).

**Anti-patterns to avoid:**
- Linking to the same post multiple times in one article
- Stuffing links in a "Related" block at the end (use contextual placement)
- Generic anchor text ("more on this here")
- Linking to category pages exclusively (mix in specific articles)

---

## Maintenance

**Routine 6** rebuilds this file quarterly. Manual edits between rebuilds are okay — they'll be reconciled at the next run.

**Routine 1** consults this file when drafting; if a post in the file is needed but the URL 404s, Routine 1 logs the issue and skips the link.

---

*Last refresh: PENDING (awaiting first Routine 6 run)*
*Initial seed: Robert*
