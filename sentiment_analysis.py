from transformers import pipeline

# Load sentiment model (one line)
sentiment_analyzer = pipeline("sentiment-analysis")

def get_sentiment(text):
    result = sentiment_analyzer(text)[0]
    return result["label"], round(result["score"], 2)
