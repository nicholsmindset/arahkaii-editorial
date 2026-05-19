# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-19T01:13:43+00:00 | routine-1 | partial | drafted "The Quiet Renaissance of Korean Heritage Brands" | post_id:1767 | words:~1670 | pillar:fashion | NOTE: mwai_image failed — AI Engine API key not configured (ChatML Engine); featured image not attached; Robert to add manually. Internal links limited to category archives (url-database.md awaiting Routine 6 first run).
2026-05-19T01:13:43+00:00 | routine-1 | email | Gmail draft created (id:r-7418618907231827537) to theonnagency@gmail.com | ARAHKAII_AUTHOR_EMAIL env var not set; fell back to WP admin_email option.
