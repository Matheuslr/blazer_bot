from time import sleep
from random import randint

from handlers.fill_login_form import fill_login_form

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def make_login(driver, email, username, password, logger, timeout=15):


    wait = WebDriverWait(driver, timeout)

    logger.info("starting login flow")

    # 1. Click "Login" button
    login_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[normalize-space()='Login']"
        ))
    )
    sleep(randint(1, 3))
    login_btn.click()
    logger.info("login button clicked")

    # 2. Click "Continue with Email"
    continue_with_email = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'continue with email')]"
        ))
    )
    sleep(randint(1, 3))
    continue_with_email.click()
    logger.info("continue with email clicked")

    # 3. Fill login form
    fill_login_form(driver, email, username, password, logger)
    logger.info("login form filled")

    # 4. Click "Sign in"
    signin_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[normalize-space()='Sign in']"
        ))
    )
    sleep(randint(1, 3))
    signin_btn.click()
    logger.info("sign in button clicked")

    logger.info(f"user {username} logged in successfully")
