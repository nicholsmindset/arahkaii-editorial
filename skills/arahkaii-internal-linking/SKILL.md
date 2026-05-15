---
name: arahkaii-internal-linking
description: Internal linking strategy for arahkaii.com articles — selecting candidate URLs from the live database, choosing anchor text, and placing 5-10 contextual links throughout an article body for SEO authority + reader navigation. Use this skill at the linking step of any drafting flow, or when Robert asks to add internal links to existing content. Triggers on phrases like "add internal links", "link this to other arahkaii posts", "build internal linking for", "where should this article link to", "improve internal linking on [post]", or any request that takes content and integrates contextual links. Reads from references/url-database.md (the live URL inventory). Pairs upstream with editorial-writer (which produces the content) and downstream with editorial-reviewer (which validates link quality) and arahkaii-publisher (which ships). Do NOT use for inbound link building from external sites (that's outreach). Do NOT use for navigation/menu linking (that's a theme concern).
---

# Internal Linking — arahkaii.com

The internal-linking skill. Reads `references/url-database.md`, selects 5–10 relevant existing posts, weaves links naturally into the article body. Internal linking is the most undervalued SEO lever — done well, it compounds the entire site's authority.

---

## When this skill runs

- During the drafting flow: after editorial-writer produces the draft, before publishing
- When refreshing existing content: identify new posts that should now link to or from this piece
- For reverse linking: when a high-performer is identified by Routine 3 (weekly performance review) as under-linked, identify candidate inbound-link sources

---

## Pre-flight load

1. `references/url-database.md` — the live URL inventory (rebuilt quarterly by Routine 6)
2. The article being linked (post_content, tags, primary keyword)
3. `references/editorial-pillars.md` — for pillar clustering logic
4. `references/brand-voice.md` section 9 — internal linking voice rules

If `references/url-database.md` is still a placeholder (first run before Routine 6), pull the live list via `arahkaii:wp_get_posts` and proceed with that data temporarily.

---

## The linking framework

### Quantity target

**5–10 internal links per article.** Hard floor: 3. Cap: 12.

Distribution:
- 3–4 from the same pillar (deep topical authority)
- 2–3 from adjacent pillars (lateral browsing, cluster strength)
- 1–2 to category archives (e.g., `/category/fashion/`)

### Placement

Stack links naturally across the body:
- 2-3 in opening third (set up the broader conversation)
- 2-3 in middle third (deepen specific points)
- 2-3 in closing third (extend the reader into the next piece)

**Anti-pattern: stacking all links at the end.** "Read more in these related articles" with 10 links is amateur. Contextual placement is the difference.

### Anchor text rules

From `brand-voice.md` section 9:

✓ **Natural-prose anchor text:** the link reads as part of the sentence
✓ **Descriptive, 3-7 words ideal**
✓ **Vary across the piece** — no two anchors identical

✗ **Generic anchors:** "click here", "read more", "this article", "the post"
✗ **Full-title-verbatim anchors:** `[The Quiet Renaissance of Korean Heritage Brands](url)` — keep it shorter and contextual
✗ **Exact-match keyword stuffing:** linking the same keyword phrase to multiple URLs

Examples:

```
WEAK: For more on Korean fashion, see our article [here](url).

STRONG: ...a pattern that traces back to the [late-90s Korean avant-garde 
designers](url) who never quite broke through commercially.
```

```
WEAK: Read our piece on [The Quiet Renaissance of Korean Heritage Brands](url).

STRONG: ...what Songzio represents fits the broader [generational shift in 
Korean luxury](url) arahkaii has been tracking since early 2026.
```

---

## Selection process

### Step 1 — Identify topic clusters

Look at the article's primary keyword, tags, and pillar. Identify which clusters from `references/url-database.md` apply:

For a piece on "Korean heritage brands":
- Primary cluster: Korean fashion cluster
- Secondary clusters: Quiet luxury cluster, Designer profiles cluster, Asian craft cluster
- Lateral cluster: Cultural reportage cluster

### Step 2 — Pull candidate URLs

From each relevant cluster, list 3-5 candidate URLs. Aim for variety:
- Most recent (last 90 days) — keeps content fresh-feeling
- Highest-trafficked (per Routine 3 data) — distributes PageRank to winners
- Cornerstone pieces (where they exist) — anchors the topical authority

Total candidate pool: 15-25 URLs.

### Step 3 — Score candidates for this article

For each candidate, score:
- **Topical relevance** (1-5): how directly does this URL relate to the article's argument?
- **Lateral value** (1-3): does linking to this URL extend the reader into a meaningful related topic?
- **Anchor opportunity** (1-3): is there a natural place in the body to insert this link?

Total score = relevance + lateral + anchor.

Select top 5-10 by score for actual placement.

### Step 4 — Place each link

For each selected link:
- Identify the specific sentence/clause where it fits naturally
- Write 3-7 word anchor text that reads as part of the sentence
- Verify the surrounding context makes the link's destination clear

Example placement:

```
ARTICLE BODY:
> The third-wave Korean designers — Songzio, Wooyoungmi, Juun.J — share 
> a structural advantage that earlier waves like Lee Sang-bong's avant-garde 
> generation never quite achieved...

LINK PLACEMENT:
> The third-wave Korean designers — Songzio, Wooyoungmi, Juun.J — share 
> a structural advantage that [earlier waves like Lee Sang-bong's avant-garde 
> generation](https://arahkaii.com/lee-sang-bong-korean-avant-garde/) never quite 
> achieved...
```

The anchor text describes what the linked piece is about. The reader knows what they'll find before clicking.

### Step 5 — Distribute across body

Check distribution:
- Opening third (first 1/3 of body): 2-3 links ✓
- Middle third: 2-3 links ✓
- Closing third (last 1/3 before conclusion): 2-3 links ✓
- Conclusion: 0-1 links max (don't end with a link)

If distribution is off, redistribute — move some links from over-represented zones to under-represented ones.

### Step 6 — Verify no duplicate destinations

Scan the link list — no URL should appear twice. If two candidate URLs would land in the same body location, pick the better one and find another spot for the other.

---

## Topic cluster reference

(Detailed in `references/url-database.md`. Brief summary here.)

### Korean fashion cluster
Posts tagged: `k-fashion`, `songzio`, `wooyoungmi`, `juun-j`, `lee-sang-bong`, `seoul`, `paris-fashion-week`, `korean-heritage-brands`

When to link from: Korean designer pieces, Asian luxury arguments, fashion week coverage
When to link to: pieces analyzing the Korean luxury trajectory, individual designer profiles

### Quiet luxury cluster
Posts tagged: `quiet-luxury`, `the-row`, `bottega-veneta`, `lemaire`, `heritage-craft`, `future-vintage`

When to link from: pieces on understated luxury, investment fashion, designer-as-restraint arguments
When to link to: foundational quiet luxury arguments, specific brand analyses

### C-beauty cluster
Posts tagged: `c-beauty`, `florasis`, `flower-knows`, `joocyee`, `chinese-makeup`

When to link from: C-beauty pieces, comparison-to-K-beauty pieces, Asian beauty market analysis
When to link to: foundational C-beauty primer, specific brand coverage

### K-beauty cluster
Posts tagged: `k-beauty`, `sulwhasoo`, `beauty-of-joseon`, `anua`, `glass-skin`, `skinflu`

When to link from: K-beauty trend pieces, ingredient deep-dives, comparison pieces
When to link to: cornerstone K-beauty pieces, ingredient-specific posts

### J-beauty cluster
Posts tagged: `j-beauty`, `tatcha`, `hada-labo`, `decorte`, `three-cosmetics`

### Investment fashion cluster
Posts tagged: `future-vintage`, `investment-handbags`, `birkin`, `andiamo`, `jackie-1961`

### Slow luxury travel cluster
Posts tagged: `slow-hotel`, `decompression-stay`, `aman`, `six-senses`, `capella`

### Modest fashion cluster
Posts tagged: `modest-fashion`, `buttonscarves`, `vivi-zubedi`, `indonesian-designers`, `malaysian-fashion`

### Designer profiles cluster
Posts tagged with any specific designer name — Daniel Lee, Pharrell, Yohji, Kawakubo, Lee Sang-bong, etc.

---

## Linking when refreshing content

When a post is being refreshed (Routine 6 flags it for `status:refresh`):

1. Read the current post's existing links — keep what still works, remove broken/outdated ones
2. Identify newly-published pieces (since the post's last modification) that should now link here OR be linked from here
3. Add 2-5 new internal links based on the article's argument
4. Optionally: add reverse links — go to the newly-identified posts and edit them to link back to the refreshed piece (use `arahkaii:wp_alter_post` for surgical edits)

---

## Reverse linking (high-performer reinforcement)

Routine 3 (weekly performance review) identifies winning posts that are under-linked from a contextually-relevant cluster. To strengthen these:

1. Identify 3-5 recent posts that would naturally link to the winner
2. For each, find a sentence where the winner's topic fits naturally
3. Use `arahkaii:wp_alter_post` to insert the link surgically
4. Anchor text: descriptive, 3-7 words

This is one of the highest-leverage SEO activities — taking already-performing posts and reinforcing them with relevant inbound internal links.

---

## Validation before handoff

Before declaring linking complete:

- [ ] 5-10 internal links present (3 minimum, 12 maximum)
- [ ] No two links to the same destination
- [ ] Distribution: opening / middle / closing thirds each have at least one
- [ ] No "click here", "read more", "this article" anchors
- [ ] No full-title-verbatim anchors
- [ ] All anchor text reads naturally in its sentence
- [ ] Anchor text variety (no two identical)
- [ ] No links in the final closing paragraph
- [ ] All linked URLs verified (no 404s — check against `url-database.md`)
- [ ] Cluster coverage: same pillar (3-4), adjacent pillars (2-3), archives (1-2)

Pass all → hand to publisher.

---

## When URL database is stale

If `references/url-database.md` shows posts that no longer exist (404 on the live site), the file is stale. Flag this and:

1. Skip the broken link, choose another from the cluster
2. Log to `run-log.md`: "URL database has stale entry — <slug> no longer resolves"
3. Continue with the current article

Routine 6's next quarterly run will rebuild and reconcile.

---

## Anti-patterns to actively avoid

### Reciprocal-spam pattern
Linking from A to B and immediately from B to A in identical anchor text. Looks manipulative. Reciprocal links are fine, but anchor text and context must vary.

### Hub-and-spoke over-pumping
Linking every new piece to one cornerstone article repeatedly. Spreads PageRank too thinly. Mix cornerstone links with specific-piece links.

### Stuffed sentences
Three links in one sentence is too many. Two is the max. One is usually plenty.

```
WEAK (over-stuffed):
The [Korean designers](url1) at the [Paris shows](url2) demonstrate the 
[third-wave shift](url3) we've covered.

STRONG:
The Korean designers at the Paris shows demonstrate the [third-wave shift 
arahkaii has been tracking](url) since early 2026.
```

### Exact-match keyword stuffing
Linking the exact phrase "korean fashion designers" to multiple URLs. Google detects this as manipulation. Vary anchor text.

---

## Output format

When this skill is done, return the article with links integrated. The publisher skill takes the linked article and ships it.

For audit purposes, also produce a link inventory:

```
INTERNAL LINKING REPORT for: <Title>

Total links inserted: <n>

By cluster:
- Korean fashion: <count>
- Quiet luxury: <count>
- Designer profiles: <count>
- Categories: <count>

By distribution:
- Opening third: <count>
- Middle third: <count>
- Closing third: <count>

Link table:
| Anchor text | Destination | Cluster | Position |
|---|---|---|---|
| ... | ... | ... | ... |
```

This report is logged to `run-log.md` when the routine completes.

---

*Skill maintained by Robert. The cluster definitions in `references/url-database.md` are the canonical source — when adding new clusters, update that file, not this skill.*
