from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yfinance as yf

app = FastAPI()

class StockRequest(BaseModel):
    query: str

@app.post("/fetch-data")
def fetch_stock_data(request: StockRequest):
    try:
        ticker = yf.Ticker(request.query)
        data = ticker.info
        
        # Basic validation
        if "currentPrice" not in data:
            raise HTTPException(status_code=404, detail="Stock data not found")
        
        # Fetch historical closing prices (last 5 days)
        hist = ticker.history(period="5d")
        historical_prices = hist['Close'].round(2).to_dict()
        
        return {
            "symbol": request.query.upper(),
            "price": data.get("currentPrice"),
            "name": data.get("longName"),
            "currency": data.get("currency"),
            "sector": data.get("sector"),
            "website": data.get("website"),
            "historical_prices": historical_prices,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching stock data: {str(e)}")
