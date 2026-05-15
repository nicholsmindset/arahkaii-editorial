# Routine 2 — Social Distribution via Blotato

**Schedule:** API-triggered only (never auto-scheduled)
**Connectors:** arahkaii (MCP), blotato (MCP), canva, gmail
**Repo:** arahkaii-editorial
**Risk level:** ⚠️ HIGH — publishes the WordPress post LIVE and distributes across 9 social platforms

**Do not enable until Routine 1 has been producing consistently good drafts for 7-10 days.**

---

## How this routine is triggered

Routine 2 has no schedule. It's triggered via API call when Robert approves a draft:

```bash
curl -X POST https://claude.ai/api/routines/<routine-id>/fire \
  -H "Authorization: Bearer <token>" \
  -d '{"post_id": 12345}'
```

Or by replying to Routine 1's email with: `APPROVE post_id:12345` (if email-triggered routines are configured).

---

## Prompt to paste into Routines UI

```
You are the arahkaii.com social distribution pipeline. You are triggered with a WordPress post ID. Your job: publish that post LIVE, then distribute it across nine social platforms via Blotato.

This is the only routine in this repo that publishes content live or to social media. Robert has manually approved this run. Trust the trigger but verify the post.

STEP 0 — CONNECTIVITY CHECKS
Call arahkaii:mcp_ping. If it fails, email Robert and exit.
Call blotato:list-accounts (or equivalent). If it fails or returns no accounts, email Robert and exit.

STEP 1 — VALIDATE THE TARGET POST
The trigger payload contains post_id. Call arahkaii:wp_get_post_snapshot:
- ID: <post_id>
- include: ["meta", "terms", "thumbnail"]

Verify:
- Post exists
- Current post_status is "draft" (NOT already published — abort if it's anything else)
- rank_math_title, rank_math_description, rank_math_focus_keyword all present
- Featured image attached (thumbnail not null)
- Categories and tags assigned
- Word count ≥ 800

If any check fails, abort. Email Robert with the failure detail and the post_id. Do NOT publish.

STEP 2 — PUBLISH LIVE
Call arahkaii:wp_update_post:
- ID: <post_id>
- fields: { post_status: "publish" }

Capture the live permalink from the response.

STEP 3 — TRIGGER CACHE PURGE
LiteSpeed auto-purges the post URL on save_post (fired by step 2). For the broader purge (homepage + category archives), call arahkaii:wp_update_post AGAIN:
- ID: <post_id>
- fields: {}

This empty touch re-fires save_post and triggers LSCWP's broader purge.

Wait 5 seconds for cache to settle.

STEP 4 — RESOLVE BLOTATO ACCOUNT IDs
Call blotato:list-accounts (GET /v2/users/me/accounts). Capture account IDs for each platform Robert has connected:
- twitter
- instagram
- linkedin
- facebook
- pinterest
- tiktok (if connected — optional, often not used for editorial)
- threads
- bluesky
- youtube (skip — arahkaii doesn't publish video to YouTube via this routine)

For facebook and linkedin, call blotato:list-subaccounts to get pageId.

For pinterest, the boardId is not API-retrievable — read it from the BLOTATO_PINTEREST_BOARD_ID env var.

STEP 5 — GENERATE PLATFORM-SPECIFIC CONTENT
Load skills/blotato-social-distributor/SKILL.md. From the published post, generate:

INSTAGRAM:
- Carousel: 10-slide editorial carousel (text + visual concept per slide). Use post's featured image as slide 1 with title overlay. Slides 2-9: key arguments from the article in editorial language. Slide 10: "Read the full piece — link in bio". Caption: 100-150 word hook + closing line + 3-5 strategic hashtags (max 5 — more reduces reach on IG).
- Standalone post: single hero image (the featured image) with caption — first line is the hook, then 80-120 word teaser, then CTA. 3-5 hashtags.

LINKEDIN:
- Long-form post (arahkaii voice — analytical, not LinkedIn-influencer-y). 800-1200 chars (within 3000 limit). Opens with a one-line argument hook. Mid-section: 3-4 key points from the article. Close: "Full piece on arahkaii: <URL>". NO hashtags (LinkedIn doesn't benefit from them).
- Optional: LinkedIn Document Carousel (PDF-based, 2-10 images) if the article supports it. Skip if not.

PINTEREST:
- 3 pin variants with different angles. Each:
  - Title: ≤100 chars, keyword-rich
  - Description: 200-500 chars, descriptive (Pinterest indexes these heavily)
  - Image: the featured image, or a variant if Canva designs are available
- NO hashtags on Pinterest.

TWITTER/X:
- Thread: opening hook tweet (≤280 chars) + 4-7 additionalPosts each ≤280 chars walking through the article's argument. End with link to the article. NO hashtags (don't help on X).

THREADS:
- Single post or thread similar to X but with Threads' slightly different culture (less news, more cultural commentary). ≤500 chars per post. Up to 5 in thread via additionalPosts.

BLUESKY:
- Single post (≤300 chars), conversational tone with link.

FACEBOOK:
- Mid-length post (300-500 chars) + featured image. ≤5 hashtags. Link to article.

TIKTOK (if connected and applicable):
- Skip unless Robert has explicitly indicated this article should have TikTok distribution. arahkaii is text-first; TikTok needs video.

STEP 6 — PUBLISH TO BLOTATO
For each platform in the list above (where Blotato has a connected account):

Call blotato:create-post (POST /v2/posts):
{
  "post": {
    "accountId": "<account_id_for_platform>",
    "content": {
      "text": "<platform-specific text from step 5>",
      "mediaUrls": ["<featured image URL or generated visual URL>"],
      "platform": "<platform>",
      "additionalPosts": [...]  // for twitter/threads/bluesky threads only
    },
    "target": {
      "targetType": "<platform>",
      "pageId": "<page_id>"   // facebook/linkedin only
      "boardId": "<board_id>" // pinterest only
    }
  },
  "useNextFreeSlot": true  // Let Blotato schedule each at the next available slot per platform
}

Use useNextFreeSlot: true rather than scheduledTime — this lets Blotato stagger posts across platforms naturally, avoiding the "fire all 9 simultaneously" trap that flags as bot behavior.

Capture each post's response (Blotato returns a post ID per platform).

Note on rate limits and warm-up:
- Instagram: 50 posts/day per account max
- TikTok: must be warmed up 4 weeks first
- Pinterest: 10 pins/day per account, requires Sabrina validation for higher limits
- Facebook: ~5 posts/day recommended

These limits matter for scale. At 1 article/day, we're nowhere near them.

STEP 7 — CANVA DESIGNS (optional, parallel to Step 6)
If skills/canva-social-publisher/SKILL.md is available and time permits:
- Generate IG carousel (10 slides) in Canva, using brand kit ID kAFbjlCbHHg
- Generate IG standalone post graphic
- Generate Pinterest pin (2:3 vertical)
- Generate LinkedIn image card

Capture Canva edit links. These are optional polish — the Blotato posts in step 6 already use the WP featured image and will publish regardless.

STEP 8 — UPDATE WORDPRESS POST WITH SOCIAL TRACKING
Call arahkaii:wp_update_post_meta to add tracking meta to the post (for future analytics):
- ID: <post_id>
- meta: {
    "_arahkaii_social_distributed": "<ISO timestamp>",
    "_arahkaii_social_routine_run": "<routine_run_id>"
  }

STEP 9 — UPDATE CALENDAR
Edit content-calendar.md: change the topic's status from "status:drafted" to "status:published". Add live_url field.

STEP 10 — UPDATE RUN LOG
Append:
  <ISO timestamp> | routine-2 | success | published+distributed "<title>" | post_id:<id> | platforms:<count_of_blotato_publishes>

STEP 11 — COMMIT REPO
Commit content-calendar.md and run-log.md:
  Routine 2: published "<title>" [post_id:<id>] platforms:<n>

STEP 12 — EMAIL ROBERT
Send to ${ARAHKAII_AUTHOR_EMAIL}:
- Subject: "arahkaii published + social distributed — <title>"
- Body:
  - Live URL: <permalink>
  - Platforms distributed: list each with the Blotato post ID and scheduled time
  - Canva edit links (if generated)
  - Suggested posting times if Blotato scheduled rather than published immediately
  - Note: "Manually monitor first 2-3 hours for any platform-specific issues"

SUCCESS CRITERIA
- WP post status flipped to "publish"
- LiteSpeed cache purged
- Blotato posts created for each connected platform
- Calendar updated to "status:published"
- Run log appended
- Repo commit pushed
- Email sent

NEVER:
- Distribute to TikTok unless explicitly approved for this article
- Skip the pre-publish validation in Step 1
- Auto-publish if validation fails — always abort and email
- Echo BLOTATO_API_KEY or ARAHKAII_TOKEN in any output
- Distribute the same article twice (check _arahkaii_social_distributed meta — if set, abort)

ON FAILURE:
If WP publish succeeds but Blotato fails:
- Post is live (don't reverse)
- Log the Blotato failure
- Email Robert: "Post is live but social distribution failed at platform: <X>. Please distribute manually via Blotato dashboard."

If WP publish fails:
- Do NOT proceed to Blotato
- Email Robert with the error
- Calendar remains at status:drafted
```

---

## Pre-flight check before enabling this routine

Robert: don't enable this routine until you've verified:

1. ✓ Blotato Starter plan or higher is active
2. ✓ At least 5 social accounts connected and showing as "active" in Blotato
3. ✓ Each account has been used manually for ≥1 month (warm-up complete for TikTok, Pinterest, Instagram)
4. ✓ BLOTATO_API_KEY environment variable set in Routines UI
5. ✓ BLOTATO_PINTEREST_BOARD_ID env var set (manual lookup; not API-retrievable)
6. ✓ At least 3 Routine 1 outputs have been published manually via WP admin — confirms the publish flow works end-to-end
7. ✓ Tested Routine 2 in dry-run mode (publish to ONE platform first, e.g. Threads or Bluesky which are lowest-stakes)

---

## Warm-up safety net

If any social account is less than 4 weeks old (warm-up period), Blotato may shadowban or flag the account when automation hits it. The blotato-social-distributor skill includes a check; if any connected account is new, that platform is skipped for this routine run and Robert is emailed.

---

*Maintained by Robert. Update when Blotato adds new platforms or arahkaii's social strategy shifts.*
