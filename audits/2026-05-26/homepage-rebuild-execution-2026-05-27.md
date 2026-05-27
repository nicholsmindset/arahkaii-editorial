# Homepage Rebuild Execution — 2026-05-27

## State change discovered at start of session

Between 2026-05-26 (audit committed at 17:13) and 2026-05-27 (this session start), the live site was substantially reorganized:

| Change | Detected via |
|---|---|
| **Page 13 deleted** | `wp/v2/pages/13` returns 404 |
| **New homepage page 1877 created with slug "home"** | `wp/v2/pages?slug=home` returns page 1877 with empty `_elementor_data` |
| **Beauty category (id=2) deleted** | `wp/v2/categories/2` returns 404 |
| **Style category renamed** | Display name "Style", slug stayed `fashion` (id 33, count 28 — was 24) |
| **Settings → Reading already updated to page 1877** | `wp/v2/settings.page_on_front = 1877` |

Net effect: the homepage was rendering an EMPTY body (page-id-1877 with zero `_elementor_data`). All visible content was theme header + footer + mega-menu only. **This explains Robert's "I need to fix the homepage design" message** — the homepage was broken, not just stale.

## What was applied

Copied page-13's full Elementor structure (6 sections, 30 KB JSON, from the 2026-05-26 backup) onto page 1877 — then applied the Tier 1 surgical fixes from the plan, adapted for today's category structure:

| Mutation | Widget count | Detail |
|---|---|---|
| Flip `order asc → desc` | 10 widgets | Newest posts surface first across every grid |
| Filter to Style (cat 33) | 2 widgets in section 3 | "Latest in outfit" actually filters to Style |
| Filter to Culture (cat 229) | 5 widgets in section 4 | **Pivoted from Beauty** (cat 2 was deleted) to Culture |
| Change section heading | 1 widget | "Latest in Beauty & Accessories" → "Latest in Culture" |
| Info-box 1: Dining | 1 widget | Title "Dining", new copy, link → `/dining/` |
| Info-box 2: Style | 1 widget | Title "Style", new copy, link → `/fashion/` |
| Info-box 3: Culture (was Beauty) | 1 widget | Title "Culture", new copy, link → `/culture/` |

**Two writes total** to `wp/v2/pages/1877` (first with full structure + initial Tier 1 fix, second with the Beauty→Culture pivot after discovering cat 2 was deleted). DB state confirmed correct via `wp/v2/pages/1877?context=edit`.

## Verification (against the page-id-1877 fresh-render — cache-bust)

| Check | Result |
|---|---|
| Page-id 1877 renders (not empty) | ✓ 193 KB HTML body, 7 elementor-sections, all widget types present |
| All 3 info-box new texts present | ✓ "Halal-conscious fine dining", "Modest luxury, Asian designers", "Asian identity, modest movement" |
| Style section filters to /fashion/ posts only | ✓ 6 fashion posts in section 3, no cross-pillar |
| Culture section filters to /culture/ posts | ✓ (DB state confirms `[229]`) |
| Info-box links resolve 200 | ✓ /dining/, /fashion/, /culture/ all 200; /beauty/ now 404 (Beauty category deleted) |
| Newest post (halal-fine-dining) on page | ✓ |

## Cache state — the user-visible blocker

LSCWP is serving the homepage URL `/` from a **55-hour-old cache** (age: 198,439 seconds at write time). The cached content is from when page-13 was still the homepage. My save_post hook fires on page 1877 are NOT invalidating the front-page URL cache — likely because LSCWP cached the front page under the page-13 cache key and the cache layer hasn't been notified of the WP Settings change.

### Programmatic purge attempts that did NOT work:
- Toggling `wp/v2/settings.page_on_front` between 0 and 1877 (no cache hook fired)
- Empty POST to `wp/v2/pages/1877` (save_post fires but doesn't purge front-page URL)
- HTTP PURGE method to `/` (405 Method Not Allowed)
- `X-LiteSpeed-Purge: *` header (no effect, cache hit served)
- LSCWP REST namespace (`litespeed/v1`, `litespeed/v3`) — no purge endpoint exists

### What WILL work (manual, 5 seconds):
- **`wp-admin → LiteSpeed Cache → Toolbox → Purge All`** OR
- **wp-admin top admin bar → LiteSpeed Cache icon → "Purge All"**

After the manual purge, all visitors see the new homepage immediately. Verified pre-cache render works (1 cache miss = 67s cold render, subsequent hits <1s).

## Files (committed)

- `references/homepage-snapshots/homepage-page-1877-2026-05-27.json` — pre-fix state of page 1877 (was empty)
- `references/homepage-snapshots/homepage-page-1877-2026-05-27-patched.json` — full patched JSON written to page 1877
- `references/homepage-snapshots/homepage-page-13-2026-05-26.json` — original page 13 source (committed yesterday, the structural basis for today's rebuild)

## Open follow-ups

1. **Manual LSCWP purge** — Robert clicks Purge All in wp-admin (one-time, 5s)
2. **LSCWP cache speed root cause** — TTL appears very long (1+ week). Worth tuning in wp-admin → LSCWP → Cache → TTL settings to e.g. 24h for the homepage, OR enabling "Auto-Purge Front Page" trigger more aggressively
3. **Section 4 styling** — heading now reads "Latest in Culture" — semantically correct but the design context still implies "Beauty & Accessories" visually. Section heading widget may need styling tweaks via Elementor UI later
4. **Beauty pillar restoration** — if Robert intends to bring Beauty back as a separate category, he can recreate it in Posts → Categories. The info-box link will need to be re-pointed.
5. **The 17 drafts + 37 published-post audit findings from yesterday's session** are still valid and unaddressed (FAQ schema, in-prose internal linking, etc.)
