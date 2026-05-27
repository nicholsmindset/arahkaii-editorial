# Manual wp-admin Customizer Steps (2026-05-27)

The 2026-05-27 audit execution wrote everything possible via WP REST API. Three things remain that **only the wp-admin Customizer can change** — Penci theme stores them in `penci_options` (single serialized option), and that option isn't exposed via REST. Each step is 30 seconds and unblocks already-done DB work.

## Step 1 — Switch Footer Layout from "Social Media Only" to "Widgets + Social"

**Path:** wp-admin → Appearance → Customize → Footer → Footer Layout (or similar)

**Current:** body class shows `penci-footer-social-media` — renders ONLY the social icon row.

**Change to:** "Widgets + Social Media" OR "Magazine Footer" (whichever Penci offers in the dropdown).

**Why:** Unblocks 4 footer widgets I already wrote to the DB (block-9 to block-12), assigned to `footer-1` through `footer-4` sidebars. Once the layout switches, these render automatically:
- Footer 1 — logo + brand mission paragraph
- Footer 2 — Editorial nav (Style, Dining ★, Travel, Culture, Living, People, Guides)
- Footer 3 — "Read next" + 4 latest posts (dynamic)
- Footer 4 — "The Arahkaii Circular" newsletter promo + Join us CTA

Also unblocks the Footer Links menu (id 251) I created → footer-menu location: About → Contact → Advertise → Terms → Privacy.

## Step 2 — Replace 6 placeholder social URLs

**Path:** wp-admin → Appearance → Customize → Social Networks (or Footer → Social Icons)

**Current:** All 6 social icons in the footer link to `#` (placeholder, dead).

**Change to:**
| Platform | URL |
|---|---|
| Instagram | https://www.instagram.com/arahkaii/ |
| TikTok (add if option exists) | https://www.tiktok.com/@arahkaii |
| Pinterest | https://www.pinterest.com/arahkaii/ |
| YouTube | https://www.youtube.com/@arahkaii |
| Facebook | https://www.facebook.com/arahkaii/ |
| Twitter (X) | https://twitter.com/arahkaii |
| Snapchat | **remove** (low ROI for editorial) |

**Why:** The 6 `#` links are dead clicks visible on every page of the site — visitors who click get nothing. Each is a small trust hit. If a handle doesn't exist yet, leave that platform's URL empty so Penci hides the icon (vs linking to `#`).

## Step 3 — Enable Topbar + Dark Mode Toggle (optional polish)

**Path:** wp-admin → Appearance → Customize → Header → Top Bar

**Toggles:**
- Enable Top Bar — turn ON (assigns the "Topbar" menu I created with id 252; it has About / Contact / Join the Arahkaii Circular)
- Top Bar Promo Text — set to *"Living beautifully, with intention — join the Arahkaii Circular →"* linking to `/join-us/`
- Dark Mode Switch — enable (Penci Soledad supports both light/dark; the toggle is a Customizer setting)

**Why:** Topbar is a known UX pattern for editorial sites — promotes newsletter signup without taking main-header real estate. Dark mode toggle is a 2024+ expectation, and the theme already supports it (body has `pclight-mode` class — needs the user-facing switch).

---

## Step 4 — One-time LSCWP Purge All (still pending from prior session)

**Path:** wp-admin → LiteSpeed Cache → Toolbox → Purge All (button at top)

**Why:** LSCWP front-page cache is stuck on the OLD page-13 layout from 60+ hours ago. None of the REST-based hooks I tried (status pulse, settings toggle, save_post on 1877) have invalidated it. ONE click here makes every change in this audit visible to anonymous visitors immediately.

## Step 5 — LSCWP TTL tuning (optional)

**Path:** wp-admin → LiteSpeed Cache → Cache → TTL

**Change:** "Default Public Cache TTL" from 604800 (7 days) → **86400 (24 hours)**.

**Why:** With a new site adding posts daily, a 7-day TTL means stale homepage content. 24h is the sweet spot — long enough to compound cache benefits, short enough to keep pages fresh.

Also, on the **Purge** tab, verify "Auto Purge Rules For Publish/Update" has **Front Page**, **Home Page**, **Pages**, and **All pages with Recent Posts widget** all checked.

---

## What's already live (DB) and will appear AS SOON AS Step 1 + Step 4 are done

- ✓ Page 1877 has 6 new per-pillar sections (Dining ★ / Style / Travel / Culture / Living / Guides) — each with H2, tagline, dynamic latest-posts grid, and "More {Pillar}" CTA button
- ✓ Main menu reordered: Home → Style → Dining → Travel → Culture → Living → People → Guides
- ✓ Default comments + pings closed site-wide (new posts only — existing posts unchanged)
- ✓ WordPress MCP plugin deactivated (AI Engine MCP is the canonical path per CLAUDE.md)
- ✓ Page 1774 ("Home 2026 Rebuild" draft) trashed
- ✓ Footer-1...4 widgets, Footer Links menu, Topbar menu all created in DB

## What couldn't be done via REST

- Plugin DELETE (Classic Editor, Easy Table of Contents, Hostinger Easy Onboarding, Hostinger Tools) — REST returns 404 on DELETE. They stay inactive (inert; no code executes). Can be deleted from wp-admin → Plugins.
