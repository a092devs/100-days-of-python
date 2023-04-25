import re
import requests
import smtplib
from bs4 import BeautifulSoup
from os import environ
from dotenv import load_dotenv

load_dotenv('config.env', override=True)

FROM_EMAIL = environ.get("FROM_EMAIL")
FROM_PASSWORD = environ.get("FROM_PASSWORD")
TO_EMAIL = environ.get("TO_EMAIL")

# Define a regular expression pattern for Amazon product URLs
amazon_url_pattern = r"https?://(?:www\.)?amazon\.(?:com|ca|co\.uk|de|fr|it|es|co\.jp|com\.au|com\.mx|nl|com\.br|ae|in)/(?:[\w-]+/)?(?:dp|gp/product)/(?:\w{10}|\w{13})"

# Keep asking for a valid Amazon product URL from the user
while True:
    URL = input("Please provide the URL of the product on Amazon:\n")
    if re.match(amazon_url_pattern, URL):
        break
    else:
        print("Invalid Amazon product URL. Please try again.")

http_headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58"
}

response = requests.get(URL, headers=http_headers)
soup = BeautifulSoup(response.text, 'html.parser')

price_str = soup.find(name="span", class_="a-offscreen").getText().replace(",", "")
if price_match := re.search(r"([\d,]+(?:\.\d{1,2})?)", price_str):
    price = float(price_match[1].replace(",", ""))
else:
    print("Could not extract price information. Exiting.")
    exit()

product_name = " ".join(soup.find(
    name="span", class_="a-size-large product-title-word-break").getText().split())

user_price_str = input("What amount do you want to compare the product with?\n")
if user_price_match := re.search(r"([\d,]+(?:\.\d{1,2})?)", user_pri ce_str):
    user_price = float(user_price_match[1].replace(",", ""))
else:
    print("Could not extract user price information. Exiting.")
    exit()

if price < user_price:
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, FROM_PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=f"Subject: Price Drop Alert!\n\n{product_name} is now available for ₹{price}\n\nVisit: {URL}".encode('utf-8')
                            )