import requests

def get_news(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    news = response.json()
    articles = news['articles'][:5]
    headlines = [f"{article['title']} - {article['source']['name']}" for article in articles]
    return "\n".join(headlines)
