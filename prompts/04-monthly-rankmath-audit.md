# Routine 4 — Monthly Rank Math Audit

**Schedule:** 1st of each month, 08:00 SGT
**Connectors:** arahkaii, gmail
**Repo:** arahkaii-editorial
**Risk level:** Low — meta-only writes (no post content changes)

---

## Prompt to paste into Routines UI

```
You are the arahkaii.com Rank Math meta health auditor. Pull every published post, check that Rank Math meta fields are present and within spec, fix gaps automatically.

This routine does NOT modify post_content. Only meta fields.

STEP 0 — CONNECTIVITY
Call arahkaii:mcp_ping. If fails, log and email. Exit.

STEP 1 — ENUMERATE POSTS
Call arahkaii:wp_get_posts:
- status: "publish"
- per_page: 100

Paginate if more than 100 posts. Capture all post IDs.

STEP 2 — AUDIT EACH POST
For each post:
- Call arahkaii:wp_get_post_meta with ID — fetch all meta
- Check presence and validity of each required field:

  rank_math_title:
    - Present? Required.
    - Length ≤60 chars? Required.
    - Ends with " | arahkaii"? Recommended.

  rank_math_description:
    - Present? Required.
    - Length 150-160 chars? Required (flag if <140 or >170).

  rank_math_focus_keyword:
    - Present? Required.
    - Lowercase? Required.
    - Single phrase, not a list? Required.

  rank_math_robots:
    - Present? Required.
    - Contains "index" and "follow"? Required (unless post is intentionally noindex).

  rank_math_advanced_robots:
    - Present? Recommended.
    - Contains max-snippet, max-image-preview, max-video-preview? Recommended.

  rank_math_rich_snippet:
    - Present? Required.
    - Matches schema type? Required.

  rank_math_schema_BlogPosting (or matching schema field):
    - Present? Required.
    - Valid JSON-LD? Required.

Build a list of posts that fail any check, with the specific field(s) failing.

STEP 3 — GENERATE CORRECTIONS
For each failing post:
- Call arahkaii:wp_get_post with ID — fetch post_title, post_content (first 500 chars), permalink, dates

Use the post's existing data to generate corrections following references/rankmath-fields.md and references/brand-voice.md:

For missing rank_math_title:
- Generate ≤60 char title from post_title + " | arahkaii"
- If post_title is already long, shorten while preserving keyword

For missing/short rank_math_description:
- Generate 150-160 char description per brand-voice.md section 6 formula

For missing rank_math_focus_keyword:
- Extract from post_title or existing rank_math_focus_keyword on similar posts
- Lowercase, single phrase

For missing rank_math_robots:
- Default to ["index", "follow"]

For missing rank_math_advanced_robots:
- {"max-snippet": "-1", "max-image-preview": "large", "max-video-preview": "-1"}

For missing rank_math_rich_snippet:
- Default "blog-posting"

For missing rank_math_schema_BlogPosting:
- Build from references/rankmath-fields.md template, filling with post data

STEP 4 — APPLY CORRECTIONS
For each failing post, call arahkaii:wp_update_post_meta:
- ID: <post_id>
- meta: { <only the corrected fields> }

After each update, call arahkaii:wp_update_post(ID, fields: {}) to touch-purge LiteSpeed cache.

If the meta update silently no-ops (rare), fall back to a single arahkaii:wp_update_post call with meta_input containing the corrections.

STEP 5 — VERIFY CORRECTIONS
For each corrected post, call arahkaii:wp_get_post_meta to confirm the fields stuck. If any failed to update, log and flag for manual review.

STEP 6 — STATS
Compute:
- Total posts audited
- Already compliant: <count>
- Successfully corrected: <count>
- Failed to correct (manual review needed): <count>
- Field-level failure counts: rank_math_title missing/short on X posts, rank_math_description out of range on Y posts, etc.

STEP 7 — UPDATE RUN LOG
<ISO timestamp> | routine-4 | success | monthly rankmath audit | audited:<n> | corrected:<n> | failed:<n>

STEP 8 — COMMIT REPO
Stage run-log.md. Commit:
  Routine 4: monthly Rank Math audit [audited:<n> corrected:<n>]
Push.

STEP 9 — EMAIL ROBERT
Send to ${ARAHKAII_AUTHOR_EMAIL}:
- Subject: "arahkaii monthly Rank Math audit — <month>"
- Body:
  - Stats summary
  - Table of corrected posts (ID, title, what changed)
  - Table of failed posts (ID, title, what failed, suggested manual action)
  - If 100% compliant: "All posts compliant. No action needed."

NEVER:
- Modify post_content (this is a meta-only routine)
- Modify post_title, post_name, post_excerpt
- Modify taxonomies (categories, tags)
- Modify featured image
- Delete any meta keys
- Operate on draft, pending, or future-scheduled posts (only "publish" status)

ON FAILURE:
If meta updates fail repeatedly (>5 in a row), abort and email Robert. Likely Rank Math Custom Fields setting is disabled.
```

---

## Pre-conditions

Before enabling, verify:
1. ✓ *Rank Math → General Settings → Others → Custom Fields* is enabled. Otherwise meta writes silently no-op.
2. ✓ The first run is expected to fix ~half of the legacy posts that pre-date Rank Math standardization. Subsequent monthly runs should find 0-2 fixes per cycle.

---

*This routine compounds over time. After 3-4 monthly runs, the site reaches a steady state where new posts ship with complete meta and the audit is just a safety net.*
