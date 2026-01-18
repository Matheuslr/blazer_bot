from time import sleep
from random import randint

from handlers.fetch_latest_blaze_code import fetch_latest_blaze_code
from handlers.fill_signup_form import fill_signup_form
from handlers.fill_verification_code import fill_verification_code
from handlers.save_user_to_csv import save_user_to_csv

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def make_signup(driver, email, user, password, logger, timeout=20):

    wait = WebDriverWait(driver, timeout)

    logger.info("starting signup flow")
    signup_button = wait.until(
        EC.element_to_be_clickable((By.ID, "signup-button"))
    )
    sleep(randint(1, 3))
    signup_button.click()
    logger.info("Signup button clicked")

    continue_with_email = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'continue with email')]"
        ))
    )
    sleep(randint(1, 3))
    continue_with_email.click()
    logger.info("Continue with email clicked")

    fill_signup_form(driver, email, user, password, logger)

    signup_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign Up']"))
    )
    sleep(randint(1, 3))
    signup_btn.click()
    logger.info("Signup form submitted")


    code = fetch_latest_blaze_code(user, logger)
    fill_verification_code(driver, code, logger)

    confirm_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Confirm']"))
    )
    sleep(randint(1, 3))
    confirm_btn.click()
    logger.info(f"User {user} confirmed")

    save_user_to_csv(user, email, password, logger)