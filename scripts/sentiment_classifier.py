
import pandas as pd
from transformers import pipeline
import os

# 1. Load cleaned tweets
df = pd.read_csv('data/processed/cleaned_climate_tweets.csv')

print(f"✅ Loaded {len(df)} cleaned tweets from data/processed/cleaned_climate_tweets.csv")

# 2. Load pre-trained sentiment classifier
classifier = pipeline("sentiment-analysis")
print("✅ Loaded pre-trained sentiment analysis model")

# 3. Classify tweets
df['sentiment'] = df['clean_text'].apply(lambda x: classifier(x)[0]['label'])

print("✅ Sentiment classification complete!")
print(df[['clean_text', 'sentiment']].head())

# 4. Save results
# Make sure processed directory exists
os.makedirs('data/processed', exist_ok=True)

# Save to new file
df.to_csv('data/processed/classified_climate_tweets.csv', index=False)
print("✅ Classified tweets saved to data/processed/classified_climate_tweets.csv")
