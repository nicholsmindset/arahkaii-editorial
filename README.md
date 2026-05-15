# arahkaii-editorial

Content automation infrastructure for **arahkaii.com** — a premium Asian fashion and lifestyle publication built to Tatler / Vogue editorial standards.

This repo is consumed by **Claude Code Routines** running in the cloud. Routines read CLAUDE.md, load skills from `skills/`, follow prompts from `prompts/`, and write back to `content-calendar.md` and `run-log.md` after each run.

## What this repo does

- **Daily:** drafts one article from the topic queue, publishes to WordPress as `draft`, emails you for review
- **On approval:** publishes the draft live and distributes across 9 social platforms via Blotato
- **Weekly:** pulls performance data, flags decay candidates, suggests calendar additions
- **Monthly:** audits Rank Math meta health, tracks AI citation visibility, surfaces thin content
- **Quarterly:** rebuilds the live URL database and queues refresh candidates

Human review and live publication stays under your control. Routines never publish to social autonomously — they require explicit approval via API trigger.

## Repo structure

```
arahkaii-editorial/
├── CLAUDE.md                       # Master instructions read by every Routine
├── README.md                       # This file
├── .mcp.json                       # MCP server config (arahkaii + blotato)
├── .gitignore
├── content-calendar.md             # Topic queue (Routine 1 reads/updates)
├── run-log.md                      # Append-only audit log
├── prompts/
│   ├── 01-daily-draft.md
│   ├── 02-social-distribution-blotato.md
│   ├── 03-weekly-performance-review.md
│   ├── 04-monthly-rankmath-audit.md
│   ├── 05-monthly-ai-citations.md
│   ├── 06-quarterly-refresh-sweep.md
│   └── 07-thin-content-rescue.md
├── references/
│   ├── brand-voice.md              # Tatler-caliber editorial standards (canonical)
│   ├── editorial-pillars.md        # Coverage areas + voice register per pillar
│   ├── rankmath-fields.md          # Full Rank Math meta schema
│   ├── category-tag-map.md         # Live taxonomy IDs (populated by Routine 6)
│   └── url-database.md             # Live URL inventory (populated by Routine 6)
└── skills/
    ├── arahkaii-publisher/         # MCP-based WordPress publish pipeline
    ├── blotato-social-distributor/ # 9-platform social via Blotato MCP
    ├── editorial-writer/           # Tatler-caliber drafting
    ├── editorial-reviewer/         # Voice + banned-phrase QA
    ├── editorial-research/         # Deep research brief before writing
    ├── seo-optimizer/              # Rank Math meta + schema + AI Overview
    ├── arahkaii-internal-linking/  # 5-10 contextual links per article
    └── featured-image-prompt/      # Editorial image prompts
```

## Setup

### One-time

1. Clone the repo locally.
2. Install the **Claude GitHub App** on this repo (Settings → Apps → grant Read + Write to contents).
3. At WordPress admin: confirm AI Engine plugin is active, MCP enabled, bearer token generated.
4. At Blotato: confirm paid plan (Starter or higher), API key generated at Settings → API, social accounts connected.

### Environment variables (set in Routines UI)

| Variable | Source | Used by |
|---|---|---|
| `ARAHKAII_TOKEN` | AI Engine → Settings → MCP → Bearer Token | All routines |
| `BLOTATO_API_KEY` | Blotato → Settings → API | Routine 2 (social distribution) |
| `ARAHKAII_AUTHOR_EMAIL` | Your WP admin email | All routines (Gmail sender) |

Never commit any of these. The `.gitignore` excludes `.env` files.

### First routine to enable

Start with **Routine 1 (Daily Draft)** only. Run it manually via "Run now" 2-3 times. Watch the WordPress draft output. Tune the prompt or `brand-voice.md` until quality is consistent. Then enable the daily schedule. Only after 7-10 days of clean output should Routine 2 (social distribution) be activated.

## Brand identity

Read `references/brand-voice.md` before writing anything for this site. The publication is positioned alongside Tatler, Vogue Asia, Harper's Bazaar Asia, and Business of Fashion — not lifestyle blogs. Voice rules are strict and non-negotiable.

## Pitfalls to avoid

- **Don't commit secrets.** API keys, bearer tokens, WordPress passwords go in environment variables only.
- **Don't enable all routines at once.** Stage them. Routine 1 → 3 → 4 → 5 → 6 → 7 → 2. Routine 2 (social) is last because it's the only one that publishes live.
- **Don't auto-publish to social.** Routine 2 is API-triggered, not scheduled. You trigger it after reviewing each draft.
- **Don't bypass round-trip reads.** Every WordPress write must be verified via `wp_get_post_snapshot` before reporting success.
- **Don't create new categories autonomously.** Tags are okay (lowercase only). Categories require manual approval.

## Maintenance

This repo is canonical for routine behavior. When skills are updated locally on your Mac, commit changes here too — Routines run in the cloud and only see what's in this repo.

When `brand-voice.md` is updated, every routine that drafts content picks up the change on next run. This is the single highest-leverage file in the repo.

---

*Maintained by Robert Nichols. Last major revision: 2026-05-15. The publisher skill verified against the live `arahkaii.com` MCP on that date.*
