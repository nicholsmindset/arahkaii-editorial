# Arahkaii Skills — Revamp Bundle (May 2026)

This folder contains the **full rebuild** of every Arahkaii skill, aligned to the new Muslim-owned, 8-pillar, halal-conscious editorial position.

**What you're looking at:** workspace-first version. Reviewed by you, then pushed to the `nicholsmindset/arahkaii-editorial` GitHub repo as a single PR.

---

## What changed from the current repo

### 1. Brand position (the biggest shift)

| Before | After |
|---|---|
| Premium Asian fashion + lifestyle | **Muslim-owned, Asian modern-luxury, modest-conscious** |
| Tatler / Vogue Asia bar | **Tatler Asia + Vogue Arabia + halal editorial bar** |
| No halal lens | **Halal substitution framework is non-negotiable** |
| Generic luxury aesthetic | **Locked moodboard palette + 24 anti-AI-slop image templates** |

### 2. Pillar architecture (6 → 8)

| Old pillar | New home |
|---|---|
| Fashion | → **Style** (renamed, modest-inclusive) |
| Beauty | → **Beauty** (absorbs Wellness) |
| Culture | → **Culture** |
| Travel | → **Travel** (with mandatory modest-traveller sidebar) |
| Wellness | → folded into **Beauty** |
| Sustainability | → cross-cutting `#sustainable` tag (no longer a pillar) |
| *(new)* | → **Dining** ★ (biggest validated SEO opportunity — CNA Luxury's Mother's Day Dining article alone pulls 8,537 visits/month) |
| *(new)* | → **Living** |
| *(new)* | → **People** (carved out of profiles) |
| *(new)* | → **Guides** (service journalism + the signature Arahkaii Evening Edit) |

### 3. Three new shared reference files

All skills now load these BEFORE generating anything:

- `_shared/VOICE.md` — master voice + 8 category-specific voice variants + AI-slop checklist
- `_shared/EDITORIAL_PILLARS.md` — 8-pillar architecture with target output share
- `_shared/HALAL_SUBSTITUTIONS.md` — alcohol/nightlife redirect table (16 substitutions)
- `_shared/IMAGE_SYSTEM.md` — locked palette + 24 image-prompt templates + anti-slop rules

### 4. Every skill renamed `arahkaii-*` for namespacing

The legacy `editorial-writer`, `editorial-reviewer`, `editorial-research`, `featured-image-prompt`, `social-media-creator`, `content-auditor`, `seo-optimizer` skills are now prefixed `arahkaii-*` to make scope explicit.

### 5. Per-skill change log

| Skill | Major change |
|---|---|
| **arahkaii-editorial-writer** | Loads VOICE.md + pillar voice + halal rule. 5 locked article templates. Halal status declaration mandatory in Dining/Travel/Guides. AI-slop checklist runs before output. |
| **arahkaii-editorial-reviewer** | 9-layer review (was 7). Adds halal compliance layer + image prompt validation layer. Returns pass/fail verdict with specific rewrites. |
| **arahkaii-editorial-research** | Always classifies pillar + locked template + halal positioning before researching. Briefs are writer-ready. |
| **arahkaii-content-research** | Sibling of editorial-research, wider scope, produces dossiers for future clusters. |
| **arahkaii-internal-linking** | Maps to the 8 keyword clusters. Cross-link rules per cluster. Live URL database with pre-written anchor suggestions. |
| **arahkaii-publisher** | Refuses to publish anything failing halal/voice/AI-slop checks. Pre-publish gate is mandatory. |
| **arahkaii-featured-image-prompt** | 24 locked templates across 8 pillars. Locked palette tokens. Anti-slop modifiers appended to every prompt. 60-second post-generation review. |
| **arahkaii-social-media-creator** | Locked to 10 fixed Canva/Figma templates. Captions written in pillar voice. Per-platform hashtag families per pillar. |
| **arahkaii-content-auditor** | Audits against the new 8-pillar architecture. Halal violation scan is top-priority. Recommends keep / refresh / rebuild / unpublish per article. |
| **arahkaii-seo-optimizer** | Validated keyword clusters from May 2026 Ahrefs data. AI Overview optimisation checklist. Local SEO for SG/KL/JKT/DXB. Refuses to optimise for alcohol keywords. |

---

## Folder structure

```
skills-revamp/
├── README.md                              # this file
├── _shared/
│   ├── VOICE.md                           # ★ master voice + 8 category voices
│   ├── EDITORIAL_PILLARS.md               # ★ 8-pillar architecture
│   ├── HALAL_SUBSTITUTIONS.md             # ★ alcohol → halal redirect table
│   └── IMAGE_SYSTEM.md                    # ★ 24 image templates + palette
├── arahkaii-editorial-writer/SKILL.md
├── arahkaii-editorial-reviewer/SKILL.md
├── arahkaii-editorial-research/SKILL.md
├── arahkaii-content-research/SKILL.md
├── arahkaii-internal-linking/SKILL.md
├── arahkaii-publisher/SKILL.md
├── arahkaii-featured-image-prompt/SKILL.md
├── arahkaii-social-media-creator/SKILL.md
├── arahkaii-content-auditor/SKILL.md
└── arahkaii-seo-optimizer/SKILL.md
```

---

## How to push to GitHub

Once reviewed, this maps directly into the live repo. Two staging options:

### Option A — Single PR (recommended)

```bash
# 1. Clone the repo locally (if not already)
git clone https://github.com/nicholsmindset/arahkaii-editorial.git
cd arahkaii-editorial

# 2. Branch
git checkout -b revamp/2026-05-brand-rebuild

# 3. Copy the shared references into the repo
mkdir -p references/_shared
cp -r /path/to/skills-revamp/_shared/* references/_shared/

# 4. Replace the existing brand-voice + pillars references
cp /path/to/skills-revamp/_shared/VOICE.md references/brand-voice.md
cp /path/to/skills-revamp/_shared/EDITORIAL_PILLARS.md references/editorial-pillars.md
cp /path/to/skills-revamp/_shared/HALAL_SUBSTITUTIONS.md references/halal-substitutions.md
cp /path/to/skills-revamp/_shared/IMAGE_SYSTEM.md references/image-system.md

# 5. Overwrite each skill (keeping any non-SKILL.md assets like scripts/ references/)
for skill in editorial-writer editorial-reviewer editorial-research featured-image-prompt seo-optimizer arahkaii-publisher arahkaii-internal-linking; do
  cp /path/to/skills-revamp/arahkaii-${skill}/SKILL.md skills/${skill}/SKILL.md 2>/dev/null || \
  cp /path/to/skills-revamp/arahkaii-${skill}/SKILL.md skills/${skill}/SKILL.md
done

# 6. Add the new skills not in the repo yet
mkdir -p skills/arahkaii-content-research skills/arahkaii-content-auditor skills/arahkaii-social-media-creator
cp /path/to/skills-revamp/arahkaii-content-research/SKILL.md skills/arahkaii-content-research/SKILL.md
cp /path/to/skills-revamp/arahkaii-content-auditor/SKILL.md skills/arahkaii-content-auditor/SKILL.md
cp /path/to/skills-revamp/arahkaii-social-media-creator/SKILL.md skills/arahkaii-social-media-creator/SKILL.md

# 7. Commit + push
git add .
git commit -m "Brand revamp: 8-pillar architecture, halal substitution framework, anti-AI-slop image system, category-specific voices"
git push origin revamp/2026-05-brand-rebuild

# 8. Open PR on GitHub for review before merging to main
```

### Option B — Atomic commits per skill (for cleaner review)

Same as above but commit each skill separately:

```bash
git add references/_shared/ references/brand-voice.md references/editorial-pillars.md references/halal-substitutions.md references/image-system.md
git commit -m "Add shared reference files: voice, pillars, halal substitutions, image system"

git add skills/editorial-writer/
git commit -m "Rewrite editorial-writer: 8-pillar voice, halal rule, locked templates"

# ...and so on, one commit per skill
```

---

## Things I did NOT change (yet)

These files in the live repo still need updating to match the revamp — they're not in this bundle because they require live data or your input:

1. **`content-calendar.md`** — Robert should regenerate this from the new 90-day publishing cadence in `Arahkaii_Final_Gameplan.docx` (Section 8)
2. **`references/url-database.md`** — Routine 6 (quarterly) regenerates this. After the brand revamp, run Routine 6 manually to refresh it against the new 8-pillar tags.
3. **`references/category-tag-map.md`** — Add the new pillar categories in WordPress first (Style, Beauty, Dining, Travel, Living, People, Culture, Guides), then run Routine 6 to refresh.
4. **`CLAUDE.md`** — Should be updated to reference the new pillar count and the halal rule. Minor edit — I can do this on request.
5. **`README.md`** in the repo root — Brand position description should be updated.
6. **`prompts/01-daily-draft.md`** through `prompts/07-thin-content-rescue.md` — These reference the legacy 6-pillar structure. They need a sweep to update the pillar count + add halal compliance steps.
7. **`blotato-social-distributor` skill** — Should now load `arahkaii-social-media-creator` upstream and enforce the same halal/voice rules. Quick edit.

If you want me to do any of those follow-ups, say the word.

---

## Validation

Every SKILL.md in this bundle:
- ✅ Has YAML frontmatter with `name` and `description`
- ✅ Description includes specific trigger phrases
- ✅ Loads the shared reference files before producing output
- ✅ Has a "Hard rules" section that includes the halal position
- ✅ Has an explicit refusal protocol for out-of-scope requests
- ✅ Pairs with adjacent skills (named upstream/downstream)

---

## The new editorial pipeline (visualised)

```
                       ┌──────────────────────────────────┐
                       │  _shared/VOICE.md                │
                       │  _shared/EDITORIAL_PILLARS.md    │  ← loaded by every skill
                       │  _shared/HALAL_SUBSTITUTIONS.md  │
                       │  _shared/IMAGE_SYSTEM.md         │
                       └────────────────┬─────────────────┘
                                        │
   ┌──────────────────────┐             │
   │ arahkaii-content-    │             │
   │ research             │             │
   │ (dossier for future) │             │
   └────────┬─────────────┘             │
            │                           │
            ↓                           ↓
   ┌──────────────────────┐    ┌──────────────────────┐
   │ arahkaii-editorial-  │ →  │ arahkaii-editorial-  │
   │ research             │    │ writer               │
   │ (writer's brief)     │    │ (drafts the article) │
   └──────────────────────┘    └────────┬─────────────┘
                                        │
                                        ↓
                       ┌──────────────────────────────┐
                       │ arahkaii-internal-linking    │
                       │ (5–8 contextual links)       │
                       └────────┬─────────────────────┘
                                │
                                ↓
                       ┌──────────────────────────────┐
                       │ arahkaii-seo-optimizer       │
                       │ (Rank Math meta + schema)    │
                       └────────┬─────────────────────┘
                                │
                                ↓
                       ┌──────────────────────────────┐
                       │ arahkaii-featured-image-     │
                       │ prompt                       │
                       │ (24 locked image templates)  │
                       └────────┬─────────────────────┘
                                │
                                ↓
                       ┌──────────────────────────────┐
                       │ arahkaii-editorial-reviewer  │
                       │ (9-layer QA — pass / fail)   │
                       └────────┬─────────────────────┘
                                │
                                ↓ (pass)
                       ┌──────────────────────────────┐
                       │ arahkaii-publisher           │
                       │ (WordPress write + verify)   │
                       └────────┬─────────────────────┘
                                │
                                ↓
                       ┌──────────────────────────────┐
                       │ arahkaii-social-media-       │
                       │ creator                      │
                       │ (10 locked Canva templates)  │
                       └────────┬─────────────────────┘
                                │
                                ↓
                       ┌──────────────────────────────┐
                       │ blotato-social-distributor   │
                       │ (manual trigger only)        │
                       └──────────────────────────────┘

   Run weekly/monthly/quarterly:
   ┌──────────────────────────────┐
   │ arahkaii-content-auditor     │
   │ (refresh sprint planning)    │
   └──────────────────────────────┘
```

---

*Built 2026-05-24 from the validated Ahrefs data and the Final Gameplan. The shared reference files (`_shared/*.md`) are the highest-leverage files in the bundle — when voice drifts in production, update them before tuning any prompt.*
