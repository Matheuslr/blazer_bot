import csv
import os
from datetime import datetime


CSV_PATH = "files/created_users.csv"


def save_user_to_csv(username, email, password, logger, status="created"):
    file_exists = os.path.isfile(CSV_PATH)

    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "username",
            "email",
            "password",
            "status",
            "created_at"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "username": username,
            "email": email,
            "password": password,
            "status": status,
            "created_at": datetime.utcnow().isoformat()
        })

    logger.info(f"{username} has been saved on the {CSV_PATH} file")