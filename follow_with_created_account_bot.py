import argparse
import os

from time import sleep
from random import randint

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from handlers.generate_user import generate_user
from handlers.make_login import make_login
from handlers.follow_user import follow_user
from handlers.get_users_from_csv import get_users_from_csv
from handlers.check_follow import check_follow
from utils.logger import setup_logger
from utils.driver_startup import driver_startup

from selenium.webdriver.support.ui import WebDriverWait

parser = argparse.ArgumentParser(description="Blaze account automation")
parser.add_argument(
    "--count",
    type=int,
    default=1,
    help="Number of accounts to create"
)
args = parser.parse_args()

logger = setup_logger("blaze_signup")
logger.info("Starting automation")

BASE_URL = os.getenv('BASE_URL')

STREAMERS = ["darkmarine27"]

logger.info(f"Accounts to create: {args.count}")
try:
    logger.info(STREAMERS)
    for _ in range(args.count):
        try:
            users = get_users_from_csv()
            for user in users:
                for streamer in STREAMERS:
                    driver = driver_startup()
                    wait = WebDriverWait(driver, 15)
                    username, email, password = user[0],user[1],user[2]
                    follow_user(driver, streamer, BASE_URL, email, username, password, logger, timeout=20)
                    driver.quit()
            
        except Exception as e:
            logger.error(f"Error creating user {user}: {e}")
        except KeyboardInterrupt:
            driver.quit()
            logger.info("Automation finished")
        finally:
            driver.quit()

        sleep((60*60)/4)
except Exception as e:
    logger.error(e)
except KeyboardInterrupt:
    driver.quit()
    logger.info("Automation finished")

