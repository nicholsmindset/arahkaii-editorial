# Run Log

Append-only audit trail. Every routine writes one line per run.

Format: `<ISO 8601 timestamp> | <routine-id> | <status> | <metadata>`

Status values: `success`, `partial`, `failed`, `skipped`, `noop`

---

2026-05-15T01:30:00+08:00 | repo-init | success | repo created, 24 files committed, MCP tested
2026-05-21T07:00:00+08:00 | routine-1 | failed | mcp_ping failed — "MCP tool call requires approval"; arahkaii MCP server unreachable; pipeline aborted per error protocol; Gmail notification also blocked (same error); all MCP tools pending approval in this session
