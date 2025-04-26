# scripts/run_pipeline.py

import subprocess

def run_script(script_path):
    """Runs a python script located at script_path."""
    print(f"🚀 Running {script_path}...")
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"❌ Error running {script_path}:")
        print(result.stderr)
    else:
        print(f"✅ Successfully finished {script_path}")

if __name__ == "__main__":
    # 1. Scrape tweets
    run_script('scripts/scrape_tweets.py')
    
    # 2. Clean tweets
    run_script('scripts/clean_tweets.py')

    # 3. Clssify tweets
    run_script('scripts/sentiment_classifier.py')

    # 4. Analyze & visualize results
    run_script('scripts/analyze_sentiment.py')

    print("🏁 Full pipeline (scrape ➡ clean ➡ classify ➡ analyze) completed successfully!")
