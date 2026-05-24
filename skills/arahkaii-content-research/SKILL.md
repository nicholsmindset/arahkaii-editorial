---
name: arahkaii-content-research
description: Deep web research for arahkaii.com future articles — gathering source material, analysing competitor coverage, identifying expert perspectives, collecting data and statistics, developing unique editorial angles. Use when the output is a comprehensive research brief NOT the final article. Triggers on "research [topic]", "what's the current landscape for [X]", "find sources on", "competitive analysis for [cluster]". Loads VOICE.md, EDITORIAL_PILLARS.md, HALAL_SUBSTITUTIONS.md before researching to ensure all gathered material is on-brand and halal-aligned. Sibling to arahkaii-editorial-research (which produces briefs ready for drafting); this skill goes wider, deeper, longer.
---

# Arahkaii Content Research

Deep editorial reconnaissance for future Arahkaii pieces. Wider scope and longer horizon than `arahkaii-editorial-research`. Output is a research dossier, not a writer's brief.

## Step 0 — Load the foundation

1. `_shared/EDITORIAL_PILLARS.md`
2. `_shared/VOICE.md`
3. `_shared/HALAL_SUBSTITUTIONS.md`

## Step 1 — Scope the research

Confirm with Robert (or infer from the brief):
- **Pillar(s)** the research will inform
- **Horizon** — single article, cluster, quarterly campaign, cornerstone piece
- **Format of output** — research dossier (default), source library, competitive teardown, trend report
- **Halal lens** required? (Yes for everything by default — only "No" if explicitly for benchmarking competitor content)

## Step 2 — The 5-Lens Research Framework

### Lens 1 — Cultural / editorial landscape

What is the conversation happening around this topic *right now* in:
- *Vogue Arabia*, *Vogue Singapore*, *Vogue Business*
- *Tatler Asia*, *Harper's Bazaar Asia*
- *CNA Lifestyle*, *CNA Luxury*
- *Wallpaper*, *Monocle*, *The Atlantic*, *T Magazine*
- *Halal Travel Media*, *Modest Style Magazine*, *Hijab Style*

What are they saying? What are they missing? Where is the Arahkaii-specific gap?

### Lens 2 — SEO landscape

From Ahrefs MCP (or saved CSVs):
- Top-ranking pages for the keyword cluster
- Search volume + difficulty
- Striking-distance keywords (positions 4–15) that Arahkaii could attack
- Content gaps vs CNA Lifestyle, CNA Luxury, Tatler

### Lens 3 — Expert / source landscape

- Named experts in the space (academics, founders, designers, chefs)
- Recent studies, reports, white papers
- Public interviews and quotable material
- Muslim-owned / halal-certified / modest-fashion-led sources (always overweighted)

### Lens 4 — Data landscape

- Industry reports (Bain, McKinsey, NielsenIQ, BoF)
- Market sizing (where verifiable)
- Specific statistics with sources
- Cultural data (e.g. modest-fashion-economy figures, halal-tourism growth)

### Lens 5 — Visual / cultural references

- Aesthetic touchstones — campaigns, editorials, films, exhibitions
- Material / craft references
- Imagery moodboards (to pass to `arahkaii-featured-image-prompt`)

## Step 3 — Output: the research dossier

```markdown
# Research Dossier — [Topic / Cluster]

**Pillar(s):** [name(s)]
**Horizon:** [single piece / cluster / cornerstone]
**Halal lens:** [Yes / No / Applied via substitution: [original → new]]
**Date:** [ISO date]

## Executive read
[3–5 sentence summary of what this research reveals and why it matters for Arahkaii]

## Lens 1 — Editorial landscape
| Outlet | What they've covered | Angle | Date | Gap for us |
|---|---|---|---|---|

## Lens 2 — SEO landscape
| Keyword | Volume | KD | Current SERP leader | Striking distance for Arahkaii? |
|---|---:|---:|---|---|

## Lens 3 — Sources & experts
| Source | Type | Credentials | Why useful | Contactable? |
|---|---|---|---|---|

## Lens 4 — Data points
| Statistic | Source | Date | Verifiability |
|---|---|---|---|

## Lens 5 — Visual references
[List of campaigns, films, exhibitions, photographers — with notes on how they map to IMAGE_SYSTEM.md templates]

## Suggested article angles (Arahkaii-ready)
1. [Angle 1] — pillar: [X], template: [Y], working headline: [Z]
2. [Angle 2] — ...
3. [Angle 3] — ...

## Halal / modest framing notes
[Specific notes on how the halal lens enters this cluster — where it naturally fits, where it would feel forced]

## What we should NOT do
[Topics within this space that violate brand position — alcohol angles, gossip angles, etc.]

## Calendar recommendation
[How many articles, over what period, and where they fit in the 90-day plan]
```

## Rules

1. Every dossier states the pillar(s) explicitly.
2. Every cluster's halal angle is identified before sources are pulled.
3. Sources are real, dated, and verifiable. No fabricated industry data.
4. Visual references map to one of the 24 IMAGE_SYSTEM.md templates.
5. Suggested angles are paired with locked article templates.
6. If the cluster legitimately has no halal angle, flag it — do not invent one.

---

*Output handed to: arahkaii-editorial-research (which converts the dossier into a writer's brief), or stored in the calendar as a future cluster.*
