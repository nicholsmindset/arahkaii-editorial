---
name: featured-image-prompt
description: Generate sophisticated AI image prompts for arahkaii.com featured images at editorial photography standard. Use this skill when creating hero images for any new arahkaii article, when regenerating featured images for refreshes, or when Robert asks for "an image prompt" or "the featured image" for any piece. Triggers on phrases like "generate the featured image", "image prompt for [article]", "create a hero image", "what should the featured image be", or any image generation request tied to an arahkaii article. Produces prompts optimized for arahkaii:mwai_image (AI Engine's image generation, which uses GPT-image-1 / DALL-E / Stable Diffusion variants depending on plugin config). The output is a single detailed prompt + alt text + dimensions specification. Pairs with arahkaii-publisher (which uploads via mwai_image and sets as featured). Do NOT use for in-content article images (those use a different workflow). Do NOT use for social-media-specific imagery (that's the canva-social-publisher skill's job).
---

# Featured Image Prompt — arahkaii.com

The featured image is the SERP thumbnail, the OG share image, the homepage card visual, the Pinterest pin source, the LinkedIn post image. It's the single most-seen visual asset per article — and most AI-generated images look generic precisely because their prompts are generic.

This skill produces prompts that yield editorial photography, not generic AI sheen.

---

## When this skill runs

- Step 7 of Routine 1 (daily draft) — every new article
- When refreshing existing content (often the featured image needs a refresh too)
- Ad-hoc: Robert asks for an image prompt for a specific piece

---

## Pre-flight load

1. The article (post_title, primary keyword, pillar)
2. The research brief (for cultural context, specific entities mentioned)
3. `references/brand-voice.md` — for tone-aligned visual register

---

## The arahkaii visual register

### What we want

- **Editorial photography aesthetic** — looks like it could appear in a magazine, not stock
- **Soft natural light** — golden hour, overcast, indirect window light
- **Neutral warm tones** — cream, taupe, mushroom, bone, soft black; never garish saturation
- **Negative space** on one side (for text overlay potential on social shares)
- **Considered composition** — rule of thirds, leading lines, intentional crops
- **Atmospheric over explicit** — suggests the subject rather than centers it

### What we want to avoid

- **Stock photo aesthetic** — generic studio shots, white backgrounds
- **AI sheen** — that telltale over-smoothness, plastic skin, dead eyes
- **Generic luxury markers** — gold filigree, marble, champagne, oversaturated florals
- **Cliché stock subjects** — laughing women with salad, business handshakes, "diverse hands meeting"
- **Over-detailed composition** — too many objects, no breathing room
- **Wrong cultural reads** — generic "Asian" imagery that conflates cultures, kimono on a non-Japanese model, hanbok in a Tokyo setting

---

## Per-pillar visual templates

### Fashion

**Default approach:** Editorial fashion photography. Subject styled in a specific designer/brand piece. Environmental shot or moody portrait. Could be: a model walking through a quiet European street, a close-up of a hand holding a specific bag, a still-life of a styled outfit on a chair.

**Cultural specificity matters.** For Korean fashion pieces, lean Korean visual cues (hanbok-inspired silhouettes, Seoul cityscape suggestion). For Japanese, lean Japanese cues. Don't blur cultures.

**Sample prompt:**
> Editorial fashion photography. A young Korean woman in her late twenties wearing a deconstructed black avant-garde silhouette in soft Songzio-style draping, photographed in a Seoul gallery interior with concrete walls and a single shaft of late afternoon light. Negative space to the left. Shot on medium format film, slight grain, warm tones, moody. Vogue Korea aesthetic. Composition: 3/4 portrait, subject looking away from camera, contemplative. 1200x675.

### Beauty

**Default approach:** Hero ingredient or product still-life. Soft, considered light. Often close-cropped to show texture. Or: a hand-and-product editorial shot.

For ingredient-focused pieces: a still-life of the raw ingredient itself (centella leaves, propolis comb, jeju green tea, Korean rice grains) styled minimally.

For product-focused pieces: the actual product (when known) in editorial composition with negative space.

For brand-focused pieces: a packaging detail or brand-aesthetic still-life.

**Sample prompt:**
> Editorial beauty still-life. A single glass bottle of K-beauty essence on a bone-colored linen surface, soft window light from the left, slight droplet of essence on the bottle's surface. A sprig of fresh centella leaves placed asymmetrically. Cream and pale-green tones. Close composition, intentional crop, negative space upper-right. Slight grain, magazine quality. Allure / Glossy aesthetic. 1200x675.

### Travel

**Default approach:** Atmospheric destination photography. Architecture detail, interior space, environmental moment. Not the obvious touristed angle.

For hotels: a specific room/space at golden hour, or a detail (a hand on tea pot, slippers by door). Never the full-frontal exterior shot.

For destinations: a quiet street, a market interior, a temple detail. Locals' angle, not tourist angle.

**Sample prompt:**
> Editorial travel photography. The Aman Kyoto Tower Suite interior at dawn — a low Japanese platform bed, raw cedar walls, a single shaft of light through a paper screen revealing a moss garden beyond. Empty room, no people. Neutral palette: bone, cedar, moss green. Soft morning light, slight haze. Composition: room frames the moss garden view as a focal point. Negative space upper-left. Condé Nast Traveler / Mr Hudson aesthetic. 1200x675.

### Culture

**Default approach:** Cultural reportage photography. Atelier interiors, hands-at-work shots, heritage-object close-ups. Documentary-editorial register.

For atelier pieces: hands working with material (silk, leather, lacquer, metal). Implied skill, no faces necessary.

For designer profiles: portrait if a specific designer, environmental otherwise.

**Sample prompt:**
> Editorial documentary photography. The hands of a Kyoto kimono atelier artisan, painting fine detail on a silk panel with a single horsehair brush, photographed in soft north-facing window light. Warm wooden workbench, scattered brushes and pigments in handmade ceramic dishes. Close composition, depth of field shallow, focus on the brushstroke. Negative space to the right. NY Times T Magazine aesthetic. 1200x675.

### Lifestyle / Wellness

**Default approach:** Quiet, considered, anti-influencer aesthetic. NOT the bright "wellness routine" tableau. Instead: a single object in considered light, a simple moment, an atmospheric scene.

For fasting pieces: a glass of water on a wooden table at golden hour. A simple bowl of broth. An empty plate.

For longevity pieces: an aging hand, a quiet morning ritual, a sunlit window.

**Sample prompt:**
> Editorial still-life. A simple ceramic bowl of clear broth on a worn wooden table, photographed in late afternoon golden light. A single sprig of dried herb beside the bowl. Warm, contemplative palette: cream, ochre, soft wood tones. Composition: bowl off-center to the right, negative space upper-left where light pools. Subtle steam rising. Magnum Photos / Kinfolk aesthetic, but quieter. 1200x675.

### Sustainability / Design

**Default approach:** Materials and craft. Texture-focused. Quiet, considered.

Raw materials (Sea Island cotton, vicuña fleece, hand-loomed silk) in studio compositions. Or finished objects with implied longevity (a worn leather bag, an heirloom textile).

**Sample prompt:**
> Editorial materials photography. A folded length of natural-dyed hand-loomed Indonesian batik on a raw wood surface, photographed in soft directional window light. Earth-tone palette: indigo, ochre, cream. Texture-forward composition, slight depth of field. Negative space to the left. Wallpaper* magazine aesthetic. 1200x675.

---

## Prompt structure framework

Every prompt follows this template:

```
[Genre / register] — [Subject] [in/on/with] [Specific context and styling].
[Lighting condition] [from direction] [revealing/casting/illuminating] [specific detail].
[Palette description: 3-4 specific colors/tones].
[Composition direction: where subject sits, what's framed, what's blurred].
Negative space [direction].
[Texture/grain note].
[Reference aesthetic: specific magazine or photographer].
[Dimensions]: 1200x675.
```

Each line is a specific instruction. The detail level is what separates editorial output from generic AI sheen.

---

## What to avoid in prompts

### Bad prompt patterns

❌ "A beautiful luxury fashion image"
- Too generic. AI defaults to maximalist stock-look.

❌ "Stunning Korean fashion photography"
- "Stunning" produces AI maximalism. Drop the adjective.

❌ "Asian woman in traditional clothing"
- Too vague. Cultures conflate. Ages, ethnicities, contexts blur.

❌ "Luxury bag on marble"
- Stock-photo trope. Marble is overdone. Bags don't sit on marble in real editorial.

❌ "Modern minimalist composition"
- These adjectives are AI-noise. Be specific about composition.

### Specific words to avoid

- "stunning" / "iconic" / "amazing"
- "luxurious" (instead: "considered", "quiet", "specific brand")
- "vibrant" (we don't do vibrant)
- "happy" / "joyful" (we don't do that register)
- "modern" (too vague — what does modern mean in this context?)
- "trendy"

### Cultural specifics to nail

- **Korean** vs **Japanese** vs **Chinese** vs **Vietnamese** vs **Singaporean** — all distinct visual languages. Don't blur them.
- **Hanbok** is not kimono is not qipao. If a piece references Korean traditional dress, specify hanbok.
- **Singapore** specific: HDB blocks, shophouses, Tiong Bahru, Joo Chiat — name the specific architectural register.
- **Tokyo** specific: cedar interiors, paper screens (shoji), low platforms, tatami — specify the visual register.

---

## Alt text generation

Featured image alt text:
- Descriptive of the actual image content (for accessibility)
- ≤125 chars
- Includes primary keyword naturally
- NOT a CTA or promotional language

Example:
- Article: "The Quiet Renaissance of Korean Heritage Brands"
- Alt: "Korean fashion designer collection on display in Seoul gallery interior" (66 chars)

OR

- Alt: "Editorial portrait in Songzio-inspired draped silhouette, Seoul cityscape behind" (80 chars)

---

## Dimensions and format

Featured image standard for arahkaii.com:

- **Aspect ratio:** 16:9 (1200×675)
- **File size target:** <200KB after upload (Cloudflare/Hostinger will compress)
- **Format:** JPG for photographic content, PNG only if transparency is needed (rare for featured)
- **Color space:** sRGB

The prompt should specify "1200x675" at the end. AI Engine respects dimensions when set.

---

## Calling arahkaii:mwai_image

The arahkaii MCP exposes `mwai_image` which generates AND uploads in one call.

Call structure:

```
arahkaii:mwai_image(
  message: "<the full prompt from this skill>",
  title: "<article title - hyphenated slug optional>",
  caption: "",  // usually empty for featured images
  description: "<article title>",
  alt: "<alt text from this skill>",
  postId: <optional - omit, attach separately after>
)
```

Returns: `{ id, url, title, caption, alt }`

Then attach as featured:
```
arahkaii:wp_set_featured_image(
  post_id: <post_id>,
  media_id: <returned id>
)
```

---

## Quality check before saving

After generation, before attaching:

1. **Does it look editorial?** Or does it look like generic AI?
2. **Cultural specifics correct?** Right tradition, right setting?
3. **Color palette in arahkaii register?** Not garish, not maximalist?
4. **Composition has breathing room?** Negative space for text overlay?
5. **No obvious AI tells?** No weird hands, fused fingers, melting eyes?

If any check fails, regenerate with a refined prompt. AI image generation is iterative — don't accept the first output if it doesn't meet the bar.

Typically 1-3 generations to land a usable image. For high-stakes pieces (cornerstone), budget 5+ attempts.

---

## Output format

Return:

```
PROMPT:
<full detailed prompt per the framework above>

ALT TEXT:
<descriptive alt, ≤125 chars, includes keyword naturally>

DIMENSIONS:
1200x675

REFERENCE AESTHETIC:
<e.g., "Vogue Korea editorial", "NY Times T Magazine reportage", "Wallpaper* materials feature">

NOTES FOR ROBERT:
<Any specific consideration — cultural sensitivity to check, alternative direction if first generation fails, suggestion for visual variation for social media derivatives>
```

---

## Iteration playbook

If the first generation doesn't land:

**Too generic / AI sheen** → Add more specific aesthetic references. Add film/grain specifications. Specify a real photographer or magazine.

**Wrong cultural read** → Tighten cultural specifics. Specify country, region, era, specific architectural cues.

**Composition flat** → Add negative space direction, focal point, depth-of-field instruction.

**Colors garish** → Specify the palette explicitly (3-4 colors). Add "neutral warm tones" or "muted palette."

**Too literal** → Move from explicit-subject to atmospheric-suggestion. "A woman wearing X" → "A folded length of X on a wooden table."

---

## Anti-cultural-flattening rules

For Asian-cultural-context pieces, get the specifics right:

- A piece on **Korean designers** → Korean visual cues (hanbok references, Seoul architecture). Not "Asian fashion."
- A piece on **C-beauty** → Chinese visual cues (TCM imagery, Chinese ceramic, traditional packaging). Not generic Asian beauty.
- A piece on **Singapore** → Singaporean cues (shophouses, HDB, Peranakan tile patterns where relevant). Not generic Southeast Asian.

The visual specificity supports the editorial argument. Cultural flattening in images undermines the cultural fluency the article claims.

---

*Skill maintained by Robert. Visual register tuned quarterly against actual Vogue Korea / NY Times T Magazine / Wallpaper* samples.*
