import pandas as pd
import re
import os

# 1. Load scraped tweets (utf-8 encoding)
df = pd.read_csv('data/raw/climate_tweets.csv', encoding='utf-8')

print(f"✅ Loaded {len(df)} tweets from data/raw/climate_tweets.csv")

# 2. Define cleaning function
def clean_tweet(text):
    text = re.sub(r"http\S+", "", text)       # Remove URLs
    text = re.sub(r"@\w+", "", text)           # Remove mentions
    text = re.sub(r"#", "", text)              # Remove hashtag symbols
    # text = re.sub(r"[â€™â€œâ€\x80-\xFF]", "", text)  # Remove broken unicode artifacts only
    text = re.sub(r"[^\x00-\x7F]+", "", text)  # Remove non-ASCII characters (like â€¦ðŸ˜µ)
    text = re.sub(r"\s+", " ", text)           # Remove extra whitespace
    return text.strip()

# 3. Apply cleaning
df['clean_text'] = df['text'].apply(clean_tweet)

print("✅ Tweets cleaned successfully with emojis retained!")

# 4. Save cleaned tweets
os.makedirs('data/processed', exist_ok=True)

df.to_csv('data/processed/cleaned_climate_tweets.csv', index=False)
print("✅ Cleaned tweets saved to data/processed/cleaned_climate_tweets.csv")
