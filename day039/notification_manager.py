import requests
from os import environ
from dotenv import load_dotenv

load_dotenv('config.env', override=True)

BOT_TOKEN = environ.get("BOT_TOKEN")
CHAT_ID = environ.get("CHAT_ID")

class NotificationManager:
    def telegram_bot_send_text(self, bot_message):
        bot_token = BOT_TOKEN
        bot_chatID = CHAT_ID
        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'
        bot_response = requests.get(send_text)
        return bot_response.json()