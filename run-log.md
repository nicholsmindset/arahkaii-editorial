# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-27T01:13:53+08:00 | routine-1 | partial | mwai_image failed — AI Engine API key not configured in WP Settings (ChatML Engine); featured image not attached to post_id:1879 — Robert to add manually in WP Admin
2026-05-27T01:13:53+08:00 | routine-1 | success | drafted "The Rise of Modest Luxury in Asian Fashion" | post_id:1879 | words:~1750 | pillar:style | slug:modest-luxury-asian-fashion | calendar:2026-05-25 status corrected to published (post_id:1782)

