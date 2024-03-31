from selenium import webdriver
from selenium.webdriver.common.by import By
# for getting the keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# opens the chrome with the link entered
driver.get("https://google.com")

# Waiting for the response for 5 seconds
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# selecting the input element of the Google.com
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()  # clearing the text field or input field
input_element.send_keys("Darshan Gautam" + Keys.ENTER)  # entering the element to the input box

# finding the element with the text
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Darshan Gautam - Advanced College of Engineering")))
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Darshan Gautam - Advanced College of Engineering")
link.click()  # click on the link

# to hold the browser for 10 seconds
time.sleep(10)

# closes the browser
driver.quit()

