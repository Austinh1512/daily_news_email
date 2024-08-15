from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
from datetime import date

load_dotenv()
api_key = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key)

topic = "olympics"
res = newsapi.get_everything(
    qintitle=topic,
    from_param=date.today(),
    sort_by="popularity"
)

print(res["articles"])


