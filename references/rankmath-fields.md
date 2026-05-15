# Rank Math Meta Fields — Full Schema

Canonical reference for every Rank Math meta key Routines write to. All keys go to `meta_input` on `wp_create_post`, or to `wp_update_post_meta` after the fact.

---

## Core SEO fields

| Key | Required | Constraints | Notes |
|---|---|---|---|
| `rank_math_title` | Yes | ≤60 chars; end with " \| arahkaii" | The SERP title tag |
| `rank_math_description` | Yes | 150–160 chars | Meta description; soft pull, not CTA |
| `rank_math_focus_keyword` | Yes | Lowercase, single phrase, no quotes | Primary keyword |
| `rank_math_robots` | Yes | Array of strings | Default: `["index", "follow"]`; `["noindex"]` for utility pages |
| `rank_math_advanced_robots` | Recommended | Object | Default: `{"max-snippet": "-1", "max-image-preview": "large", "max-video-preview": "-1"}` |
| `rank_math_canonical_url` | Optional | Full URL | Only for syndicated content |

---

## Open Graph (Facebook + general)

| Key | Notes |
|---|---|
| `rank_math_facebook_title` | OG title override; defaults to `rank_math_title` |
| `rank_math_facebook_description` | OG description; defaults to `rank_math_description` |
| `rank_math_facebook_image` | OG image URL; defaults to featured image |
| `rank_math_facebook_image_overlay` | Optional overlay (`play`, `gif`) |

---

## Twitter / X Cards

| Key | Notes |
|---|---|
| `rank_math_twitter_card_type` | Default `summary_large_image` |
| `rank_math_twitter_title` | Override; defaults to FB title |
| `rank_math_twitter_description` | Override; defaults to FB description |
| `rank_math_twitter_image` | Override; defaults to FB image |

---

## Schema (structured data)

| Key | Notes |
|---|---|
| `rank_math_schema_Article` | JSON-LD Article schema (use `json.dumps()` to serialize) |
| `rank_math_schema_BlogPosting` | BlogPosting variant (default for arahkaii editorial) |
| `rank_math_schema_FAQPage` | For pieces with explicit FAQ sections |
| `rank_math_schema_HowTo` | For instructional pieces (rare for arahkaii) |
| `rank_math_rich_snippet` | Schema type identifier: `article`, `blog-posting`, `faq-page`, etc. |

### Default Article schema template

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "<post_title>",
  "description": "<rank_math_description>",
  "image": "<featured_image_url>",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "<permalink>"
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
  "datePublished": "<ISO date>",
  "dateModified": "<ISO date>"
}
```

---

## Other Rank Math fields

| Key | Purpose |
|---|---|
| `rank_math_breadcrumb_title` | Shorter breadcrumb label override |
| `rank_math_pillar_content` | Set `"on"` for cornerstone pieces only |
| `rank_math_focus_keyword_secondary` | Up to 5 additional related keywords (PRO feature; check before using) |
| `rank_math_news_sitemap_robots` | News sitemap inclusion (not applicable; arahkaii isn't a news pub) |
| `rank_math_internal_links_processed` | Auto-managed by Rank Math; don't write to this |

---

## Title formulas

### Pattern 1: Argument-headline
```
[Argument-stating headline] | arahkaii
```
Examples:
- `The Quiet Renaissance of Korean Heritage Brands | arahkaii` (51 chars)
- `Why C-Beauty Is Outselling K-Beauty in Singapore | arahkaii` (58 chars)

### Pattern 2: Keyword-front
```
[Primary keyword]: [Specific hook] | arahkaii
```
Examples:
- `Korean Heritage Brands: A Generational Shift | arahkaii` (54 chars)
- `J-Beauty's Return: 5 Brands Sephora Now Stocks | arahkaii` (55 chars)

### Pattern 3: Inside/Future
```
Inside [Specific] | arahkaii
Future Vintage: [Specific] | arahkaii
```

**Hard limit:** 60 characters including " | arahkaii" suffix.

---

## Meta description formula

```
[Specific hook]. [What the piece argues]. [Implicit promise].
```

Length: 150–160 chars. Soft pull, not CTA. Never "click to read more" or "discover here."

**Good:** "Songzio's Paris debut signals a generational shift in Korean luxury. A reported look at the third-wave designers reshaping how Seoul exports taste."

**Bad:** "Discover the best Korean fashion designers in 2026. Find out why they're trending and shop our complete guide!"

---

## Focus keyword guidance

- **Single phrase** — not a list, not multiple keywords stuffed in
- **Lowercase** — `korean heritage brands` not `Korean Heritage Brands`
- **Natural** — not "korean-fashion-best-2026"; should read as something a person would type
- **Search-volume-aware** — prefer keywords with measurable search volume (use `ahrefs:keywords-explorer-overview` to verify)

---

## Common gotchas

**Meta writes silently no-op.**
Check *Rank Math → General Settings → Others → Custom Fields* is enabled. If still failing, fall back to `wp_update_post_meta` with explicit keys.

**Title truncated in SERP.**
Google truncates around 600px. 60 chars is the practical limit. " | arahkaii" suffix uses ~12 chars.

**Schema not rendering.**
Verify `rank_math_rich_snippet` is set to match the schema type. `rank_math_schema_Article` alone isn't sufficient; the rich_snippet field tells Rank Math which schema to surface.

**Open Graph image not picking up.**
Featured image is the default. Explicit `rank_math_facebook_image` overrides. URL must be publicly accessible and on `arahkaii.com` (or a CDN that allows hotlinking).

---

*Maintained by Robert. Schema templates updated when Google's structured data requirements change. Field reference verified against Rank Math 1.0.224+ (as of mid-2026).*
