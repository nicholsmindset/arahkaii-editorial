---
name: editorial-research
description: Deep editorial research and brief generation for arahkaii.com articles before drafting. Use this skill whenever a new article needs research, sourcing, competitive analysis, expert perspectives, data points, and a stake-claimed editorial angle — typically the FIRST step of any drafting flow. Triggers on phrases like "research [topic]", "gather information about", "what's the current landscape for", "find sources on", "competitive analysis for", "build a brief on", "what's the angle on [topic]", or any request requiring deep investigation before content creation. Produces a comprehensive research brief that editorial-writer then drafts from. Pairs downstream with editorial-writer, editorial-reviewer, seo-optimizer. Do NOT use for the actual writing — that's editorial-writer's job. Do NOT use for short fact-checks within an existing draft — those go through targeted ahrefs / firecrawl calls.
---

# Editorial Research — arahkaii.com

The research-before-drafting step. Produces a comprehensive brief that editorial-writer drafts from. A thin brief produces thin output — this skill's quality is the upstream lever for the entire content pipeline.

---

## When this skill runs

- Step 1 of Routine 1 (daily draft) — always
- When Robert asks "research [topic]" before deciding whether to write
- When refreshing existing content — fresh research to identify what's changed
- For one-off deep-dives that don't immediately become articles (Robert keeps the brief in his Project knowledge for later)

---

## What this skill produces

A structured brief with this shape (this is the contract — editorial-writer reads this format):

```
TOPIC: <Article title or working title>
PILLAR: <fashion / beauty / culture / travel / lifestyle / sustainability>
TARGET WORD COUNT: <number>

EDITORIAL ANGLE
<One paragraph stating the article's argument. Must be a position, not a topic. Must be specific.>

KEY FACTS (the empirical anchor for the argument)
- <Fact 1 with source>
- <Fact 2 with source>
- <Fact 3 with source>
- <Fact 4 with source>
- <Fact 5 with source>

CULTURAL REFERENCES (demonstrating fluency)
- <Reference 1 — designer / movement / cultural moment>
- <Reference 2>
- <Reference 3>

NAMED SPECIFICS (people, brands, places to invoke by name)
- People: <list with role/affiliation>
- Brands: <list>
- Places: <list at locals' granularity>

COMPETITIVE LANDSCAPE
- Top 5 SERP results for primary keyword:
  1. <URL> — <publication> — angle they take — what they miss
  2. ...
- Reference-publication takes (where arahkaii's bar sits):
  - <Vogue / Tatler / BoF / etc. piece>: <their angle>
- Gap arahkaii fills: <one sentence on what's missing in current coverage>

INTERNAL LINK CANDIDATES (from references/url-database.md)
- <URL> — <why it's relevant>
- <URL> — <why it's relevant>
- ... 5-10 candidates

SEO TARGETS
- Primary keyword: <single phrase, lowercase>
- Secondary keywords: <2-3 related terms with search volume notes>
- Monthly search volume: <number>
- Keyword difficulty: <0-100>
- AI Overview opportunity: <yes / no / partial — based on serp-overview data>

STRUCTURE SUGGESTION
- Opening pattern: <Pattern A (reported lead) or Pattern B (editorial thesis)>
- H2 outline:
  1. <H2 heading + 1-sentence summary of what this section argues>
  2. <H2 heading + summary>
  3. <H2 heading + summary>
  4. <H2 heading + summary>
  (optional 5-6)
- Closing approach: <forward provocation / cultural reframe / sharper thesis>

OPEN QUESTIONS / RISKS
- <Anything unverified that drafting will need to resolve>
- <Cultural sensitivities to watch>
- <Reportage gaps to flag>
```

If editorial-writer receives a brief missing the **EDITORIAL ANGLE** or **KEY FACTS** sections, it must return the brief for revision before drafting. Drafting on a thin brief produces thin output.

---

## The research process

### Step 1 — Keyword landscape

For the topic's primary keyword:

```
ahrefs:keywords-explorer-overview
  keyword: "<primary keyword>"
  country: "us" (or "sg" for Singapore-specific)
```

Capture:
- Search volume (monthly)
- Keyword difficulty (KD)
- Top-of-funnel related terms
- Question keywords (these become H2 candidates)
- SERP features active (AI Overview, Featured Snippet, People Also Ask, Image Pack)

Then for related terms:
```
ahrefs:keywords-explorer-related-terms
  keyword: "<primary keyword>"
```

Capture top 10 related terms with volume and intent indicators.

### Step 2 — SERP analysis

```
ahrefs:serp-overview
  keyword: "<primary keyword>"
  country: "us"
```

Capture top 10 ranking URLs. For each:
- Publication
- Article title
- Date published / last modified
- Approximate word count (rough indicator)
- Their angle / structure
- What they emphasize
- What they miss

This becomes the **COMPETITIVE LANDSCAPE** section. Pattern-match: if top 5 are all listicles, arahkaii's opportunity is a reported analytical piece. If top 5 are all shopping guides, arahkaii's opportunity is the cultural argument behind the products.

### Step 3 — Reference publication scan

Search for how Vogue, Tatler Asia, Harper's Bazaar Asia, Business of Fashion, NYTimes T Magazine, AnOther have covered the same topic (where applicable):

```
firecrawl:firecrawl_search
  query: "<topic> site:vogue.com OR site:tatler.asia OR site:businessoffashion.com"
  limit: 10
```

Capture their angles. These are the bar arahkaii is being measured against, not the top-ranking listicles. The arahkaii angle should be of equivalent depth and stake-claim — without copying.

### Step 4 — Deep scrape top sources

For the top 3-5 most analytically substantive sources from steps 2 and 3:

```
firecrawl:firecrawl_scrape
  url: "<url>"
  formats: ["markdown"]
```

Read full content. Extract:
- Specific data points
- Specific names of designers, brands, places, people
- Sourced facts with their original citations
- Cultural context not yet captured

These feed the **KEY FACTS** and **NAMED SPECIFICS** sections.

### Step 5 — Synthesize the angle

This is the highest-leverage step. The angle is the entire article's foundation.

Test a candidate angle against three questions:

1. **Is it a position?** Could a reasonable reader disagree?
2. **Is it specific?** Does it name specific people, brands, places, or moments?
3. **Is it current?** Does it root in something happening now, not "this thing exists"?

If yes to all three → the angle is publishable. Move forward.

If no to any → keep researching, sharpen until yes to all three. If after 30 min of research you still can't find an angle, the topic may not be ready. Email Robert: "Topic needs more development; suggest moving to backlog."

### Step 6 — Cultural reference selection

For pieces that touch culture (most arahkaii pieces do):

Identify 2-3 cultural references that demonstrate fluency without performing knowledge. Bad: an exhaustive history paragraph. Good: a single accurate aside that signals "this writer knows the context."

Examples of good cultural references:

- For a Korean designer piece: "...the kind of avant-garde experimentation Lee Sang-bong attempted in the late 1990s but never sold commercially — a lineage the third-wave designers like Songzio now resolve."
- For a Tokyo travel piece: "...the slow-stay register that Hoshinoya pioneered before Aman Kyoto refined it."
- For a C-beauty piece: "...drawing on the same TCM heritage that Yue Sai built in the 1990s — but with Gen-Z packaging and TikTok distribution."

These references aren't filler. They're the ribbons that show the writer is operating at a Tatler register, not a Buzzfeed register.

### Step 7 — Internal linking candidates

Read `references/url-database.md`. Identify 5-10 existing arahkaii posts that would link naturally into the new piece:

- 3-4 from the same pillar (deep topical authority)
- 2-3 from adjacent pillars (lateral browsing)
- 1-2 category archives

For each, capture WHY it's relevant — not just "related topic" but "in this specific section, this link would extend the reader into [X]".

### Step 8 — Output the brief

Assemble all of the above into the brief format at the top of this skill.

---

## Quality bars for research output

### Editorial angle
- One paragraph (4-6 sentences)
- Names at least 3 specific entities (designers, brands, places)
- Stakes a position the reader could disagree with
- Roots in a specific current moment (a recent show, a launch, a recent data point)

### Key facts
- 3-5 facts minimum
- Each with a source attribution (publication, report, official data)
- At least 2 are quantitative (numbers, percentages, dates)
- All are defensible — verifiable on inspection

### Cultural references
- 2-3 references
- Each demonstrates fluency without showing off
- All factually verifiable

### Competitive landscape
- Top 5 SERP results captured
- 2-3 reference-publication takes captured
- Clear gap statement: what's missing that arahkaii will provide

### Internal links
- 5-10 candidates
- Each with a one-line "why relevant"
- Span at least 2 pillars

---

## Research depth by article type

Different article types need different research depth:

| Article type | Sources to consult | Research time |
|---|---|---|
| Hot take (800-1200 words) | 3-5 sources | 15-20 min |
| Trend explainer (1200-1800) | 8-10 sources | 30-45 min |
| Standard feature (1800-2200) | 10-15 sources | 45-60 min |
| Long feature (2200-2800) | 15-20 sources + 1-2 deep scrapes | 60-90 min |
| Cornerstone (2800-3500) | 20+ sources, multiple deep scrapes, possibly real outreach | 2-3 hours |

For routines: the daily routine 1 should NOT attempt cornerstone-level research. It should aim for standard-feature depth maximum. Cornerstone pieces are written manually with this skill in Claude.ai Project context.

---

## Failure modes to watch for

### "Topic summary, not angle"
The brief describes the topic but has no position. Drafting from this produces summary-content, not editorial.

**Symptoms:** "The C-beauty market is growing rapidly..." (descriptive, no stake).
**Fix:** What's the specific argument? "C-beauty's craft-and-theatre proposition is fundamentally different from K-beauty's science-and-minimalism approach, and this difference explains why Singapore Sephora's H1 2026 data shows C-beauty pulling ahead."

### "No specifics"
The brief mentions "Korean designers" but doesn't name any. Drafting from this produces adjective-stacked filler.

**Fix:** Name 5+ specific designers, brands, places, people. Specificity is the editorial voice.

### "Stale references"
The brief cites a 2019 trend report. Drafting from this produces dated-feeling content.

**Fix:** Insist on sources from the last 18 months for trend pieces. Older references are fine as historical context, not as current evidence.

### "Cultural blur"
The brief treats hanbok / kimono / qipao as interchangeable, or treats Singapore / KL / Jakarta as one market.

**Fix:** Sharpen cultural specifics. Different markets, different histories, different products. Get this right at research stage; it's much harder to fix during drafting.

### "Wrong-bar references"
The brief benchmarks arahkaii against Refinery29 or Insider listicles.

**Fix:** Benchmark against Tatler Asia, Vogue Business, AnOther, BoF. Even when those publications don't have a direct piece on the topic, their depth and voice are the bar.

---

## Tools used

Primary:
- `ahrefs:keywords-explorer-overview` — keyword landscape
- `ahrefs:serp-overview` — SERP competitor analysis
- `ahrefs:keywords-explorer-related-terms` — keyword expansion
- `firecrawl:firecrawl_search` — broad source discovery
- `firecrawl:firecrawl_scrape` — deep content extraction

Secondary:
- `web_search` — fallback for sources Firecrawl misses
- `web_fetch` — fetching specific URLs Robert provides
- `ahrefs:brand-radar-cited-pages` — for current-trend validation (what AI overviews are already citing)

---

## Handoff to editorial-writer

When research is complete, hand off the brief AS IS in the format at the top of this skill. Don't paraphrase. The writer reads the brief structurally.

The writer is allowed to deviate from the structure suggestion if a different structure serves the angle better — but the angle and key facts are non-negotiable. They're the contract.

---

*Skill maintained by Robert. Tools list updated when new MCP integrations are available. Research depth bars tuned quarterly based on what actually produces strong drafts.*
