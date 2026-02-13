import requests
import pandas as pd

URL = "https://hn.algolia.com/api/v1/search_by_date"

URL = "https://hn.algolia.com/api/v1/search_by_date"

PARAMS = {
    "tags": "story",
    "hitsPerPage": 100
}


response = requests.get(URL, params=PARAMS)
data = response.json()

rows = []

for hit in data["hits"]:
    text = hit.get("story_text")
    if not text:
        text = hit.get("title")

    rows.append({
        "subreddit": "hackernews",
        "title": hit.get("title"),
        "text": text,
        "score": hit.get("points"),
        "comments": hit.get("num_comments"),
        "url": hit.get("url")
    })


df = pd.DataFrame(rows)

df.to_csv("startup_ideas_raw.csv", index=False)

print("Saved", len(df), "Hacker News posts")
