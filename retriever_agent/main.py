from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/get-data")
def get_data(query: Query):
    try:
        stock_response = requests.post(
            "http://127.0.0.1:8001/fetch-data",
            json={"query": query.query}
        )
        news_response = requests.post(
            "http://127.0.0.1:8002/get-news",
            json={"query": query.query}
        )

        stock_response.raise_for_status()
        news_response.raise_for_status()

        stock_data = stock_response.json()
        news_data = news_response.json()

        return {
            "stock_info": stock_data,
            "news": news_data["top_news"]
        }

    except Exception as e:
        return {"error": str(e)}
