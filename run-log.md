# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-22T01:15:52Z | routine-1 | partial | drafted "The Quiet Renaissance of Korean Heritage Brands" | post_id:1772 | words:~1850 | pillar:fashion | note:featured-image-skipped (mwai_image error — AI Engine API key not configured in WP admin; internal-links limited to category archive, URL database awaiting first Routine 6 run)
