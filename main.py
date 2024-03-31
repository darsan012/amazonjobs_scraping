from selenium import webdriver
from selenium.webdriver.common.by import By
# for getting the keys
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

#opens the chrome with the link entered
driver.get("https://google.com")

#selecting the input element of the google.com
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("tech with tim" + Keys.ENTER) #entering the element to the input box

# to hold the browser for 10 seconds
time.sleep(10)

#closes the browser
driver.quit()

