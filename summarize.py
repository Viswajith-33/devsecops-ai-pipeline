import os
import requests

def read(path):
    try:
        return open(path, encoding="utf-8").read()[:6000]
    except FileNotFoundError:
        return "No output"

bandit = read("bandit.txt")
audit = read("audit.txt")

prompt = f"""You are a security engineer. Below are scan results from
Bandit (code scanner) and pip-audit (dependency scanner).
Write a short summary for a developer:
1. The top 3 risks ranked by severity, with one line on why each matters.
2. A one-line fix for each.
Keep it under 200 words.

BANDIT:
{bandit}

PIP-AUDIT:
{audit}
"""

key = os.environ["GEMINI_API_KEY"]
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent"
import time

for attempt in range(5):
    r = requests.post(
        url,
        headers={"x-goog-api-key": key},
        json={"contents": [{"parts": [{"text": prompt}]}]},
        timeout=60,
    )
    if r.status_code in (429, 500, 503):
        print(f"Attempt {attempt + 1} failed ({r.status_code}), retrying...")
        time.sleep(15)
        continue
    break
r.raise_for_status()
text = r.json()["candidates"][0]["content"]["parts"][0]["text"]

print(text)
with open(os.environ.get("GITHUB_STEP_SUMMARY", "summary.md"), "a", encoding="utf-8") as f:
    f.write("## AI Security Summary\n\n" + text)