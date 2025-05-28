from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LanguageInput(BaseModel):
    stock_info: dict
    news_info: dict
    insight: str

@app.post("/summarize")
def summarize_response(data: LanguageInput):
    stock = data.stock_info
    news = data.news_info.get("top_news", [])
    sentence = f"{stock['name']} ({stock['symbol']}) is currently trading at {stock['price']} {stock['currency']}. "
    sentence += f"Sector: {stock['sector']}. {data.insight}.\n\n"
    
    sentence += "Top News:\n"
    for i, article in enumerate(news[:3], 1):
        sentence += f"{i}. {article['title']} ({article['source']})\n"

    return {"response": sentence}
