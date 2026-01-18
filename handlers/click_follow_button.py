from time import sleep
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_follow_button(driver, logger):
    wait = WebDriverWait(driver, 20)

    follow_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[.//span[normalize-space()='Follow']]"
        ))
    )

    sleep(randint(1,3))

    follow_btn.click()
    logger.info("Follow button clicked")
