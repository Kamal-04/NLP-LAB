
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

analyer = SentimentIntensityAnalyzer()
text = "I am Happy always"

sentiment_scores =analyer.polarity_scores(text)
compound_score = sentiment_scores['compound']

if compound_score>=0.05:
    sentiment="Positive"
elif compound_score<=-0.5:
    sentiment="Negative"
else:
    sentiment="Neutral"

print("Sentiment : ",sentiment)
print("Compound Score: ",compound_score)