---
name: editorial-reviewer
description: Quality control review for arahkaii.com drafts before publishing. Use this skill after editorial-writer produces a draft, or whenever Robert asks to review, edit, polish, or QA an article for publication readiness. Triggers on phrases like "review this draft", "is this ready to publish", "edit this piece", "polish before publishing", "QA this article", or any request that takes a written draft and prepares it for the final publishing step. Runs the full checklist: banned-phrase scan, voice fidelity against brand-voice.md, structural compliance, cultural accuracy, length compliance, and the 10-point pre-publish gate. Pairs upstream with editorial-writer (which drafted) and downstream with seo-optimizer (meta), arahkaii-internal-linking (links), arahkaii-publisher (ship). Do NOT use for first-pass drafting — that's the writer skill's job. Do NOT use for already-published posts being refreshed — those go through arahkaii-publisher's wp_alter_post flow.
---

# Editorial Reviewer — arahkaii.com

The QA gate. Sits between editorial-writer's draft and the publishing pipeline. Catches voice drift, banned phrases, structural issues, and the cultural errors that kill credibility.

If you wouldn't show this piece to a senior Tatler editor with confidence, it doesn't pass.

---

## When this skill runs

- After every editorial-writer draft, before publishing
- When Robert asks to review an existing draft (in WP admin or as a paste-in)
- When refreshing existing content (read the live post, then apply this skill to the updated version)
- As a standalone polish pass when Robert asks "make this better"

---

## Pre-flight load

Before reviewing, load:

1. `references/brand-voice.md` — canonical voice doc (banned phrases, structural rules)
2. `references/editorial-pillars.md` — to verify pillar-appropriate voice register
3. The draft being reviewed
4. The original brief (from editorial-research or content-calendar.md entry) — so review can check fidelity to the stated argument

---

## The review framework

A draft passes review only when it passes ALL checks. A single failure on any check = revise.

### Check 0 — Structural integrity (runs BEFORE all other checks)

This check catches concatenated content — the single most common generation failure mode, where multiple separate AI drafts are merged into one post without editorial curation. Concatenated content cannot be fixed by editing; it must be re-drafted.

Scan the entire draft for:

**H1 tags in post_content.** WordPress sets the H1 from post_title automatically. Any `<h1>` tag inside post_content is a structural SEO error. One H1 in content = fail.

**"---" separators or empty `##` headings mid-content.** These are concatenation seams — they appear where one generated article ends and another begins. Any separator = fail.

**Duplicate H2 headings.** If the same H2 (or near-identical phrasing) appears more than once, multiple drafts were merged. Duplicate = fail.

**Multiple introduction or conclusion blocks.** Each article has exactly one opening and one closing. If the content reads as if it restarts or concludes more than once, it is concatenated. Multiple intros/outros = fail.

**Multiple title variants appearing as headings mid-content.** If the article title (or a close variant) appears again as an H1 or bold heading partway through, a second article was appended. Any recurrence = fail.

**Word count exceeding 3,500 words.** Standard features are 1,800-2,200 words. Long features 2,800-3,500. If the draft exceeds 3,500 words, it almost certainly contains appended content. Over-ceiling = fail.

**Auto-reject rule:** If Check 0 fails on ANY criterion, do not proceed to Checks 1-10. Return to editorial-writer with a specific diagnosis: "Concatenated content detected — [H1 in body / separator found at line X / duplicate H2 '[heading text]' / word count N]. Re-draft as a single editorial piece. Do not attempt to fix by deletion."

### Check 1 — Banned-phrase scan

Scan the entire draft for every phrase in `brand-voice.md` section 2 banned list:

stunning · iconic · game-changer · in today's world · let's dive in · buckle up · without further ado · a must-have · you won't believe · the perfect [X] · level up · obsessed · literally (intensifier) · absolutely (intensifier) · incredibly (intensifier) · amazing · ultimate · elevated · curated · delve into · navigate (non-literal) · in our increasingly [adjective] world · navigate the complexities of · etc.

**If ANY appear:** flag for replacement. The replacement should be specific, not just a synonym.

- "stunning bag" → name the bag with specifics: "Bottega Veneta's Andiamo in cognac intrecciato"
- "iconic Birkin" → "the Birkin's resale ceiling" or whatever specific aspect matters here
- "must-have piece" → just describe what it is and why it matters; the must-have framing is dead
- "elevated" → say what it actually does ("more structured", "tonally restrained", "shorter hemmed")
- "curated" → "selected", "chosen", "edited"

### Check 2 — Opening paragraph compliance

Read the first 150 words. They must follow one of two patterns (brand-voice.md section 7):

**Pattern A — Reported Lead:** Opens with a specific scene, date, or fact, then moves to argument.

**Pattern B — Editorial Thesis:** Opens with the argument stated cleanly, then builds the case.

**Auto-reject if the opening:**
- Restates or rephrases the headline
- Opens with a question to the reader ("Have you ever wondered...?")
- Opens with "In a world where..." or "In today's...world"
- Opens with "When it comes to..."
- Opens with "Picture this:" or any imperative scene-setting
- Opens with a list ("From X to Y to Z...")
- Opens with what the article will do ("In this article, we'll explore...")

### Check 3 — Argument clarity

The article must have a clear editorial argument. Test:

> *Can the reader summarize the article's thesis in one sentence after reading?*

If yes → pass. If no → the piece reads as topic summary, not analysis. Reject with: "Argument unclear. The piece needs a thesis the reader can summarize in one sentence."

The argument should be:
- A position (something a reader could disagree with)
- Specific (names specific players, brands, places)
- Defended by the body (not just stated)

### Check 4 — Specificity and named references

Sample 5 paragraphs at random. Each should contain at least one of:
- A specific designer / brand / studio name
- A specific place name (at granularity locals would use)
- A specific date, season, or event
- A specific data point
- A specific quote (real, sourced)

**Auto-reject if** a draft is more than 30% adjective-stacking without specifics. ("Stunning, bold, fierce silhouettes that elevate any look" — out.)

### Check 5 — Cultural accuracy

Scan for every cultural reference and verify:
- Designer name spelled correctly with conventions intact (Saint Laurent vs YSL, Comme des Garçons with accent, THE ROW caps)
- Heritage terms used correctly (hanbok ≠ kimono ≠ qipao; Peranakan, Baba-Nyonya, Straits Chinese all have distinct meanings)
- Place names at locals' granularity (Tiong Bahru, not "Singapore's central district")
- Fashion week conventions ("Spring/Summer 2026" not "Spring 2026")
- Date math: if the piece references "two years ago" or "last September," confirm the math against current date

**Auto-reject if** any cultural fact is wrong. Wrong cultural details destroy the piece's credibility entirely.

### Check 6 — Length compliance

Word count within target ±10%.

Hard floor: 800 words. Anything below = reject (thin content risk to AdSense + low editorial quality).

If under target by >10%: identify which sections are thin, suggest specific expansion (not "expand the intro" but "Section 3 lacks empirical anchor — add the Fashionphile resale data point").

If over target by >10%: identify cut candidates. Usually it's a section that recapitulates rather than advances the argument.

### Check 7 — Structural compliance

H2 sections: 4–6 for standard features. 3–4 for shorter pieces.

Each H2's lead sentence is standalone-extractable (AI Overview-ready).

Question-format H2s where natural; declarative where punchier.

Conclusion does NOT recap. It sharpens. Test: would the closing paragraph make sense if you removed everything before it? If yes, it's a recap — reject and rewrite.

### Check 8 — Internal linking quality

Count internal links (links to other arahkaii.com pages):
- Target: 5–10 per piece
- Distribution: 2-3 in opening third, 2-3 middle, 2-3 closing third
- Anchor text: descriptive, natural to the sentence
- No "click here", no link-as-CTA at end, no full-title-verbatim anchors

**Reject if** all links are stacked at the end. **Reject if** any anchor text is "click here" or "read more about [X]".

### Check 9 — Em-dash and punctuation discipline

Count em-dashes per paragraph. Reject any paragraph with more than 1. This is the single clearest AI-output tell.

Scan for double dashes (`--`) and convert to proper em-dashes (`—`) only where the rule allows.

Scan for ellipses used as dramatic pauses (`...`). Replace with sentences. Editorial voice doesn't trail off.

### Check 10 — Reportage integrity

Scan for direct quotes. For each:
- Is it real (sourceable to a public interview, real statement)?
- Or clearly paraphrased synthesis ("Daniel Lee has spoken about this dynamic")?

**Auto-reject if** any direct quote is attributed to a real person but cannot be sourced. Inventing quotes is the single fastest way to destroy editorial credibility.

For data claims:
- Specific numbers should be defensible (Reuters, McKinsey, Bain, NielsenIQ-type sources where possible)
- Vague approximations ("a significant percentage") should usually be sharpened to specifics
- If a claim can't be confidently anchored, soften the language ("Singapore retailers report" rather than "Singapore Sephora's H1 2026 data shows" — only use the specific framing if it's actually defensible)

---

## Review output format

After running all 10 checks, produce a structured report:

```
EDITORIAL REVIEW: <Title>
PILLAR: <pillar>
WORD COUNT: <actual> / <target> (<delta%>)
RECOMMENDATION: ☑ Publish | ◐ Revise | ✗ Reject

STRENGTHS:
- <2-3 bullet points: what works>

ISSUES BY CHECK:
1. Banned phrases: <count found> | <list>
2. Opening: <pass / fail with reason>
3. Argument clarity: <pass / fail>
4. Specificity: <pass / fail>
5. Cultural accuracy: <pass / fail with any errors>
6. Length: <within range / under / over>
7. Structure: <pass / fail>
8. Internal links: <count> | <distribution issue if any>
9. Em-dash/punctuation: <pass / fail>
10. Reportage integrity: <pass / fail>

CRITICAL FIXES (must address before publish):
- <specific line-level fixes with exact text changes>

RECOMMENDED IMPROVEMENTS (would strengthen):
- <suggestions>

REVISED DRAFT (if revisions applied):
<full revised draft with all critical fixes applied>
```

---

## Revision philosophy

When revising:
- **Preserve voice.** Don't rewrite the writer's argument — sharpen its execution.
- **Surgical, not wholesale.** Replace banned phrases in-place; expand thin sections; tighten verbose ones. Don't redraft entire articles unless they're fundamentally broken.
- **Match the writer's pillar register.** A culture piece reviewed too literally turns into a beauty product comparison.
- **Cut more than you add.** Most thin drafts need expansion, but most drafts that read as AI-padded need contraction.

---

## Voice-drift indicators

Specific patterns that signal AI tone slipping in (review extra carefully when you see these):

- **Triple-list rhythms.** "Considered, deliberate, and unhurried." "Bold, daring, and unforgettable." AI loves three. One or two specifics beats three abstractions.
- **Em-dash density.** AI uses em-dashes to mimic editorial rhythm. One per paragraph is the ceiling.
- **"It's not just X, it's Y."** AI's favorite reframe pattern. Use sparingly — once per piece max.
- **Soft hedge framings.** "Some might argue..." "Many believe..." — replace with stated positions.
- **Adverb stacking.** "Particularly notable", "incredibly compelling", "remarkably consistent." Cut the adverbs; the nouns and verbs do the work.
- **Closing recaps.** "From X to Y to Z, this piece has explored..." — automatic reject. Conclusions sharpen, not summarize.
- **"In the world of [X]"** — pattern AI uses to set up a topic. Cut and rewrite.

---

## When to ask Robert for input vs. revise autonomously

**Revise autonomously:**
- Banned phrases
- Em-dash density
- Em-dash to period conversion
- Adverb tightening
- Closing recaps
- Light structural reordering
- Specificity additions where the brief provides the specifics

**Ask Robert / flag for review:**
- Argument unclear (might need re-research)
- Cultural error you're uncertain about
- Length significantly off target (>20%)
- Reportage integrity issue (suspected invented data)
- Pillar voice mismatch (the piece was written in wrong register)
- Suggested major structural rework

For routines: anything in the second category goes to email; routine cannot auto-publish.

---

## Pre-publish gate (the final 10-point check)

A draft must pass ALL 10 to ship:

- [ ] No banned phrases (Check 1)
- [ ] Opening uses Pattern A or B (Check 2)
- [ ] One-sentence argument is clear (Check 3)
- [ ] Specifics over adjectives throughout (Check 4)
- [ ] Cultural references verified (Check 5)
- [ ] Length within ±10% of target (Check 6)
- [ ] H2 structure compliant; closing sharpens not recaps (Check 7)
- [ ] 5–10 internal links well-distributed (Check 8)
- [ ] Em-dash density ≤1 per paragraph (Check 9)
- [ ] All quotes real or clearly paraphrased; data defensible (Check 10)

10/10 → pass to publishing pipeline.

---

*Skill maintained by Robert. The check list expands when new voice-drift patterns are identified in production output.*
