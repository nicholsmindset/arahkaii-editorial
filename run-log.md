# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-18T01:05:35+00:00 | routine-1 | skipped | topic "The Quiet Renaissance of Korean Heritage Brands" — post_id:1665 already published on site; calendar entry was status:ready (calendar out of sync); updated calendar to status:published
2026-05-18T01:18:21+00:00 | routine-1 | partial | drafted "C-Beauty's Second Wave: Why Florasis, Flower Knows, and Joocyee Now Outsell K-Beauty in Southeast Asia" | post_id:1766 | words:~1900 | pillar:beauty | slug:c-beauty-second-wave-singapore | status:draft | all rank_math_* meta set | category:Beauty & Accessories (2) | tags:C-Beauty,K-Beauty,Makeup,Beauty Science,Skincare,Florasis,Flower Knows,Joocyee | FAILURE: mwai_image — "No API Key provided. Please visit the Settings. (ChatML Engine)" — featured image NOT attached; requires WP AI Engine API key configuration in admin settings
