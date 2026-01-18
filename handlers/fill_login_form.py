from time import sleep
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_login_form(driver, email, username, password, logger):
    wait = WebDriverWait(driver, 20)
    
    # Email
    sleep(randint(1,3))
    email_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "email"))
    )
    email_input.clear()
    email_input.send_keys(email)
    
    # Password
    sleep(randint(1,3))
    password_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "password"))
    )
    password_input.clear()
    password_input.send_keys(password)

    logger.info(f"Email - {email}, username - {username} and password filled")

    