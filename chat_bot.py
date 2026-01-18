import argparse
import os

from time import sleep
from random import randint, choice

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from handlers.type_on_chat import type_on_chat
from handlers.make_login import make_login
from handlers.get_users_from_csv import get_users_from_csv
from utils.logger import setup_logger
from utils.driver_startup import driver_startup

from selenium.webdriver.support.ui import WebDriverWait

parser = argparse.ArgumentParser(description="Blaze account automation")
parser.add_argument(
    "--count",
    type=int,
    default=1,
    help="Number of messages to send"
)

args = parser.parse_args()

logger = setup_logger("blaze_signup")
logger.info("Starting automation")

BASE_URL = os.getenv('BASE_URL')

STREAMERS = ["darkmarine27"]

logger.info(f"Accounts to create: {args.count}")

counter = 0
users = get_users_from_csv()
try: 
    for _ in range(args.count):
        try:
            driver = driver_startup()
            wait = WebDriverWait(driver, 15)
            for streamer in STREAMERS:
                driver.get(f"{BASE_URL}/{streamer}")
                sleep(randint(2, 4))
                user = choice(users)
                username, email, password = user[0], user[1], user[2]
                make_login(driver, email, username, password, logger)
                type_on_chat(driver, logger)
        except Exception as e:
            logger.error(f"Error creating user {user}: {e}")
        except KeyboardInterrupt:
            driver.quit()
            logger.info("Automation finished")
except Exception as e:
    logger.error(e)
except KeyboardInterrupt:
    driver.quit()
    logger.info("Automation finished")

