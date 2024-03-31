from selenium import webdriver
import time

driver = webdriver.Chrome()

#opens the chrome with the link entered
driver.get("https://google.com")

# to hold the browser for 10 seconds
time.sleep(10)

#closes the browser
driver.quit()

