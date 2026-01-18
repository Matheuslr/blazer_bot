from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_verification_code(driver, code, logger):
    wait = WebDriverWait(driver, 20)

    inputs = wait.until(
        EC.presence_of_all_elements_located((
            By.XPATH,
            "//div[contains(@class,'flex') and contains(@class,'gap')]//input[@maxlength='1']"
        ))
    )

    if len(inputs) < len(code):
        raise Exception("Not enough OTP input fields found")

    for i, char in enumerate(code):
        inputs[i].clear()
        inputs[i].send_keys(char)

    logger.info("Verification code entered")