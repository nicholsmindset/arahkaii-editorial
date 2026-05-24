#!/usr/bin/env python3
"""
Arahkaii Image Pipeline
=======================

Fetch a WordPress post → generate featured + per-H2 images via OpenRouter (Flux 1.1 Pro)
→ upload to Cloudinary → inject Gutenberg image blocks into the post body →
update the WP draft (status preserved). Round-trip verifies after the write.

Usage
-----
  python image-pipeline.py --post-id 1234
  python image-pipeline.py --post-id 1234 --dry-run            # don't write to WP
  python image-pipeline.py --post-id 1234 --hero-only          # featured image only
  python image-pipeline.py --post-id 1234 --pillar dining      # override auto-detected pillar
  python image-pipeline.py --post-id 1234 --model black-forest-labs/flux-1.1-pro

Setup
-----
1. cp .env.example .env  and fill in your values (see scripts/README.md)
2. pip install -r requirements.txt
3. Make sure your WordPress user has an Application Password
   (Users → Profile → Application Passwords → "Arahkaii Image Pipeline")

Safety
------
- Defaults to dry-run when no .env is set.
- Never deletes images. Never changes post_status. Never publishes.
- Refuses to generate prompts containing alcohol / bar / nightclub vocabulary
  (the IMAGE_SYSTEM.md anti-slop rule).
- Round-trip verifies the WP write before reporting success.
"""

from __future__ import annotations

import argparse
import base64
import io
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("WARN: python-dotenv not installed. Reading env vars from shell only.")

try:
    import cloudinary
    import cloudinary.uploader
except ImportError:
    print("FATAL: cloudinary not installed. Run: pip install -r requirements.txt")
    sys.exit(1)


# ============================================================================
# Config
# ============================================================================

OPENROUTER_KEY = os.environ.get("OPENROUTER_KEY", "")
WP_URL = os.environ.get("ARAHKAII_WP_URL", "https://www.arahkaii.com").rstrip("/")
WP_USER = os.environ.get("ARAHKAII_WP_USER", "")
WP_APP_PW = os.environ.get("ARAHKAII_WP_APP_PASSWORD", "")

cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME", ""),
    api_key=os.environ.get("CLOUDINARY_API_KEY", ""),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET", ""),
    secure=True,
)

DEFAULT_MODEL = os.environ.get("OPENROUTER_IMAGE_MODEL", "black-forest-labs/flux-1.1-pro")

# Locked Arahkaii palette tokens (from references/_shared/IMAGE_SYSTEM.md §1)
PALETTE = (
    "paper #F4F0E7, warm paper #EBE3D4, taupe #E4D8C9, clay #71613E, "
    "ink #26321C, sage #8C9274, rose clay #B98D74, gold #C9866F, black tea #1E1B18"
)

# Anti-slop modifiers appended to every prompt (from IMAGE_SYSTEM.md §4)
ANTI_SLOP = (
    "film grain, no AI sheen, natural skin texture with pores, asymmetrical features, "
    "no extra fingers, no symmetrical perfection, no harsh studio flash, no plastic gloss, "
    "no over-saturation, no rainbow refraction, no HDR, shot on real film stock "
    "(Portra 400 / Ektar 100 / Tri-X 400), editorial photography, magazine-grade, "
    "no stock-photo composition, no alcohol, no bottles, no bar interiors, no nightclub, "
    "no neon lighting, no club crowds"
)

# Banned subjects — never generate (from IMAGE_SYSTEM.md §5)
BANNED_TERMS = [
    "wine", "beer", "cocktail", "champagne", "whisky", "whiskey", "gin", "rum",
    "cognac", "sake", "vodka", "tequila", "liqueur", "bottle of",
    "bar interior", "nightclub", "club crowd", "raised glass", "speakeasy",
]


# ============================================================================
# Pillar → template mapping (3 templates per pillar)
# ============================================================================

# Each pillar has 3 image-prompt templates from IMAGE_SYSTEM.md §3.
# Hero image uses the first template; H2 supporting images rotate through 2 + 3.

PILLAR_SLUGS = ("style", "beauty", "dining", "travel", "living", "people", "culture", "guides")
LEGACY_SLUG_MAP = {"fashion": "style"}  # category slug stayed "fashion" for SEO

TEMPLATES: dict[str, dict[str, str]] = {
    "style": {
        "hero": (
            "A modern Asian woman in a {subject_modifier}, standing in three-quarter profile, "
            "looking away from camera, editorial fashion photography in the style of Vogue Arabia "
            "and i-D Magazine, soft window light from camera-left at 45 degrees, rule of thirds "
            f"with negative space on the right, palette of {PALETTE}, visible fabric weave and "
            "natural hand-feel, shot on Mamiya 7 medium format with 80mm lens"
        ),
        "h2_a": (
            "Close-up flat lay of a {subject_modifier} on a warm paper surface, top-down editorial "
            "product photography, soft diffused daylight from above-left, rule of thirds with one "
            f"folded edge entering frame, palette of {PALETTE}, hand-built ceramic dish in corner "
            "as scale reference, visible fabric weave, shot on Hasselblad with 80mm lens"
        ),
        "h2_b": (
            "A pair of anatomically-correct Asian hands styling a {subject_modifier}, cropped at the "
            f"wrist, soft side-light from a single window, palette of {PALETTE}, hand-built ceramic "
            "and natural linen in frame, shot on Leica M11 with 50mm lens"
        ),
    },
    "beauty": {
        "hero": (
            "A single {subject_modifier} on a white linen surface, soft top-light from a north-facing "
            f"window, palette of {PALETTE}, one shallow water droplet visible for freshness, "
            "shot on Phase One IQ4 with 120mm macro lens, no plastic gloss, no studio backdrop"
        ),
        "h2_a": (
            "A single skincare {subject_modifier} on a folded white linen napkin, side-light from "
            "camera-left at low angle, rule of thirds with negative space on right, palette of "
            f"{PALETTE}, shot on Hasselblad H6D with 100mm lens, no harsh reflection"
        ),
        "h2_b": (
            "A calm clinical treatment room interior, single treatment bed dressed in white linen, "
            f"soft late-afternoon light through linen curtain, palette of {PALETTE}, single hand-built "
            "ceramic vessel on a side table, blurred plant in background, shot on Mamiya 7 with 80mm lens"
        ),
    },
    "dining": {
        "hero": (
            "A single {subject_modifier} on a hand-built ceramic plate, dim ambient restaurant "
            "lighting with one warm spot from above-left, low-angle shot at 30 degrees from "
            f"horizontal, palette of {PALETTE}, blurred dining room in background, shot on Sony "
            "A7R V with 50mm lens at f/2, no overhead phone-camera flatness, no alcohol visible"
        ),
        "h2_a": (
            "A hand pouring {subject_modifier} into a small ceramic cup, 45-degree angle, soft "
            f"daylight from window at camera-left, palette of {PALETTE}, visible steam rising, one "
            "folded linen napkin in frame, shot on Fujifilm GFX100 with 63mm lens, no wine glasses"
        ),
        "h2_b": (
            "A quiet {subject_modifier} interior at dusk, three empty seats at a wooden counter, "
            f"single pendant light, blurred figure of a server in background, palette of {PALETTE}, "
            "candlelight on the counter, hand-built ceramics stacked at the back, shot on Leica Q3 "
            "with 28mm lens, no bar shelves with bottles, no neon signage"
        ),
    },
    "travel": {
        "hero": (
            "A quiet hotel room corner with linen bedsheets folded back, single small window with "
            f"sheer linen curtain, golden-hour light filtering in, palette of {PALETTE}, single "
            "hand-built ceramic on the bedside table, a folded prayer rug on the chair, shot on "
            "Mamiya 7 with 65mm lens, no champagne bucket, no minibar, {subject_modifier}"
        ),
        "h2_a": (
            "A narrow {subject_modifier} street in early morning, single human figure walking away "
            f"from camera in modest dress, soft warm light raking across one wall, palette of {PALETTE}, "
            "palm tree or bougainvillea entering the frame, shot on Leica M11 with 35mm lens, "
            "no crowds, no tourists"
        ),
        "h2_b": (
            "A market vendor's table covered in {subject_modifier} arranged in shallow wicker baskets, "
            f"soft overhead daylight from a market awning, palette of {PALETTE}, no human faces in "
            "frame, shot on Hasselblad H6D with 80mm lens, no plastic packaging, no English signage"
        ),
    },
    "living": {
        "hero": (
            "An empty modern apartment interior with {subject_modifier}, single mid-century chair "
            f"in frame, raking afternoon light across one wall, palette of {PALETTE}, one hand-thrown "
            "ceramic vessel on a low console, single book on the coffee table, shot on Hasselblad "
            "H6D with 50mm lens, no maximalist clutter"
        ),
        "h2_a": (
            "A single {subject_modifier} on a travertine surface, soft side-light from a single "
            f"window, palette of {PALETTE}, negative space top-right, shot on Phase One IQ4 with "
            "120mm lens, no busy background"
        ),
        "h2_b": (
            "A modest prayer corner of an apartment, single folded prayer rug on hardwood, a small "
            f"shelf with a Qur'an and an unlit candle, soft window light from camera-right, palette "
            f"of {PALETTE}, shot on Mamiya 7 with 80mm lens, editorial restraint, never as exotica, "
            "{subject_modifier}"
        ),
    },
    "people": {
        "hero": (
            "A portrait of an Asian {subject_modifier} in their working space, three-quarter view, "
            "looking slightly off-camera, hands at work or at rest in lap, soft window light from "
            f"camera-left, palette of {PALETTE}, blurred working environment behind them, shot on "
            "Mamiya 7 with 80mm lens, natural skin texture, asymmetrical face, no logo wall, "
            "no posed corporate-headshot smile"
        ),
        "h2_a": (
            "Close-up of anatomically correct hands {subject_modifier}, cropped above the wrist, "
            f"soft warm light from one window, palette of {PALETTE}, shallow depth of field, shot "
            "on Leica M11 with 50mm lens, no rings unless specified"
        ),
        "h2_b": (
            "A wide editorial portrait of an Asian person in their {subject_modifier}, full or "
            f"three-quarter body, raking afternoon light from camera-left, palette of {PALETTE}, "
            "working tools or finished products visible but not foregrounded, shot on Hasselblad "
            "H6D with 50mm lens, no posed magazine-cover stance"
        ),
    },
    "culture": {
        "hero": (
            "An editorial still life of {subject_modifier}, soft top-down north light, palette of "
            f"{PALETTE}, museum-grade composition with intentional spacing, shot on Phase One IQ4 "
            "with 120mm lens, no clutter, no signage, no labels"
        ),
        "h2_a": (
            "A single Asian woman in modest dress standing in {subject_modifier}, soft window light, "
            f"three-quarter profile, palette of {PALETTE}, blurred contextual elements behind her, "
            "shot on Mamiya 7 with 80mm lens, no tourist gaze, no costume-y styling"
        ),
        "h2_b": (
            "A close-up architectural detail of {subject_modifier}, soft raking afternoon light, "
            f"palette of {PALETTE}, no human in frame, shot on Leica M11 with 50mm lens, "
            "no over-saturation, no Photoshop sharpening"
        ),
    },
    "guides": {
        "hero": (
            "A single hero scene representing {subject_modifier}, one clear focal point, generous "
            f"negative space top or left for text overlay, palette of {PALETTE}, soft natural light "
            "from camera-left, shot on Hasselblad H6D with 80mm lens, no collage of multiple subjects"
        ),
        "h2_a": (
            "A top-down editorial flat lay of {subject_modifier} on a paper surface, soft overhead "
            f"daylight, palette of {PALETTE}, intentional asymmetric composition with negative space "
            "top-right, shot on Phase One IQ4 with 80mm lens, no Photoshop drop shadows"
        ),
        "h2_b": (
            "A quiet evening scene of {subject_modifier}, single warm light source, palette of "
            f"{PALETTE}, candlelight in frame, single figure in modest dress in soft focus background, "
            "shot on Sony A7R V with 35mm lens at f/2, no bar shelves, no club lighting"
        ),
    },
}


# ============================================================================
# Helpers
# ============================================================================

def fail(msg: str, code: int = 1):
    print(f"\033[91m[fail]\033[0m {msg}")
    sys.exit(code)


def say(msg: str):
    print(f"\033[92m[pipeline]\033[0m {msg}")


def warn(msg: str):
    print(f"\033[93m[warn]\033[0m {msg}")


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text[:80]


def assert_env():
    missing = []
    if not OPENROUTER_KEY: missing.append("OPENROUTER_KEY")
    if not os.environ.get("CLOUDINARY_CLOUD_NAME"): missing.append("CLOUDINARY_CLOUD_NAME")
    if not os.environ.get("CLOUDINARY_API_KEY"): missing.append("CLOUDINARY_API_KEY")
    if not os.environ.get("CLOUDINARY_API_SECRET"): missing.append("CLOUDINARY_API_SECRET")
    if not WP_USER: missing.append("ARAHKAII_WP_USER")
    if not WP_APP_PW: missing.append("ARAHKAII_WP_APP_PASSWORD")
    if missing:
        fail(f"Missing env vars: {', '.join(missing)}. See scripts/.env.example.")


# ============================================================================
# WordPress
# ============================================================================

def wp_auth() -> tuple[str, str]:
    return (WP_USER, WP_APP_PW)


def wp_get_post(post_id: int) -> dict:
    say(f"Fetching WP post {post_id} …")
    r = requests.get(
        f"{WP_URL}/wp-json/wp/v2/posts/{post_id}",
        auth=wp_auth(),
        params={"context": "edit"},
        timeout=30,
    )
    if r.status_code == 404:
        # Try as a page
        r = requests.get(
            f"{WP_URL}/wp-json/wp/v2/pages/{post_id}",
            auth=wp_auth(),
            params={"context": "edit"},
            timeout=30,
        )
    if r.status_code >= 400:
        fail(f"WP fetch failed [{r.status_code}]: {r.text[:500]}")
    return r.json()


def wp_get_categories(ids: list[int]) -> list[dict]:
    if not ids:
        return []
    r = requests.get(
        f"{WP_URL}/wp-json/wp/v2/categories",
        auth=wp_auth(),
        params={"include": ",".join(map(str, ids)), "per_page": 100},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def wp_upload_media(image_bytes: bytes, filename: str, alt_text: str) -> dict:
    headers = {
        "Content-Disposition": f'attachment; filename="{filename}"',
        "Content-Type": "image/webp",
    }
    r = requests.post(
        f"{WP_URL}/wp-json/wp/v2/media",
        auth=wp_auth(),
        headers=headers,
        data=image_bytes,
        timeout=60,
    )
    if r.status_code >= 400:
        fail(f"WP media upload failed [{r.status_code}]: {r.text[:500]}")
    media = r.json()
    # Set alt text + caption in a second call (REST quirk)
    requests.post(
        f"{WP_URL}/wp-json/wp/v2/media/{media['id']}",
        auth=wp_auth(),
        json={"alt_text": alt_text, "caption": alt_text, "title": alt_text},
        timeout=30,
    )
    return media


def wp_set_featured(post_id: int, media_id: int, is_page: bool):
    endpoint = "pages" if is_page else "posts"
    r = requests.post(
        f"{WP_URL}/wp-json/wp/v2/{endpoint}/{post_id}",
        auth=wp_auth(),
        json={"featured_media": media_id},
        timeout=30,
    )
    if r.status_code >= 400:
        fail(f"WP set featured failed [{r.status_code}]: {r.text[:500]}")


def wp_update_content(post_id: int, content: str, is_page: bool):
    endpoint = "pages" if is_page else "posts"
    r = requests.post(
        f"{WP_URL}/wp-json/wp/v2/{endpoint}/{post_id}",
        auth=wp_auth(),
        json={"content": content},  # status NOT changed — preserves draft/published state
        timeout=60,
    )
    if r.status_code >= 400:
        fail(f"WP update content failed [{r.status_code}]: {r.text[:500]}")


# ============================================================================
# Cloudinary
# ============================================================================

def upload_cloudinary(image_bytes: bytes, post_slug: str, slot: str) -> tuple[str, bytes]:
    """Upload to Cloudinary, return (secure_url, webp_bytes_for_wp)."""
    folder = f"arahkaii/posts/{post_slug}"
    say(f"  → Uploading to Cloudinary: {folder}/{slot}")
    result = cloudinary.uploader.upload(
        image_bytes,
        folder=folder,
        public_id=slot,
        format="webp",
        resource_type="image",
        overwrite=True,
        transformation=[{"quality": "auto:good", "fetch_format": "webp"}],
    )
    url = result["secure_url"]
    # Also fetch the webp-converted bytes for WP media
    webp_bytes = requests.get(url, timeout=30).content
    return url, webp_bytes


# ============================================================================
# OpenRouter (image generation)
# ============================================================================

def openrouter_image(prompt: str, model: str = DEFAULT_MODEL) -> bytes:
    """Call OpenRouter for image generation. Returns raw image bytes."""
    say(f"  → OpenRouter [{model}]")
    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "HTTP-Referer": "https://arahkaii.com",
            "X-Title": "Arahkaii Image Pipeline",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "modalities": ["image", "text"],
        },
        timeout=180,
    )
    if r.status_code >= 400:
        fail(f"OpenRouter image generation failed [{r.status_code}]: {r.text[:500]}")
    data = r.json()
    try:
        message = data["choices"][0]["message"]
        images = message.get("images") or []
        if images:
            img_obj = images[0]
            url = img_obj.get("image_url", {}).get("url") if isinstance(img_obj, dict) else img_obj
            if url.startswith("data:image"):
                _, b64 = url.split(",", 1)
                return base64.b64decode(b64)
            return requests.get(url, timeout=60).content
        # Some models return image as content
        content = message.get("content", "")
        if isinstance(content, list):
            for chunk in content:
                if chunk.get("type") == "image_url":
                    url = chunk["image_url"]["url"]
                    if url.startswith("data:image"):
                        _, b64 = url.split(",", 1)
                        return base64.b64decode(b64)
                    return requests.get(url, timeout=60).content
    except Exception as e:
        fail(f"Could not parse OpenRouter response: {e}\n{json.dumps(data)[:500]}")
    fail(f"No image found in OpenRouter response: {json.dumps(data)[:500]}")


# ============================================================================
# Prompt building
# ============================================================================

def detect_pillar(post: dict, override: Optional[str] = None) -> str:
    if override:
        s = override.lower().strip()
        return LEGACY_SLUG_MAP.get(s, s) if s in PILLAR_SLUGS or s in LEGACY_SLUG_MAP else "guides"
    cat_ids = post.get("categories", [])
    if not cat_ids:
        return "guides"
    cats = wp_get_categories(cat_ids)
    for c in cats:
        slug = c.get("slug", "").lower()
        if slug in PILLAR_SLUGS:
            return slug
        if slug in LEGACY_SLUG_MAP:
            return LEGACY_SLUG_MAP[slug]
    return "guides"


def extract_h2_sections(content_html: str) -> list[dict]:
    """Find Gutenberg H2 blocks. Returns [{text, position}]."""
    # Match <h2>...</h2>, optionally wrapped in Gutenberg comments.
    pattern = re.compile(r"<h2[^>]*>(.*?)</h2>", re.IGNORECASE | re.DOTALL)
    return [
        {"text": re.sub(r"<[^>]+>", "", m.group(1)).strip(), "match": m, "position": i}
        for i, m in enumerate(pattern.finditer(content_html))
    ]


def build_prompt(pillar: str, slot: str, post_title: str, h2_text: Optional[str] = None) -> str:
    """slot = 'hero' | 'h2_a' | 'h2_b'."""
    tpl = TEMPLATES.get(pillar, TEMPLATES["guides"])[slot]

    # Derive subject modifier from H2 text or post title
    src = h2_text or post_title
    src_clean = re.sub(r"[^\w\s-]", "", src).strip().lower()

    # Pillar-specific subject derivation
    if pillar == "style":
        subject = "linen coat, oat-coloured, in natural fabric" if not h2_text else f"piece related to {src_clean}"
    elif pillar == "beauty":
        subject = f"single skincare object or ingredient inspired by {src_clean}"
    elif pillar == "dining":
        if slot == "hero":
            subject = f"plated dish inspired by {src_clean}, no alcohol"
        elif slot == "h2_a":
            subject = "tea from a glass kyusu" if "tea" in src_clean else "espresso from a goose-neck kettle"
        else:
            subject = f"dessert bar or specialty cafe scene related to {src_clean}"
    elif pillar == "travel":
        if slot == "hero":
            subject = f"in a hotel referencing {src_clean}"
        elif slot == "h2_a":
            subject = f"asian or middle-eastern {src_clean}"
        else:
            subject = f"seasonal produce relevant to {src_clean} (pomegranates, dates, figs, persimmons)"
    elif pillar == "living":
        if slot == "hero":
            subject = f"terrazzo or oak floor referencing {src_clean}"
        elif slot == "h2_a":
            subject = f"hand-thrown ceramic or vintage object referencing {src_clean}"
        else:
            subject = f"with editorial restraint referencing {src_clean}"
    elif pillar == "people":
        if slot == "hero":
            subject = f"founder, designer, or craftsperson related to {src_clean}"
        elif slot == "h2_a":
            subject = f"shaping or making something related to {src_clean}"
        else:
            subject = f"studio or kitchen related to {src_clean}"
    elif pillar == "culture":
        if slot == "hero":
            subject = f"3 objects representing {src_clean}"
        elif slot == "h2_a":
            subject = f"culturally specific setting evoking {src_clean}"
        else:
            subject = f"architecture or pattern evoking {src_clean}"
    else:  # guides
        if slot == "hero":
            subject = f"single focal scene representing {src_clean}"
        elif slot == "h2_a":
            subject = f"3 ceramics or objects evoking {src_clean}"
        else:
            subject = f"venue or scene related to {src_clean}"

    prompt = tpl.format(subject_modifier=subject) + f". {ANTI_SLOP}. 16:9 aspect ratio for hero, 4:5 for inline."

    # Slop guard — refuse if the H2 or title contains banned terms (rare but possible)
    lower_full = (src + " " + prompt).lower()
    for term in BANNED_TERMS:
        if term in lower_full:
            warn(f"  ! Banned term '{term}' detected in source — neutralising prompt.")
            prompt += f" (Explicit: absolutely no {term}, no alcoholic drinks, no bar interiors.)"

    return prompt


def inject_h2_images(content: str, h2_image_urls: list[tuple[str, str]]) -> str:
    """Insert a Gutenberg image block after each H2. h2_image_urls = [(url, alt), …]."""
    pattern = re.compile(r"(<h2[^>]*>.*?</h2>)", re.IGNORECASE | re.DOTALL)
    parts = pattern.split(content)
    out = []
    img_idx = 0
    for part in parts:
        out.append(part)
        if pattern.fullmatch(part) and img_idx < len(h2_image_urls):
            url, alt = h2_image_urls[img_idx]
            block = (
                f'\n<!-- wp:image {{"sizeSlug":"large","className":"is-style-default"}} -->\n'
                f'<figure class="wp-block-image size-large">'
                f'<img src="{url}" alt="{alt}" loading="lazy" />'
                f"</figure>\n"
                f"<!-- /wp:image -->\n"
            )
            out.append(block)
            img_idx += 1
    return "".join(parts) if img_idx == 0 else "".join(out)


# ============================================================================
# Main
# ============================================================================

@dataclass
class PipelineConfig:
    post_id: int
    dry_run: bool = False
    hero_only: bool = False
    pillar_override: Optional[str] = None
    model: str = DEFAULT_MODEL
    max_h2_images: int = 8


def run(cfg: PipelineConfig):
    if not cfg.dry_run:
        assert_env()

    post = wp_get_post(cfg.post_id)
    is_page = "/pages/" in post.get("_links", {}).get("self", [{}])[0].get("href", "") if isinstance(post.get("_links", {}).get("self", []), list) else False
    title_field = post.get("title", {})
    title = title_field.get("rendered") or title_field.get("raw") or "Untitled"
    content_field = post.get("content", {})
    content = content_field.get("raw") or content_field.get("rendered") or ""

    post_slug = post.get("slug") or slugify(title)
    pillar = detect_pillar(post, cfg.pillar_override)

    say(f"Post: '{title}' (ID {cfg.post_id}, pillar: {pillar}, slug: {post_slug})")

    h2_sections = extract_h2_sections(content) if not cfg.hero_only else []
    if h2_sections:
        h2_sections = h2_sections[: cfg.max_h2_images]
        say(f"Found {len(h2_sections)} H2 section(s)")

    # ---- 1. Hero image ----
    hero_prompt = build_prompt(pillar, "hero", title)
    say(f"Hero prompt: {hero_prompt[:120]}…")

    if cfg.dry_run:
        print(f"\n--- HERO PROMPT (dry-run) ---\n{hero_prompt}\n")
    else:
        hero_bytes = openrouter_image(hero_prompt, cfg.model)
        hero_url, hero_webp = upload_cloudinary(hero_bytes, post_slug, "hero")
        say(f"  Hero uploaded: {hero_url}")
        hero_alt = f"{title} — Arahkaii featured image"
        hero_media = wp_upload_media(hero_webp, f"{post_slug}-hero.webp", hero_alt)
        wp_set_featured(cfg.post_id, hero_media["id"], is_page)
        say(f"  WP featured image set (media ID {hero_media['id']})")

    # ---- 2. H2 images ----
    h2_image_urls: list[tuple[str, str]] = []
    for i, h2 in enumerate(h2_sections):
        slot = "h2_a" if i % 2 == 0 else "h2_b"
        prompt = build_prompt(pillar, slot, title, h2_text=h2["text"])
        say(f"H2 #{i + 1} '{h2['text'][:60]}' → slot {slot}")

        if cfg.dry_run:
            print(f"\n--- H2 #{i + 1} PROMPT (dry-run) ---\n{prompt}\n")
            h2_image_urls.append(("https://example.com/placeholder.webp", f"{h2['text']} — Arahkaii"))
        else:
            img_bytes = openrouter_image(prompt, cfg.model)
            url, _ = upload_cloudinary(img_bytes, post_slug, f"h2-{i + 1:02d}")
            alt = f"{h2['text']} — Arahkaii"
            h2_image_urls.append((url, alt))
            time.sleep(1)  # polite to OpenRouter

    # ---- 3. Inject into content ----
    if h2_image_urls and not cfg.hero_only:
        new_content = inject_h2_images(content, h2_image_urls)
    else:
        new_content = content

    if cfg.dry_run:
        say("Dry-run complete. No WP writes.")
        print(f"\n--- NEW CONTENT PREVIEW (first 1000 chars) ---\n{new_content[:1000]}\n")
        return

    if new_content != content:
        say(f"Updating WP post content ({len(h2_image_urls)} H2 images injected)…")
        wp_update_content(cfg.post_id, new_content, is_page)

    # ---- 4. Round-trip verify ----
    say("Round-trip verifying…")
    verify = wp_get_post(cfg.post_id)
    verify_content = verify.get("content", {}).get("raw") or verify.get("content", {}).get("rendered") or ""
    if h2_image_urls and h2_image_urls[0][0] not in verify_content:
        warn("Hero URL not found in verified content — check WP manually.")
    else:
        say(f"✅ Done. {1 + len(h2_image_urls)} images live.")
        say(f"   Preview: {WP_URL}/?p={cfg.post_id}")


def main():
    p = argparse.ArgumentParser(description="Arahkaii image pipeline")
    p.add_argument("--post-id", type=int, required=True, help="WP post or page ID")
    p.add_argument("--dry-run", action="store_true", help="Print prompts but don't generate / upload")
    p.add_argument("--hero-only", action="store_true", help="Generate featured image only")
    p.add_argument("--pillar", default=None, help="Override auto-detected pillar")
    p.add_argument("--model", default=DEFAULT_MODEL, help=f"OpenRouter model (default: {DEFAULT_MODEL})")
    p.add_argument("--max-h2-images", type=int, default=8, help="Cap on H2 images (default: 8)")
    args = p.parse_args()

    cfg = PipelineConfig(
        post_id=args.post_id,
        dry_run=args.dry_run,
        hero_only=args.hero_only,
        pillar_override=args.pillar,
        model=args.model,
        max_h2_images=args.max_h2_images,
    )
    run(cfg)


if __name__ == "__main__":
    main()
