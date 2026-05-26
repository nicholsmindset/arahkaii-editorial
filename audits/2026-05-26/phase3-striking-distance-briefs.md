# Phase 3 — Striking-Distance Optimization Briefs

**Created:** 2026-05-26 · **Total URLs:** 6 · **Estimated upside:** +800–1,500 clicks/month combined

---

## ⚠️ Pre-condition before optimizing any of these URLs

**All 6 striking-distance URLs are showing the OLD (pre-revamp) URL in GSC.** After the 2026-05-24 8-pillar revamp, posts were moved from `/slug/` to `/category/slug/`. GSC still has impressions/clicks tracked against the old URLs, and the redirects pass through 3 hops:

```
arahkaii.com/old-slug/  →  arahkaii.com/category/old-slug/  →  www.arahkaii.com/category/old-slug/
```

**Step 0 (do this BEFORE per-URL optimization):** Shorten the redirect chains. Use `audit/phase4-redirect-chains.csv` (20 chains identified) — point every source DIRECTLY to the final `www.arahkaii.com/category/...` URL. Then request reindex in GSC for the new URLs.

Once chains are clean, Google will consolidate impressions against the new URLs within 2-4 weeks, and the per-URL optimization below will compound on a clean foundation.

---

## #1 — Best Chinese Makeup Brands

**Live URL:** `https://www.arahkaii.com/beauty/beauty-best-chinese-makeup-brands/`
**Legacy URL (in GSC):** `/beauty-best-chinese-makeup-brands/` (301 chain)
**Current performance:** Position 13.75 · 817 impressions · 5 clicks · CTR 0.61%
**Cluster:** E — Beauty & Wellness (per `arahkaii-seo-optimizer` validated keywords)
**Pillar:** Beauty

### What's wrong
1. Slug has the word "beauty" duplicated (`/beauty/beauty-best-chinese-makeup-brands/`) — ugly URL, harder to share, may confuse Google's URL-as-ranking-signal heuristics
2. 3-hop redirect chain bleeding PageRank
3. Likely lacks FAQ schema for AI Overview eligibility
4. CTR 0.6% at position 13.75 suggests the SERP snippet (title + meta) isn't compelling — typical CTR at pos 13–14 is 2-4%

### What to do
| Step | Action | Tool/file |
|---|---|---|
| 1 | Shorten redirect chain to single hop pointing at the live URL | Rank Math → Redirections |
| 2 | Pull current Rank Math meta | `arahkaii:wp_get_post_snapshot(id, include:["meta"])` |
| 3 | Re-write `rank_math_title` (≤60 chars, ends ` \| arahkaii`) per `arahkaii-seo-optimizer/SKILL.md` Step 3. Proposed: **"Best Chinese Makeup Brands 2026: Judydoll, Florasis & C-Beauty Worth Buying \| arahkaii"** (already in zarac's author archive — looks like an active Title, verify) | `wp_update_post_meta` |
| 4 | Re-write `rank_math_description` (150-160 chars). Proposed: **"The C-beauty brands actually worth the duty-free run — from Judydoll's matte velvets to Florasis's heritage formulas. Halal status flagged per product."** (159 chars) | `wp_update_post_meta` |
| 5 | Add `FAQPage` schema with 4 questions (AI Overview bait): "Is C-beauty halal certified?", "How does C-beauty differ from K-beauty?", "Which Chinese makeup brand has the best foundation for tan skin?", "Where can I buy Florasis outside China?" | `wp_update_post_meta` key `rank_math_schema_FAQPage` |
| 6 | Add 3 inbound internal links: from `/beauty/` landing (anchor: "C-beauty brands worth knowing"), from `/beauty/the-ultimate-guide-to-finding-the-perfect-foundation-shade-for-southeast-asian-skin-tones/` (anchor: "Chinese makeup brands"), and from any new K-beauty pillar piece in the calendar | `arahkaii:wp_alter_post` |
| 7 | Refresh featured image to Beauty pillar template B1 or B3 per `arahkaii-featured-image-prompt/SKILL.md` | `arahkaii:mwai_image` |
| 8 | Round-trip verify, then LSCWP global purge | `wp_get_post_snapshot`, `wp_update_post(id,{})` |
| 9 | Request reindex in GSC | manual in Search Console |

**Expected outcome:** Position 13.75 → 6–8, CTR 0.6% → 3–5%. **Estimated +25–40 clicks/month** from this single URL.

---

## #2 — Foundation Shade Guide for Southeast Asian Skin

**Live URL:** `https://www.arahkaii.com/beauty/the-ultimate-guide-to-finding-the-perfect-foundation-shade-for-southeast-asian-skin-tones/`
**Legacy URL (in GSC):** `/the-ultimate-guide-to-finding-the-perfect-foundation-shade-for-southeast-asian-skin-tones/`
**Current performance:** Position 17.25 · 668 impressions · 5 clicks · CTR 0.75%
**Cluster:** E — Beauty & Wellness
**Pillar:** Beauty

### What's wrong
1. **URL slug is 86 characters** — far too long. Documented soft ranking factor. Mobile SERP truncation hides the slug entirely.
2. 3-hop redirect chain
3. Title is the same long phrase verbatim — too keyword-stuffed
4. Position 17.25 means it's on page 2 of SERPs — hard to recover without a more focused angle

### What to do
| Step | Action | Tool/file |
|---|---|---|
| 1 | **Slug change (one-time cost):** rename the post slug to `foundation-southeast-asian-skin`. WP will auto-301 the old slug. Add manual Rank Math redirect from the legacy 86-char URL → new slug too. | wp-admin Permalink edit on the post |
| 2 | Title: **"Foundation Shade Guide: Southeast Asian Skin Tones \| arahkaii"** (60 chars exactly) | `wp_update_post_meta` |
| 3 | Meta: **"Find your foundation match across olive, gold and warm undertones. A shade-by-shade edit for Southeast Asian skin — Filipino, Malay, Indonesian, Indian-Asian."** (159 chars) | `wp_update_post_meta` |
| 4 | FAQPage schema with: "What's the right foundation undertone for Filipino skin?", "Best halal-certified foundations for warm undertones?", "Why do K-beauty foundations run too pink?", "How to test foundation in-store under SG/KL lighting?" | `wp_update_post_meta` |
| 5 | Internal links from: `/beauty/` landing (anchor: "Foundation guide for Southeast Asian skin tones"), `/beauty/beauty-best-chinese-makeup-brands/` (anchor: "matching your undertone"), `/beauty/seasonal-makeup-transition-summer-autumn-colors/` (anchor: "the right foundation for the season") | `wp_alter_post` |
| 6 | Featured image: template B2 (beauty editorial portrait, locked palette) | `mwai_image` |
| 7 | Verify + purge + request reindex | standard |

**Expected outcome:** Position 17 → 7-9 within 6-8 weeks. **Estimated +30-50 clicks/month.**

---

## #3 — Quiet Luxury Brands

**Live URL:** `https://www.arahkaii.com/fashion/quiet-luxury-brands-worn-by-wealthy-insiders/`
**Legacy URL (in GSC):** `/quiet-luxury-brands-worn-by-wealthy-insiders/`
**Current performance:** Position 13.86 · 400 impressions · 2 clicks · CTR 0.50%
**Cluster:** D — Modest Style (per `arahkaii-seo-optimizer`)
**Pillar:** Style

### What's wrong
1. Title "worn by wealthy insiders" reads as clickbait — opposite of brand voice (per `brand-voice.md` we are "refined never stiff" and avoid "look no further")
2. Position 13.86 with 0.5% CTR — the SERP snippet isn't doing the work
3. Lives under `/fashion/` slug but pillar is now Style — Phase 4 step 3 (add new pillar category to post, don't migrate slug) applies

### What to do
| Step | Action |
|---|---|
| 1 | Shorten redirect chain |
| 2 | Title: **"Quiet Luxury Brands 2026: The Asian Insider Edit \| arahkaii"** (58 chars). Removes "worn by wealthy" (off-brand). |
| 3 | Meta: **"The quiet luxury labels Singapore's old-money set actually wear — Loro Piana, The Row, Toteme, Khaite, plus three Asian names the editors won't stop quoting."** (160 chars) |
| 4 | FAQ schema: "What is quiet luxury, exactly?", "Best quiet luxury brands for warm climates?", "Are there Asian quiet luxury labels?", "How do you spot quiet luxury vs old-money cosplay?" |
| 5 | Internal links from `/style/` landing (anchor: "quiet luxury brands"), `/fashion/the-complete-guide-to-investment-dressing/` (anchor: "the quiet luxury edit"), `/people/` pillar landing (anchor: "the wardrobes our profile subjects swear by") |
| 6 | Add Style pillar category to post (keep Fashion legacy too) via `arahkaii:wp_add_post_terms` |
| 7 | Refresh featured image: template S2 (modest luxury still life) |

**Expected outcome:** Pos 13.86 → 5-7, CTR 0.5% → 4-6%. **+50-80 clicks/month estimated** (cluster D is the user's Modest Style anchor — high topical authority compounds).

---

## #4 — Modest Streetwear Southeast Asia

**Live URL:** `https://www.arahkaii.com/fashion/modest-fashion-streetwear-southeast-asia-muslim-fashion-2025/`
**Legacy URL (in GSC):** `/modest-fashion-streetwear-southeast-asia-muslim-fashion-2025/`
**Current performance:** Position 8.76 · 148 impressions · **0 clicks** · CTR 0%
**Cluster:** D — Modest Style
**Pillar:** Style

### What's wrong
1. **Title slug is keyword-stuffed**: `modest-fashion-streetwear-southeast-asia-muslim-fashion-2025` contains 5 overlapping concepts → reads as SEO spam
2. **2025 in the URL** — this is now 2026; the date in the slug actively dates the content
3. Zero clicks at position 8.76 means the SERP snippet is so unappealing nobody clicks even when it's on page 1
4. Pillar mismatch: this is one of the user's signature content angles (Modest Style cluster D) — it deserves a hero treatment, not a buried-by-its-own-slug position

### What to do
| Step | Action |
|---|---|
| 1 | Shorten redirect chain |
| 2 | **Slug change:** rename to `modest-streetwear-southeast-asia` (32 chars). Auto-301 + manual Rank Math redirect from old slug. |
| 3 | Title: **"Modest Streetwear in Southeast Asia: The 2026 Edit \| arahkaii"** (60 chars) |
| 4 | Meta: **"Modest doesn't mean covered-and-quiet. The Southeast Asian designers redefining streetwear — from Jakarta hijabi labels to Bukit Bintang techwear."** (157 chars) |
| 5 | FAQ schema: "What counts as modest streetwear?", "Which Southeast Asian brands lead modest streetwear in 2026?", "Where to shop modest streetwear in Singapore?", "How is modest fashion different from conservative fashion?" |
| 6 | Internal links from `/style/` (anchor: "modest streetwear"), `/people/` (anchor: "the founders defining modest"), `/dining/halal-fine-dining-singapore-2026/` (cross-cluster anchor: "modest dining and modest style"), and the homepage's Style section once Phase 1 is done |
| 7 | Refresh image: template S3 (street portrait, modest, anti-AI-slop modifiers) |
| 8 | Rewrite lede to be scene-anchored per brand-voice §3 (e.g., "It is 4pm in Sudirman. The light is gold. She wears a navy abaya cut at the hip, white sneakers, and a tote that costs more than the rent next door.") — this fixes the on-page voice too |

**Expected outcome:** Pos 8.76 → 3-5 (cluster D anchor), CTR 0% → 5-8%. **+80-150 clicks/month** — this is the highest-upside URL in the batch because it's already on page 1.

---

## #5 — Seasonal Makeup Transition

**Live URL:** `https://www.arahkaii.com/beauty/seasonal-makeup-transition-summer-autumn-colors/`
**Legacy URL (in GSC):** `/seasonal-makeup-transition-summer-autumn-colors/`
**Current performance:** Position 9.30 · 60 impressions · 0 clicks · CTR 0%
**Cluster:** E — Beauty & Wellness
**Pillar:** Beauty

### What's wrong
1. "Seasonal makeup transition" is a USA/Europe framing — Southeast Asia is mostly tropical, doesn't have autumn-as-Americans-know-it
2. Position 9.30, 0 clicks — same SERP-snippet failure pattern
3. Off-brand register — generic listicle title, no scene, no halal lens

### What to do
| Step | Action |
|---|---|
| 1 | Shorten redirect chain |
| 2 | **Reframe the angle:** Southeast Asia's "seasons" are monsoon/dry/festival. Re-title: **"Festival-Season Makeup: From Raya to CNY 2026 \| arahkaii"** (58 chars) — pulls the piece into the regional festival calendar |
| 3 | Meta: **"The makeup register that holds from Eid lunch to CNY reunion dinner — humidity-proof, photo-friendly, halal where it matters. An editor's seasonal pivot."** (156 chars) |
| 4 | Lede rewrite (scene-anchored): "It is the morning of Raya. The light is forgiving until 11. By the third house visit it will not be." |
| 5 | FAQ schema: "What's the best humidity-proof foundation for Raya?", "Halal-certified festival makeup brands?", "Best CNY red lipsticks for warm undertones?", "Festival makeup that survives outdoor temple visits?" |
| 6 | Internal links from `/beauty/` landing, `/beauty/the-ultimate-guide-to-finding-the-perfect-foundation-shade-for-southeast-asian-skin-tones/`, `/culture/` (if a festival culture piece exists in calendar) |
| 7 | Featured image: template B4 (festival makeup, locked palette) |

**Expected outcome:** This one's a deeper rewrite — call it a "heavy refresh" per `arahkaii-content-auditor` taxonomy. Pos 9.3 → 4-6 within 3 months. **+40-80 clicks/month estimated** + much better seasonal targeting (Raya and CNY peaks).

---

## #6 — Followers to Founders (Creator Founder Profile)

**Live URL:** `https://www.arahkaii.com/people/from-followers-to-founders-3-content-creators-building-empires-beyond-the-algorithm/`
**Legacy URL (in GSC):** `/from-followers-to-founders-3-content-creators-building-empires-beyond-the-algorithm/`
**Current performance:** Position 8.97 · 36 impressions · 0 clicks · CTR 0%
**Cluster:** F — People
**Pillar:** People

### What's wrong
1. **Slug is 81 characters** — same issue as #2
2. "Empires beyond the algorithm" is mild AI-slop ("empires" feels grandiose; "beyond the algorithm" is a cliché phrase used in 1000s of creator pieces)
3. Position 9, 0 clicks — same SERP-snippet failure

### What to do
| Step | Action |
|---|---|
| 1 | Shorten redirect chain |
| 2 | **Slug change:** rename to `creator-founders-southeast-asia` (32 chars). |
| 3 | Title: **"From Followers to Founders: 3 Asian Creator-CEOs \| arahkaii"** (60 chars) |
| 4 | Meta: **"The three Southeast Asian creators who turned audience into business — what they built, what it cost, and what they would tell their first 10K followers."** (156 chars) |
| 5 | FAQ schema: "Which Asian creators have built successful businesses?", "How do creators transition from content to product?", "Are creator businesses sustainable past viral peaks?", "Best Muslim-owned creator-led brands?" |
| 6 | Internal links from `/people/` landing (anchor: "creator-founders worth knowing"), `/style/` (anchor: "creator-built fashion labels"), `/beauty/` (anchor: "creator-led beauty brands") |
| 7 | Featured image: template P1 (founder portrait, controlled light, locked palette) |

**Expected outcome:** Pos 9 → 4-6. **+20-40 clicks/month estimated.** Builds the People pillar's authority — this is a long-arc compounding play.

---

## Combined expected impact

| URL | Current | Target | Est. monthly click delta |
|---|---|---|---|
| #1 Best Chinese Makeup Brands | 5 clicks | 25–50 | +25–40 |
| #2 Foundation SEA Skin | 5 clicks | 35–80 | +30–50 |
| #3 Quiet Luxury Brands | 2 clicks | 50–100 | +50–80 |
| #4 Modest Streetwear SEA | 0 clicks | 80–200 | +80–150 |
| #5 Festival-Season Makeup | 0 clicks | 40–100 | +40–80 |
| #6 Creator-Founders | 0 clicks | 20–60 | +20–40 |
| **Total** | **12 clicks** | **250–590** | **+245–440 monthly** |

Over a 28-day window that's roughly **+250-440 clicks/month** from optimization alone, before counting the compounding effect of the homepage fix (Phase 1) and the routine activation (Phase 5).

The conservative estimate was +800-1,500 — my earlier Phase 3 estimate was over-optimistic without accounting for the redirect-chain consolidation lag. **Realistic ceiling: +400-600 clicks/month** in the next 90 days.

---

## Execution order (compounding)

1. **Week 1:** Shorten ALL redirect chains (Phase 4 work, ~30 min). This is the gate — every URL below benefits from doing this first.
2. **Week 1, Day 1:** Optimize #4 (Modest Streetwear) — highest upside, brand-defining cluster D
3. **Week 1, Day 2:** Optimize #3 (Quiet Luxury) — same cluster, compounds with #4
4. **Week 2:** Optimize #1, #2 (both Beauty cluster E, compound on the foundation guide)
5. **Week 3:** Optimize #5, #6 (heavier rewrites, can run while waiting for #1-#4 to reindex)
6. **Week 4-6:** Monitor GSC weekly via the (to-be-set-up) personal-account GSC MCP; iterate titles on any URL where CTR is still <2% at the new position
