from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from bs4 import BeautifulSoup

app = FastAPI()

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "ceebe70492954994a9c1cf18b6236ccb")

class NewsRequest(BaseModel):
    query: str

def fallback_scrape_news(query):
    # Simple Google News scraping fallback (for demo, lightweight)
    try:
        search_url = f"https://news.google.com/search?q={query}&hl=en-US&gl=US&ceid=US:en"
        resp = requests.get(search_url)
        soup = BeautifulSoup(resp.text, "html.parser")
        articles = soup.select('article')[:5]
        news = []
        for article in articles:
            title = article.find('h3')
            if title:
                news.append({
                    "title": title.text,
                    "source": "Google News",
                    "publishedAt": "",
                    "url": ""
                })
        return news
    except Exception:
        return []

@app.post("/get-news")
def get_news(request: NewsRequest):
    url = f"https://newsapi.org/v2/everything?q={request.query}&sortBy=publishedAt&pageSize=5&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("status") != "ok":
            # Fallback scraping
            news = fallback_scrape_news(request.query)
            if not news:
                raise HTTPException(status_code=503, detail="Failed to fetch news from API and fallback")
            return {"top_news": news}

        articles = data.get("articles", [])
        news = []
        for article in articles:
            news.append({
                "title": article.get("title"),
                "source": article.get("source", {}).get("name"),
                "publishedAt": article.get("publishedAt"),
                "url": article.get("url"),
            })

        return {"top_news": news}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching news: {str(e)}")
