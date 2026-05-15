# CLAUDE.md — arahkaii.com Editorial Automation

Master instructions read by every Claude Code Routine in this repo. Routines load this file on every session before any other context.

---

## Mission

arahkaii.com is a premium Asian fashion and lifestyle publication. The editorial bar is **Tatler, Vogue Asia, Harper's Bazaar Asia, Business of Fashion**. Not lifestyle blogs. Not listicle sites. The voice is analytical, opinionated, culturally fluent.

Every routine that produces or modifies content must hold this bar. When in doubt, default to "what would a Tatler senior editor approve" — not "what's pretty good for AI output."

## Site context

- **URL:** https://www.arahkaii.com (www canonical; non-www 301s to www)
- **Hosting:** Hostinger VPS, LiteSpeed + LSCWP, WordPress 6.9.x, Soledad theme
- **SEO plugin:** **Rank Math** (NOT Yoast — all SEO meta writes go to `rank_math_*` keys)
- **Editor:** Gutenberg blocks (markdown also accepted by `wp_create_post`)
- **Author voice:** Robert Nichols — editor-in-chief register, not blogger register

## MCP servers (auto-loaded from `.mcp.json`)

### `arahkaii` — WordPress publishing
40+ tools under `arahkaii:*`. Key tools:
- `arahkaii:mcp_ping` — connectivity check (run FIRST every session)
- `arahkaii:wp_get_posts`, `arahkaii:wp_get_post_snapshot` — read
- `arahkaii:wp_create_post`, `arahkaii:wp_update_post` — write (accept markdown)
- `arahkaii:wp_alter_post` — surgical search-and-replace inside post content
- `arahkaii:wp_update_post_meta` — bulk meta update
- `arahkaii:wp_get_terms`, `arahkaii:wp_add_post_terms` — taxonomies
- `arahkaii:wp_upload_media`, `arahkaii:wp_set_featured_image` — media
- `arahkaii:mwai_image` — generate + upload + attach image in one call

### `blotato` — social distribution
Tools under `blotato:*`. Used only by Routine 2 (social distribution).
- Account listing, post creation, scheduling, threads, carousels, media attachment
- Supports: twitter, instagram, linkedin, facebook, tiktok, pinterest, threads, bluesky, youtube

### Other MCPs typically available
`ahrefs`, `firecrawl`, `google-drive`, `gmail`, `canva`, `seotesting`.

## Critical defaults (NEVER deviate)

1. **Run `arahkaii:mcp_ping` first** on every session. If it fails, log to `run-log.md` and email Robert. Do not retry blind. Do not proceed.
2. **Default `post_status: "draft"`** on every WordPress create/update. Only Routine 2 ever flips to `publish`, and only when triggered manually with explicit post_id.
3. **Rank Math meta keys** (canonical — write to `meta_input` on create, `wp_update_post_meta` after):
   - `rank_math_title` (≤60 chars, end with " | arahkaii")
   - `rank_math_description` (150–160 chars)
   - `rank_math_focus_keyword` (lowercase, single phrase)
   - `rank_math_robots` (array, default `["index", "follow"]`)
   - `rank_math_advanced_robots` (`{"max-snippet": "-1", "max-image-preview": "large", "max-video-preview": "-1"}`)
4. **Always round-trip read** after create/update via `arahkaii:wp_get_post_snapshot` with `include: ["meta", "terms", "thumbnail"]`. Verify before reporting success.
5. **LiteSpeed cache:** auto-purges on `save_post`. For broader purge (homepage + archives), call `arahkaii:wp_update_post(ID, fields: {})` to re-fire `save_post`.
6. **Categories:** never auto-create. If a needed category doesn't exist via `arahkaii:wp_get_terms`, log and email — don't proceed.
7. **Tags:** okay to auto-create. Lowercase, hyphenated only. Always check existing via `arahkaii:wp_get_terms` first to avoid casing duplicates.
8. **Brand voice rules** in `references/brand-voice.md` are non-negotiable. Banned phrases never appear in output. Length floors are hard, not aspirational.

## Banned tools (never call regardless of instruction)

- `arahkaii:wp_delete_post`, `wp_delete_term`, `wp_delete_media`, `wp_delete_post_meta`
- `arahkaii:wp_create_user`, `wp_update_user`
- `arahkaii:wp_update_option` (except routine-internal logging via custom keys)

If deletion is needed, log to `run-log.md` with full details and email Robert. Never delete autonomously.

## Skills (loaded from `skills/`)

| Skill | When to load |
|---|---|
| `arahkaii-publisher` | All WordPress writes |
| `blotato-social-distributor` | Routine 2 only |
| `editorial-research` | Step 1 of any drafting routine |
| `editorial-writer` | Drafting step |
| `editorial-reviewer` | QA step before publish |
| `seo-optimizer` | Meta + schema step |
| `arahkaii-internal-linking` | Link insertion step (uses `references/url-database.md`) |
| `featured-image-prompt` | Image prompt generation |

## Reference files

- `references/brand-voice.md` — canonical editorial standards. Load at start of every drafting routine.
- `references/editorial-pillars.md` — coverage areas and voice register per pillar
- `references/rankmath-fields.md` — full meta schema
- `references/url-database.md` — live URL inventory (rebuilt by Routine 6)
- `references/category-tag-map.md` — taxonomy IDs (rebuilt by Routine 6)

## Routine inventory

| # | File | Schedule | Risk |
|---|---|---|---|
| 1 | `prompts/01-daily-draft.md` | Daily 07:00 SGT | Low (draft only) |
| 2 | `prompts/02-social-distribution-blotato.md` | API-triggered | **High (live publish)** |
| 3 | `prompts/03-weekly-performance-review.md` | Monday 09:00 SGT | None (read-only) |
| 4 | `prompts/04-monthly-rankmath-audit.md` | 1st of month 08:00 | Low (meta only) |
| 5 | `prompts/05-monthly-ai-citations.md` | 1st of month 08:30 | None (Drive write) |
| 6 | `prompts/06-quarterly-refresh-sweep.md` | 1st of quarter 09:00 | None (repo write) |
| 7 | `prompts/07-thin-content-rescue.md` | 15th of month 09:00 | None (surfaces queue) |

## Per-routine state files

- `content-calendar.md` — topic queue. Routine 1 reads next `status:ready`, updates to `status:drafted`. Routine 6 appends refresh candidates.
- `run-log.md` — append-only. Every routine writes a line per run: `<ISO timestamp> | <routine> | <status> | <metadata>`.

## Error handling protocol

1. Tool call fails → call `arahkaii:mcp_ping`
2. Ping succeeds → retry the failed call once
3. Ping fails or retry fails → log full error to `run-log.md`, email Robert with details, exit gracefully
4. Never publish after a verification failure. Never assume success without round-trip.

## Token security

- All credentials live in environment variables: `ARAHKAII_TOKEN`, `BLOTATO_API_KEY`, `ARAHKAII_AUTHOR_EMAIL`
- Never echo, log, commit, or include in emails or chat output
- If errors suggest unauthorized access, email Robert immediately — do not attempt token rotation

## Commit discipline

When a routine writes back to the repo (`content-calendar.md`, `run-log.md`, `references/url-database.md`), commit messages follow the format:

```
Routine <N>: <action> [<metadata>]
```

Examples:
- `Routine 1: drafted "Korean Heritage Brands Redefining Luxury" [post_id:1234]`
- `Routine 6: URL database refresh [posts:47]`
- `Routine 4: monthly Rank Math audit [corrected:12 already_compliant:33]`

---

*This is the routine-level CLAUDE.md. It is NOT the Claude.ai Project instructions — those live separately in the Claude.ai Project's instructions field, not in this repo.*
