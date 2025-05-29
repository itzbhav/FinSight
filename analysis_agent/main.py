from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

class AnalysisRequest(BaseModel):
    historical_prices: Dict[str, float]
    current_price: float
    sector: str
    news_headlines: List[str]

@app.post("/analyze")
def analyze(request: AnalysisRequest):
    prices = list(request.historical_prices.values())

    if not prices:
        return {"error": "No historical prices provided."}

    # Basic price change analysis
    price_change = round(((request.current_price - prices[0]) / prices[0]) * 100, 2)

    # Basic news summarization (stub)
    headline_summary = " | ".join(request.news_headlines[:3])

    # Basic recommendation logic
    recommendation = (
        "Hold" if -2 <= price_change <= 2 else ("Buy" if price_change < -2 else "Sell")
    )

    return {
        "price_trend": f"{price_change}% over last 5 days",
        "sector": request.sector,
        "latest_news": headline_summary,
        "recommendation": recommendation,
    }
