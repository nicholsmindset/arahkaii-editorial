---
name: arahkaii-publisher
description: Publish drafted articles to arahkaii.com (self-hosted WordPress on Hostinger VPS, LiteSpeed) via the AI Engine MCP server. Use this skill whenever Robert wants to push a finished article to WordPress, schedule a post, upload featured images, set categories and tags, write Rank Math SEO meta, or update an existing post. Triggers on phrases like "publish to arahkaii", "push this to WordPress", "schedule this post", "upload as draft", "update the [slug] post", "set the featured image", or any request that ends an editorial workflow with WordPress as the destination. Also triggers when Robert pastes finished editorial output and asks where it should go next. Pairs with editorial-writer (input), editorial-reviewer (QA before publish), arahkaii-internal-linking (link insertion), seo-optimizer (final meta), and featured-image-prompt (hero image generation). Do NOT use for WordPress.com hosted sites — that uses a different connector path.
---

# arahkaii Publisher Skill

Bridge between Claude editorial output and the live arahkaii.com WordPress install. Self-hosted WordPress on a Hostinger VPS running LiteSpeed + LSCWP, with the **AI Engine** plugin exposing an MCP server. The MCP connection gives Claude (Desktop or Code) full create/update/upload access — so this skill exists to keep the workflow disciplined and prevent accidental publishes.

The SEO plugin in use is **Rank Math** (not Yoast). All SEO meta in this skill writes to `rank_math_*` post meta keys.

---

## Setup (one-time)

### On the WordPress side

1. Install **AI Engine** plugin (free version is sufficient for MCP).
2. Go to *AI Engine → Settings → MCP*. Toggle MCP on.
3. Generate a Bearer Token: `openssl rand -hex 32` on the VPS, paste it in.
4. Enable feature groups:
   - **Core** (posts, pages, media, taxonomies) — required
   - **Plugins/Themes** — only if needed; off by default for safety
   - **Polylang / Multilingual** — leave off (arahkaii is single-language)
5. (Optional) Install **SEO Engine** by Meow Apps to expose analytics + SEO audit tools through the same MCP connection.
6. Whitelist `/wp-json/` in Wordfence/security plugin if installed — otherwise REST calls 403.
7. Confirm Rank Math is installed and "Custom Fields" is enabled under *Rank Math → General Settings → Others* (this is what allows MCP-written `rank_math_*` meta to be picked up by the SEO scoring engine).

### On Claude Desktop

Settings → Developer → Edit Config:

```json
{
  "mcpServers": {
    "arahkaii": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://arahkaii.com/wp-json/mcp/v1/http"],
      "env": {
        "AUTH_HEADER": "Bearer YOUR_TOKEN_HERE"
      }
    }
  }
}
```

Restart Claude Desktop. Confirm the `arahkaii` server shows connected in the tools panel.

### On Claude Code

```bash
claude mcp add arahkaii https://arahkaii.com/wp-json/mcp/v1/YOUR_TOKEN --transport http
```

Run `/mcp` inside Claude Code to confirm `✔ connected`.

### Token storage

Store the token in `~/.config/arahkaii/token` (chmod 600), not in shell history or repo. Regenerate it from AI Engine settings if compromised — old tokens stop working immediately.

### Connection sanity check (first call every session)

Before any publish or update, run `mcp_ping` once. It returns the current GMT time and the site name (`arahkaii.com`). If it fails or times out, pause all tool calls and surface the error to Robert — do not retry blind.

---

## Available tools (verified live)

These are the actual MCP tool names exposed by `arahkaii.com` as of 2026-05-15. Use these exact names — earlier drafts of this skill referenced speculative names (`wp_list_categories`, `wp_list_tags`, `wp_search_posts`) that don't exist.

**Connectivity**
- `mcp_ping` — connectivity check, returns GMT time + site name

**Posts (read)**
- `wp_get_post` — basic post data by ID (title, content, status, dates, permalink)
- `wp_get_post_snapshot` — full post + meta + terms + featured image + author in ONE call (use this when context matters)
- `wp_get_posts` — list posts (filterable)
- `wp_count_posts` — counts by status

**Posts (write)**
- `wp_create_post` — create post/page/CPT; `post_title` required; accepts markdown in `post_content`; defaults to `draft`
- `wp_update_post` — update `fields` and/or `meta_input` in one call; also takes `schedule_for` for scheduled posts
- `wp_alter_post` — surgical search-and-replace inside a post field (useful for small content edits without re-uploading)
- `wp_delete_post` — trash/delete (BLOCKED by safety rails below; do not call)

**Post meta**
- `wp_get_post_meta` — read meta key(s)
- `wp_update_post_meta` — bulk update via `meta` object (preferred) or single `key`+`value`
- `wp_delete_post_meta` — remove meta keys

**Terms (categories, tags, custom taxonomies)**
- `wp_get_terms` — list terms in a taxonomy (use this — there is no `wp_list_categories` / `wp_list_tags`)
- `wp_count_terms` — total terms in a taxonomy
- `wp_get_post_terms` — terms attached to a post
- `wp_add_post_terms` — attach/replace terms; `append: true` to add, default `false` REPLACES
- `wp_create_term` — create new category/tag (use sparingly; prefer reusing existing)
- `wp_update_term`, `wp_delete_term`

**Media**
- `wp_upload_media` — upload by URL (preferred) or base64 (small files only)
- `wp_upload_request` — get a one-time upload URL for `curl -F` on local files (use for anything large; base64 over MCP is impractical)
- `wp_get_media`, `wp_count_media`, `wp_update_media`, `wp_delete_media`
- `wp_set_featured_image` — attach thumbnail; pass `post_id` + `media_id` (omit `media_id` to remove)

**Image generation (AI Engine native)**
- `mwai_image` — generate image via AI Engine and store it in the Media Library; can attach directly to a `postId`. Optional alternative to the external `featured-image-prompt` + manual upload flow.
- `mwai_vision` — analyze an existing image (alt text generation, accessibility checks)

**Site / options / users / comments**
- `wp_get_option`, `wp_update_option` — site options (use with extreme caution)
- `wp_get_post_types`, `wp_get_taxonomies` — schema introspection
- `wp_list_plugins` — confirm Rank Math + LiteSpeed Cache are active
- `wp_get_users`, `wp_create_user`, `wp_update_user` — user management (BLOCKED by safety rails)
- `wp_get_comments`, `wp_create_comment`, `wp_update_comment`, `wp_delete_comment` — moderation (out of scope for this skill)

---

## Pre-publish checklist

Never publish without confirming all of these. If any is missing, hand back to the upstream skill instead of pushing to WordPress.

- [ ] `mcp_ping` succeeded this session
- [ ] Article passed `editorial-reviewer` (or human review)
- [ ] Internal links inserted via `arahkaii-internal-linking` (5–10 contextual links)
- [ ] SEO meta set via `seo-optimizer` (Rank Math title ≤60 chars, meta desc 150–160 chars)
- [ ] Featured image generated via `featured-image-prompt` (or `mwai_image`) and uploaded
- [ ] Category assigned (one primary, optional secondary)
- [ ] Tags assigned (3–7 relevant, lowercase, no duplicates of existing tags)
- [ ] Slug confirmed (lowercase, hyphenated, ≤60 chars, no stop words)
- [ ] Status decision made: `draft`, `future` (scheduled), or `publish`

**Default to `draft`.** Robert reviews in the WP admin before going live unless explicitly told otherwise.

---

## Publishing workflow

### Step 1: List existing taxonomies first

Before creating new categories or tags, always pull the existing list to avoid duplicates and casing inconsistencies (e.g. "Travel Guides" vs "travel guides").

```
Call wp_get_terms with taxonomy: "category"  — returns all categories with IDs
Call wp_get_terms with taxonomy: "post_tag"  — returns all tags with IDs
```

Match against existing entries. Only call `wp_create_term` when no close match exists, and confirm with Robert first.

### Step 2: Upload the featured image

Two paths — pick based on source:

**A. Image already exists at a URL** (e.g. Unsplash, prior CDN, or generated by `featured-image-prompt` and hosted somewhere):
```
Call wp_upload_media with:
  url:         <https URL>
  alt:         <descriptive, keyword-aware, ≤125 chars>
  title:       <article title, plain>
  caption:     (optional) photographer credit or scene context
  description: (optional) extended accessibility text
```

**B. Image needs to be AI-generated inline:**
```
Call mwai_image with:
  message: <full image prompt from featured-image-prompt skill>
  title:   <article title>
  alt:     <descriptive alt text>
  postId:  (set this AFTER step 3, to auto-attach)
```

Capture the returned `id` (media ID) — needed for `wp_set_featured_image` in step 4.

**Local file** (rare in chat sessions, common in Claude Code): use `wp_upload_request` to get a one-time URL, then `curl -F "file=@/local/path/file.jpg" "<returned URL>"`. URL expires in 5 minutes, single use.

### Step 3: Create the post

`wp_create_post` only takes the core post fields + `meta_input`. Categories, tags, and featured image are attached **after** in step 4.

```
Call wp_create_post with:
  post_title:   <H1, no site name suffix>
  post_name:    <slug — hyphenated, ≤60 chars>   ← NOT "slug"
  post_content: <Gutenberg block markup — see formatting note>
  post_excerpt: <2–3 sentences, 50–75 words, hook-driven>
  post_status:  draft | future | publish
  post_type:    post   (default; set to "page" or CPT slug if needed)
  meta_input:
    rank_math_title:            <SEO title, ≤60 chars>
    rank_math_description:      <meta description, 150–160 chars>
    rank_math_focus_keyword:    <primary keyword (lowercase, no quotes)>
    rank_math_robots:           ["index", "follow"]
    rank_math_advanced_robots:  {"max-snippet": "-1", "max-image-preview": "large", "max-video-preview": "-1"}
    rank_math_canonical_url:    (only if syndicated)
    rank_math_facebook_title:        (optional OG override)
    rank_math_facebook_description:  (optional OG override)
    rank_math_facebook_image:        (optional OG image URL)
    rank_math_twitter_title:         (optional, defaults to FB)
    rank_math_twitter_description:   (optional)
    rank_math_twitter_image:         (optional)
    rank_math_breadcrumb_title:      (optional shorter breadcrumb label)
    rank_math_pillar_content:        (set "on" for cornerstone pieces only)
```

For scheduled posts, do NOT pass `post_status: "future"` directly here — instead create as `draft`, then use `wp_update_post` with `schedule_for: "2026-05-20 09:00:00"` (local SGT). The MCP tool calculates GMT from the WP timezone setting and flips status to `future` automatically.

Capture the returned post ID.

### Step 4: Attach categories, tags, and featured image

```
Call wp_add_post_terms with:
  ID:       <post_id from step 3>
  terms:    [<category_id>]
  taxonomy: "category"
  append:   false      ← false replaces all categories with this list

Call wp_add_post_terms with:
  ID:       <post_id>
  terms:    [<tag_id_1>, <tag_id_2>, <tag_id_3>]
  taxonomy: "post_tag"
  append:   false

Call wp_set_featured_image with:
  post_id:  <post_id>
  media_id: <media_id from step 2>
```

### Step 5: Verify (round-trip read)

```
Call wp_get_post_snapshot with:
  ID: <post_id>
  include: ["meta", "terms", "thumbnail"]
```

Confirm:
- Title, slug, status, scheduled date (if any) match expectations
- All `rank_math_*` keys are present and non-empty
- Categories and tags resolved to the correct IDs
- Featured image attached (`thumbnail` is not null)
- `permalink` returns expected URL shape

**Do not announce success without this round-trip.**

### Step 6: Purge LiteSpeed cache

LSCWP automatically purges the post URL on `save_post` — which fires from `wp_create_post`, `wp_update_post`, `wp_update_post_meta`, and `wp_set_featured_image`. So if the post was just created or updated, that URL is already purged.

**However**, the following do NOT auto-purge and need a manual purge:
- Homepage / category archives showing the new post in a listing
- Sitemap (`/sitemap_index.xml`)
- AMP variants if AMP is enabled
- After Rank Math meta-only updates on already-published posts (purges the post URL but not the listing pages)

**Two ways to handle it** (in order of preference):

**A. Touch the post (MCP-native, no curl needed)** — call `wp_update_post` with the same ID and an empty `fields: {}`. This re-fires `save_post` and triggers LSCWP's purge logic, including the broader "purge related" sweep that hits category/tag archives:

```
Call wp_update_post with:
  ID: <post_id>
  fields: {}
```

**B. Direct LSCWP REST purge (Claude Code / terminal only)** — LiteSpeed Cache exposes a purge endpoint guarded by the same Bearer token if `LSCWP_CTRL_PURGE` is enabled. Use only when (A) is insufficient (e.g. full-site purge after a sitewide template change):

```bash
# Purge a single URL
curl -X POST "https://arahkaii.com/wp-admin/admin-ajax.php?action=litespeed_purge" \
  -H "Authorization: Bearer $ARAHKAII_TOKEN" \
  -d "url=https://arahkaii.com/your-slug/"

# Purge everything (use sparingly — recrawl cost)
curl -X POST "https://arahkaii.com/wp-admin/admin-ajax.php?action=litespeed_purge_all" \
  -H "Authorization: Bearer $ARAHKAII_TOKEN"
```

If neither path is available (rare), the fallback is the WP admin: *LiteSpeed Cache → Toolbox → Purge → Purge All*. Surface this option to Robert rather than retrying blind.

After purging, confirm by curl-ing the URL and inspecting the `x-litespeed-cache: miss` header on first hit (then `hit` on second). Skip this in chat sessions unless Robert asks for proof.

---

## Content formatting

arahkaii uses Gutenberg. Feed `post_content` as Gutenberg block markup so the post is editable in the block editor without conversion warnings:

```html
<!-- wp:paragraph -->
<p>Opening hook paragraph here.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Section heading</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":1234,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large">
  <img src="https://arahkaii.com/wp-content/uploads/..." alt="..." class="wp-image-1234"/>
  <figcaption>Optional caption</figcaption>
</figure>
<!-- /wp:image -->

<!-- wp:quote -->
<blockquote class="wp-block-quote">
  <p>Pull quote text.</p>
  <cite>Source name</cite>
</blockquote>
<!-- /wp:quote -->
```

Markdown is also accepted by `wp_create_post` — AI Engine converts to blocks server-side. Use markdown for speed, Gutenberg block markup when precise block IDs / attributes matter (e.g. embedding a specific media ID in an image block).

Block types used most on arahkaii: `paragraph`, `heading`, `image`, `quote`, `list`, `separator`, `embed`. Avoid raw `<div>`s — they break the block editor view.

---

## Field mapping cheat sheet

When `editorial-writer` produces output, map fields like this:

| Editorial output | WordPress field | Notes |
|---|---|---|
| H1 / title | `post_title` | Strip site name if appended |
| Slug suggestion | `post_name` | If missing, derive from title: lowercase, hyphenate, drop "the/a/and" |
| Hook + intro | first 2 paragraphs of `post_content` | |
| Body | rest of `post_content` (markdown or blocks) | |
| TL;DR / excerpt | `post_excerpt` | 50–75 words |
| SEO title | `meta_input.rank_math_title` | ≤60 chars, brand suffix optional |
| Meta description | `meta_input.rank_math_description` | 150–160 chars |
| Primary keyword | `meta_input.rank_math_focus_keyword` | lowercase, no quotes |
| Robots directives | `meta_input.rank_math_robots` | array of strings |
| Hero image prompt | `featured-image-prompt` → `wp_upload_media` (or `mwai_image`) → `wp_set_featured_image` | 2-step: upload, then attach |
| Suggested categories | resolve via `wp_get_terms` → `wp_add_post_terms` | prompt before creating new |
| Suggested tags | same — match existing before creating | |
| OG image override | `meta_input.rank_math_facebook_image` | URL, optional |

---

## Update flow (existing post)

For refreshes (Robert audits and refreshes content quarterly):

1. Find the post: `wp_get_posts` with a `search` filter on slug or title (NOT `wp_search_posts` — that tool doesn't exist).
2. Capture current state: `wp_get_post_snapshot` with `include: ["meta", "terms", "thumbnail"]`.
3. Apply changes: `wp_update_post` — pass only changed fields under `fields:` and changed meta under `meta_input:`.
4. If updating content, preserve the original publish date; WordPress bumps `modified` automatically.
5. Meta updates with `meta_input` on `wp_update_post` are **additive/upsert** (existing keys not in the call are preserved). To explicitly clear a key, use `wp_delete_post_meta`.
6. After update, do step 6 (LiteSpeed purge) — option A (touch) is usually enough.

For full refresh playbook: pair with `content-auditor` skill upstream.

---

## Scheduling

Two valid paths:

**A. Use `schedule_for` on `wp_update_post`** (recommended — it converts SGT → GMT correctly and sets status):
```
Call wp_update_post with:
  ID: <post_id>
  schedule_for: "2026-05-20 09:00:00"   ← local Singapore time, no offset string
```

**B. Manual** — set `post_status: "future"` on `wp_create_post` with a `post_date_gmt` meta. Less reliable; use (A) instead.

Verify the scheduled time after creation with `wp_get_post_snapshot` — `post_date` shows site timezone, `post_date_gmt` shows UTC. Both should make sense.

---

## Pitfalls (encountered in practice)

**REST API blocked (403).** Wordfence, iThemes Security, or Cloudflare WAF rules. Whitelist `/wp-json/` paths and the Hostinger server IP in Cloudflare if used.

**Tags created with wrong casing.** AI Engine creates tags case-sensitive — `Singapore`, `singapore`, and `SINGAPORE` become three separate tags. Always pull `wp_get_terms` first and reuse IDs.

**Featured image missing in editor preview.** `wp_set_featured_image` writes `_thumbnail_id` correctly but doesn't always trigger Gutenberg's featured image panel refresh in an already-open editor tab. The image IS attached — just refresh the editor. If it really hasn't stuck, re-call `wp_set_featured_image` once more.

**Rank Math score not updating after MCP write.** Rank Math's content analysis runs in the editor JS, not on save. The meta keys (`rank_math_title`, `rank_math_description`, `rank_math_focus_keyword`) are stored correctly and used by the frontend `<head>`, but the green/orange/red score in the editor only recalculates when Robert opens the post. This is cosmetic — don't retry the write.

**Rank Math meta not saving.** If `meta_input` writes silently no-op on Rank Math keys, check that *Rank Math → General Settings → Others → Custom Fields* is enabled. If still failing, fall back to `wp_update_post_meta` with the `rank_math_*` keys passed individually:
```
Call wp_update_post_meta with:
  ID: <post_id>
  meta: {
    rank_math_title: "...",
    rank_math_description: "...",
    rank_math_focus_keyword: "..."
  }
```

**Long content gets truncated.** If `post_content` exceeds ~32KB, AI Engine may silently truncate. For 3,000+ word articles, send content in two passes: `wp_create_post` with intro + first 2 H2 sections, then `wp_alter_post` or `wp_update_post` appending remaining content.

**Scheduled post publishes immediately.** WP-Cron is unreliable on under-traffic'd Hostinger VPS plans. If scheduling matters, set up real cron on the VPS:
```bash
*/5 * * * * curl -s https://arahkaii.com/wp-cron.php?doing_wp_cron > /dev/null 2>&1
```
Disable internal WP-Cron in `wp-config.php`: `define('DISABLE_WP_CRON', true);`

**SSE connection drops mid-publish.** AI Engine uses SSE; long-running operations (large media uploads) sometimes drop. Each SSE session ties up one PHP worker — Hostinger gives 5–8 workers per site, so two parallel Claude sessions can exhaust them. Restart php-fpm if site becomes unresponsive after MCP work.

**LiteSpeed cache serving stale content.** LSCWP's auto-purge covers the post URL but not always the homepage / category listing. If a freshly-published post doesn't appear on `/category/<slug>/` within 30s, do the option-A purge touch from step 6.

**`.html` files 404.** LiteSpeed handles rewrites differently than Apache. Static `.html` files in the WordPress root return 404 — rename to `.php` or serve via a subdomain. (This isn't a publishing concern, but comes up adjacent.)

---

## Safety rails

- **Never publish (`post_status: "publish"`) on first call** unless Robert explicitly says "publish live". Default to `draft`.
- **Never call `wp_delete_post`, `wp_delete_term`, `wp_delete_media`, or any `wp_*_user` write tool.** If asked, decline and surface what you'd delete — Robert removes via WP admin.
- **Never modify plugins, themes, or site options** (`wp_update_option`). This skill is content-only. Site config lives in a separate `arahkaii-admin` flow Robert has not built yet.
- **Never store the bearer token** in conversation history, in artifact code, in committed files, or in present_files output. The token is read from MCP config only.
- **Always round-trip read** via `wp_get_post_snapshot` after create/update before reporting success. Trust nothing without confirmation.
- **Run `mcp_ping` first** on a fresh session before any other tool call.

---

## Standard handoff format

When this skill completes, return to Robert in this shape:

```
✓ Published to arahkaii.com

  Status:       draft
  Post ID:      1234
  Title:        <title>
  Slug:         <slug>
  Edit:         https://arahkaii.com/wp-admin/post.php?post=1234&action=edit
  Preview:      https://arahkaii.com/?p=1234&preview=true
  Categories:   Travel Guides, Singapore
  Tags:         michelin-stars, hawker-culture, peranakan-cuisine
  Featured:     media_id 5678 (uploaded ✓)
  Rank Math:    title ✓  description ✓  focus_keyword ✓  robots ✓
  LiteSpeed:    auto-purged on save_post ✓
  
  Next: review in WP admin and toggle status to publish when ready.
```

For scheduled posts, replace status line with `Status: scheduled for 2026-05-20 09:00 SGT`.

---

## When NOT to use this skill

- WordPress.com hosted sites → use the WordPress.com Claude connector instead
- HumbleHalal, Tulab, Hastras → those need their own publisher skills, not this one
- Bulk operations across 50+ posts → write a one-off Claude Code script, not a chat session
- Anything touching plugin/theme files, user accounts, or site-wide options → out of scope
