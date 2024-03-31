from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver") #chromedriver is the driver file for the chrome
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

# to hold the browser for 10 seconds
time.sleep(50)

driver.quit()

