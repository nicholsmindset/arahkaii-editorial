---
name: arahkaii-editorial-reviewer
description: Quality-control review for arahkaii.com drafts — Muslim-owned, modest-luxury, anti-AI-slop standards. Use whenever Robert asks to review, QA, edit, polish, score, or sanity-check an Arahkaii draft before it goes to WordPress. Loads VOICE.md, HALAL_SUBSTITUTIONS.md, EDITORIAL_PILLARS.md, IMAGE_SYSTEM.md. Runs the 9-layer review: pillar voice fidelity, banned-phrase scan, halal compliance, AI-slop checklist, image-prompt validation, internal-link density, SEO meta, length floor, factual / cultural accuracy. Returns a pass/fail verdict plus specific rewrites.
---

# Arahkaii Editorial Reviewer

Hold every draft to the *Tatler Asia + Vogue Arabia + halal-conscious editorial* bar before it touches WordPress.

## Step 0 — Load the foundation

1. `_shared/VOICE.md`
2. `_shared/HALAL_SUBSTITUTIONS.md`
3. `_shared/EDITORIAL_PILLARS.md`
4. `_shared/IMAGE_SYSTEM.md` (for image prompts)

## The 9-Layer Review

For every draft, score each layer Pass / Fail / Needs work and provide specific rewrites.

### Layer 1 — Pillar voice fidelity

- Which of the 8 pillars is this? (Style / Beauty / Dining / Travel / Living / People / Culture / Guides)
- Does the draft hold the specific micro-voice for that pillar (VOICE.md §4.1–§4.8)?
- Are pillar-specific banned phrases present?
- Are pillar-specific imagery cues honoured in the suggested visuals?

**Fail trigger:** Draft reads like a generic luxury lifestyle piece rather than the named pillar voice.

### Layer 2 — Banned-phrase scan

Search for:
- Every Tier-1 phrase in VOICE.md §2
- Every Tier-1 phrase in the legacy brand-voice.md (for completeness)
- Pillar-specific bans

**Fail trigger:** Any Tier-1 phrase appears. Reject the draft. Return the list of hits with rewrite suggestions.

### Layer 3 — Halal & substitution compliance

- Does the draft contain ANY mention of alcohol, bar, nightclub, wine, beer, cocktail, champagne, whisky, gin, rum, cognac?
- If the draft is in Dining / Travel / Guides — is halal status declared for every restaurant / hotel / venue?
- Is the halal lens matter-of-fact (not apologetic, not preachy)?
- For After-Dark / Evening / Nightlife angles — has the draft applied the Evening Edit substitution?

**Fail trigger:** Any alcohol reference, any missing halal declaration in Dining/Travel/Guides, any moralising tone.

### Layer 4 — The Anti-AI-Slop Checklist (VOICE.md §6)

Run all 11 boxes. Two or more failures = rewrite the offending sections from a specific scene.

### Layer 5 — Opening 100 words

- Does the draft open with a scene, not an adjective?
- Can the reader picture what's in front of them by the end of sentence one?
- No headline restatement?
- No "in today's…", no "are you looking for…", no question-as-clickbait?

**Fail trigger:** Generic opener. Rewrite the lede entirely using one of VOICE.md §1's good-open patterns.

### Layer 6 — Specificity audit

For every paragraph, ask: *could this exact wording describe ten different brands / hotels / restaurants?* If yes, that paragraph is filler.

- Designer names, hotel names, dish names, neighbourhood names, prices, dates — are they specific and recent?
- Any vague claim without a named source?
- Any descriptive word that could be cut without losing meaning?

**Fail trigger:** Three or more paragraphs that read as filler.

### Layer 7 — Structural compliance

- Word count ≥ 800?
- Article matches one of the 5 locked templates?
- 5–8 internal links from `references/url-database.md`?
- H2s are specific (not "The Vibe", "The Experience", "The Verdict")?
- Each H2 section opens with a standalone, extractable sentence (for AI Overview)?
- Concludes on a forward image / quiet recommendation / sharper-thought-than-the-start — not "what do you think?"

### Layer 8 — SEO meta check

- `rank_math_title` ≤ 60 chars, ending " | arahkaii"?
- `rank_math_description` 150–160 chars, hook + value + soft pull (no CTA verb)?
- `rank_math_focus_keyword` lowercase, one phrase?
- Primary keyword appears in H1, first paragraph, and at least one H2?

### Layer 9 — Image prompt validation

If the draft includes featured / inline image prompts:
- Each prompt uses one of the 24 locked templates in IMAGE_SYSTEM.md §3?
- Palette is named using IMAGE_SYSTEM.md §1 tokens?
- Anti-slop modifiers (§4) appended?
- Aspect ratio specified?
- Never-images list (§5) clean?

## Output format

```markdown
# Editorial Review — [Article H1]

**Pillar:** [name]
**Verdict:** ✅ Pass / ⚠️ Needs work / ❌ Reject

## Layer-by-layer
| Layer | Status | Notes |
|---|---|---|
| 1 · Pillar voice | ✅/⚠️/❌ | ... |
| 2 · Banned phrases | ✅/⚠️/❌ | [list any hits + rewrites] |
| 3 · Halal compliance | ✅/⚠️/❌ | ... |
| 4 · AI-slop | ✅/⚠️/❌ | [list any boxes ticked] |
| 5 · Opening | ✅/⚠️/❌ | ... |
| 6 · Specificity | ✅/⚠️/❌ | [paragraphs flagged] |
| 7 · Structure | ✅/⚠️/❌ | [word count, links, H2s] |
| 8 · SEO meta | ✅/⚠️/❌ | ... |
| 9 · Image prompts | ✅/⚠️/❌ | ... |

## Specific rewrites
[Paragraph-by-paragraph rewrite suggestions in priority order]

## What's working
[2–3 lines on what the draft does well — don't only critique]

## Final action
- [ ] Approve as-is and route to arahkaii-publisher
- [ ] Apply the rewrites above and re-submit
- [ ] Reject and rebrief writer
```

## When to escalate to Robert

Email Robert if:
- The draft requires alcohol coverage that cannot be substituted
- The brief contradicts the halal position
- The cultural accuracy concern is beyond your verification
- The brand wants to publish something that would damage long-term positioning

---

*Loaded immediately after arahkaii-editorial-writer and before arahkaii-publisher. Never let a draft skip this skill.*
