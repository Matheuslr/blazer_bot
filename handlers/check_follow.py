from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def check_follow(driver, username, stremaer, logger) -> bool:
    """
    True -> Follow button not present
    False  -> Follow button exists (user is not following)
    """
    try:
        driver.find_element(
            By.XPATH,
            "//button[.//span[normalize-space()='Follow']]"
        )
        logger.info(f"{username} is not following {stremaer}")
        return False
    except NoSuchElementException:
        logger.info(f"{username} already following {stremaer}")
        return True