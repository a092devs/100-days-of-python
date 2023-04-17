from os import environ
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv('config.env', override=True)

TWILIO_SID = environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = environ.get("TWILIO_NUMBER")
TWILIO_VERIFIED_NUMBER = environ.get("MY_NUMBER")

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)