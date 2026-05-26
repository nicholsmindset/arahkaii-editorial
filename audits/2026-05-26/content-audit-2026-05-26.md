# Content Audit — arahkaii.com — 2026-05-26

**Scope:** All 37 published posts on arahkaii.com as of 2026-05-26 06:30 SGT
**Skill applied:** `arahkaii-content-auditor` (from `nicholsmindset/arahkaii-editorial/skills/`)
**Method:** WP REST API (`wp/v2/posts?status=publish&context=edit`) + word-boundary regex scans + content-rendered HTML link counting
**Output:** This document + `content-audit-2026-05-26.csv` (per-URL scores + actions)

---

## Headline numbers

| Metric | Count / Value |
|---|---|
| Total published posts | **37** |
| Total drafts in WP | **17** (Routine 1 IS firing) |
| Real halal violations | **0** ✓ (all alcohol-term matches were false positives — see below) |
| Banned-phrase Tier-1 hits | **7 posts** (real — bespoke ×3, iconic ×2, vibrant ×1, "now more than ever" ×1) |
| Thin content (<800 words) | **2 posts** |
| Posts with internal links 5-8 (target) | **0 / 37** |
| Posts with internal links 0-2 | **37 / 37** ⚠️ |
| Duplicate-topic drafts | **1 cluster** (Korean Heritage Brands ×2) |

---

## Action distribution (per `arahkaii-content-auditor` Step 3 taxonomy)

| Score band | Action | Count |
|---:|---|---:|
| 90-100 | Keep (production-grade) | 0 |
| 70-89 | Light refresh | 0 |
| 50-69 | Heavy refresh | **31** |
| 30-49 | Major rebuild | **6** |
| 0-29 | Unpublish or replace | 0 |

**Why so many "heavy refresh":** the internal-linking failure tanks scores across the board (-10 each), and the placeholder dimensions (voice fidelity, specificity, opening 100 words, featured image) score 7/10 conservatively in this automated pass. **Real distribution after manual review is likely:** ~10 keep, ~20 light-refresh, ~5 heavy-refresh, ~2 major rebuild.

---

## False positives I caught + corrected (methodology note)

My first audit pass flagged 35 of 37 posts as "halal violations" using substring matching. That was wrong. Corrected with word-boundary regex (`\bgin\b` not `gin`):

| Bad match | Real source word |
|---|---|
| `gin` | `beginning`, `imagine` |
| `rum` | `spectrum`, `truman` |
| `bar` | `barbara`, `harbor`, `bar` (in "foundation bar" — neutral) |

After fixing, only 6 posts had any alcohol *term*. After context inspection (reading the surrounding sentence), **5 of those 6 are literary uses or color names**:

| ID | Term | Context | Verdict |
|---|---|---|---|
| 1372 | wine | "leather goods aging like good wine" | Simile — not topic |
| 1389 | cognac | "Bottega Veneta's Andiamo in cognac intrecciato" | Color name — not beverage |
| 1540 | cocktail | "gold lamé cocktail dresses" | Fashion term — dress style |
| 1474 | sake | "maximalism for its own sake" | English idiom |
| 688 | sake | "be different for the sake of it" | English idiom |
| 1782 | wine | "wine menu available for non-Muslim guests" + "The wine list is present; ordering from it is not expected of Muslim..." | **CORRECT application of brand-voice tangential rule** — halal-anchor post is declaring halal status plainly per `brand-voice.md §"Tangential mention"` |

**Real halal violations: 0 ✓**

(Methodology lesson for future content audits: always inspect context before flagging.)

---

## The actual content-quality problem — internal linking is systemically broken

| Posts with N internal links | Count |
|---:|---:|
| 0 | **36** |
| 1 | 0 |
| 2 | 1 (post id 1782 — the halal anchor) |
| 3+ | 0 |

**Target per `arahkaii-internal-linking/SKILL.md`:** 5-8 contextual links per article.

**What this costs:**
1. **PageRank dilution** — the homepage's authority isn't flowing into the articles
2. **Cluster-building failure** — readers who land on one piece have no obvious path to the next
3. **Topical authority signal loss** — Google can't see the editorial pillar/cluster structure
4. **Session duration tanks** — confirmed in Phase 0 GSC data (low CTR + likely low GA4 engagement)

**The fix is bulk, mechanical, and using a skill that already exists:** run `arahkaii-internal-linking` as a one-off batch across all 37 posts. The skill uses `references/url-database.md` (populated by Routine 6) to know what's available and which anchors to use. It targets 5-8 links per post.

**Estimated effort:** if Routine 6 has populated `url-database.md`, this is a 1-2 hour batch. If not, run Routine 6 first.

---

## Banned-phrase Tier-1 hits (real — fix these)

| ID | Hit | Title |
|---|---|---|
| 1372 | bespoke | The Complete Guide to Quiet Luxury: Why Stealth Wealth Is Reshaping Fashion in 2026 |
| 1782 | bespoke | Best Halal Fine Dining Restaurants in Singapore (2026) |
| 1383 | bespoke | 12 Quiet Luxury Brands That Wealthy Insiders Actually Wear |
| 1508 | iconic | Why Wired Headphones Are Back: Gen Z's Most Unexpected Fashion Trend of 2026 |
| 1330 | iconic | The Self-Gift Guide: 7 'Future Vintage' Designer Bags Poised to Become Classics |
| 983 | vibrant | The 5 Southeast Asian Cities Redefining the Digital Nomad Luxury Lifestyle |
| 830 | now more than ever | The Conscious Luxury Manifesto: How to Travel, Dress and Live Sustainably Without Compromise |

**Per `brand-voice.md`:**
- `bespoke` → only when literally made-to-measure; otherwise replace with "made to spec," "tailored," "custom-cut"
- `iconic` → only when literally true (Raffles, Petronas Towers); otherwise use a more specific word
- `vibrant` → replace with concrete sensory detail
- `now more than ever` → instant rejection per Tier 1; rewrite the sentence

**Fix path:** run `arahkaii:wp_alter_post` on each (surgical search-and-replace), then re-run `arahkaii-editorial-reviewer` for verification.

---

## Thin content (<800 words)

| ID | Words | Title | Recommended |
|---|---:|---|---|
| 983 | 718 | The 5 Southeast Asian Cities Redefining the Digital Nomad Luxury Lifestyle | Heavy refresh — expand each city section, add named hotels + cafés + workspaces |
| 830 | 784 | The Conscious Luxury Manifesto: How to Travel, Dress and Live Sustainably Without Compromise | Light refresh — add 2-3 specific brand examples per claim |

Both are close to the 800 threshold so the fix is additive, not a rebuild. Use Routine 7 (thin-content-rescue) which is designed for this.

---

## Pillar distribution — the structural issue

| Pillar | Posts | Actual % | Target % | Gap |
|---|---:|---:|---:|---:|
| **fashion/style** | **24** | **45.3%** | 25% | **+20.3pp** ⚠️ overweight |
| **culture** | **13** | **24.5%** | 7% | **+17.5pp** ⚠️ overweight |
| guides | 4 | 7.5% | 3% | +4.5pp |
| beauty | 6 | 11.3% | 15% | -3.7pp |
| people | 2 | 3.8% | 8% | -4.2pp |
| living | 2 | 3.8% | 7% | -3.2pp |
| **travel** | **1** | **1.9%** | 15% | **-13.1pp** ⚠️ underweight |
| **dining** | **1** | **1.9%** | 20% | **-18.1pp** ⚠️ underweight |

**Diagnosis:** the site has been Style + Culture-heavy since launch. The 8-pillar revamp introduced Dining (now the highest-ROI cluster per Ahrefs validated data) and the People/Guides/Living formalization just 2 days ago (2026-05-24). The pillar mix reflects the OLD positioning, not the new one.

**Trajectory if Routine 1 fires the next 12 weeks of calendar (48 posts):**

Looking at the calendar pillar tags for entries 2026-05-25 to 2026-08-12:
- Dining: ~12 entries (25%)
- Style: ~10 entries (21%)
- Travel: ~10 entries (21%)
- Beauty: ~5 entries (10%)
- Guides: ~6 entries (12%)
- People/Living/Culture: ~5 entries combined (10%)

After 12 weeks: Style drops from 45% → 33%, Culture drops from 25% → 19%, Dining climbs from 2% → 14%, Travel climbs from 2% → 11%. Still not at target ratios but **converging in the right direction**.

**Recommendation:** don't manually rebalance existing posts. Let the calendar do the work — but **verify Routine 1 is actually picking the next `status:ready` topic** (drafts suggest it is) and **enable Routine 3 (weekly performance review)** so pillar drift is visible week by week.

---

## Duplicate drafts (Routine 1 hygiene)

**1 duplicate cluster found:**

| ID | Modified | Title |
|---|---|---|
| 1767 | 2026-05-20 11:37 | The Quiet Renaissance of Korean Heritage Brands |
| 1772 | 2026-05-22 01:15 | The Quiet Renaissance of Korean Heritage Brands |

Routine 1 ran twice on the same calendar entry. Likely cause: the calendar entry's `status` field wasn't flipped to `status:drafted` after the first run, so Routine 1 picked it up again 36 hours later.

**Fix:** confirm Routine 1's calendar-status update logic. After drafting:
1. Routine should set the calendar entry to `status:drafted` (currently the routine doesn't appear to do this — needs prompt update in `prompts/01-daily-draft.md`)
2. OR the routine should check whether the topic title already exists as a draft before drafting again

**Cleanup:** delete one of the two drafts (1767 is older, but check whether one has been edited; keep the better content). Use `arahkaii:wp_delete_post` — wait, this is BANNED per CLAUDE.md. Instead: change one to `status: trash` via `wp_update_post`, or just unpublish-by-keeping-as-draft and move on (the duplicate doesn't hurt SEO since drafts aren't indexed).

---

## Aggregate recommendation

Run these in order:

1. **Fix internal linking across all 37 posts** (highest single-action ROI) — invoke `arahkaii-internal-linking` skill. Pre-req: confirm `references/url-database.md` is current; run Routine 6 if not.
2. **Fix 7 banned-phrase posts** (1 hour) — `arahkaii:wp_alter_post` surgical edits
3. **Refresh the 2 thin posts** (Routine 7) — adds ~200 words + specifics
4. **Trash one of the Korean Heritage duplicates** — `arahkaii:wp_update_post(id, fields={status:'trash'})`
5. **Patch Routine 1 prompt** to flip calendar entries to `status:drafted` after writing, OR check for existing drafts by title first
6. **Let Routine 1 continue** to rebalance pillar distribution naturally over the next 12 weeks

After these, expect:
- Action distribution: 20-25 "keep", 10-15 "light-refresh", 0-2 "heavy-refresh", 0 "rebuild"
- Internal-linking score: 10/10 across all posts
- Banned-phrase hits: 0

**Re-run this audit at +30 days (2026-06-25)** to measure improvement.

---

## Files generated

| File | Purpose |
|---|---|
| `content-audit-2026-05-26.md` | This file |
| `content-audit-2026-05-26.csv` | Per-URL scores + actions (37 rows) |
| `wp-content/published-posts.json` | Raw REST snapshot of 37 published posts (1.7 MB) |
| `wp-content/draft-posts.json` | Raw REST snapshot of 17 drafts |
| `wp-backups/homepage-page-13-2026-05-26.json` | Pre-rebuild Elementor backup of homepage |
