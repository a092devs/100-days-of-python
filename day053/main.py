import requests
from os import environ
from time import sleep
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

load_dotenv('config.env', override=True)

ZILLOW_URL = environ.get("ZILLOW_URL")
G_FORM_URL = environ.get("G_FORM_URL")

http_headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/99.0.4844.51 Safari/537.36",
}

service = Service("C:\Development\chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

response = requests.get(ZILLOW_URL, headers=http_headers)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
search_results = soup.find("div", {"id": "grid-search-results"})

def get_link():
    link_list = [a["href"] for a in search_results.find_all("a", tabindex="0")]
    for i in range(len(link_list)):
        if not link_list[i].startswith("https"):
            link_list[i] = f'https://www.zillow.com{link_list[i]}'
    return link_list

def get_address():
    return [address.getText() for address in search_results.find_all("a", tabindex="0") if address.getText()]

def get_price():
    return [price.getText() for price in soup.find_all("div", class_="StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 bqsBln")]


driver.get(G_FORM_URL)
sleep(4)

for i in range(len(get_address())):
    property_address = driver.find_element(By.XPATH, value='//*[@aria-describedby = "i2 i3"]')
    property_price = driver.find_element(By.XPATH, value='//*[@aria-describedby = "i6 i7"]')
    property_link = driver.find_element(By.XPATH, value='//*[@aria-describedby = "i10 i11"]')

    property_address.send_keys(get_address()[i])
    property_price.send_keys(get_price()[i])
    property_link.send_keys(get_link()[i])
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    next_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next_response.click()

driver.quit()
