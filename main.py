from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key)

topic = "olympics"
res = newsapi.get_everything(
    qintitle=topic,
    from_param="2024-07-14",
    sort_by="popularity"
)

print(res["articles"])


