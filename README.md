# Tweet-o-meter: Climate & Agriculture Sentiment Analysis 🌍📈
A mini NLP project to scrape, clean, classify, and visualize real-time tweets related to climate and agriculture.

---
## 🚀 Features
- Scrapes Twitter for climate/agriculture tweets
- Cleans and pre-processes the text
- Classifies sentiment (positive/negative)
- Analyzes trends over time
- Basic visualizations

---
## 📁 Project Structure
- `scripts/`: All main Python scripts
- `data/`: Raw and processed datasets
- `outputs/`: Plots and results
- `run_pipeline.py`: Full project runner

---
## 🛠 Tools Used
- Python
- Tweepy
- HuggingFace Transformers
- scikit-learn
- pandas, matplotlib, seaborn

---
## ⚡ How to Run
```bash
# Create virtual environment
python -m venv tweet

# Activate
# Windows:
tweet\Scripts\activate
# Mac/Linux:
source tweet/bin/activate

# Install dependencies
pip install -r requirements.txt

#Update Token in Scraping Script.

# Run the full pipeline!
python run_pipeline.py

# Future Ideas
## Add Topic Modeling (LDA)
## Geolocation-based sentiment
## Deploy as a dashboard (Streamlit)