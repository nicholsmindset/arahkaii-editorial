# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-16T01:20:00+08:00 | routine-1 | partial | drafted "The Quiet Renaissance of Korean Heritage Brands" | post_id:1665 | words:~1800 | pillar:fashion | WARN: mwai_image failed — no API key in ChatML Engine (AI Engine Settings) — featured image not attached, Robert must add manually | WARN: internal links limited to 2 category archive links — url-database.md awaits first Routine 6 run
