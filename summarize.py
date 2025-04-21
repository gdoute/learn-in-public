import os
import sys
import re
import datetime
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

from atproto import Client, client_utils
import requests

# Load API credentials from environment
bsky_handle = os.getenv("BLUESKY_HANDLE")
bsky_app_password = os.getenv("BLUESKY_APP_PASSWORD")
yourls_signature = os.getenv("YOURLS_SIGNATURE")

dry_run = os.getenv("DRY_RUN", "false").lower() == "true"

# Use YESTERDAY'S date for summary target
yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
post_filename = f"content/Journal/{yesterday}.md"
article_url = f"https://gdoute.github.io/learn-in-public/Journal/{yesterday}"


def shorten_url_yourls(url):
    try:
        res = requests.get(f"https://cosmogol.net/yourls/yourls-api.php?url={url}&format=simple&action=shorturl&signature={yourls_signature}")
        if res.status_code == 200:
            return res.text
        else:
            print(f"⚠️ Failed to shorten URL: {res.text}")
            return url
    except Exception as e:
        print(f"⚠️ Failed to shorten URL: {e}")
        return url

# Check if post file exists
if not os.path.exists(post_filename):
    print(f"⚠️ Input file '{post_filename}' not found. Skipping.")
    sys.exit(0)

# Read the article
with open(post_filename, 'r', encoding='utf-8') as f:
    article_content = f.read()

short_url = shorten_url_yourls(article_url)
# Compose prompt for OpenAI
prompt = f"""
Summarize the following article in a way that fits into a BlueSky post (max 200 characters), preserving key ideas and using engaging language. Add a hashtag #LearnInPublic to the end of the summary and at most two other hashtags that references key points of the summary.
add a link to the article in the summary at the address of the daily note that is : {short_url}

At the beginning of the summary, mention there is a new update in the learn-in-public site. When mentioning the author use the first person, for example "I wrote this article".

Article:
{article_content}
"""

# Call OpenAI API
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional content summarizer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300)
    summary = response.choices[0].message.content.strip()
    print("📝 Summary:\n" + summary)
except Exception as e:
    print(f"❌ OpenAI API call failed: {e}")
    sys.exit(1)

# ─── Build rich text with hashtag facets ──
# Split the summary on either URLs or hashtags
pattern = r"(https?://\S+|#\w+)"
segments = re.split(pattern, summary)

tb = client_utils.TextBuilder()
for seg in segments:
    if not seg:
        continue
    if re.match(r"^https?://", seg):
        # Add a link facet
        tb.link(seg, seg)
    elif seg.startswith("#") and re.match(r"^#\w+$", seg):
        # Add a hashtag facet (strip leading '#')
        tb.tag(seg, seg.lstrip("#"))
    else:
        tb.text(seg)


# ─── Post to BlueSky ───
if not dry_run:
    try:
        client = Client()
        client.login(bsky_handle, bsky_app_password)
        # sending the TextBuilder itself ensures facets are sent
        post = client.send_post(tb)
        print("✅ Posted to BlueSky:", post.uri)
    except Exception as e:
        print(f"❌ BlueSky post failed: {e}")
        sys.exit(1)
else:
    print("🧪 DRY RUN: Skipping BlueSky post.")

