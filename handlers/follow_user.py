from time import sleep
from random import randint

from handlers.fill_login_form import fill_login_form
from handlers.click_follow_button import click_follow_button
from handlers.type_on_chat import type_on_chat
from handlers.check_follow import check_follow

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def follow_user(driver, streamer, BASE_URL, email, username, password, logger, timeout=20):
    wait = WebDriverWait(driver, timeout)

    logger.info("starting follow user flow")

    target_url = f"{BASE_URL}/{streamer}"
    driver.get(target_url)
    sleep(randint(2, 4))
    
    click_follow_button(driver, logger)
    try: 
        continue_with_email = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'continue with email')]"
            ))
        )
        sleep(randint(1, 3))
        continue_with_email.click()

        fill_login_form(driver, email, username, password, logger)

        signin_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign in']"))
        )
        sleep(randint(1, 3))
        signin_btn.click()

        logger.info(f"User {username} logged in")
        sleep(randint(2, 4))
        is_following = check_follow(driver, username, streamer, logger)
        logger.info(is_following)
        if not is_following:
            click_follow_button(driver, logger)
            sleep(randint(1, 2))
            type_on_chat(driver, logger)

            sleep(randint(2, 4))
    except Exception as e:
        pass
    finally:
        logger.info(f"{username} followed {streamer}")