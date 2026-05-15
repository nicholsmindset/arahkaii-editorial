---
name: blotato-social-distributor
description: Distribute published arahkaii.com articles across nine social platforms via the Blotato MCP. Use this skill whenever Robert wants to push an approved WordPress article to Instagram, LinkedIn, Pinterest, Twitter/X, Threads, Bluesky, Facebook, TikTok, or YouTube. Triggers on phrases like "distribute to social", "post to all platforms", "social rollout for [post]", "Blotato this article", "publish to socials", "carousel for [topic]", or any request that takes editorial output and adapts it across platforms. Pairs with arahkaii-publisher (which produces the WP post first), social-media-creator (which drafts platform-specific copy), and canva-social-publisher (for native Canva designs alongside Blotato distribution). Do NOT use for the initial WordPress publish — that's the publisher skill's job. This skill assumes the WP post is already live or being published as part of the same flow.
---

# Blotato Social Distributor

Bridge between a published arahkaii.com article and the nine social platforms Blotato supports. The Blotato API handles platform-specific authentication, media upload, rate limiting, and the different formatting requirements per platform — this skill orchestrates what to send and when.

---

## Setup (one-time)

### Blotato account requirements

1. **Paid plan required.** Free Trial does not include API access. Starter, Creator, or Agency plans all include it.
2. **Connect social accounts** at https://my.blotato.com/settings — at minimum: Instagram, LinkedIn, Pinterest, Twitter/X. Optional: Threads, Bluesky, Facebook, TikTok, YouTube.
3. **Warm up new accounts.** Any social account less than 4 weeks old will get shadowbanned if connected to automation immediately. Manual usage daily for 2-4 weeks first.
4. **Generate API key** at Settings > API. **WARNING: generating an API key immediately ends free trial and starts paid Starter subscription.**
5. **For Pinterest:** also note your Board ID manually — Blotato cannot retrieve it via API. Get it from the URL of any of your boards: `https://www.pinterest.com/<username>/<board-slug>/` → the board ID is visible in board settings.

### Environment variables

- `BLOTATO_API_KEY` — from step 4 above
- `BLOTATO_PINTEREST_BOARD_ID` — manual lookup per step 5

### MCP config

Already set in repo `.mcp.json`:
```json
{
  "blotato": {
    "command": "npx",
    "args": ["-y", "mcp-remote", "https://mcp.blotato.com/mcp"],
    "env": {
      "AUTH_HEADER": "blotato-api-key: ${BLOTATO_API_KEY}"
    }
  }
}
```

If working in Claude Code instead of cloud Routines, also add to local config:
```bash
claude mcp add blotato https://mcp.blotato.com/mcp --transport http --header "blotato-api-key: YOUR_KEY"
```

---

## Tool inventory (via MCP)

The Blotato MCP exposes the same operations as the REST API. Key tools:

- `blotato:list-accounts` — GET /v2/users/me/accounts (with optional platform filter)
- `blotato:list-subaccounts` — GET /v2/users/me/accounts/{accountId}/subaccounts (for FB Pages, LinkedIn Company Pages, YouTube playlists)
- `blotato:create-post` — POST /v2/posts (publish or schedule)
- `blotato:upload-media` — for local files when public URLs aren't available

If unsure of exact MCP tool names, fall back to direct REST calls via the documented endpoints. The MCP wraps the same API surface.

---

## Platform-by-platform reference

### Instagram

**Account ID resolution:** `blotato:list-accounts` filtered by `platform: "instagram"`. Use the returned `id` as `accountId`.

**Content rules:**
- Max 5 hashtags (more reduces reach)
- First line of caption is the hook — it's what shows in feed previews
- Image must be public URL (or upload via presigned URL)
- For carousels: 2-10 items, all cropped to first image's aspect ratio (default 1:1)
- For Reels: video, vertical 9:16, max 90 seconds for native discovery (Blotato will convert if needed, up to 120s)

**Post payload:**
```json
{
  "post": {
    "accountId": "<instagram_account_id>",
    "content": {
      "text": "<caption: hook line + 80-120 word teaser + soft CTA + 3-5 hashtags>",
      "mediaUrls": ["<featured image URL>"],
      "platform": "instagram"
    },
    "target": {
      "targetType": "instagram",
      "altText": "<alt text for accessibility, ≤1000 chars>"
    }
  }
}
```

**Carousel variant:** `mediaUrls` array with 2-10 items. All cropped to first image's aspect ratio.

**Rate limit:** 50 posts/day per account.

---

### LinkedIn

**Account ID resolution:** `list-accounts` filtered by `platform: "linkedin"`. For Company Page posting (not personal profile), also call `list-subaccounts` and use the page's ID as `pageId`.

**Content rules:**
- 3000 character limit
- NO hashtags (LinkedIn frowns on them, doesn't improve discovery)
- Long-form is rewarded — 800-1500 char posts often outperform short ones
- LinkedIn Document Carousels (PDF-based): 2-10 images, automatically built by Blotato when carousel is posted to LinkedIn

**Post payload:**
```json
{
  "post": {
    "accountId": "<linkedin_account_id>",
    "content": {
      "text": "<800-1500 char post in arahkaii voice, no hashtags>",
      "mediaUrls": ["<featured image URL>"],
      "platform": "linkedin"
    },
    "target": {
      "targetType": "linkedin",
      "pageId": "<company_page_id_or_omit_for_personal>"
    }
  }
}
```

**Voice note:** arahkaii LinkedIn voice is analytical and editorial — NOT LinkedIn-influencer-y. No "I have a confession", no "🚀 thread incoming", no false vulnerability hooks.

---

### Pinterest

**Account ID resolution:** `list-accounts` filtered by `platform: "pinterest"`.
**Board ID:** NOT retrievable via API. Use `BLOTATO_PINTEREST_BOARD_ID` env var.

**Content rules:**
- Title: ≤100 chars
- Description: ≤800 chars (Pinterest indexes this heavily — write it SEO-rich)
- Alt text: ≤800 chars
- URL link: ≤2048 chars
- Image: PNG or JPG, ≤20MB, recommended 1000x1500 (2:3 vertical)
- NO hashtags

**Post payload:**
```json
{
  "post": {
    "accountId": "<pinterest_account_id>",
    "content": {
      "text": "<description with keywords>",
      "mediaUrls": ["<vertical pin image URL>"],
      "platform": "pinterest"
    },
    "target": {
      "targetType": "pinterest",
      "boardId": "<board_id>",
      "title": "<pin title, ≤100 chars>",
      "altText": "<alt text>",
      "link": "<article URL>"
    }
  }
}
```

**Multi-variant strategy:** Generate 3 pins per article with different titles, angles, and (if Canva is available) different visual treatments. Pinterest favors fresh pins linking to the same URL.

**Rate limit:** 10 pins/day per account.

---

### Twitter / X

**Account ID resolution:** `list-accounts` filtered by `platform: "twitter"`.

**Content rules:**
- 280 character limit per post
- NO hashtags (don't help on X)
- Threads via `additionalPosts` array — each item is a separate tweet, each ≤280 chars
- Media: up to 4 images per tweet, or 1 video

**Thread post payload:**
```json
{
  "post": {
    "accountId": "<twitter_account_id>",
    "content": {
      "text": "<hook tweet ≤280 chars>",
      "mediaUrls": ["<featured image URL>"],
      "platform": "twitter",
      "additionalPosts": [
        { "text": "<tweet 2 ≤280 chars>", "mediaUrls": [] },
        { "text": "<tweet 3 ≤280 chars>", "mediaUrls": [] },
        { "text": "<tweet 4 ≤280 chars>", "mediaUrls": [] },
        { "text": "<tweet 5 with link to full article>", "mediaUrls": [] }
      ]
    },
    "target": {
      "targetType": "twitter"
    }
  }
}
```

**arahkaii voice on X:** declarative, opinionated, no rhetorical-question hooks. Skip the "🧵" emoji — it reads as influencer-y. Open with the argument.

---

### Threads

**Account ID resolution:** `list-accounts` filtered by `platform: "threads"`.

**Content rules:**
- 500 character limit per post
- Supports threads via `additionalPosts` (similar to Twitter)
- NO hashtags
- More cultural-commentary culture than X — slightly more space for nuance

**Post payload:** same structure as Twitter, just `platform: "threads"` and `targetType: "threads"`.

---

### Bluesky

**Account ID resolution:** `list-accounts` filtered by `platform: "bluesky"`.

**Content rules:**
- 300 character limit
- Threads supported via `additionalPosts`
- NO hashtags
- Conversational, link-friendly

**Post payload:** standard structure, `platform: "bluesky"`, `targetType: "bluesky"`.

---

### Facebook

**Account ID resolution:** `list-accounts` filtered by `platform: "facebook"`. Always need `pageId` from `list-subaccounts`.

**Content rules:**
- No hard character limit (Facebook truncates after ~500 chars in feed)
- Max 5 hashtags
- Link previews work natively — Facebook fetches OG meta from the URL
- Image attachments fine

**Post payload:**
```json
{
  "post": {
    "accountId": "<facebook_account_id>",
    "content": {
      "text": "<300-500 char post + soft CTA + 3-5 hashtags>",
      "mediaUrls": ["<featured image URL>"],
      "platform": "facebook"
    },
    "target": {
      "targetType": "facebook",
      "pageId": "<facebook_page_id>"
    }
  }
}
```

**Rate limit:** ~5 posts/day recommended.

---

### TikTok

**Skip for arahkaii by default.** TikTok requires video content; arahkaii is text-first. Only distribute to TikTok when Robert explicitly approves a specific article for video adaptation.

**Setup if used:**
- Account must be warmed up 4+ weeks
- Starter plan: 3 unique TikTok accounts per 24h, 10 posts per account
- Video format: vertical 9:16, max 60 seconds for For You eligibility
- TikTok-specific options: `autoAddMusic: true`, `privacyLevel`, `disabledComments`, etc.

---

### YouTube

**Skip for arahkaii by default** unless an article has accompanying video content.

If used: requires OAuth via Blotato Settings. Videos under 60s with vertical aspect become Shorts automatically.

---

## Scheduling strategy

For a single article distribution across 9 platforms, **do NOT fire all 9 simultaneously** — platforms' spam-detection systems flag synchronized cross-posting.

Two strategies:

### Strategy A — useNextFreeSlot (recommended)

Use Blotato's calendar slots. In Blotato settings, configure posting times per platform (e.g., IG at 8pm SGT, LinkedIn at 8am SGT, Pinterest 3 staggered times, X mid-day). Then pass `useNextFreeSlot: true` in the post payload:

```json
{
  "post": { ... },
  "useNextFreeSlot": true
}
```

Each platform's post lands in its next configured slot. Blotato handles the staggering.

### Strategy B — Manual scheduledTime

Stagger manually with `scheduledTime`:

```json
{
  "post": { ... },
  "scheduledTime": "2026-05-20T15:30:00+08:00"
}
```

ISO 8601 with timezone offset.

Suggested staggering for arahkaii (in SGT):
- Twitter/X thread: immediate publish or +5 min
- Instagram: 8:00 PM same day (after-work feed time)
- LinkedIn: 8:00 AM next morning
- Pinterest pin 1: +30 min
- Pinterest pin 2: +6 hours
- Pinterest pin 3: +24 hours
- Facebook: 7:00 PM same day
- Threads: +1 hour after Twitter
- Bluesky: +2 hours after Twitter

---

## Multi-variant content generation

For each article, generate platform-specific copy. **Don't post the same caption everywhere** — platforms penalize identical content and audiences prefer native voice.

### Per-platform copy framework

Use this mental model:

| Platform | Length | First line role | Hashtag strategy | Tone |
|---|---|---|---|---|
| Instagram | 100-150 word caption | Hook (single line, declarative) | 3-5 strategic | Editorial, conversational |
| LinkedIn | 800-1500 chars | One-line argument | None | Analytical, professional |
| Pinterest | 200-500 char desc | Keyword-rich, search-optimized | None | SEO-descriptive |
| Twitter/X | 280 char + thread | Sharp argument or fact | None | Declarative, witty |
| Threads | 500 char | Cultural observation | None | Discursive, considered |
| Bluesky | 300 char | Conversational hook | None | Casual, thoughtful |
| Facebook | 300-500 char | Curiosity prompt | 3-5 max | Approachable |

---

## Quality safeguards

Before any `create-post` call, validate:

1. ✓ Caption/text length is within the platform's hard limit
2. ✓ Image URL is publicly accessible (test fetch if uncertain)
3. ✓ Hashtag count respects platform rules
4. ✓ For FB/LinkedIn: pageId is present
5. ✓ For Pinterest: boardId is present
6. ✓ For threads: each additionalPost respects its own character limit

If any validation fails, skip that platform for this run and log to run-log.md — don't try to publish a malformed post.

---

## Error handling

Common Blotato errors and responses:

| Error | Cause | Action |
|---|---|---|
| 401 Unauthorized | Bad/expired API key | Log, email Robert, abort |
| 400 Validation | Payload malformed (likely length or required field) | Log, fix or skip platform |
| 403 Forbidden | Account not connected or revoked | Log, skip platform, email Robert |
| 429 Rate Limited | Platform-specific daily limit hit | Skip platform, retry next run |
| Network/timeout | Transient | Retry once, then skip if still failing |

Use the API Dashboard for debugging: https://my.blotato.com/api-dashboard

---

## Voice safeguards

The single biggest risk in social distribution is **arahkaii's editorial voice drifting on social platforms** — sounding like a content marketer on LinkedIn, like an influencer on Instagram, like a Twitter joke account on X.

The voice rules in `references/brand-voice.md` apply to social copy with the same strictness as articles. The banned phrases list is universal — they're banned on social too.

Specific platform pitfalls:

**Instagram:** Avoid "✨", "💕", "obsessed", "must-have", "the perfect [X]". Open with a specific observation, not a question or platitude.

**LinkedIn:** Avoid "I have to share something", "Quick thread on [X]", "Here's what I learned". Open with the argument.

**Twitter/X:** Avoid "Take", "Hot take", "Just thinking...", "Unpopular opinion:". Just state the thing.

**Pinterest:** SEO-friendly descriptions ARE the goal — but they should still sound like editorial, not keyword salads.

---

## Pre-flight checklist (before this skill runs at all)

The triggering routine (typically Routine 2) must verify:

1. ✓ WordPress post exists and meets editorial bar
2. ✓ Featured image is uploaded and has a public URL
3. ✓ Post is being published live (status flipped to "publish") OR is already published
4. ✓ Blotato accounts are connected and warmed up
5. ✓ BLOTATO_API_KEY env var is set
6. ✓ BLOTATO_PINTEREST_BOARD_ID env var is set
7. ✓ The post is approved by Robert (not auto-triggered)

---

## When NOT to use this skill

- For an article still in draft — wait until publish
- For an article that violates platform rules (e.g., explicit content, copyright issues)
- For an article in a topic that's not appropriate for some platforms (e.g., skip Pinterest for ultra-niche industry analysis pieces that won't gain traction there)
- When Blotato API is down — check status at https://my.blotato.com/api-dashboard first
- For non-arahkaii content (HumbleHalal, etc. — those would need their own setup)

---

## Standard handoff format

When this skill completes a distribution run, report back:

```
✓ Distributed to <n> platforms

  WP post: <title> (post_id: <id>)
  Live URL: <permalink>
  
  Platforms successfully distributed:
  - Instagram:   <blotato_post_id> | scheduled for <time> | <feed_url_if_immediate>
  - LinkedIn:    <id> | scheduled for <time>
  - Pinterest:   <id> x3 pins | scheduled for <times>
  - Twitter:     <id> | thread of <n> tweets | live now
  - Threads:     <id> | scheduled for <time>
  - Bluesky:     <id> | live now
  - Facebook:    <id> | scheduled for <time>
  
  Platforms skipped:
  - TikTok:      not in scope for this article
  - YouTube:     no video content
  
  Errors / partial:
  - <if any>
  
  Total reach (est): <n> followers across platforms
  Next: monitor first 2-3 hours for any platform-specific flags
```

---

*Skill maintained by Robert. Update when Blotato adds platforms (Mastodon? Lemmy? When they ship) or when platform rules change.*

*Verified against Blotato API documentation as of 2026-05-15.*
