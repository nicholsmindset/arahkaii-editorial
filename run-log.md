# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-25T09:22:16+08:00 | routine-1 | partial | drafted "Best Halal Fine Dining Restaurants in Singapore (2026)" | post_id:1782 | words:~2450 | pillar:dining | notes: featured-image-skipped(mwai_image returned "No API Key provided" — AI Engine plugin needs ChatML key configured in WP Settings); 2 internal links to existing published posts; sibling dining/guide links deferred until those articles publish; Rempapa entry flagged explicitly non-halal — Robert to review before publish; Ammakase halal certification unconfirmed — verify with restaurant
