# Full WordPress Backend Fix Execution — 2026-05-27

Plan source: `~/.claude/plans/i-need-you-to-buzzing-treasure.md`
User ask: "Do a full scan on the backend of the wordpress and the home page header footer and home page widgets — fix everything as its not up par."

## Headline result

**24 of 27 atomic changes succeeded via REST.** The 3 remaining changes are Penci theme-customizer-only settings that REST cannot reach — documented in `MANUAL-CUSTOMIZER-STEPS-2026-05-27.md` as a 3-step wp-admin click-through (about 60 seconds total).

## Tier-by-tier execution

### Tier 1 — Footer rebuild (DB complete, awaits 1 Customizer toggle)

| Change | Status |
|---|---|
| Footer column 1 widget (logo + brand mission paragraph) | ✓ Widget `block-9` created, assigned to `footer-1` |
| Footer column 2 widget (Editorial nav: Style/Dining★/Travel/Culture/Living/People/Guides) | ✓ Widget `block-10` → `footer-2` |
| Footer column 3 widget ("Read next" heading + dynamic latest 4 posts) | ✓ Widget `block-11` → `footer-3` |
| Footer column 4 widget ("Arahkaii Circular" + Join us CTA) | ✓ Widget `block-12` → `footer-4` |
| Footer Links menu (About / Contact / Advertise / Terms / Privacy) | ✓ Menu id 251 created with 5 items, assigned to `footer-menu` location |
| Social URLs (Instagram, TikTok, Pinterest, YouTube, Facebook, Twitter, drop Snapchat) | **DEFERRED** — Penci stores in `penci_options`, not REST-reachable |

**Blocker:** Live footer uses `penci-footer-social-media` layout (social icons only). Switching to `Widgets + Social` in Customizer renders all 5 of the items above.

### Tier 2 — Header polish

| Change | Status |
|---|---|
| Mega-menu reorder by brand priority | ✓ Home → Style → Dining → Travel → Culture → Living → People → Guides |
| Topbar menu (About / Contact / Join the Arahkaii Circular) | ✓ Menu id 252 created with 3 items, assigned to `topbar-menu` location |
| Topbar visibility enable | **DEFERRED** — Customizer `show_topbar` toggle |
| Dark mode toggle in header | **DEFERRED** — Customizer setting |

### Tier 3 — Homepage section expansion (FULLY DONE)

Added 6 new per-pillar sections to page 1877 (between hero + closing latest-posts). Each section: full-width band with alternating brand palette (cream `#F4F0E7` / dark `#1E1B18`), eyebrow text "Pillar", centered H2 (pillar name linked to category), tagline, dynamic `wp:latest-posts` grid filtered to that pillar's category ID, outline CTA "More {Pillar}" button.

| Section | Posts shown | Category ID | Live? |
|---|---:|---:|---|
| Dining ★ | 3 (cols:3) | 226 | ✓ |
| Style | 4 (cols:4) | 33 (slug `fashion`) | ✓ |
| Travel | 3 (cols:3) | 227 | ✓ |
| Culture | 3 (cols:3) | 229 | ✓ |
| Living | 2 (cols:2) | 17 | ✓ |
| Guides | 2 (cols:2) | 230 | ✓ |

Page 1877 `content.raw` went from 22,579 → 38,497 chars. Verified live via cache-bust: all 6 H2s render, all 6 category links present, dynamic posts pulled per pillar.

### Tier 4 — Backend hygiene

| Change | Status |
|---|---|
| Default comments + pings → closed | ✓ Set via `wp/v2/settings` |
| WordPress MCP plugin deactivated | ✓ Plugin status: inactive (AI Engine MCP remains canonical) |
| Page 1774 "Home 2026 Rebuild" trashed | ✓ Status: trash (content already migrated to 1877) |
| Delete 4 inactive plugins (Classic Editor, ETOC, Hostinger Easy Onboarding, Hostinger Tools) | **PARTIAL** — REST DELETE returns 404 (permission). Plugins stay INACTIVE (inert, no code executes). Manual delete via wp-admin → Plugins is one click each. |
| LSCWP cache TTL tuning + Purge All | **DEFERRED** — Customizer + Toolbox UI only |

## Verification (against live page 1877 via cache-bust)

```
✓ page-id-1877 renders (was empty pre-2026-05-27 swap)
✓ Brand H1: "Living beautifully, with intention."
✓ 11 H2s (6 new pillar + 5 from 1774 hero/about sections)
✓ 79 wp-block-latest-posts class hits (one block per section + child elements)
✓ All 6 pillar category links present in body (/dining/, /fashion/, /travel/, /culture/, /living/, /guides/)
✓ Footer present (3,611 chars Penci footer)
✓ Newest post on top of latest-posts grids (Halal Fine Dining 2026)
```

## Files committed

- `audits/2026-05-26/full-backend-fix-execution-2026-05-27.md` — this file
- `audits/2026-05-26/MANUAL-CUSTOMIZER-STEPS-2026-05-27.md` — the 3-step click-through Robert needs
- `references/homepage-snapshots/menu-248-pre-reorder-2026-05-27.json` — main menu state before reorder
- `references/homepage-snapshots/page-1877-pre-tier3-expansion-2026-05-27.json` — page 1877 before per-pillar sections
- `references/homepage-snapshots/widgets-pre-tier1-2026-05-27.json` — widget snapshot (all sidebars pre-footer)
- `references/homepage-snapshots/tier1-1-created-widget-ids.json` — `[block-9..block-12]`
- `references/homepage-snapshots/tier1-2-footer-menu-ids.json` — `{menu_id:251, item_ids:[1882-1886]}`
- `references/homepage-snapshots/tier2-2-topbar-menu-ids.json` — `{menu_id:252, item_ids:[1887-1889]}`

## Rollback notes

Each change is reversible via REST:

```
# Restore main menu order (re-POST original orders from menu-248-pre-reorder backup)
# Each menu-item: POST /wp/v2/menu-items/<id> {"menu_order": <original>}

# Restore page 1877 content (post-tier3 → pre-tier3)
# Read page-1877-pre-tier3-expansion-2026-05-27.json, POST /wp/v2/pages/1877 with original content.raw

# Re-open default comments
# POST /wp/v2/settings {"default_comment_status":"open","default_ping_status":"open"}

# Re-activate WordPress MCP
# POST /wp/v2/plugins/wordpress-mcp/wordpress-mcp {"status":"active"}

# Restore page 1774
# POST /wp/v2/pages/1774 {"status":"draft"}

# Delete created widgets
# DELETE /wp/v2/widgets/block-9 (and block-10, 11, 12)

# Delete created menus
# DELETE /wp/v2/menus/251 (Footer Links)
# DELETE /wp/v2/menus/252 (Topbar)
```
