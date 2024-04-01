import os
# For working with the email
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# working with selenium packages
from selenium import webdriver
from selenium.webdriver.common.by import By
# for getting the keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for clicking the select element
from selenium.webdriver.support.ui import Select
import time

#load .env variables
load_dotenv()

#Function to send the email
def send_email(subject, body):
    # Email credentials and settings
    email_from = os.getenv("EMAIL_FROM")
    email_to = os.getenv("EMAIL_TO")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")

    #creating message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = email_to

    # Create the body of the message (a plain-text and an HTML version).
    text = body
    html = body

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    # sending the email via smtp server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(email_from, email_to, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", e)

# user input
print("Welcome to amazon job scraping site. This app is used to provide the notification whenever there is jobs available in site.")
country_name = input("\nPlease enter the name of the country.")
state_name = input("\nPlease enter the name of the state.")
print("Email preferences:")
# check_interval = int(input("\nAt what interval would you like to check the site? Enter in seconds: "))

# Interval between the checks
check_interval = 10  # Check for certain interval

driver = webdriver.Chrome()

# runs in the loop
while True:
    try:
        # opens the chrome with the link entered
        driver.get("https://hvr-amazon.my.site.com/")

        # Waiting for the response for 5 seconds
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "accordion-toggle"))
        )

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

        country_dropdown.click()  # Click to open the dropdown menu
        country_dropdown.send_keys(country_name)  # Start typing "Canada"

        # Wait for the dropdown menu for states to become visible
        state_dropdown = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "j_id0:portId:j_id67:State"))
        )
        # Scroll to the element (optional)
        driver.execute_script("arguments[0].scrollIntoView();", state_dropdown)

        state_dropdown.click()  # Click to open the dropdown menu
        state_dropdown.send_keys(state_name)  # Start typing "Ontario"

        state_dropdown.send_keys(Keys.ENTER)  # Press Enter to select

        # Check if the response contains "No jobs found"
        response_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@id='j_id0:portId:j_id67:recentJobsOuter']"))
        )

        # try catch because some time the XPATH changes
        try:
            # Check if the response contains "No jobs found"
            no_jobs_element = response_element.find_element(By.XPATH, ".//span[@id='j_id0:portId:j_id67:j_id80']")
            if no_jobs_element.text.strip() == "No jobs found":
                print("No jobs found")
            else:
                print("Jobs found")
                send_email("Amazon hourly job alert", "New jobs are available on the website.")
        except:
            print("Jobs found")
            send_email("Amazon hourly job alert", "New jobs are available on the website.")

        # to hold the browser for certain interval
        time.sleep(check_interval)
    except Exception as e:
        print(f"An error occurred: {e}")

# closes the browser
driver.quit()