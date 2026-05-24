# Arahkaii Image Pipeline

Auto-generate **featured image + per-H2 supporting images** for an Arahkaii WordPress post.

- **Image generation**: OpenRouter → Flux 1.1 Pro (defaults; swappable)
- **CDN hosting**: Cloudinary (`arahkaii/posts/{slug}/`)
- **Insertion**: Gutenberg image blocks injected after every H2
- **Featured image**: uploaded to WP media library, set as featured
- **Post status**: preserved (never auto-publishes)

> Pairs with: `skills/arahkaii-image-pipeline/SKILL.md` (the workflow doc) and `references/_shared/IMAGE_SYSTEM.md` (the 24 locked image templates this script implements).

---

## One-time setup (5 minutes)

### 1. Install Python deps

```bash
cd scripts
pip install -r requirements.txt
```

### 2. Create the env file

```bash
cp .env.example .env
```

Then open `.env` and fill in:

| Variable | Where to get it |
|---|---|
| `OPENROUTER_KEY` | https://openrouter.ai/keys → "Create Key" |
| `CLOUDINARY_CLOUD_NAME` | https://console.cloudinary.com/ → top-left, e.g. `db7dybii2` |
| `CLOUDINARY_API_KEY` | Console → Settings → API Keys |
| `CLOUDINARY_API_SECRET` | Console → Settings → API Keys |
| `ARAHKAII_WP_USER` | Your WP username (not email) |
| `ARAHKAII_WP_APP_PASSWORD` | See below ↓ |

### 3. Create the WordPress Application Password

In WP admin:

1. **Users → Profile** (your own user)
2. Scroll to **Application Passwords**
3. New Application Password Name → `Arahkaii Image Pipeline`
4. Click **Add New Application Password**
5. Copy the password it shows (format: `abcd efgh ijkl mnop qrst uvwx` — yes, with spaces, paste as-is)
6. WP will never show it again — paste straight into `.env`

This password is scoped to your user. Revoke any time from the same screen.

### 4. Verify the .env is gitignored

```bash
git check-ignore -v scripts/.env
# Should output: .gitignore:N:*.env  scripts/.env
```

The repo's `.gitignore` already excludes `.env` files. Double-check before committing anything.

---

## Usage

### Generate hero + per-H2 images for a post

```bash
python image-pipeline.py --post-id 1234
```

This fetches post 1234 from `arahkaii.com`, detects the pillar from its category, generates one hero image and one image per `<h2>` section, uploads everything to Cloudinary, injects Gutenberg image blocks into the post body, and updates the WP draft. Round-trip verifies before reporting success.

### Dry run (see prompts, no API calls)

```bash
python image-pipeline.py --post-id 1234 --dry-run
```

Prints every prompt that would be sent to OpenRouter. Useful for tuning before spending credits.

### Hero image only (cheaper)

```bash
python image-pipeline.py --post-id 1234 --hero-only
```

~$0.04 per article instead of ~$0.20.

### Override the auto-detected pillar

```bash
python image-pipeline.py --post-id 1234 --pillar dining
```

Useful for cross-pillar pieces or when the category isn't set yet.

### Swap models

```bash
python image-pipeline.py --post-id 1234 --model google/imagen-3
python image-pipeline.py --post-id 1234 --model openai/gpt-image-1
```

Default is `black-forest-labs/flux-1.1-pro` (best hands + faces for editorial photography).

### Cap H2 image count

```bash
python image-pipeline.py --post-id 1234 --max-h2-images 4
```

Useful for long pieces — caps cost.

---

## What gets generated

| Slot | Template | Aspect ratio | Where it lands |
|---|---|---|---|
| **Hero / featured** | Pillar `hero` template from IMAGE_SYSTEM.md §3 | 16:9 | WP media library + set as featured image |
| **H2 #1, #3, #5…** | Pillar `h2_a` template (flat lay / detail / hands) | 4:5 | Gutenberg image block, after each H2 |
| **H2 #2, #4, #6…** | Pillar `h2_b` template (scene / wider / contextual) | 4:5 | Gutenberg image block, after each H2 |

Every prompt automatically includes the **Arahkaii locked palette tokens** and the **anti-AI-slop modifier block** (film grain, no plastic gloss, no symmetrical faces, no extra fingers, no alcohol, etc.) from `references/_shared/IMAGE_SYSTEM.md`.

---

## Cost estimate

| Article type | Images | Cost (Flux 1.1 Pro @ $0.04) |
|---|---:|---:|
| Quick take (1 hero, 0 H2) | 1 | $0.04 |
| Standard feature (1 + 4 H2s) | 5 | $0.20 |
| Long feature (1 + 8 H2s) | 9 | $0.36 |
| Cornerstone (1 + 12 H2s) | 13 | $0.52 |

Plus Cloudinary free tier: 25 GB storage + 25 GB bandwidth/month — covers many years of Arahkaii growth.

---

## Pillar → template mapping

The script auto-detects the pillar from the WP category. Legacy `fashion` slug maps to `style`.

| Pillar slug in WP | Pillar in code | Hero template | H2_a | H2_b |
|---|---|---|---|---|
| `fashion` *(legacy)* / `style` | style | S1 portrait | S2 flat lay | S3 hands w/ garment |
| `beauty` | beauty | B1 ingredient still life | B2 product on porcelain | B3 treatment room |
| `dining` | dining | D1 single plate, dim | D2 tea / coffee ritual | D3 dessert bar interior |
| `travel` | travel | T1 hotel room corner | T2 narrow street 7am | T3 market produce |
| `living` | living | L1 apartment interior | L2 single design object | L3 prayer corner |
| `people` | people | P1 subject portrait | P2 hands at work | P3 subject in studio wide |
| `culture` | culture | C1 object still life | C2 figure + cultural context | C3 architectural detail |
| `guides` | guides | G1 listicle hero | G2 flat lay | G3 evening edit scene |

---

## Safety rails

The script will **refuse to generate** any image containing:

- Alcohol vocabulary (wine, beer, cocktail, champagne, whisky, gin, rum, cognac, sake, vodka, tequila, liqueur)
- "Bottle of [drink]", "bar interior", "nightclub", "raised glass", "speakeasy"
- Anything from the IMAGE_SYSTEM.md `§5 NEVER-IMAGES LIST`

If banned terms appear in the post's title or H2 (rare but possible), the script appends an explicit negative-prompt clarifier. If you see a `[warn]` line about a banned term during a run, regenerate the image manually after editing the H2.

---

## Pre-publish review (manual — 60 seconds per image)

Per `IMAGE_SYSTEM.md §8`. After the script runs, open the WP draft and for every image:

1. Open at full size. Does it look like editorial photography or AI?
2. Hands and faces anatomically correct?
3. Palette inside the locked tokens?
4. At least 30% breathing room (negative space)?
5. Any alcohol / club lighting / banned subject?
6. Would this look at home in *Tatler Asia* or *Vogue Arabia*?
7. Grain / texture, or smooth AI plasticness?

If any fails → re-run the pipeline with a different model, or regenerate that one image manually.

---

## Troubleshooting

### "Missing env vars"
You haven't created `.env` from `.env.example`. Run `cp .env.example .env` and fill it in.

### "OpenRouter image generation failed [401]"
Bad `OPENROUTER_KEY`. Get a new one from https://openrouter.ai/keys.

### "WP fetch failed [401]"
Bad `ARAHKAII_WP_USER` or `ARAHKAII_WP_APP_PASSWORD`. Application passwords use *username* not email. Re-create the app password in WP admin if unsure.

### "WP fetch failed [404]"
Wrong post ID, or the post is in trash. Try fetching it via `wp_get_posts` first.

### "No image found in OpenRouter response"
The model returned text instead of an image. Verify the model supports image generation:
- ✅ `black-forest-labs/flux-1.1-pro`
- ✅ `google/imagen-3`
- ✅ `openai/gpt-image-1`
- ❌ `anthropic/claude-*` (text only)

### Cloudinary "401 Unauthorized"
API secret is wrong, or the cloud name doesn't match the secret. Re-copy all three Cloudinary values from the console.

---

## What this script does NOT do

- ❌ Publish posts (status is always preserved — drafts stay drafts)
- ❌ Delete images (Cloudinary keeps the full history under `arahkaii/posts/{slug}/`)
- ❌ Edit text (only injects image blocks after H2s)
- ❌ Override existing featured images without overwriting (set as featured, replaces previous)
- ❌ Run on a schedule (it's a manual CLI script — pair with a routine prompt if you want automation)

---

## Triggering it from a Claude Code routine (optional)

If you want this to fire after every drafted article without manual intervention, add a step to `prompts/01-daily-draft.md` that shells out to this script:

```bash
python scripts/image-pipeline.py --post-id $DRAFT_POST_ID
```

The skill `skills/arahkaii-image-pipeline/SKILL.md` documents the full integration.

---

*Built 2026-05-24 as part of the brand revamp bundle.*
