# News API Email

A Python project that retrieves daily news articles about a specified topic using the News API and sends a daily email update with the results.

## Features

- Retrieves news articles about a specified topic.
- Sends an email update with the latest news.
- Uses environment variables to securely store API keys and email credentials.
- Easy to customize and extend.

## Prerequisites

- Python 3.6 or higher
- A valid [News API](https://newsapi.org/) key.
- A Gmail account with an [App Password](https://support.google.com/accounts/answer/185833) set up (if using SMTP to send emails).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/news-api-email.git
   cd news-api-email
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *If you don't have a `requirements.txt`, install the following packages:*

   ```bash
   pip install python-dotenv requests
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root with the following content:

   ```properties
   NEWS_API_KEY=your_news_api_key
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_email_app_password
   ```

## Usage

1. **Modify the topic (optional):**  
   Update the `topic` variable in `main.py` if you want to search for news on a different topic.

2. **Run the script:**

   ```bash
   python main.py
   ```

   This will fetch news articles from yesterday and send you an email with a summary.

## Troubleshooting

- **No Articles Returned/Errors:**  
  Ensure your API key is valid and the query parameters are correct. Check the printed API response in the terminal for error details.

- **Email Not Sent:**  
  Double-check your email credentials and ensure you’re using an App Password if two-factor authentication (2FA) is enabled on your Gmail account.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [News API](https://newsapi.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Python Requests](https://pypi.org/project/requests/)