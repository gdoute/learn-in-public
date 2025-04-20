import os
import sys
import datetime
import subprocess
import openai
from atproto import Client

# Load API credentials from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
bsky_handle = os.getenv("BLUESKY_HANDLE")
bsky_app_password = os.getenv("BLUESKY_APP_PASSWORD")

# Determine today's date
today = datetime.date.today().isoformat()
post_filename = f"content/Journal/{today}.md"

# Check git log for existing summary commit
def summary_already_committed():
    try:
        check_cmd = ['git', 'log', '--grep', f'summary for {today}', '--pretty=oneline']
        result = subprocess.run(check_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.returncode == 0 and bool(result.stdout.strip())
    except Exception as e:
        print(f"⚠️ Failed to check git log: {e}")
        return False

if summary_already_committed():
    print(f"✅ Summary already committed for {today}, skipping.")
    sys.exit(0)

# Check if the post file exists
if not os.path.exists(post_filename):
    print(f"⚠️ Input file '{post_filename}' not found. Skipping.")
    sys.exit(0)

# Read the file content
with open(post_filename, 'r', encoding='utf-8') as f:
    article_content = f.read()

# Construct OpenAI prompt
prompt = f"""
Summarize the following article in a way that fits into a BlueSky post (max 300 characters), preserving key ideas and using engaging language.

Article:
{article_content}
"""

# Call OpenAI API
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional content summarizer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    summary = response.choices[0].message['content'].strip()
    print("📝 Summary:\n" + summary)
except Exception as e:
    print(f"❌ OpenAI API call failed: {e}")
    sys.exit(1)

# Post to BlueSky
try:
    client = Client()
    client.login(bsky_handle, bsky_app_password)
    client.send_post(summary)
    print("✅ Posted to BlueSky.")
except Exception as e:
    print(f"❌ BlueSky post failed: {e}")
    sys.exit(1)

# Create marker commit to indicate that summary was generated today
try:
    subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], check=True)
    subprocess.run(['git', 'config', 'user.email', 'github-actions[bot]@users.noreply.github.com'], check=True)
    subprocess.run(['git', 'commit', '--allow-empty', '-m', f'chore: summary for {today}'], check=True)
    print(f"✅ Created marker commit for {today}")
except Exception as e:
    print(f"⚠️ Failed to create marker commit: {e}")
    sys.exit(1)

