import requests

url = "http://127.0.0.1:8003/analyze"

payload = {
    "historical_prices": {
        "2024-05-20": 97.5,
        "2024-05-21": 98.2,
        "2024-05-22": 100.1,
        "2024-05-23": 99.4,
        "2024-05-24": 101.0
    },
    "current_price": 101.0,
    "sector": "Technology",
    "news_headlines": [
        "Samsung profits fall 2% in Q1",
        "TSMC beats earnings expectations",
        "Investors cautious amid rising bond yields"
    ]
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())
