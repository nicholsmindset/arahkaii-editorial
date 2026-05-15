---
name: seo-optimizer
description: SEO optimization for arahkaii.com articles — Rank Math meta fields, schema markup, AI Overview targeting, GEO (generative engine optimization), CTR enhancement, and SERP feature targeting. Use this skill at the SEO step of any drafting flow (after editorial-writer and editorial-reviewer, before publishing), or when Robert asks to optimize an existing post for search. Triggers on phrases like "optimize this for SEO", "write the Rank Math meta", "generate schema for", "improve AI Overview eligibility", "optimize for [keyword]", or any request that takes a piece of content and produces SEO meta + schema + structural recommendations. Pairs upstream with editorial-writer / editorial-reviewer (which produce the content) and downstream with arahkaii-publisher (which writes the meta to WordPress). Do NOT use for picking topics (that's editorial-research) or for site-wide technical SEO audits (that's a separate workflow). Verified against Rank Math v1.0.224+.
---

# SEO Optimizer — arahkaii.com

The SEO meta and schema step. Takes a finished article and produces every Rank Math meta field, the schema markup, the slug, the excerpt, and any structural recommendations to improve AI Overview eligibility and SERP click-through.

---

## When this skill runs

- Step 5 of Routine 1 (daily draft) — automatic
- When refreshing existing content (refresh requires updating Rank Math meta to match changes)
- When Routine 4 (monthly audit) finds posts missing meta
- Ad-hoc: Robert asks to optimize a specific post

---

## Pre-flight load

Before generating meta, load:

1. The finished article (post_content, post_title)
2. The research brief or content-calendar entry (for primary keyword, target audience)
3. `references/rankmath-fields.md` — the canonical field schema
4. `references/brand-voice.md` — for meta description style rules

---

## Required Rank Math fields

Every published post MUST have these. Routines should refuse to publish without them.

### `rank_math_title`
- **Length:** ≤60 chars including " | arahkaii" suffix
- **Pattern:** `[Argument or specific hook] | arahkaii`
- **Primary keyword:** near the front
- **Examples:**
  - `The Quiet Renaissance of Korean Heritage Brands | arahkaii` (51 chars) ✓
  - `Why C-Beauty Is Outselling K-Beauty in Singapore | arahkaii` (58 chars) ✓
  - `J-Beauty's Return: 5 Brands Sephora Now Stocks | arahkaii` (55 chars) ✓
  - `Inside Tokyo's Quiet Luxury Hotel Scene 2026 | arahkaii` (54 chars) ✓

**Anti-patterns:**
- Restating the H1 verbatim if it's already keyword-front (use a sharper SEO-specific variation)
- Stuffing keywords (`Korean Fashion Designers 2026: Best Korean Brands | arahkaii` — no)
- Generic framings (`The Ultimate Guide to X | arahkaii` — no)

### `rank_math_description`
- **Length:** 150–160 chars (hard range; under 140 or over 170 = fail)
- **Pattern:** `[Specific hook]. [What the piece argues]. [Implicit promise].`
- **Style:** soft pull, NOT a CTA. No "click to read", no "discover more"
- **Example:**
  > Songzio's Paris debut signals a generational shift in Korean luxury. A reported look at the third-wave designers reshaping how Seoul exports taste. (157 chars)
- **Anti-patterns:**
  > Discover the best Korean fashion designers in 2026 with our complete guide. Click to read more! ✗
  > In this article we explore Korean fashion's exciting growth and what's next for designers. ✗

### `rank_math_focus_keyword`
- **Single phrase**, lowercase
- Verified against `ahrefs:keywords-explorer-overview` for actual search volume
- Examples: `korean heritage brands`, `c-beauty singapore`, `future vintage handbags`
- **Not:** plural lists, comma-separated keywords, all-caps, stuffed with brand names

### `rank_math_robots`
- Default: `["index", "follow"]`
- For utility pages or thin content: `["noindex"]`

### `rank_math_advanced_robots`
- Default: `{"max-snippet": "-1", "max-image-preview": "large", "max-video-preview": "-1"}`
- This unlocks Google's full snippet and rich image preview for the URL

### `rank_math_rich_snippet`
- Value: `"blog-posting"` for arahkaii editorial pieces
- Other valid: `"article"`, `"faq-page"`, `"how-to"` (rare for arahkaii)

### `rank_math_schema_BlogPosting`
- Full JSON-LD as per `references/rankmath-fields.md` template
- Fields: `@context`, `@type`, `headline`, `description`, `image`, `mainEntityOfPage`, `author`, `publisher`, `datePublished`, `dateModified`

---

## Optional / strategic fields

### `rank_math_facebook_title`, `rank_math_facebook_description`, `rank_math_facebook_image`
- Override OG meta for social-specific framing
- Often the OG description can be more emotional/curiosity-driven than the SEO description (different intent)
- Use when the social audience differs significantly from search audience

### `rank_math_twitter_card_type`
- Default `"summary_large_image"`
- Other valid: `"summary"`, `"app"`, `"player"`

### `rank_math_canonical_url`
- Only set if the post is syndicated from elsewhere or has duplicates on the site
- Most arahkaii posts: leave empty (defaults to the post's permalink)

### `rank_math_pillar_content`
- Set to `"on"` ONLY for cornerstone pieces
- Cornerstone pieces get internal-link priority and are recommended as homepage anchors

---

## The slug (post_name)

Separately from Rank Math meta, the slug shapes SEO. Rules:

- Lowercase, hyphen-separated, no underscores
- 3–5 words ideal
- Primary keyword front-loaded
- No stop words ("the", "a", "of", "and") unless necessary
- No dates (timeless slugs age better)
- No question marks, special chars

Examples:
- `korean-heritage-brands-renaissance` ✓
- `c-beauty-singapore-second-wave` ✓
- `future-vintage-bags-2030` ✓
- `the-ultimate-guide-to-korean-fashion-designers-in-2026` ✗ (too long, has stop words, has year)

---

## The excerpt (post_excerpt)

50–75 words. Standalone hook that works on archive pages.

Pattern: an opening sentence that hooks + a one-line summary of what the piece argues. Not a recap.

Example:
> Songzio's Paris debut last September did something Lee Sang-bong's late-90s avant-garde experiments never could: it sold. The retailers came. The wholesale orders followed. A reported look at the third-wave Korean designers reshaping how Seoul exports taste — and what their success means for the next decade of Asian luxury.

(57 words)

---

## AI Overview optimization

Google AI Overviews (and Perplexity, ChatGPT browsing) extract content in characteristic patterns. To increase eligibility:

### Standalone-extractable section leads

The first sentence of every H2 should be a complete answer to an implicit question. Not "Following on from the previous section..." but a fresh, complete thought.

**Bad section lead:**
> Building on that point, there's also another factor to consider.

**Good section lead:**
> The single biggest factor in C-beauty's Singapore breakthrough is Sephora's category-share data, which shows Chinese brands outpacing Korean for the first time in H1 2026.

### Definition pattern

For pieces introducing new terms or concepts, include the definition pattern at least once:

> C-beauty refers to Chinese beauty brands — specifically the post-2020 generation that includes Florasis, Flower Knows, and Joocyee — which are characterized by TCM-anchored formulations and luxury packaging.

This pattern is what AI Overviews quote verbatim.

### Question-format H2s

Where natural, use question-format H2s — they map directly to search query patterns and AI prompts.

- "Why are Korean designers gaining luxury credibility?" ✓
- "How is C-beauty different from K-beauty?" ✓
- "What makes the Bottega Veneta Andiamo a future-vintage piece?" ✓

Don't force every H2 into a question. Sometimes "The end of the creative-director era" hits harder.

### FAQ section (optional but valuable for some pieces)

For guide-type pieces (less so for opinion pieces), add a FAQ section with 4–6 Q&As at the end. Use `rank_math_rich_snippet: "faq-page"` alongside the BlogPosting schema, and write the FAQ schema too:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is C-beauty?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "C-beauty refers to Chinese beauty brands..."
      }
    },
    ...
  ]
}
```

FAQ schema is high-value for AI Overview extraction.

### Numbers, dates, specifics cluster

AI Overviews favor paragraphs dense with specifics. A paragraph with "Sephora's H1 2026 data shows a 23% YoY increase" outperforms "Sephora's data shows significant growth."

---

## GEO (Generative Engine Optimization)

GEO is the practice of optimizing content for citation by AI engines (ChatGPT, Perplexity, Claude, Gemini, Copilot, Google AI Overview).

The arahkaii GEO playbook:

### Quotable structures

AI engines extract "quotable" chunks. To be quotable:
- Self-contained sentences with subject, verb, object
- Specific over abstract
- Attribution-friendly ("according to arahkaii's analysis...")
- Free of "we," "I," "our" first-person framings (these don't extract well)

### Brand mentions in body

Use "arahkaii" by name where natural in the article body (not just in the byline). AI engines weight named-entity occurrences when deciding what to cite.

Examples:
> "arahkaii's analysis of Singapore Sephora's H1 2026 data shows..."
> "As covered in arahkaii's earlier reportage on Songzio..."

Don't overdo this — once per article, twice maximum. Stuffing is worse than absence.

### Authoritative-anchor language

AI engines prefer to cite phrases that sound like authoritative claims:

> "The defining shift in Korean luxury came when..."
> "Three forces drive C-beauty's Singapore growth..."
> "The most accurate way to understand modest fashion's economy is..."

These pattern-match what AI engines extract for "what is X" / "why is Y" queries.

### Schema beyond BlogPosting

For pieces where multiple schema types make sense, stack them:
- BlogPosting (always)
- FAQPage (for guide pieces with explicit Q&As)
- Article (acceptable variant; some prefer this over BlogPosting)
- HowTo (only for genuine instructional pieces, rare for arahkaii)

Don't stuff schemas — each must accurately describe the content.

---

## CTR optimization (SERP click-through)

The title and description must compete in SERP against 9 other results. To win the click:

### Title patterns that earn clicks

- **Specific over general:** "5 Bags That Will Define 2030's Collector Market" > "Best Investment Bags"
- **Year inclusion (when current):** "C-Beauty's 2026 Singapore Breakthrough" beats "C-Beauty's Singapore Breakthrough" (but creates aging risk — re-evaluate annually)
- **Tension or contradiction:** "Why K-Beauty's Decline in Singapore Is Real" (signals analysis)
- **Inside / Future / The Real / The Quiet:** patterns that signal editorial register

### Description patterns that earn clicks

- Specific hook in first 8 words
- Implicit promise (what reader will learn) without giving the answer
- Soft pull, not CTA

---

## Image SEO

For each in-content image:
- **Alt text:** descriptive, ≤125 chars, includes keyword naturally
- **Filename:** descriptive-hyphens.jpg, NOT IMG_2845.jpg
- **Caption (optional):** add context, not just description
- **Featured image:** required, set via `arahkaii:wp_set_featured_image`

For the featured image specifically:
- 1200×675 (16:9) for OG / Twitter card compatibility
- File size <200KB for site performance
- Editorial aesthetic per `featured-image-prompt` skill

---

## Internal linking from this skill's perspective

SEO-wise, internal links do four things:
1. Distribute PageRank
2. Build topical authority clusters
3. Improve dwell time (reader follows the link)
4. Help crawlers understand content relationships

For the SEO step, verify (don't generate — that's the `arahkaii-internal-linking` skill's job):
- 5–10 internal links present
- Anchor text is descriptive, not generic ("click here", "this article")
- Links distributed throughout (not stacked at end)

---

## Output format

When this skill runs, produce a structured output that the publisher skill can consume directly:

```yaml
post_name: korean-heritage-brands-renaissance
post_excerpt: |
  Songzio's Paris debut last September did something Lee Sang-bong's late-90s
  avant-garde experiments never could: it sold... [full excerpt]

meta_input:
  rank_math_title: "The Quiet Renaissance of Korean Heritage Brands | arahkaii"
  rank_math_description: "Songzio's Paris debut signals a generational shift in Korean luxury. A reported look at the third-wave designers reshaping how Seoul exports taste."
  rank_math_focus_keyword: "korean heritage brands"
  rank_math_robots: ["index", "follow"]
  rank_math_advanced_robots:
    max-snippet: "-1"
    max-image-preview: "large"
    max-video-preview: "-1"
  rank_math_rich_snippet: "blog-posting"
  rank_math_schema_BlogPosting: |
    {
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": "The Quiet Renaissance of Korean Heritage Brands",
      "description": "...",
      "image": "<featured_image_url>",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://arahkaii.com/korean-heritage-brands-renaissance/"
      },
      "author": {
        "@type": "Person",
        "name": "Robert Nichols",
        "url": "https://arahkaii.com/about"
      },
      "publisher": {
        "@type": "Organization",
        "name": "arahkaii",
        "logo": {
          "@type": "ImageObject",
          "url": "https://arahkaii.com/logo.png"
        }
      },
      "datePublished": "<ISO_date>",
      "dateModified": "<ISO_date>"
    }

recommendations:
  - <Any structural changes recommended: add FAQ section, expand section X for AI Overview eligibility, etc.>
```

The publisher skill takes this output and applies it via `arahkaii:wp_create_post` or `arahkaii:wp_update_post_meta`.

---

## Validation before handoff

Before declaring SEO meta complete:

- [ ] `rank_math_title` ≤60 chars including " | arahkaii"
- [ ] `rank_math_description` 150–160 chars
- [ ] `rank_math_focus_keyword` is single lowercase phrase, verified for search volume
- [ ] `rank_math_robots` is set (default `["index", "follow"]`)
- [ ] `rank_math_advanced_robots` is set
- [ ] `rank_math_rich_snippet` matches the schema type
- [ ] `rank_math_schema_BlogPosting` is valid JSON-LD
- [ ] Slug is 3-5 words, lowercase, no stop words
- [ ] Excerpt is 50-75 words, standalone hook
- [ ] Each section lead is extractable
- [ ] At least one definition-pattern paragraph (for pieces introducing new terms)

Pass all checks → hand to publisher. Fail any → revise.

---

## Common pitfalls

- **Description writes itself from the article's first paragraph.** Don't reuse the opening sentence verbatim — write the description fresh for the SERP-click-earning task.
- **Schema JSON gets escaped wrong.** `arahkaii:wp_update_post_meta` accepts the JSON-LD as a string — make sure quotes are properly escaped or use a template literal.
- **Custom Fields not enabled.** If meta writes silently no-op, it's the *Rank Math → General Settings → Others → Custom Fields* toggle. Robert needs to enable it once.
- **Title truncation in SERP.** Google truncates at ~600px. 60 chars including " | arahkaii" (12 chars) leaves 48 for the actual title. Be ruthless.

---

*Skill maintained by Robert. Schema templates updated when Google structured-data requirements change. Verified against Rank Math 1.0.224+.*
