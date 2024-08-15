from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
from datetime import date
from send_email import send_email

load_dotenv()
api_key = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key)

topic = ""
res = newsapi.get_everything(
    qintitle=topic,
    from_param=date.today(),
    sort_by="popularity"
)

send_email(res["articles"], topic)
