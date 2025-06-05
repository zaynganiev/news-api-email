import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    receiver = username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)