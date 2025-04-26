# scripts/scrape_tweets_loop.py

import tweepy
import pandas as pd
import os
import time
from datetime import datetime

# Set up your credentials (replace with your actual bearer token)
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKum0gEAAAAACAr8T9GlMZ6WlN1Blk1vSCizP4Q%3DHxxdBxCZqIaAKmW4fUpjycnF3BcFS8oWFNIjNgYWBe2YLYdw0c"

# Initialize Tweepy client
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

# Define your search query
query = "climate change -is:retweet lang:en"
max_results = 100  # Max per request

# Output directory
output_dir = os.path.join('data', 'raw')
os.makedirs(output_dir, exist_ok=True)

def scrape_and_save():
    tweets_data = []

    # Make the API request
    response = client.search_recent_tweets(
        query=query,
        max_results=max_results,
        tweet_fields=['created_at', 'lang', 'text']
    )

    if response.data:
        for tweet in response.data:
            tweets_data.append({
                'created_at': tweet.created_at,
                'text': tweet.text
            })

        # Create a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save to CSV
        filename = f"climate_tweets_{timestamp}.csv"
        output_path = os.path.join(output_dir, filename)

        df = pd.DataFrame(tweets_data)
        df.to_csv(output_path, index=False)

        print(f"✅ [{timestamp}] Scraped {len(df)} tweets and saved to {output_path}")
    else:
        print(f"⚠️ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] No tweets found for this query.")

# Loop to scrape every 2 hours
while True:
    scrape_and_save()
    print("⏳ Waiting for 2 hours before next scrape...")
    time.sleep(2 * 60 * 60)  # Sleep for 2 hours (in seconds)
