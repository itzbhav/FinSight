from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/analyze")
def analyze_data(request: QueryRequest):
    query = request.query
    try:
        # Stock data
        stock_res = requests.post("http://127.0.0.1:8001/fetch-data", json={"query": query})
        stock_res.raise_for_status()
        stock_data = stock_res.json()

        # News data
        news_res = requests.post("http://127.0.0.1:8002/get-news", json={"query": query})
        news_res.raise_for_status()
        news_data = news_res.json()

        # Analysis
        analysis_res = requests.post("http://127.0.0.1:8003/analyze-data", json={
            "stock_info": stock_data,
            "news_info": news_data
        })
        analysis_res.raise_for_status()
        analysis_data = analysis_res.json()

        # Language agent to summarize everything
        language_res = requests.post("http://127.0.0.1:8004/summarize", json={
            "stock_info": stock_data,
            "news_info": news_data,
            "insight": analysis_data.get("sentiment", "")
        })
        language_res.raise_for_status()
        language_data = language_res.json()

        return language_data  # ✅ this will contain the "response" key

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}