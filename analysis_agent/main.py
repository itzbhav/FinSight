from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

class StockInfo(BaseModel):
    symbol: str
    price: float
    name: str
    currency: str
    sector: str
    website: str

class NewsArticle(BaseModel):
    title: str
    source: str
    publishedAt: str
    url: str

class AnalysisRequest(BaseModel):
    stock_info: StockInfo
    news_info: Dict[str, List[NewsArticle]]

@app.post("/analyze-data")
def analyze_data(request: AnalysisRequest):
    stock = request.stock_info
    news = request.news_info.get("top_news", [])

    # Basic sentiment logic
    positive_words = ["gain", "growth", "strong", "profit", "surge"]
    negative_words = ["loss", "decline", "weak", "fall", "drop"]

    score = 0
    for article in news:
        title = article.title.lower()
        for word in positive_words:
            if word in title:
                score += 1
        for word in negative_words:
            if word in title:
                score -= 1

    sentiment = "Neutral"
    if score > 1:
        sentiment = "Positive"
    elif score < -1:
        sentiment = "Negative"

    return {
        "summary": f"{stock.name} ({stock.symbol}) in {stock.sector} sector",
        "sentiment": sentiment,
        "sentiment_score": score,
        "articles_analyzed": len(news)
    }
