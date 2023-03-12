import requests
from datetime import datetime
from dateutil.parser import isoparse
import time
import smtplib

MY_EMAIL = "arsalanakhtar0@yahoo.com"
PASSWORD = "odhbambwuxzhiuot"
MY_LAT = 23.603900
MY_LONG = 87.117700

def datetime_from_utc_to_local(utc_datetime):
    now_time = t.time()
    offset = datetime.fromtimestamp(now_time) - datetime.utcfromtimestamp(now_time)
    return utc_datetime + offset

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = isoparse(data["results"]["sunrise"])
    sunrise = datetime_from_utc_to_local(sunrise).hour
    sunset = isoparse(data["results"]["sunset"])
    sunset = datetime_from_utc_to_local(sunset).hour
    time_now = datetime.now().hour
 
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="arsalanakhtar0@gmail.com",
                msg="Subject:Look Up👆🏼\n\nThe ISS is above you in the sky!".encode("utf-8"))