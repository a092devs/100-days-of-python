import smtplib
import requests
from os import environ
from dotenv import load_dotenv

load_dotenv('config.env', override=True)

BOT_TOKEN = environ.get("BOT_TOKEN")
CHAT_ID = environ.get("CHAT_ID")
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.mail.yahoo.com"
MY_EMAIL = environ.get("MY_EMAIL")
MY_PASSWORD = environ.get("MY_PASSWORD")

class NotificationManager:
    def telegram_bot_send_text(self, bot_message):
        bot_token = BOT_TOKEN
        bot_chatID = CHAT_ID
        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'
        bot_response = requests.get(send_text)
        return bot_response.json()

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )