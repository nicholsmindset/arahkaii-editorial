# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-29T09:11:00+08:00 | routine-1 | skipped | 2026-05-25 entry "Best Halal Fine Dining Restaurants in Singapore (2026)" already published as post_id:1782 — calendar was still status:ready; corrected to status:published
2026-05-29T09:15:04+08:00 | routine-1 | partial | mwai_image failed — "No API Key provided. Please visit the Settings. (ChatML Engine)" — featured image NOT attached to post_id:1913; Robert must add manually in WP admin
2026-05-29T09:15:04+08:00 | routine-1 | success | drafted "The Rise of Modest Luxury in Asian Fashion" | post_id:1913 | words:~1700 | pillar:style | slug:modest-luxury-fashion-asia | NOTE: featured image missing — mwai_image API key not configured
