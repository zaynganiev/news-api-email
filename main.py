import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Load variables from .env

api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-05-05&sortBy=publishedAt&apiKey={api_key}"

# Make a request to the News API
request = requests.get(url)

# Get a dictionary from the response
content = request.json()

# Access the articles in the response
for article in content["articles"]:
    print(article["title"])
    print(article["description"])