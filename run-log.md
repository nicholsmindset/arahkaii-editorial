# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-25T09:22:16+08:00 | routine-1 | partial | drafted "Best Halal Fine Dining Restaurants in Singapore (2026)" | post_id:1782 | words:~2450 | pillar:dining | notes: featured-image-skipped(mwai_image returned "No API Key provided" — AI Engine plugin needs ChatML key configured in WP Settings); 2 internal links to existing published posts; sibling dining/guide links deferred until those articles publish; Rempapa entry flagged explicitly non-halal — Robert to review before publish; Ammakase halal certification unconfirmed — verify with restaurant
2026-05-25T10:33:00+08:00 | hotfix | success | post_id:1782 | cleared rank_math_schema_BlogPosting (both cases) after WP critical error reported post-schema-fix; rank_math_rich_snippet:blog-posting retained; Rank Math will auto-generate BlogPosting schema from default template; email drafted to Robert with diagnosis; rankmath-fields.md updated with correct schema guidance and pipeline warning
