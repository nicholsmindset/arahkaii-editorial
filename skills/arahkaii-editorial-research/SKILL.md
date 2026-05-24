---
name: arahkaii-editorial-research
description: Deep editorial research and outline creation for arahkaii.com — Muslim-owned, modest-luxury, Asian editorial standards. Use when researching a topic before drafting, building a brief, mapping competitor coverage, finding expert sources, or scoping a cornerstone piece. Loads VOICE.md, EDITORIAL_PILLARS.md, HALAL_SUBSTITUTIONS.md to ensure research stays on-brand. Produces a research brief + locked outline that any writer (human or AI) can execute against. Always identifies the pillar, the locked article template, and the halal angle before any research is gathered.
---

# Arahkaii Editorial Research

Build research briefs that already encode Arahkaii's voice, pillar architecture, and halal lens — so the writer who picks them up cannot drift off-brand.

## Step 0 — Load the foundation

1. `_shared/EDITORIAL_PILLARS.md`
2. `_shared/VOICE.md`
3. `_shared/HALAL_SUBSTITUTIONS.md`

## Step 1 — Classify the topic

- **Pillar:** Style / Beauty / Dining / Travel / Living / People / Culture / Guides
- **Locked template:** Local Listicle / Destination Guide / Profile / Beauty Explainer / Evening Edit / Cornerstone Feature
- **Halal positioning:** Halal-positive (Muslim-owned, halal-certified) · Halal-tangential (modest-friendly, alcohol-free venue) · Halal-redirect (the original topic was alcohol/nightlife; apply substitution)
- **Search intent:** Informational · Investigational · Navigational · Commercial · Transactional · Local
- **Target keyword cluster** (from the gameplan keyword tables)

If the topic redirects under HALAL_SUBSTITUTIONS.md, state the substitution upfront and proceed with the new topic.

## Step 2 — Run the research

### Phase A — Competitor & SERP audit

Use Ahrefs (or the saved CSVs in `/uploads/`):
- Top 10 ranking articles for primary keyword
- Their structures, word counts, unique angles
- Multimedia usage
- Content gaps + Arahkaii-specific differentiator (modest, halal, Muslim-owned, Asian-modern)

Use Firecrawl / WebSearch:
- CNA Lifestyle, CNA Luxury, Tatler Asia, Vogue Singapore, Vogue Arabia, Halal Travel Media — what have they done in this cluster?
- Where is the gap Arahkaii owns?

### Phase B — Source identification

- 3–5 named experts (chef, designer, dermatologist, hotelier, founder)
- 2–3 recent studies / reports / industry data points
- 1 contrarian view for balance
- For dining / travel: at least one Muslim-owned or halal-certified source where relevant

### Phase C — AI Overview research

- Identify the question-based queries this article should answer
- Map related entities (brands, neighbourhoods, ingredients, designers)
- Note definition opportunities (e.g. "PDRN refers to…")
- Identify table / comparison opportunities

### Phase D — Local SEO (if applicable)

- Local search volume for SG / KL / Jakarta / Dubai / Tokyo
- Neighbourhood-level granularity
- Local terminology variations (e.g. "kopitiam" vs "coffee shop")
- Modest-traveller-specific intent (halal restaurant, prayer room, modest dress climate)

## Step 3 — Produce the brief

```markdown
# Research Brief — [Working title]

## Classification
- **Pillar:** [name]
- **Locked template:** [name]
- **Halal positioning:** [type]
- **Search intent:** [type]
- **Primary keyword:** [keyword]
- **Secondary keywords:** [list]
- **Target word count:** [from EDITORIAL_PILLARS.md length register]

## The argument
[One-paragraph thesis — what is this article going to claim that nobody else is claiming?]

## The differentiator
[Why Arahkaii is the right outlet — modest, halal-aware, Asian-modern, Muslim-owned source access, etc.]

## Outline (locked template applied)
[Section-by-section outline matching the chosen template]

## Sources to use
| Source | Type | Why |
|---|---|---|

## Named subjects (people, places, brands)
| Subject | Verified spelling | One-line context |
|---|---|---|

## Halal lens
[How halal status appears in the article — never buried, never apologised for]

## Internal link candidates (from url-database.md)
- [URL] — anchor text in context

## SEO meta draft
- `rank_math_title`: [≤60 chars, ends " | arahkaii"]
- `rank_math_description`: [150–160 chars]
- `rank_math_focus_keyword`: [lowercase, one phrase]

## Suggested featured image template
[One of the 24 in IMAGE_SYSTEM.md §3, with bracket variables filled in]

## AI Overview optimization
- Question-format H2s to include
- Definition-pattern paragraphs
- FAQ section recommended? [Yes/No]
- Data points to lead with
```

## Rules

1. Never produce a brief for an alcohol / nightclub / wine topic. Redirect using HALAL_SUBSTITUTIONS.md.
2. Always classify the pillar before researching.
3. Always identify the locked template before researching.
4. Sources must be real and verifiable. No fabricated industry data.
5. Named subjects must have their spelling verified (designer surnames, neighbourhood names, terminology).
6. If you cannot find a Muslim-owned / halal-certified source for a Dining / Travel / Beauty piece, flag it — do not fake it.

---

*Pairs upstream of: arahkaii-editorial-writer. Feeds into: arahkaii-internal-linking, arahkaii-seo-optimizer.*
