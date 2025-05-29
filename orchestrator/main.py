from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/orchestrate")
def orchestrate(query: Query):
    try:
        stock_data = requests.post("http://localhost:8001/fetch-data", json={"query": query.query}).json()
        news_data = requests.post("http://localhost:8002/fetch-news", json={"query": query.query}).json()
        analysis_data = requests.post("http://localhost:8003/analyze", json={
            "stock_data": stock_data,
            "news_data": news_data
        }).json()

        return {
            "stock": stock_data,
            "news": news_data,
            "analysis": analysis_data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal orchestrator error: {str(e)}")
