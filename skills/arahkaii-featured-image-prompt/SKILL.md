---
name: arahkaii-featured-image-prompt
description: Generate moodboard-locked, anti-AI-slop image prompts for arahkaii.com featured images, inline images, and social-media visuals. Use whenever an Arahkaii article needs a hero image, supporting inline images, an Instagram/LinkedIn/Pinterest visual, or any AI-generated picture. Loads IMAGE_SYSTEM.md (24 locked templates across 8 pillars + Arahkaii palette + anti-slop modifiers + never-images list) and matches the prompt to the article's pillar. Refuses to generate prompts for alcohol, bar, nightclub, generic AI-slop tropes, or anything outside the moodboard palette. Always specifies camera, lens, film stock, lighting direction, palette tokens, and aspect ratio.
---

# Arahkaii Featured Image Prompt

Produce AI image prompts that look like editorial photography from *Vogue Arabia* and *Tatler Asia* — not "AI-generated lifestyle".

## Step 0 — Load the foundation

1. `_shared/IMAGE_SYSTEM.md` — the locked palette, 24 templates, anti-slop modifiers, never-images list
2. `_shared/VOICE.md` — for the pillar's specific imagery cues
3. `_shared/HALAL_SUBSTITUTIONS.md` — for visual substitutes (no bottles, no bars)

## Step 1 — Identify the pillar

Map the article to one of the 8 pillars: Style · Beauty · Dining · Travel · Living · People · Culture · Guides.

Then pick the locked template from IMAGE_SYSTEM.md §3 that matches the article angle:

| Pillar | Templates |
|---|---|
| Style | S1 (portrait), S2 (garment detail), S3 (hands with garment) |
| Beauty | B1 (ingredient still life), B2 (product on porcelain), B3 (treatment room) |
| Dining | D1 (single plate, dim restaurant), D2 (tea/coffee ritual), D3 (dessert bar interior) |
| Travel | T1 (hotel room corner), T2 (empty street at 7am), T3 (market produce) |
| Living | L1 (apartment interior), L2 (single design object), L3 (prayer corner) |
| People | P1 (subject portrait), P2 (hands at work), P3 (subject in studio wide) |
| Culture | C1 (object still life), C2 (figure + cultural context), C3 (architectural detail) |
| Guides | G1 (listicle hero), G2 (flat-lay), G3 (evening edit scene) |

## Step 2 — Fill in the locked template variables

Each template has bracketed variables. Fill them with:
- Specific subjects (named ingredient, dish, garment, neighbourhood)
- Specific palette tokens from IMAGE_SYSTEM.md §1
- Specific lighting direction
- Specific camera + lens + film stock

Never invent a new prompt structure. The 24 templates are the only patterns.

## Step 3 — Append the anti-slop modifiers (mandatory)

Append IMAGE_SYSTEM.md §4 to the end of every prompt:

```
film grain, no AI sheen, natural skin texture with pores, asymmetrical features,
no extra fingers, no symmetrical perfection, no harsh studio flash,
no plastic gloss, no over-saturation, no rainbow refraction, no HDR,
shot on real film stock (Portra 400 / Ektar 100 / Tri-X 400),
editorial photography, magazine-grade, no stock-photo composition
```

## Step 4 — Specify the aspect ratio

| Use | Aspect ratio |
|---|---|
| WordPress featured | 16:9 (1920×1080) |
| WordPress inline | 4:5 (1080×1350) |
| Instagram square | 1:1 (1080×1080) |
| Instagram carousel | 4:5 (1080×1350) |
| Instagram reel cover | 9:16 (1080×1920) |
| Pinterest pin | 2:3 (1000×1500) |
| LinkedIn share | 1.91:1 (1200×627) |
| Newsletter hero | 16:9 (1600×900) |

## Step 5 — Validate the prompt against IMAGE_SYSTEM.md §7

Run the validation checklist:
- [ ] Subject is named specifically
- [ ] Lighting direction specified
- [ ] Palette named using tokens
- [ ] Composition specified
- [ ] Camera + lens specified
- [ ] Film stock or grain specified
- [ ] Anti-slop modifiers appended
- [ ] No banned subject / palette
- [ ] Aspect ratio specified
- [ ] If hands in frame: "anatomically correct, no extra fingers"
- [ ] If face in frame: "natural skin texture with pores, asymmetrical features"

If any box unchecked, rewrite before submitting.

## Step 6 — Output format

For each article, produce:

```markdown
# Image prompts for [article title]

## Featured image (16:9, hero)
**Template:** [name, e.g. D1 — Single plate, dim restaurant]
**Prompt:**
```
[full filled-in prompt + anti-slop modifiers + aspect ratio]
```
**Negative prompt (Midjourney --no):** [list, e.g. wine, bottles, bar interior, neon]
**Suggested tool:** Midjourney V7 / DALL-E 3 / Google Imagen 3 / Flux Pro

## Inline image 1 (4:5)
**Template:** [name]
**Prompt:**
```
[...]
```

## Inline image 2 (4:5)
**Template:** [name]
**Prompt:**
```
[...]
```

## Social variants
- **Instagram square (1:1):** [adapt from one of the inline images]
- **Pinterest pin (2:3):** [adapt with vertical crop]
- **LinkedIn share (1.91:1):** [adapt with horizontal crop]
```

## Step 7 — After generation, run the 60-second review

For every generated image (IMAGE_SYSTEM.md §8):

1. Editorial or AI?
2. Hands and faces anatomically correct?
3. Palette inside the locked tokens?
4. At least 30% breathing room?
5. Any alcohol / club lighting / banned subject?
6. Would this look at home in *Tatler Asia*?
7. Grain / texture, or smooth AI plastic?

If any fails → regenerate. Don't ship slop.

## Hard rules

1. Never generate an image containing alcohol, bottles, bar interiors, club lighting, or anything from the never-images list (IMAGE_SYSTEM.md §5).
2. Never deviate from the 24 locked templates. New patterns invite slop.
3. Never skip the anti-slop modifiers.
4. Never use the locked palette tokens loosely — they are exact hex values.
5. Always specify camera + lens + film stock — this is the strongest anti-AI-sheen lever.
6. If asked to generate something out of scope, refuse and offer a halal-aligned alternative from the substitution table.

## Tool-specific notes

### Midjourney V7
- Append `--ar [W:H]` for aspect ratio
- Append `--style raw` to reduce AI sheen
- Append `--stylize 50` to reduce over-stylisation
- Use `--no [banned subjects]` for negative prompts
- Append `--seed [number]` if you need consistency across a series

### DALL-E 3 (via ChatGPT or API)
- Write the aspect ratio in plain English at the end ("aspect ratio 16:9")
- Cannot use negative prompts — instead write what you want positively
- Reduce AI sheen with: "shot on real film, visible grain, natural imperfection"

### Google Imagen 3
- Aspect ratio via parameter
- Excellent for editorial portraits; weaker on hands

### Flux Pro
- Best hands and faces of any current model
- Aspect ratio via parameter
- Append the anti-slop modifiers at the very end (Flux respects late tokens)

---

*Loaded by: arahkaii-publisher (featured-image step), arahkaii-social-media-creator (every social asset), arahkaii-editorial-writer (when suggesting hero image direction).*
