# Arahkaii Image System — moodboard-locked, anti-AI-slop

> *Every AI-generated or stock image used on Arahkaii must pass this system. The goal is to look like editorial photography from a real magazine — not "AI generated lifestyle".*

Loaded by `arahkaii-featured-image-prompt`, `arahkaii-social-media-creator`, `arahkaii-publisher`, `arahkaii-editorial-reviewer`.

---

## 1. THE LOCKED PALETTE

Every image must read in one of these palette families. If the dominant colours fall outside, reject and regenerate.

| Token | Hex | Use |
|---|---|---|
| Paper | `#F4F0E7` | Background, walls, linen, plates |
| Warm Paper | `#EBE3D4` | Warmer wall, fabric, paper |
| Taupe | `#E4D8C9` | Mid-tone walls, raw wood, terracotta tile |
| Clay | `#71613E` | Earthenware ceramics, brushed brass, leather |
| Ink | `#26321C` | Deep olive accent, foliage, fabric |
| Sage | `#8C9274` | Plant tones, dried herbs, ceramics |
| Rose Clay | `#B98D74` | Skin tones, terracotta, dried roses |
| Gold | `#C9866F` | Warm metallic, candlelight, golden hour |
| Black Tea | `#1E1B18` | Black accent, dark wood, low-light scenes |

**Banned colours:** neon, electric blue, primary red, primary yellow, hot pink, lime green, fluorescent anything. Even as small accents.

**Forbidden lighting:** harsh overhead fluorescent · ring-light glare · over-saturated HDR · "magic hour" beach photos with sun flares · nightclub lasers · bar mood lighting (red/purple wash).

---

## 2. THE 8 ANTI-SLOP RULES (every image must pass)

1. **No "AI sheen"** — that plasticky, over-smooth, slightly-melted quality. Force grain, film texture, or imperfect surface.
2. **No floating fingers, six-fingered hands, or extra limbs.** Reject any image with hands unless the hands are anatomically correct.
3. **No symmetrical perfection on faces.** Editorial faces have asymmetry, pores, real skin texture.
4. **No generic "wellness woman in a robe with a green smoothie".** No "businesswoman with a folder smiling at the camera". No "happy diverse group laughing over salad". These are AI-slop and stock-slop tells.
5. **No cluttered compositions.** Editorial = negative space. If you can't see at least 30% of the frame as breathing room, it's too busy.
6. **Composition follows rule of thirds, never centred mug-shot framing** (unless it's an intentional portrait with editorial styling).
7. **No text in the image.** All text overlays are done in post (Canva/Figma).
8. **One subject focus per image.** Multiple competing focal points = scroll-past.

---

## 3. CATEGORY-LOCKED PROMPT TEMPLATES

Each pillar has 3 locked prompt patterns. Use these as the base, then swap the bracketed variables. **Do not invent new patterns** — that's where slop creeps in.

The structure for every prompt:
```
[Subject + scene], [Style anchor], [Light direction], [Composition], [Palette], [Texture], [Camera/lens], [Anti-slop modifiers]
```

---

### 3.1 STYLE pillar — 3 templates

**S1 — Modest fashion editorial portrait**
```
A modern Asian woman in a [colour] [garment: linen coat / abaya / wool blazer / silk hijab], standing in three-quarter profile, looking away from camera, editorial fashion photography in the style of Vogue Arabia and i-D Magazine, soft window light from camera-left at 45 degrees, rule of thirds composition with negative space on the right, palette of warm paper, taupe and clay, visible fabric weave and natural hand-feel, shot on Mamiya 7 medium format with 80mm lens, film grain, slightly desaturated, no harsh shadows, no AI sheen, natural skin texture with pores, asymmetrical features
```

**S2 — Garment detail / flat lay**
```
Close-up flat lay of a [garment / accessory] on a [warm paper / linen / raw cotton] surface, top-down editorial product photography, soft diffused daylight from above-left, rule of thirds composition with one folded edge entering frame, palette of paper, taupe, sage, hand-built ceramic dish in corner as scale reference, visible fabric weave, shot on Hasselblad with 80mm lens, film grain, no plastic sheen, no shadow dropoff
```

**S3 — Modest luxury still life with hands**
```
A pair of anatomically-correct Asian hands [holding / folding / styling] a [garment / piece of jewellery], cropped at the wrist, soft side-light from a single window, palette of paper, clay and gold, hand-built ceramic and natural linen in frame, shot on Leica M11 with 50mm lens, film grain, no extra fingers, no rings unless specified, no plastic skin
```

---

### 3.2 BEAUTY pillar — 3 templates

**B1 — Clinical ingredient still life**
```
A single [ingredient: salmon fillet / sliced pomegranate / date / centella leaf / cucumber] on a [white linen / pale ceramic / brushed marble] surface, soft top-light from a north-facing window, palette of paper and rose clay, one shallow water droplet visible for freshness, shot on Phase One IQ4 with 120mm macro lens, film grain, no plastic gloss, no over-saturation, no studio backdrop
```

**B2 — Product on porcelain**
```
A single [skincare bottle / serum dropper / cream jar] on a [folded white linen napkin / hand-built ceramic dish / marble slab], side-light from camera-left at low angle, rule of thirds composition with negative space on right, palette of paper, warm paper and gold, shot on Hasselblad H6D with 100mm lens, soft film grain, no harsh reflection, no rainbow refraction, no AI sheen
```

**B3 — Treatment room scene**
```
A calm clinical treatment room interior, single treatment bed dressed in white linen, soft late-afternoon light through linen curtain, palette of paper, taupe, sage, single hand-built ceramic vessel on a side table, blurred plant in background, shot on Mamiya 7 with 80mm lens, slightly desaturated film stock, no medical-stock-photo people, no smiling practitioner, no clinical-blue tones
```

---

### 3.3 DINING pillar — 3 templates

**D1 — Single plate, dim restaurant**
```
A single [dish: bowl of rice / piece of plated fish / dessert with edible flower] on a hand-built ceramic plate, dim ambient restaurant lighting with one warm spot from above-left, low-angle shot at 30 degrees from horizontal, palette of warm paper, clay and black tea, blurred dining room in background, shot on Sony A7R V with 50mm lens at f/2, slight film grain, no harsh flash, no overhead phone-camera flatness, no alcohol visible
```

**D2 — Tea or coffee ritual**
```
A hand pouring [tea from a glass kyusu / hot coffee from a goose-neck kettle] into a small [ceramic cup / matcha bowl], top-down or 45-degree angle, soft daylight from window at camera-left, palette of paper, sage and clay, visible steam rising, one folded linen napkin in frame, shot on Fujifilm GFX100 with 63mm lens, slightly desaturated, no plastic sheen, no extra hands, no wine glasses anywhere
```

**D3 — Dessert bar / specialty café interior**
```
A quiet dessert bar interior at dusk, three empty seats at a wooden counter, single pendant light, blurred figure of a server in background, palette of black tea, clay and gold, candlelight on the counter, hand-built ceramics stacked at the back, shot on Leica Q3 with 28mm lens, film grain, no bar shelves with bottles, no neon signage, no crowds
```

---

### 3.4 TRAVEL pillar — 3 templates

**T1 — Hotel room corner at dawn**
```
A quiet hotel room corner with linen bedsheets folded back, single small window with sheer linen curtain, golden-hour light filtering in, palette of paper, warm paper and gold, single hand-built ceramic on the bedside table, a folded prayer rug on the chair, shot on Mamiya 7 with 65mm lens, film grain, no extravagant bouquet, no champagne bucket, no minibar
```

**T2 — Empty narrow street at 7am**
```
A narrow [Asian / Mediterranean] street in early morning, single human figure walking away from camera in modest dress, soft warm light raking across one wall, palette of paper, clay and sage, palm tree or bougainvillea entering the frame, shot on Leica M11 with 35mm lens, film grain, no crowds, no tourists, no signage in English
```

**T3 — Market produce still life**
```
A market vendor's table covered in [seasonal produce: pomegranates / dates / figs / mangoes / persimmons] arranged in shallow wicker baskets, soft overhead daylight from a market awning, palette of rose clay, sage and paper, no human faces in frame, shot on Hasselblad H6D with 80mm lens, soft film grain, no plastic packaging, no price tags in English
```

---

### 3.5 LIVING pillar — 3 templates

**L1 — Quiet apartment interior**
```
An empty modern apartment interior with [terrazzo / oak / travertine] floor, single mid-century chair in frame, raking afternoon light across one wall, palette of paper, taupe and clay, one hand-thrown ceramic vessel on a low console, single book on the coffee table, shot on Hasselblad H6D with 50mm lens, slightly desaturated, no maximalist clutter, no Pinterest-style throw cushions
```

**L2 — Single design object**
```
A single [hand-thrown ceramic vessel / vintage stool / brass bowl] on a [travertine / linen / paper] surface, soft side-light from a single window, palette of warm paper, clay and gold, negative space top-right, shot on Phase One IQ4 with 120mm lens, film grain, no styled prop noise around the object, no busy background
```

**L3 — Prayer corner / quiet room**
```
A modest prayer corner of an apartment, single folded prayer rug on hardwood, a small shelf with a Qur'an and a candle (unlit), soft window light from camera-right, palette of paper, sage and clay, shot on Mamiya 7 with 80mm lens, film grain, treated with editorial restraint — never as exotica or styled performance, no calligraphy props that look performative
```

---

### 3.6 PEOPLE pillar — 3 templates

**P1 — Subject portrait in own space**
```
A portrait of an Asian [profession: pastry chef / designer / hotelier] in their [kitchen / studio / showroom], three-quarter view, looking slightly off-camera, hands at work or at rest in lap, soft window light from camera-left, palette of paper, warm paper and clay, blurred working environment behind them, shot on Mamiya 7 with 80mm lens, film grain, natural skin texture, asymmetrical face, no logo wall, no posed corporate-headshot smile
```

**P2 — Subject hands at work**
```
Close-up of an Asian [profession]'s anatomically correct hands [shaping dough / folding fabric / styling a dish / sketching], cropped above the wrist, soft warm light from one window, palette of warm paper, clay and rose clay, shallow depth of field, shot on Leica M11 with 50mm lens, film grain, no extra fingers, no rings unless specified
```

**P3 — Subject in studio environment, wide**
```
A wide editorial portrait of an Asian [profession] standing or sitting in their [studio / kitchen / showroom], full or three-quarter body, raking afternoon light from camera-left, palette of paper, taupe, sage and clay, working tools or finished products visible but not foregrounded, shot on Hasselblad H6D with 50mm lens, soft film grain, no posed magazine-cover stance
```

---

### 3.7 CULTURE pillar — 3 templates

**C1 — Object still life as cultural symbol**
```
An editorial still life of [3 objects representing the cultural moment: a hijab folded next to a watch, a stack of fashion books topped with a ceramic bowl, a prayer rug beside a designer shoe], soft top-down north light, palette of paper, clay and ink, museum-grade composition with intentional spacing, shot on Phase One IQ4 with 120mm lens, film grain, no clutter, no signage, no labels
```

**C2 — Single human figure with cultural context**
```
A single Asian woman in [modest dress] standing in a [culturally specific setting: a traditional teahouse, a calligraphy studio, a contemporary art gallery], soft window light, three-quarter profile, palette of paper, warm paper and clay, blurred contextual elements behind her, shot on Mamiya 7 with 80mm lens, film grain, no tourist gaze, no costume-y styling
```

**C3 — Architectural / cultural detail**
```
A close-up architectural detail [intricate latticework, a moss garden corner, a traditional doorframe, a handmade tile pattern], soft raking afternoon light, palette of paper, clay and ink, no human in frame, shot on Leica M11 with 50mm lens, film grain, no over-saturation, no Photoshop sharpening
```

---

### 3.8 GUIDES pillar — 3 templates

**G1 — Listicle hero image**
```
A single hero scene representing the [list topic: dining / dessert / travel / beauty], one clear focal point (a single plate / a single hotel room corner / a single product), generous negative space top or left for text overlay, palette of paper, warm paper and clay, soft natural light from camera-left, shot on Hasselblad H6D with 80mm lens, film grain, no collage of multiple subjects
```

**G2 — Service guide flat-lay**
```
A top-down editorial flat lay of [items relevant to the guide: 3 ceramics, a folded napkin, a sprig of greenery, a single product], on a [paper / linen / wood] surface, soft overhead daylight, palette of paper, sage and gold, intentional asymmetric composition with negative space top-right, shot on Phase One IQ4 with 80mm lens, film grain, no Photoshop drop shadows
```

**G3 — Evening edit scene**
```
A quiet evening scene [a dessert bar at dusk / a hotel lobby at 10pm / a tea house lit by lanterns], single warm light source, palette of black tea, clay, gold, candlelight in frame, single figure in modest dress in soft focus background, shot on Sony A7R V with 35mm lens at f/2, film grain, no bar shelves, no club lighting, no crowds, no glasses of alcohol
```

---

## 4. ANTI-SLOP MODIFIERS — append to every prompt

These are non-negotiable:

```
film grain, no AI sheen, natural skin texture with pores, asymmetrical features,
no extra fingers, no symmetrical perfection, no harsh studio flash,
no plastic gloss, no over-saturation, no rainbow refraction, no HDR,
shot on real film stock (Portra 400 / Ektar 100 / Tri-X 400),
editorial photography, magazine-grade, no stock-photo composition
```

Add **all of these** to every prompt's tail.

---

## 5. THE NEVER-IMAGES LIST

Reject any generated or stock image showing:

- Wine, beer, cocktail, champagne, whisky, gin, rum — bottles or glasses
- Bar interiors centred on liquor shelves
- Nightclub lighting, dance floors, neon
- "Raised glass" gestures (even with water — too "cheers" stock-feel)
- Generic "happy diverse women laughing over salad"
- Businesswoman-with-folder stock cliché
- "Wellness woman in robe holding green smoothie"
- White background product floats (Amazon-style)
- Stock-photo handshake / boardroom / pointing-at-laptop
- AI-generated humans with floating extra fingers
- Children, unless explicitly part of editorial context
- Logos of competitors visible in shot
- Anything that looks like a Canva template

---

## 6. PLATFORM SIZE TARGETS

| Use | Aspect ratio | Pixel dimensions |
|---|---|---|
| WordPress featured image | 16:9 | 1920 × 1080 |
| WordPress in-article | 4:5 | 1080 × 1350 |
| Instagram square | 1:1 | 1080 × 1080 |
| Instagram carousel | 4:5 | 1080 × 1350 |
| Instagram reel cover | 9:16 | 1080 × 1920 |
| Pinterest pin | 2:3 | 1000 × 1500 |
| LinkedIn share | 1.91:1 | 1200 × 627 |
| Newsletter hero | 16:9 | 1600 × 900 |

Always include `aspect ratio [X:Y]` in the prompt.

---

## 7. PROMPT VALIDATION CHECKLIST (before submitting to Midjourney / DALL-E / Imagen)

- [ ] Subject is named specifically (not "a woman" but "a modern Asian woman in a wool coat")
- [ ] Lighting direction is specified
- [ ] Palette is named (use the tokens above)
- [ ] Composition is specified (rule of thirds, negative space side)
- [ ] Camera + lens specified
- [ ] Film stock or grain specified
- [ ] Anti-slop modifiers appended (Section 4)
- [ ] No banned subject or palette
- [ ] Aspect ratio specified
- [ ] If hands are in frame, "anatomically correct hands, no extra fingers" included
- [ ] If face is in frame, "natural skin texture with pores, asymmetrical features" included

If any box is unchecked, the prompt fails. Rewrite.

---

## 8. THE 60-SECOND IMAGE REVIEW (after generation)

For every generated image, before using:

1. Open the image at full size. Does it look like editorial photography or like AI?
2. Are the hands and faces anatomically correct?
3. Is the palette inside the locked tokens?
4. Is there at least 30% breathing room (negative space)?
5. Is there any alcohol, club lighting, or banned subject?
6. Would this look at home in *Tatler Asia* or *Vogue Arabia*?
7. Is there grain / texture, or is it that smooth AI plasticness?

If any answer fails, **regenerate**. Don't ship slop.

---

*Loaded by: arahkaii-featured-image-prompt · arahkaii-social-media-creator · arahkaii-publisher (image generation step) · arahkaii-editorial-reviewer (image QA step).*
