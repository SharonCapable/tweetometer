# scripts/scrape_tweets.py

import tweepy
import pandas as pd
import os

# Set up your credentials (replace with your actual bearer token)
bearer_token = ""

# Initialize Tweepy client
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

# Define your search query
query = "climate change -is:retweet lang:en"
max_results = 100  # Max per request

# List to hold tweet data
tweets_data = []

# Make the API request
response = client.search_recent_tweets(
    query=query, 
    max_results=max_results, 
    tweet_fields=['created_at', 'lang', 'text']
)

# Extract needed info
if response.data:
    for tweet in response.data:
        tweets_data.append({
            'created_at': tweet.created_at,
            'text': tweet.text
        })
else:
    print("⚠️ No tweets found for this query.")

# Convert to DataFrame
df = pd.DataFrame(tweets_data)

# Ensure the output directory exists
output_dir = os.path.join('data', 'raw')
os.makedirs(output_dir, exist_ok=True)

# Save to CSV inside data/raw/
output_path = os.path.join(output_dir, 'climate_tweets.csv')
df.to_csv(output_path, index=False)

print(f"✅ Scraped {len(df)} tweets and saved to {output_path}")
