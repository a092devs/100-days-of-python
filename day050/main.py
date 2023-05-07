import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

class ExtendExpiryBot:
    def __init__(self, driver_path, mode='default'):
        self.service = Service(driver_path)
        self.options = Options()
        if mode == 'headless':
            self._headless_mode()
        elif mode == 'default':
            self.options.add_experimental_option('detach', True)

        self.driver = webdriver.Edge(
            service=self.service, options=self.options
        )
        self.website_url = 'https://www.pythonanywhere.com/'

    def open_website(self):
        self.driver.get(self.website_url)

    def go_to_login_page(self):
        login = self.driver.find_element(By.LINK_TEXT, 'Log in')
        login.click()

    def sign_in(self, username: str, password: str):
        username_input = self.driver.find_element(By.NAME, 'auth-username')
        username_input.send_keys(username)
        password_input = self.driver.find_element(By.NAME, 'auth-password')
        password_input.send_keys(password)
        login_btn = self.driver.find_element(By.ID, 'id_next')
        login_btn.click()

    def go_to_tasks_page(self):
        tasks = self.driver.find_element(By.ID, 'id_tasks_link')
        tasks.click()

    def extend_expiry(self):
        extend_expiry_btn = self.driver.find_element(
            By.CSS_SELECTOR, 'button.extend_scheduled_task')
        extend_expiry_btn.click()

    def log_out(self):
        logout_btn = self.driver.find_element(By.CSS_SELECTOR, '.logout_link')
        logout_btn.click()

    def _headless_mode(self):
        self.options.add_argument('--headless')

if __name__ == '__main__':
    load_dotenv("config.env")

    USER = os.environ.get('PA_USER')
    PASSWORD = os.environ.get('PA_PASS')

    webdriver_path = r'C:\Development\chromedriver\msedgedriver.exe'
    expBot = ExtendExpiryBot(webdriver_path)
    expBot.open_website()
    time.sleep(2)
    expBot.go_to_login_page()
    time.sleep(1)
    expBot.sign_in(USER, PASSWORD)
    time.sleep(4)
    expBot.go_to_tasks_page()
    time.sleep(2)
    expBot.extend_expiry()
    time.sleep(1)
    expBot.log_out()