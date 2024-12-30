from textblob import TextBlob # type: ignore

def analyze_sentiment(user_input):
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"
