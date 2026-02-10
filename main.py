import pandas as pd # type: ignore
import time
from sentiment_analysis import get_sentiment

# Start timer
start_time = time.time()

# Load customer feedback data
data = pd.read_csv("customer_feedback.csv")

# Create empty lists
sentiments = []
scores = []

# Go through each feedback comment
for text in data["feedback"]:
    sentiment, score = get_sentiment(text)
    sentiments.append(sentiment)
    scores.append(score)

# Add results to table
data["sentiment"] = sentiments
data["confidence"] = scores

# Save results
data.to_csv("feedback_results.csv", index=False)

# End timer
end_time = time.time()

print("Analysis finished")
print("Time taken:", round(end_time - start_time, 2), "seconds")