from os import environ
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

load_dotenv('config.env', override=True)

TWITTER_UNAME = environ.get("TWITTER_UNAME")
TWITTER_PASS = environ.get("TWITTER_PASS")
PROMISED_UP = 125
PROMISED_DOWN = 125

service = Service("C:\Development\chromedriver\msedgedriver.exe")
options = Options()
options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.maximize_window()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        sleep(3)
        self.driver.find_element(By.CLASS_NAME, "onetrust-banner-options").click()
        sleep(2)
        start_test = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_test.click()
        sleep(40)
        
        # pop up check
        pop_up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
        pop_up.click()

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(f"Download: {self.down} Mbps")
        print(f"Upload: {self.up} Mbps")
        sleep(3)
        twitter_bot.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(5)
        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_UNAME)
        sleep(2)
        email.send_keys(Keys.ENTER)
        sleep(2)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASS)
        sleep(2)
        password.send_keys(Keys.ENTER)
        sleep(15)
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        sleep(2)
        tweet = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} Mbps Download and {self.up} Mbps Upload when I pay for {PROMISED_DOWN} Mbps Download and {PROMISED_UP} Mbps Upload speed?\n\nAutomated tweet, please ignore!")
        sleep(5)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div/div[2]/div[4]').click()
        sleep(2)
        self.driver.quit()

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()