---
name: arahkaii-image-pipeline
description: Auto-generate featured image + per-H2 supporting images for an arahkaii.com post using OpenRouter (Flux 1.1 Pro by default), upload to Cloudinary CDN, inject Gutenberg image blocks into the post body, and update the WordPress draft. Loads IMAGE_SYSTEM.md (24 locked templates), VOICE.md (pillar-specific imagery cues), and HALAL_SUBSTITUTIONS.md (banned subjects). Refuses to generate anything containing alcohol, bars, nightclubs, or banned-subject vocabulary. Use whenever Robert wants images on a drafted Arahkaii post — either manually after editorial-writer finishes, or as an automated step in a daily routine. Pairs upstream with arahkaii-editorial-writer and downstream with arahkaii-publisher.
---

# Arahkaii Image Pipeline

End-to-end image automation: editorial draft → OpenRouter Flux 1.1 Pro → Cloudinary → WordPress draft with images embedded.

## Step 0 — Load the foundation

1. `references/_shared/IMAGE_SYSTEM.md` — the 24 locked image-prompt templates + palette + anti-slop modifiers + never-images list
2. `references/_shared/VOICE.md` — pillar-specific imagery cues (each of the 8 pillars has its own visual language)
3. `references/_shared/HALAL_SUBSTITUTIONS.md` — banned imagery substitution rules

## Step 1 — Verify prerequisites

Before invoking the script:

- [ ] Post is already drafted via `arahkaii-editorial-writer` and exists in WP
- [ ] Post category is set to one of the 8 pillar slugs (or `fashion` legacy = Style)
- [ ] `scripts/.env` exists with valid `OPENROUTER_KEY`, `CLOUDINARY_*`, `ARAHKAII_WP_USER`, `ARAHKAII_WP_APP_PASSWORD`
- [ ] Python deps installed (`pip install -r scripts/requirements.txt`)

If any check fails, surface the failure — never proceed blind.

## Step 2 — Detect pillar + count H2s

The script auto-detects the pillar from the post's category. If the category is missing or unclear, override with `--pillar [slug]`.

It then extracts every `<h2>` block in the post content. By default it generates one image per H2, capped at 8 (use `--max-h2-images N` to override).

| Article length | H2 count (typical) | Image count | Cost @ $0.04 |
|---|---|---|---|
| Quick take 800–1,200 words | 2–3 | 3–4 | $0.12–$0.16 |
| Standard feature 1,800–2,200 words | 4–5 | 5–6 | $0.20–$0.24 |
| Long feature 2,200–2,800 words | 6–7 | 7–8 | $0.28–$0.32 |
| Cornerstone 2,800–3,500 words | 8–10 | 8 (capped) | $0.32 |

## Step 3 — Build prompts from locked templates

Each pillar has 3 templates (hero / h2_a / h2_b). The script fills the `{subject_modifier}` variable from the post title (hero) or each H2 text (supporting images), then appends:

1. **The Arahkaii palette tokens** (Paper, Warm Paper, Taupe, Clay, Ink, Sage, Rose Clay, Gold, Black Tea)
2. **The anti-slop modifier block** (film grain, no AI sheen, anatomically correct hands, no extra fingers, no symmetrical perfection, no plastic gloss, no over-saturation, real film stock — Portra 400 / Ektar 100 / Tri-X 400 — editorial photography, magazine-grade)
3. **Banned subject negatives** (no alcohol, no bottles, no bar interiors, no nightclub, no neon)
4. **Aspect ratio** (16:9 hero, 4:5 inline)

Templates are exact strings from `IMAGE_SYSTEM.md §3`. The script never invents prompt patterns — that's where AI-slop creeps in.

## Step 4 — Generate via OpenRouter

The script calls OpenRouter's chat completions endpoint with `modalities: ["image", "text"]` and the model `black-forest-labs/flux-1.1-pro` (default). Other supported models: `google/imagen-3`, `openai/gpt-image-1`, `stability-ai/stable-diffusion-3.5-large`.

Default: Flux 1.1 Pro. Best hands and faces of any current model. ~$0.04/image.

## Step 5 — Upload to Cloudinary

Each image lands at `arahkaii/posts/{post-slug}/{slot}.webp` with:

- `quality: auto:good`
- `fetch_format: webp` (small file size, fast CDN delivery)
- Folder structure: `arahkaii/posts/{post-slug}/hero.webp`, `h2-01.webp`, `h2-02.webp`, …

URLs are stable (overwrite mode), so regenerating an image keeps the same URL.

## Step 6 — Inject into post content

For each H2 section, the script inserts a Gutenberg image block immediately after:

```html
<!-- wp:image {"sizeSlug":"large","className":"is-style-default"} -->
<figure class="wp-block-image size-large">
  <img src="https://res.cloudinary.com/{cloud}/image/upload/.../h2-01.webp"
       alt="{H2 text} — Arahkaii"
       loading="lazy" />
</figure>
<!-- /wp:image -->
```

The hero image is uploaded to the WP media library and set as the **featured image** via `featured_media`.

## Step 7 — Update WP, preserve status

The script writes only `content` and `featured_media`. It **never** changes `status`. Drafts stay drafts. Published stays published.

## Step 8 — Round-trip verify

After write, re-fetch the post and confirm:
- Hero URL appears in content (if the hero is rendered inline; for featured-image-only the script confirms `featured_media` ID)
- All H2 image URLs are present in content

If verification fails → surface a clear error with the post URL, do not retry blindly.

## Step 9 — 60-second post-generation review

After the script reports success, **manually review every image** in the WP draft per `IMAGE_SYSTEM.md §8`:

1. Editorial photography look, or AI-look?
2. Hands and faces anatomically correct?
3. Palette inside the locked tokens?
4. At least 30% breathing room?
5. Any alcohol / club lighting / banned subject?
6. Would this look at home in *Tatler Asia* or *Vogue Arabia*?
7. Visible grain / texture, or smooth AI plasticness?

If any answer fails → re-run with a different model OR regenerate that one image manually via `arahkaii-featured-image-prompt`.

## Step 10 — Hand off to arahkaii-publisher

Once images pass review, the post is ready for the publisher pipeline (still a draft — never publishes autonomously). `arahkaii-publisher` does the final pre-publish gate.

---

## Hard rules

1. **Never auto-publish.** The script only writes `content` and `featured_media`. Post status is preserved.
2. **Never generate banned subjects.** Alcohol, bars, nightclubs, raised glasses, neon lighting — caught at prompt-build time and again at OpenRouter response time.
3. **Never invent prompt structures.** Only the 24 locked templates in IMAGE_SYSTEM.md §3.
4. **Always include the anti-slop modifier block.** Non-negotiable.
5. **Always specify camera + lens + film stock.** This is the strongest anti-AI-sheen lever.
6. **Always upload to Cloudinary, never directly to WP storage.** Keeps WP fast, lets us regenerate cheaply.
7. **Always round-trip verify** before reporting success.

## Manual invocation

```bash
cd scripts
python image-pipeline.py --post-id 1234              # standard run
python image-pipeline.py --post-id 1234 --dry-run    # see prompts, no API calls
python image-pipeline.py --post-id 1234 --hero-only  # featured image only
python image-pipeline.py --post-id 1234 --pillar dining --model google/imagen-3
```

See `scripts/README.md` for full CLI documentation.

## Automation (optional)

Add to `prompts/01-daily-draft.md` after the `arahkaii-publisher` step:

```
After the draft is created and post_id is captured, shell out:
  python scripts/image-pipeline.py --post-id ${DRAFT_POST_ID}

Wait for completion. If it fails, log to run-log.md but do not retry — image generation
failure is non-blocking (article still drafts successfully without images).
```

---

*Pairs upstream with: arahkaii-editorial-writer (drafts the post) + arahkaii-publisher (creates the WP draft we then add images to). Pairs downstream with: arahkaii-editorial-reviewer (image QA step) + arahkaii-publisher (final pre-publish gate). The actual implementation lives in scripts/image-pipeline.py.*
