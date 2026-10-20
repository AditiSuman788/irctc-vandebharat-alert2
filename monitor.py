import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://news.google.com/rss/search?q=Mumbai+Bengaluru+Vande+Bharat+Sleeper"

feed = requests.get(url).text

keywords = [
    "Vande Bharat",
    "Mumbai",
    "Bengaluru"
]

if all(k.lower() in feed.lower() for k in keywords):

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": "🚄 Possible update found for Mumbai-Bengaluru Vande Bharat Sleeper. Check news now."
        }
    )
