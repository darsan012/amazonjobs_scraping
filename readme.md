# Scraping amazon jobs to get notification about the job availability
## Problem statement:
    Recently I tried to search jobs on amazon jobs and was unable to find the job at the right time.
    There is certain time when the jobs are available. There is email and text notification option but both of them are
    not working properly. So, this app resolves that problem by sending email whenever there is job available.

## Future Enhancement
    - Create frontend site with the login menu.
    - Ask the user to input the country and settings.
    - Ask user to enter their email address
    - Ask user to input the time interval when they want to refresh the page.

 ## Technologies used
- python
- selenium
- smtplib

## Usage
- Include .env file
```bash
EMAIL_FROM=your_email@outlook.com
EMAIL_TO=recipient_email@example.com
SMTP_SERVER=smtp.office365.com
SMTP_PORT=587
SMTP_USERNAME=your_email@outlook.com
SMTP_PASSWORD=your_email_password
``` 
## Steps taken for project setup
- installing selenium 
```bash 
pip install selenium
```
- install chromedriver
- for mac user put the chromedriver inside /usr/local/bin
- install dotenv
```bash 
pip install python-dotenv
```

## Resourses
 - https://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-selenium
 - https://vikramsamal.medium.com/importerror-urllib3-v2-0-only-supports-openssl-1-1-1-e74510f3a5f8

 ### Tips to move specific file on mac with paths
     hold command shift G