# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-20T01:15:44+08:00 | routine-1 | partial | drafted "C-Beauty's Second Wave: How Florasis, Flower Knows, and Joocyee Are Rewriting Southeast Asia's Beauty Map" | post_id:1768 | words:~1850 | pillar:beauty | note:first calendar topic (Korean Heritage Brands) skipped — published post ID 1665 already exists; calendar was out of sync | note:featured image not attached — mwai_image failed, AI Engine API key not configured (ChatML Engine); Robert must add featured image manually and configure AI Engine API key in Settings
