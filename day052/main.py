import time
from os import environ
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "C:\Development\chromedriver\chromediver.exe"
TARGET_ACCOUNT = "ufc"

load_dotenv("config.env")
USERNAME = environ("INSTA_ID")
PASSWORD = environ("INSTA_PASS")


class InstaFollowerBot:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME, value="username")
        password = self.driver.find_element(By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]')
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollowerBot(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()