from dotenv import load_dotenv
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from datetime import date

load_dotenv()

email = os.getenv("GMAIL_APP_EMAIL")
password = os.getenv("GMAIL_APP_PW")

port = 465
context = ssl.create_default_context()


def send_email(articles, topic):
    html = f"""
    <html>
    <body>
    <h1>{date.today().strftime("%B %d, %Y")}</h1>
    <ul>
    """

    for article in articles:
        html_item = f"""
        <li>
            <p><strong>{article["title"]}</strong></p>
            <p>{article["description"]}</p>
            <a href={article["url"]}>Read here</a>
        </li>
        """
        html += html_item

    html += """
    </ul>
    </body>
    </html>
    """
    message = MIMEText(html, "html")
    message["Subject"] = f"Today's most popular news for {topic}"
    message["From"] = email
    message["To"] = email

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, email, message.as_string())
