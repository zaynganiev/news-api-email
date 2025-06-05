import os
from dotenv import load_dotenv
import requests
from send_email import send_email

load_dotenv()  # Load variables from .env

api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-05-05&sortBy=publishedAt&apiKey={api_key}"

# Make a request to the News API
request = requests.get(url)

# Get a dictionary from the response
content = request.json()

# Access the articles in the response
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + (article["description"] or "") + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)