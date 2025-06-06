import os
from dotenv import load_dotenv
import requests
from send_email import send_email
from datetime import datetime, timedelta

load_dotenv()  # Load variables from .env

# Define the topic for news
topic = "tesla"

today = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q={topic}&from={today}&sortBy=publishedAt&apiKey={api_key}&language=en"
print(today)

# Make a request to the News API
request = requests.get(url)

# Get a dictionary from the response
content = request.json()
print(content)

# Access the articles in the response
if content.get("status") != "ok":
    print("Error from NewsAPI:", content.get("message"))
else:
    body = ""
    for article in content["articles"][:20]:
        if article["title"] is not None:
            body = "Subject: Daily News Update" \
                 + "\n" + body + article["title"] + "\n" \
                 + (article["description"] or "") + "\n" \
                 + article["url"] + "\n\n"

body = body.encode("utf-8")
send_email(message=body)