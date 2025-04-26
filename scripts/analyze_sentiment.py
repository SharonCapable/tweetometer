import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load classified tweets (parse dates properly!)
df = pd.read_csv('data/processed/classified_climate_tweets.csv', parse_dates=['created_at'])

print(f"✅ Loaded {len(df)} tweets")
print(df.head())

# Count the number of each sentiment
sentiment_counts = df['sentiment'].value_counts()

print("Sentiment Counts:")
print(sentiment_counts)

# Plot Sentiment Distribution
plt.figure(figsize=(8,5))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
plt.title("Sentiment Distribution of Climate Tweets")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.tight_layout()

# Save sentiment distribution plot
os.makedirs('outputs/plots', exist_ok=True)
plt.savefig('outputs/plots/sentiment_distribution.png')
plt.show()

print("✅ Sentiment distribution plot saved to outputs/plots/sentiment_distribution.png")

# --- Sentiment Trends Over Time (Dynamic Grouping) ---

# Check how many unique dates are in the data
unique_dates = df['created_at'].dt.date.nunique()

if unique_dates > 1:
    print("📆 Multiple days detected ➔ Grouping by DATE")
    df['time_group'] = df['created_at'].dt.date
else:
    print("🕒 Single day detected ➔ Grouping by TIME (15-min intervals)")
    df['time_group'] = df['created_at'].dt.floor('15T')

# Group by time_group and sentiment
sentiment_trends = df.groupby(['time_group', 'sentiment']).size().unstack().fillna(0)

# Plot
sentiment_trends.plot(kind='line', marker='o', figsize=(12,7))
plt.title("Sentiment Trends Over Time")
plt.xlabel("Time Group")
plt.ylabel("Number of Tweets")
plt.legend(title='Sentiment')
plt.tight_layout()
plt.savefig('outputs/plots/sentiment_trends_dynamic.png')
plt.show()

print("✅ Sentiment trends plot saved to outputs/plots/sentiment_trends_dynamic.png")
print("🏁 Analysis complete!")