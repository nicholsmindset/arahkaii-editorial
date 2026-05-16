# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-16T13:28:43+08:00 | routine-1 | partial | drafted "The Quiet Renaissance of Korean Heritage Brands" | post_id:1761 | words:~1750 | pillar:fashion | NOTE: featured image skipped — mwai_image API key not configured (ChatML Engine); tag paris-fashion-week created (id:217)
