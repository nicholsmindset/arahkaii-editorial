---
name: editorial-writer
description: Premium long-form editorial writing for arahkaii.com at the level of Tatler, Vogue Asia, Harper's Bazaar Asia, and Business of Fashion. Use this skill whenever drafting any new article for arahkaii.com — features, trend reports, designer profiles, cultural criticism, travel reportage, beauty analysis, opinion pieces. Triggers on phrases like "write an article", "draft a piece", "produce a feature", "write the [topic] article", or any request that ends with a fresh, full-length editorial draft. Pairs upstream with editorial-research (which produces the brief) and downstream with editorial-reviewer (which QAs), seo-optimizer (which adds meta), arahkaii-internal-linking (which inserts links), arahkaii-publisher (which ships to WordPress), and blotato-social-distributor (which adapts for social). Do NOT use for short social copy — that goes through blotato-social-distributor's adaptation step. Do NOT use for newsletter copy unless explicitly publishing as an arahkaii article.
---

# Editorial Writer — arahkaii.com

The drafting skill. Takes a brief (from editorial-research or content-calendar.md) and produces a full Tatler-caliber long-form piece.

The bar is non-negotiable. If the output doesn't read like Tatler, Vogue Asia, or Business of Fashion, it gets rejected at the editorial-reviewer step. Better to take longer and ship one good piece than fire three thin ones.

---

## Pre-flight (every time, no exceptions)

Before writing a word, load these in order:

1. `references/brand-voice.md` — the canonical voice doc. Banned phrases, structural bans, required moves, tone register per pillar, opening patterns, length register, headline craft, meta description craft.
2. `references/editorial-pillars.md` — coverage area for this article, voice register that pillar uses.
3. `references/url-database.md` — for internal linking targets.
4. The brief from editorial-research or the calendar entry.

If `brand-voice.md` and any instruction conflict, **brand-voice.md wins.** Always.

---

## The drafting process

### Step 1 — Stake the argument

Before writing, articulate the article's editorial argument in one sentence. If you can't, the piece isn't ready to write — go back to editorial-research and sharpen the brief.

A good argument:
- Has a position (something a reader could disagree with)
- Is specific (names specific designers, brands, places, or moments)
- Is current (rooted in something happening now, not "this trend exists")

Examples of good arguments:
- "Songzio's Paris debut signals that Korean designers no longer need to be framed as 'Asian' to compete in luxury."
- "C-beauty's second wave isn't a K-beauty replacement — it's a fundamentally different proposition built on craft and theatre."
- "The era of the celebrity creative director is ending; the next phase is design-collective and longer creative-team tenures."

Examples of failed arguments:
- "Korean fashion is having a moment." (Too broad, no position.)
- "K-beauty is popular in Singapore." (No tension, no insight.)
- "Here's everything you need to know about quiet luxury." (Topic summary, not argument.)

### Step 2 — Outline before drafting

Standard feature outline (1,800–2,200 words):

- **Opening (150–200 words)** — Reported lead or editorial thesis pattern (see brand-voice.md section 7)
- **H2 #1: Context/setup (300–400 words)** — Why this matters, who the relevant figures are
- **H2 #2: The argument's first beat (400–500 words)** — The first evidence point
- **H2 #3: The counterargument or complication (300–400 words)** — Shows analytical depth
- **H2 #4: Forward implication (300–400 words)** — What this means going forward
- **H2 #5: Practical/insider note (200–300 words)** — Where to buy / where to go / what to watch (optional, varies by pillar)
- **Closing (100–150 words)** — Empowering close. Sharper thought, forward question, cultural context.

H2s are question-format where natural ("Why are Korean designers gaining luxury credibility?"), declarative where punchier ("The end of the creative-director-as-savior era"). Don't force every H2 into a question — sometimes flat is stronger.

### Step 3 — Write the opening

The hardest 100 words in the piece. Use one of two patterns from brand-voice.md section 7:

**Pattern A — Reported Lead:** Start with a specific scene, date, fact. Move to argument.

**Pattern B — Editorial Thesis:** State the argument cleanly. Build the case.

What NEVER works as an opening:
- "When it comes to X..."
- "In a world where Y..."
- "Have you ever wondered..."
- "Picture this:"
- Any rephrasing of the headline
- "In today's [adjective] world..."
- "Let's dive into..."

If the opening could appear unchanged on a content marketing blog, rewrite it.

### Step 4 — Build the body

For each H2 section:

**Lead sentence is standalone.** AI Overview surfaces extracted paragraphs. The first sentence of every H2 should be a complete, self-contained thought — not a transition from the previous section.

**Specifics over adjectives.** Bad: "this stunning luxury handbag." Good: "Bottega Veneta's Andiamo in cognac intrecciato, currently priced at SGD 4,800 retail."

**Named references.** Designers by name. Collections by season (SS26, FW25 acceptable after first full mention). Specific shows, real publications, actual buyers/stylists where possible.

**Cultural fluency baseline.** Hanbok is not kimono is not qipao. Peranakan culture is not a vibe. Yohji is Yamamoto. Comme des Garçons is Kawakubo's. Get this wrong and the piece is dead on arrival.

**Stake positions across the body.** Don't hedge every claim. Editorial voice means having opinions. "C-beauty's craft theatricality offers something K-beauty's minimalism never could" — confident, defensible, opinionated.

**Internal links woven in naturally.** Not "click here." Not the linked article's full title verbatim. The anchor text should read as natural prose. See `arahkaii-internal-linking` skill for placement strategy. 5–10 links per piece, distributed.

### Step 5 — Close

Closes do exactly one thing: leave the reader sharper than when they started.

Patterns that work:
- **Forward-looking provocation:** "By 2030, the question won't be whether Korean designers compete in luxury. It'll be whether the term 'Korean' still attaches to their names at all."
- **Cultural reframe:** "What Loewe figured out — and what most of Europe still hasn't — is that craft heritage isn't a European inheritance to be marketed. It's a global one, and the future of luxury depends on who tells that story best."
- **Sharper version of the thesis:** Restate the argument in a tighter, more memorable form than the opening.

Patterns that fail:
- "In conclusion..." (no.)
- "To recap..." (no.)
- "Whether you're a [reader type] or a [reader type]..." (no.)
- Tailing off with a soft CTA. (no.)

---

## Voice calibration per pillar

(Detailed in `references/editorial-pillars.md`. Brief summary.)

| Pillar | Voice register |
|---|---|
| Fashion | Insider analytical — knows the industry plumbing |
| Beauty | Educated skeptic — separates marketing from dermatology |
| Culture | Cultural critic — historically literate, analytically confident |
| Travel | Repeat-visitor editor — knows which room to request |
| Lifestyle/Wellness | Pragmatic, not breathless — counter to wellness-influencer voice |
| Sustainability | Pragmatic, not preachy — frames quality and longevity |

Read the pillar's full register in `editorial-pillars.md` before drafting.

---

## Length matching to argument depth

(From `brand-voice.md` section 4.)

- 800–1,200: hot take on a single move/look/brand pivot
- 1,200–1,800: trend explainer (a movement worth explaining)
- 1,800–2,200: **standard feature** (the default — reported analysis with 4–6 H2s)
- 2,200–2,800: long feature (industry-wide arguments, profiles, cultural movements)
- 2,800–3,500: cornerstone (once per quarter; definitive coverage)

Hard floor: 800 words. Under that, the piece reads as filler and damages site-wide E-E-A-T.

---

## Headline craft

The H1 is the editorial argument compressed.

**Patterns that work:**
- The Quiet/Slow X ("The Quiet Renaissance of Korean Heritage Brands")
- Why X Matters Now ("Why Daniel Lee Leaving Burberry Is the End of an Era")
- Inside X ("Inside the Modest Fashion Economy")
- Future / Future Vintage ("The Five Bags That Will Define 2030's Collector Market")
- The Real X ("Tokyo's New Luxury Map: Where Real Insiders Stay")

**Anti-patterns:**
- "[Number] best/top/must-have X" (out)
- "You won't believe..." (out)
- "What X doesn't want you to know" (out)
- Anything ending in a question mark unless it's a deeply argued piece where the question IS the thesis

SEO consideration: 50–65 chars ideal for SERP display, primary keyword near front. The " | arahkaii" suffix lives in `rank_math_title` only, NOT in the H1.

---

## Specific things to get right

### Reportage discipline
- Real sources where possible (Reuters, BoF, Vogue Business, McKinsey, Bain, NielsenIQ)
- When synthesizing claims, make them defensible — not fabricated, plausibly approximate
- Never invent direct quotes from real people. Period.
- Quoting public figures: only real, sourced quotes — or clearly paraphrased synthesis ("Daniel Lee has spoken about this dynamic in interviews")

### Designer name conventions
- Full name first mention; surname or studio name after
- Saint Laurent (not Yves Saint Laurent unless historically required)
- Comme des Garçons (correct cap-and-special chars)
- THE ROW (all caps for the brand)
- Y/Project (with slash)
- Off-White (with hyphen)
- Bottega Veneta (two words)
- Wooyoungmi (one word)

### Place name granularity
- Singapore neighborhoods: Tiong Bahru, Joo Chiat, Holland Village — locals' granularity
- Tokyo to chōme level if known
- Seoul by district name (Gangnam, Itaewon, Hongdae — but NOT "Korean district")
- "K-fashion district" is not a place. Don't write it.

### Currency
- Local currency for local contexts (SGD, MYR, JPY, KRW)
- USD for global luxury comparisons
- Symbol upfront: SGD 8,500 (not 8,500 SGD)
- Format with comma separators for thousands

### Fashion week dates
- "Spring/Summer 2026" not "Spring 2026" (separate seasons)
- SS26 / FW25 acceptable after first mention
- Resort, Cruise, Pre-Fall are valid season names
- PFW / MFW / LFW / NYFW conventional after first use

---

## Working with research briefs

The editorial-research skill produces briefs in this format (read it before drafting):

```
TOPIC: <Title>
ANGLE: <The editorial argument in one paragraph>
KEY FACTS: <3-5 specific data points to anchor the piece>
CULTURAL REFERENCES: <2-3 references that demonstrate fluency>
COMPETITIVE LANDSCAPE: <What top-5 ranking pieces say; what we'll say differently>
INTERNAL LINKS: <5-10 suggested URLs from url-database.md>
TARGET WORD COUNT: <number>
PRIMARY KEYWORD: <focus keyword>
SECONDARY KEYWORDS: <2-3 related terms>
```

If the brief is missing critical elements (no clear angle, no specifics), do NOT write — return to editorial-research for a stronger brief. Drafting on a thin brief produces thin output.

---

## Output format

Default: **Gutenberg blocks**. arahkaii's Soledad theme works best with Gutenberg.

```
<!-- wp:paragraph -->
<p>First paragraph text...</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Section heading</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Body text with <a href="https://arahkaii.com/some-related-post/">internal link</a> woven in.</p>
<!-- /wp:paragraph -->
```

For long-form features, paragraphs and headings are usually enough. Avoid over-using:
- Pull quotes (used only when the quote IS the moment of insight; max 1-2 per piece)
- Image blocks (featured image handled separately; only inline-image if the piece references specific visuals)
- Lists (only when the topic actually is a list — e.g., "the five bags". Even then, prefer prose with named items.)

**Markdown is also accepted** by `arahkaii:wp_create_post`. If Gutenberg blocks feel unnatural for the piece, markdown is fine — WordPress will convert. Use clean markdown:

```markdown
First paragraph text...

## Section heading

Body text with [internal link](https://arahkaii.com/some-related-post/) woven in.
```

---

## What gets rejected automatically

If the editorial-reviewer skill flags any of these, the draft fails:

1. Contains any banned phrase from `brand-voice.md` section 2
2. Opens with headline restatement, question-as-clickbait, or "in a world where"
3. Lacks a clear editorial argument
4. Reads as topic summary rather than reported analysis
5. Under 800 words
6. Gets cultural details wrong
7. Invents direct quotes from real people
8. Listicle structure when not warranted by the topic
9. More than one em-dash per paragraph
10. Conclusion recaps rather than sharpens

---

## When to use simpler register

Some article types call for less reportage and more practical:

- **City guides ("Tokyo's New Luxury Map"):** the "repeat-visitor editor" voice. Personal-ish without first-person. Specific room names, restaurant names. Less argument, more curation.
- **Shopping-intent pieces ("Where to Buy C-Beauty in Singapore"):** practical SEO-friendly content with real shopping value. Still avoid "must-have" framing. Frame as "what's actually worth your attention."
- **Calendar / what's happening pieces:** factual. Still no banned phrases, but lighter on argument.

Even these stay above the lifestyle-blog bar. The voice never drops below "Tatler's city guide section." Never to "Time Out Singapore."

---

## Final pre-handoff check

Before declaring a draft done:

- [ ] One-sentence argument can be stated clearly
- [ ] Opening uses Pattern A or B; no banned openers
- [ ] No banned phrases anywhere in the body
- [ ] Word count within target (±10%)
- [ ] All cultural references verified (designer names, place names, terminology)
- [ ] 5–10 internal links woven naturally
- [ ] No invented quotes
- [ ] Close leaves reader sharper, not summarized
- [ ] Headline is one of the patterns that work; ≤65 chars including expected suffix
- [ ] Section-lead sentences are standalone extractable

Pass all 10 → hand off to `editorial-reviewer` for final QA. Fail any → revise before handoff.

---

*Skill maintained by Robert. Tuned quarterly against current Tatler / Vogue Asia / BoF samples. When voice drifts in production output, the fix usually goes in `references/brand-voice.md`, not in this file.*
