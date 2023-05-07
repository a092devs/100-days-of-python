import os
import time
import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException

dotenv.load_dotenv("config.env", True)

MY_LID_EMAIL = os.environ.get("MY_LID_EMAIL")
MY_LID_PASS = os.environ.get("MY_LID_PASS")

service = Service('C:\Development\chromedriver\msedgedriver.exe')

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()
driver.get('https://www.linkedin.com')

# Log in
username = driver.find_element(By.ID, 'session_key')
username.send_keys(MY_LID_EMAIL)
time.sleep(1)
username = driver.find_element(By.ID, 'session_password')
username.send_keys(MY_LID_PASS)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()
time.sleep(5)

driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102713980&keywords=python%20developer&location=India&refresh=true')
time.sleep(5)

jobs = driver.find_elements(by=By.CLASS_NAME, value='job-card-list__title')
jobs_available = [job.text for job in jobs]
print(jobs_available)

# Select job posting and click on apply
while jobs_available:
    posting_num = 0
    try:
        driver.find_element(by=By.LINK_TEXT, value=f'{jobs_available[posting_num]}').click()
        time.sleep(2)
        driver.find_element(by=By.CLASS_NAME, value="jobs-s-apply").click()
    except NoSuchElementException:
        posting_num += 1
        driver.find_element(by=By.LINK_TEXT, value=f'{jobs_available[posting_num]}').click()
        time.sleep(2)
        driver.find_element(by=By.CLASS_NAME, value="jobs-s-apply").click()
    finally:
        jobs_available.remove(jobs_available[posting_num])
        try:
            time.sleep(3)
            driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Continue to next step"]').click()
            time.sleep(3)
            driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Continue to next step"]').click()
            time.sleep(15)
            driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Review your application"]').click()
            time.sleep(3)
            driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Submit application"]').click()
        except NoSuchElementException:
            print('Cannot apply, skipped')
    print("Work complete")