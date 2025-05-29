from pydantic import BaseModel
from typing import Dict, List, Optional

class StockData(BaseModel):
    symbol: str
    current_price: float
    name: Optional[str]
    currency: Optional[str]
    sector: Optional[str]
    website: Optional[str]
    historical_prices: Dict[str, float]

class NewsData(BaseModel):
    news_headlines: List[str]  # empty list if no news available

class OrchestratorPayload(BaseModel):
    stock_data: StockData
    news_data: NewsData
