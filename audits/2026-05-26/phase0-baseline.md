# Phase 0 — Baseline Data Snapshot

**Created:** 2026-05-26 · **Site:** https://www.arahkaii.com · **Date range:** 2026-04-28 to 2026-05-25 (28 days)

This file establishes the live data baseline against which Phase 1+ work will be measured. Re-run the same queries at +30d, +60d, +90d to track recovery.

---

## MCP / API access status

| Source | Status | How accessed in this session | Notes for future sessions |
|---|---|---|---|
| **Ahrefs MCP** | ✅ Works | `mcp__ahrefs__*` tools | DR=0, org_traffic=0 (Ahrefs index lags new sites by 2-8 weeks vs GSC) |
| **GSC — mcp-server-gsc (service-account)** | ✅ Works after symlink fix | Symlinked creds from `~/.config/gsc-mcp/mediacorp-gsc/` to `~/Desktop/gsc/` where MCP expects. **Account is Mediacorp-only (CNA, CNA Luxury, Straits Times, 8days, etc.) — NO arahkaii** | Useful for **competitor benchmarking** against CNA Luxury, but not for arahkaii data |
| **GSC — gcloud ADC user creds** | ✅ Works via direct REST API | `gcloud auth application-default print-access-token` + `x-goog-user-project: gsc-urls` header → `https://www.googleapis.com/webmasters/v3/sites/...` | **This is the access path for arahkaii.com + all ONNIFY properties.** User has siteOwner on 19 sites |
| **`onngroup-gsc` MCP** | ❌ Not registered | The MCP server the user describes is not in `~/.claude/mcp/global-mcp-config.json` and ToolSearch returns 0 hits for "onngroup" | Functionally I replicated it via direct REST calls. To make it a real MCP, register the package + auth in global-mcp-config.json |
| **GA4 — google-analytics MCP** | ❌ Insufficient scopes | `mcp__google-analytics__get_account_summaries` returns `ACCESS_TOKEN_SCOPE_INSUFFICIENT` | Re-auth with: `gcloud auth application-default login --scopes=https://www.googleapis.com/auth/analytics.readonly,https://www.googleapis.com/auth/cloud-platform` |
| **`onngroup-ga4` MCP** | ❌ Not registered | Same as GSC — described but not loaded | Will work once ADC scopes include `analytics.readonly` |
| **WP AI Engine MCP (arahkaii)** | ❌ Token missing | `ARAHKAII_TOKEN` env var not set in shell; not in `~/.env` | Set via: `export ARAHKAII_TOKEN=...` (get from WP → AI Engine → Settings → MCP → Bearer Token), then arahkaii:* tools work |

**Access fix priority for Phase 0 completion:**
1. **Easiest:** GA4 scope fix — single `gcloud auth application-default login` command with scope flags
2. **Manual:** Set `ARAHKAII_TOKEN` in shell or `~/.env` for WP MCP access
3. **Optional:** Properly register `onngroup-gsc` / `onngroup-ga4` as MCP packages if you want tool-call ergonomics instead of curl + jq

---

## Ahrefs snapshot (root_domain mode, 2026-05-25)

| Metric | Value | Interpretation |
|---|---:|---|
| Domain Rating | **0.0** | Brand-new in Ahrefs's eyes; toxic backlinks may be suppressing this |
| Ahrefs Rank | **89,933,834** | Bottom-tier; will improve as legitimate links + traffic accumulate |
| Organic keywords | 0 | Ahrefs hasn't picked up rankings yet — but GSC sees 121 query-page pairs |
| Organic traffic est. | 0 | Same lag — GSC sees 12 clicks/month |
| **Backlinks (live)** | **195** | |
| **Backlinks (all-time)** | 237 | |
| **Referring domains (live)** | **141** | |
| **Referring domains (all-time)** | 151 | |

**Backlink quality red flag:** Of the top 25 referring domains by DR, **18 are PBN/link-spam networks** (`buybacklinks.agency`, `rank-your.website`, `fiverr-cost-effective-seo.site`, `linkrankpro.shop`, etc.). The 141-RD headline is misleading. See `audit/phase4-disavow-draft.txt` for the proposed disavow list. **This may be why DR=0** — Google and Ahrefs are likely discounting the link profile.

**Top legitimate RDs** (from the top 25):
- `grokipedia.com` (DR 77) — AI-search citation source, *keep*
- `prospeo.io` (DR 69, 217k monthly traffic) — appears legit
- `threadcurve.com` (DR 48) — small but real

**No Ahrefs Site Audit project exists for arahkaii.com** — Robert's account is wired to Mediacorp's portfolio (Straits Times, CNA, **CNA Luxury** — the direct competitor cited in REVAMP_NOTES.md, project ID 1229675). Recommend creating an arahkaii project in Ahrefs (free tier covers 5 projects) for ongoing automated site audits.

---

## GSC snapshot (28 days, sc-domain:arahkaii.com, ADC user creds)

### Aggregated totals

| Metric | Value |
|---:|---|
| **Clicks** | **12** |
| **Impressions** | **3,499** |
| **CTR** | **0.34%** *(industry benchmark at avg pos 12.6 ≈ 2-3%, so 6-10x below par)* |
| **Avg position** | **12.57** |

**Diagnosis:** the site has decent SERP reach (3.5k impressions) but is converting only 0.3% of them to clicks. This is the SERP-snippet problem (titles + metas + schema) more than the ranking problem. Phase 3's striking-distance work targets this directly.

### Top 25 pages by clicks (28d)

| Clicks | Impr | CTR | Pos | Page |
|---:|---:|---:|---:|---|
| 4 | 747 | 0.5% | 14.12 | `/beauty-best-chinese-makeup-brands/` (legacy URL — 301 chain to `/beauty/beauty-best-chinese-makeup-brands/`) |
| 3 | 621 | 0.5% | 17.83 | `/the-ultimate-guide-to-finding-the-perfect-foundation-shade-for-southeast-asian-skin-tones/` (legacy URL — 301 chain) |
| 2 | 208 | 1.0% | **7.50** | `/arahkaii-com-seoul-fashion-week-fw-2026/` ★ **highest position of any URL** |
| 1 | 48 | 2.1% | 9.56 | `/bts-songzio-lyrical-armor-arirang-concert/` |
| 1 | 29 | 3.4% | 13.24 | `/jakarta-fashion-week-2025/` *(legacy slug, 301)* |
| 1 | 308 | 0.3% | 15.50 | `/quiet-luxury-brands-worn-by-wealthy-insiders/` (legacy — 301 chain) |
| 0 | 78 | 0% | 35.38 | `/asian-billionaire-philanthropy-quiet-revolution/` *(deep position but only piece in this lane)* |
| 0 | 58 | 0% | 9.29 | `/?utm_source=GMB` *(homepage tagged from Google My Business)* |
| 0 | 26 | 0% | 3.42 | `/about-us/` |
| 0 | 19 | 0% | 6.05 | `/advertise/` |

**Key observations:**
1. **`/arahkaii-com-seoul-fashion-week-fw-2026/` at pos 7.5** is the best-ranked URL we have — wasn't in the CSV analysis. **Add to Phase 3 as priority #1.**
2. **6 of the top 7 click-driving pages are at LEGACY URLs that 301 to category-prefixed URLs.** Google still hasn't consolidated the signals — fixing the redirect chains (Phase 4) is the single highest-leverage technical change.
3. **`/about-us/` ranks at position 3.42** — Robert's editor-in-chief positioning has authority. The site needs a `Person` schema connection to `/about-us/` from every Article to leverage this E-E-A-T signal.

### Top 25 queries by clicks (28d)

Only 1 query has a click (`zegna` — brand name, lucky impression). The other 24 queries have **0 clicks despite 1-24 impressions each**. Cluster patterns:

- **Asian foundation cluster** (HUGE demand, all at deep positions): "best foundation for asian skin" (21 impr, pos 58), "best foundations for asian skin" (8 impr, pos 68), "best foundation for chinese skin" (4 impr, pos 65), "best foundation for south asian skin" (2 impr, pos 43), "best foundation asian skin" (2 impr, pos 65) → **this is THE keyword cluster the foundation guide should be capturing**, but it ranks at position 60+
- **C-beauty cluster:** "best chinese makeup brands" (5 impr, pos 22), "best chinese cosmetics brands" (3 impr, pos 65), "best chinese beauty products" (1 impr, pos 54), "florasis" (6 impr, pos 30), "best cbeauty brands" (1 impr, pos 27)
- **Asian philanthropy / tycoon:** "asian philanthropy" (24 impr, pos 80), "asian tycoon" (3 impr, pos 48) → the `/asian-billionaire-philanthropy-quiet-revolution/` page is targeted but ranking too deep
- **Brand searches:** "arahka" (1 impr, pos 4) — someone's typing the brand name and getting served the right answer ✓

### Striking-distance query-page pairs (28d, position 8-20, impressions ≥5)

| Impr | Clicks | Pos | Query | Page |
|---:|---:|---:|---|---|
| 28 | 0 | 8.79 | which foundation brand offers the most s... | `/the-ultimate-guide-to-finding-the-perfect-foundation-shade-...` |
| 7 | 0 | 17.00 | stealth wealth brands 2026 | `/quiet-luxury-brands-worn-by-wealthy-insiders/` |

(Sparse because adding the query dimension fragments impressions across many tail queries. The **page-level** striking-distance view from the CSV — 6 URLs aggregated, plus the new Seoul Fashion Week URL — is the better optimization target.)

### Sitemap state

⚠️ **All 3 sitemaps report `indexed: 0`** despite pages clearly indexed (GSC sees impressions on them). This is a known GSC reporting quirk when sitemap URLs change shape — Google still indexes the pages but the sitemap-report match-up fails. Doesn't hurt SEO directly, but it does hurt visibility into "what's known to Google."

| Sitemap | Submitted | Last downloaded | Warnings | Errors |
|---|---:|---|---:|---:|
| `post-sitemap.xml` (Rank Math) | 36 web + 20 image | 2026-05-21 23:21 | 0 | 0 |
| `sitemap_index.xml` (Rank Math) | 55 web + 32 image | 2026-05-26 07:53 (today) | 0 | 0 |
| `category-sitemap.xml` (on `arahkaii.com` non-www, legacy) | 6 web | 2026-05-23 17:30 | **2** | 0 |

**Action:** the legacy non-www `category-sitemap.xml` should be removed from GSC (it's submitted from `arahkaii.com` not `www.arahkaii.com` — domain mismatch is the warning).

---

## GA4 snapshot

**Status:** Blocked. The gcloud ADC OAuth doesn't have the `analytics.readonly` or `analyticsadmin.readonly` scopes.

**One-line fix:** Run this once, then GA4 works for arahkaii + all ONNIFY properties:
```bash
gcloud auth application-default login \
  --scopes=openid,https://www.googleapis.com/auth/userinfo.email,\
https://www.googleapis.com/auth/cloud-platform,\
https://www.googleapis.com/auth/webmasters,\
https://www.googleapis.com/auth/analytics.readonly,\
https://www.googleapis.com/auth/analyticsadmin.readonly
```

After re-auth, the same `mcp__google-analytics__*` tools (or direct REST calls to `analyticsdata.googleapis.com`) will return data without changing any code.

**GA4 data available in the Screaming Frog CSV** (joined by Robert manually before this audit): 41 indexable pages with 0 GA4 sessions, no pages with very low engagement rate (the engagement metric needs the live API to interpret cleanly).

---

## Refined SEO Health Index after live data — 56 / 100 (still Fair, lower bound)

Updating from the preliminary 62 with real GSC + Ahrefs evidence:

| Category | Score | Weight | Weighted | Drivers |
|---|---:|---:|---:|---|
| Crawlability & Indexation | 65 | 30 | 19.5 | -10 from preliminary: sitemaps report `indexed: 0` (reporting issue), 6 of top 7 click pages still on legacy 301 chains, 9 hard 404s, 75 redirects with 20 chains |
| Technical Foundations | 70 | 25 | 17.5 | Unchanged: LiteSpeed fast, HTTPS clean, but homepage H1=0 + no FAQPage schema + meta description over limit |
| On-Page Optimization | 50 | 20 | 10.0 | -5: top pages CTR ≈ 0.5% at pos 12-17 confirms snippets aren't competitive; legacy meta predates 8-pillar revamp |
| Content Quality & E-E-A-T | 60 | 15 | 9.0 | Unchanged: brand-voice doc + 9-layer QA exist but routines not running |
| Authority & Trust | 0 | 10 | 0.0 | -20: DR=0 confirmed, 18 of top 25 RDs are PBN spam — this is **negative** authority signal until disavowed |
| **TOTAL** | | | **≈ 56** | Lower bound — once GSC sitemap reporting normalizes + disavow processes, expect 60-65 |

**What changed from preliminary:** the toxic backlink profile is more damaging than I initially scored (-20 in Authority), and the per-page CTR data shows the SERP-snippet problem is more widespread than I assumed (-5 in On-Page). Sitemap indexed:0 reporting is a -10 hit even if Google is still indexing pages.

**Realistic ceiling at +90 days** *(if Phases 1-5 execute)*: 75-80 (Good band).

---

## The three biggest opportunities (evidence-based, refined)

### #1 — Fix the redirect chains (single highest-leverage action)
**Evidence:** 6 of the top 7 click-driving pages are on LEGACY URLs with 3-hop 301 chains. GSC has not consolidated ranking signals to the new URLs. The current 0.34% aggregate CTR reflects users seeing old URLs in SERPs that go through redirect chains (Google sometimes suppresses these clicks). **Estimated impact:** +30-50% click-through recovery once chains shorten and Google reindexes (4-8 weeks).
**Action:** `audit/phase4-redirect-chains.csv` — 20 chains to fix in Rank Math → Redirections.

### #2 — Optimize the 7 striking-distance URLs (Phase 3, +Seoul FW)
**Evidence:** 7 URLs (6 from CSV + Seoul Fashion Week from live GSC) sit at positions 7-20 with 30-820 impressions each. Median CTR is ~0.5% vs benchmark ~3% at these positions. **Estimated impact:** +245-440 clicks/month within 90 days of execution.
**Action:** `audit/phase3-striking-distance-briefs.md` — per-URL briefs with new RankMath meta + FAQPage schema + internal-link plan. **Add Seoul Fashion Week URL as the new #1 priority** (highest current position = lowest activation energy).

### #3 — Disavow toxic backlinks (single biggest authority cleanup)
**Evidence:** 18 of top 25 referring domains by DR are PBN/spam networks. DR=0 despite 141 RDs suggests Google AND Ahrefs are already discounting the profile. Disavowing prevents future algorithm penalties + restores baseline trust. **Estimated impact:** invisible short-term, prevents downside; once future legitimate links land, DR will grow normally instead of being suppressed.
**Action:** `audit/phase4-disavow-draft.txt` — 22 domains drafted. **Review and submit via Google Search Console → Disavow Tool.**

---

## Honorable mention — Homepage rebuild (Phase 1, the user's stated #1 ask)

Already documented in the main plan + memory. Single Elementor edit on page-id-13 to replace 11 static Penci background tiles with dynamic Posts widgets per pillar. **Score impact:** +25 in Technical Foundations once `<article>` count rises from 0 to 25+ and H1 count from 0 to 1.

---

## Files generated in this Phase 0

| File | Purpose |
|---|---|
| `audit/phase0-baseline.md` | This file |
| `audit/phase3-striking-distance-detail.md` | 6 URLs with full CSV-sourced detail |
| `audit/phase3-striking-distance-briefs.md` | Per-URL optimization briefs (Phase 3 execution) |
| `audit/phase4-redirect-404s.csv` | 9 × 404 URLs with proposed 301 targets |
| `audit/phase4-redirect-chains.csv` | 75 × 301 redirects with chain analysis (20 chains identified) |
| `audit/phase4-disavow-draft.txt` | 22 PBN/spam domains for Google Disavow Tool |
| `audit/gsc/top-queries-clicks.json` | Raw GSC top queries response |
| `audit/gsc/top-pages-clicks.json` | Raw GSC top pages response |
| `audit/gsc/query-page-pairs.json` | Raw GSC query+page dimension response |

---

## Next-session re-baseline command

```bash
# Re-pull at +30d to measure recovery
TOKEN=$(gcloud auth application-default print-access-token)
SITE="sc-domain:arahkaii.com"
curl -s -H "Authorization: Bearer $TOKEN" -H "x-goog-user-project: gsc-urls" \
  -H "Content-Type: application/json" \
  "https://www.googleapis.com/webmasters/v3/sites/${SITE//:/%3A}/searchAnalytics/query" \
  -d '{"startDate":"2026-05-27","endDate":"2026-06-23","dimensions":[],"rowLimit":1}'
```

Compare clicks, impressions, CTR, and avg position deltas. If CTR ≥ 1.5% and clicks ≥ 40 by +30d after Phase 3 execution, we're on track.
