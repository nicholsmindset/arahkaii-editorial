# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-26T01:11:00+08:00 | routine-1 | partial | drafted "Best Halal Fine Dining Restaurants in Singapore (2026)" | post_id:1804 | words:2400 | pillar:dining | ISSUE: mwai_image failed twice (MCP error -32603: No API Key provided — ChatML Engine not configured); featured image NOT attached; all other steps complete; Robert to add featured image manually in WP admin and verify restaurant halal statuses + chef details before publishing
