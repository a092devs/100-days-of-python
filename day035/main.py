import requests
from os import environ
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("config.env", override=True)

lat = environ.get("LAT")
long = environ.get("LONG")
opw_weather_api = environ.get("WEATHER_API")
account_sid = environ.get("TWILIO_ACCOUNT_SID")
auth_token = environ.get("TWILIO_AUTH_TOKEN")
from_num = environ.get("TWILIO_NUMBER")
to_num = environ.get("MY_NUMBER")


URL = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": lat,
    "lon": long,
    "exclude": "current,minutely,daily",
    "appid": opw_weather_api,
}

resp = requests.get(URL, parameters)
resp.raise_for_status()
weather_data = resp.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for i in weather_slice:
    condition = i["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=from_num,
        to=to_num,
    )
