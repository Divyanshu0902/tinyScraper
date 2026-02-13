import pandas as pd

INPUT_FILE = "startup_ideas_raw.csv"

df = pd.read_csv(INPUT_FILE)

KEYWORDS = [
    "problem", "struggle", "struggling", "difficult",
    "issue", "issues", "pain", "broken", "waste", "hard"
]

def looks_like_problem(text):
    if pd.isna(text):
        return False

    text = text.lower()

    for word in KEYWORDS:
        if word in text:
            return True

    return False


df["is_problem"] = df["text"].apply(looks_like_problem)

problem_posts = df[df["is_problem"] == True]

THEMES = {
    "freelancing": ["client", "freelance", "payment", "scope"],
    "transport": ["bus", "transport", "train", "metro", "traffic"],
    "saas_growth": ["users", "signup", "customer", "acquisition"],
    "civic": ["government", "public", "city", "municipal"]
}

def detect_theme(text):
    if pd.isna(text):
        return "other"

    text = text.lower()

    for theme, words in THEMES.items():
        for w in words:
            if w in text:
                return theme

    return "other"

problem_posts["theme"] = problem_posts["text"].apply(detect_theme)


print("Total posts:", len(df))
print("Problem-like posts:", len(problem_posts))

print("\n--- Problem posts ---\n")
print(problem_posts[["subreddit", "title", "text"]])
problem_posts.to_csv("problem_posts.csv", index=False)

print("\n--- Problems per theme ---\n")
print(problem_posts["theme"].value_counts())
