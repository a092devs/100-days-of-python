import requests
import smtplib
from bs4 import BeautifulSoup
from os import environ
from dotenv import load_dotenv

load_dotenv('config.env', override=True)

FROM_EMAIL = environ.get("FROM_EMAIL")
FROM_PASSWORD = environ.get("FROM_PASSWORD")
TO_EMAIL = environ.get("TO_EMAIL")

URL = "https://www.amazon.in/dp/B09RHCYZ82"

http_headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58"
}

response = requests.get(URL, headers=http_headers)
soup = BeautifulSoup(response.text, 'html.parser')

price = float(soup.find(name="span", class_="a-offscreen").getText()[1:])
product_name = " ".join(soup.find(
    name="span", class_="a-size-large product-title-word-break").getText().split())

if price < 400.00:
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, FROM_PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=f"Subject: Price Drop Alert!\n\n{product_name} is now available in ₹{price}\n\nVisit: {URL}".encode('utf-8')
                            )