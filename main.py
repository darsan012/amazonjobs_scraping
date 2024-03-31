from selenium import webdriver
from selenium.webdriver.common.by import By
# for getting the keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for clicking the select element
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

# opens the chrome with the link entered
driver.get("https://hvr-amazon.my.site.com/")

# Waiting for the response for 5 seconds
WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.CLASS_NAME, "accordion-toggle"))
)

# # selecting the input element of the Google.com
# input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# input_element.clear() # clearing the text field or input field
# input_element.send_keys("Darshan Gautam" + Keys.ENTER) # entering the element to the input box

# finding the search button
search_button = driver.find_element(By.CLASS_NAME, "accordion-toggle")
search_button.click()

# Wait for the dropdown menu for countries to become visible
country_dropdown = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located(
    (By.ID, "j_id0:portId:j_id67:Country"))
)

# Scroll to the element (optional)
driver.execute_script("arguments[0].scrollIntoView();", country_dropdown)

country_dropdown.click() # Click to open the dropdown menu
country_dropdown.send_keys("Canada") # Start typing "Canada"

# Wait for the dropdown menu for states to become visible
state_dropdown = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located(
    (By.ID, "j_id0:portId:j_id67:State"))
)
# Scroll to the element (optional)
driver.execute_script("arguments[0].scrollIntoView();", state_dropdown)

state_dropdown.click() # Click to open the dropdown menu
state_dropdown.send_keys("Ontario") # Start typing "Ontario"

state_dropdown.send_keys(Keys.ENTER) # Press Enter to select

# to hold the browser for 10 seconds
time.sleep(10)

# closes the browser
driver.quit()