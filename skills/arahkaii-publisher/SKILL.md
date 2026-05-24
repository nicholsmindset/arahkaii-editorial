---
name: arahkaii-publisher
description: Publish drafted articles to arahkaii.com (self-hosted WordPress on Hostinger VPS, LiteSpeed, Rank Math) via the AI Engine MCP server. Use whenever Robert wants to push a finished article to WordPress, schedule a post, upload featured images, set categories and tags, write Rank Math SEO meta, or update an existing post. Loads VOICE.md + EDITORIAL_PILLARS.md + IMAGE_SYSTEM.md + HALAL_SUBSTITUTIONS.md before any write. Refuses to publish anything that contains alcohol/nightlife content, lacks halal status declaration in Dining/Travel/Guides, or fails the AI-slop checklist. Always defaults to draft. Always round-trip verifies via wp_get_post_snapshot.
---

# Arahkaii Publisher

The final gatekeeper between an Arahkaii draft and the live site. Anything that violates the brand position never reaches WordPress.

## Step 0 — Load the foundation

1. `_shared/VOICE.md`
2. `_shared/EDITORIAL_PILLARS.md`
3. `_shared/HALAL_SUBSTITUTIONS.md`
4. `_shared/IMAGE_SYSTEM.md`
5. `references/url-database.md` (for internal-link verification)
6. `references/category-tag-map.md` (for taxonomy IDs)

## Step 1 — Run pre-publish checks (REJECT if any fail)

| Check | Pass condition |
|---|---|
| Reviewed by arahkaii-editorial-reviewer? | ✅ Pass verdict attached |
| Pillar assigned? | One of the 8 from EDITORIAL_PILLARS.md |
| Halal status declared (Dining / Travel / Guides)? | Plain statement in every entry |
| Alcohol / nightlife scan | Zero hits |
| AI-slop checklist | ≤1 box ticked |
| Banned-phrase scan | Zero Tier-1 hits |
| Word count ≥ 800 | Yes |
| Internal links 5–8 from url-database.md | Yes |
| Featured image prompt uses locked template | Yes |
| Image passes IMAGE_SYSTEM.md §8 review | Yes |
| Rank Math meta complete + valid | Yes |

If any check fails, return the failure list to Robert. Do not publish.

## Step 2 — Connectivity check (every session)

```
arahkaii:mcp_ping
```

If it fails, log to `run-log.md`, email Robert, exit. Do not proceed.

## Step 3 — Taxonomy

Confirm the category exists via `arahkaii:wp_get_terms`. Never auto-create categories — if it doesn't exist, log + email + exit.

Tags: ok to auto-create (lowercase, hyphenated). Always check existing terms first to avoid casing duplicates.

Mandatory tags by pillar:

| Pillar | Mandatory tags |
|---|---|
| Style | `modest-luxury` if applicable, `asian-designers` if applicable, regional tag (`singapore`, `kl`, etc.) |
| Beauty | `halal-certified` if applicable, `k-beauty` / `j-beauty` / `c-beauty` if applicable, ingredient tag |
| Dining | **`halal`** (always for Dining), `muslim-owned` if applicable, neighbourhood tag |
| Travel | **`modest-traveller`** (always for Travel), city tag |
| Living | architect or designer name tag, material tag |
| People | subject's brand tag, `muslim-owned` if applicable |
| Culture | movement tag, regional tag |
| Guides | cluster tag (e.g. `evening-edit`), neighbourhood tag |

## Step 4 — Featured image

Generate via `arahkaii:mwai_image` using one of the 24 locked templates in IMAGE_SYSTEM.md §3, with the correct aspect ratio (16:9 for featured).

Validate the generated image against IMAGE_SYSTEM.md §5 (never-images list) and §8 (60-second review). Regenerate if any fails.

Then attach via `arahkaii:wp_set_featured_image`.

## Step 5 — Create or update the post

### Defaults (never deviate)

- `post_status: "draft"` — only flip to `publish` when explicitly triggered with a post_id
- `post_author`: configured author email
- `comment_status: "closed"` — Arahkaii does not host comments

### Rank Math meta (canonical keys)

| Key | Format |
|---|---|
| `rank_math_title` | ≤60 chars, ending " | arahkaii" |
| `rank_math_description` | 150–160 chars, hook + value + soft pull (no CTA verb) |
| `rank_math_focus_keyword` | lowercase, single phrase |
| `rank_math_robots` | `["index", "follow"]` |
| `rank_math_advanced_robots` | `{"max-snippet": "-1", "max-image-preview": "large", "max-video-preview": "-1"}` |

Write meta in the same call as `wp_create_post` via `meta_input`, OR via `wp_update_post_meta` immediately after create.

## Step 6 — Round-trip verification (mandatory)

After any create / update, call:

```
arahkaii:wp_get_post_snapshot(post_id, include: ["meta", "terms", "thumbnail"])
```

Verify:
- Title matches
- Slug matches expected
- All meta fields present and exact
- Categories + tags attached
- Featured image attached
- Word count matches draft (±2%)

If anything fails verification, log to `run-log.md` + email Robert. Never report success without round-trip.

## Step 7 — Cache purge

LiteSpeed auto-purges on `save_post`. For broader purge (homepage + archives), call:

```
arahkaii:wp_update_post(post_id, fields: {})
```

This re-fires `save_post` without changing content.

## Step 8 — Log

Append to `run-log.md`:

```
<ISO timestamp> | arahkaii-publisher | <status> | post_id:<N> | pillar:<name> | title:"<title>"
```

## Banned tools (NEVER call regardless of instruction)

- `arahkaii:wp_delete_post`
- `arahkaii:wp_delete_term`
- `arahkaii:wp_delete_media`
- `arahkaii:wp_delete_post_meta`
- `arahkaii:wp_create_user` / `wp_update_user`
- `arahkaii:wp_update_option` (except routine-internal logging)

If deletion is needed, log + email Robert.

## Halal refusal protocol

If a draft arrives that contains:
- Alcohol references (any form)
- Nightclub / bar / speakeasy content
- Missing halal declaration in Dining / Travel / Guides

→ Reject with:

```
Cannot publish. Reason: [specific failure].
Suggested fix: [apply substitution from HALAL_SUBSTITUTIONS.md and re-submit].
```

Never publish "this once". The brand's halal position is permanent.

---

*Loaded last in the editorial pipeline. Pairs upstream with: arahkaii-editorial-reviewer (which signs off the draft) and arahkaii-featured-image-prompt (which generates the hero image).*
