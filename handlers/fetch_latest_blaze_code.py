import imaplib
import email
import re
import time
import imaplib
import os

def fetch_latest_blaze_code(username, logger, timeout=120):
    IMAP_SERVER = os.getenv('IMAP_SERVER')
    IMAP_PORT = os.getenv('IMAP_PORT')
    EMAIL_ACCOUNT = os.getenv('EMAIL_ACCOUNT')
    APP_PASSWORD = os.getenv('APP_PASSWORD')

    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL_ACCOUNT, APP_PASSWORD)
    mail.select("INBOX")

    start = time.time()

    username_lower = username.lower()

    while time.time() - start < timeout:
        status, messages = mail.search(None, "UNSEEN")
        logger.info("checking inbox...")

        if messages[0]:
            for num in messages[0].split():
                _, data = mail.fetch(num, "(RFC822)")
                msg = email.message_from_bytes(data[0][1])

                subject = msg.get("Subject", "")
                sender = msg.get("From", "")

                if "blaze" not in sender.lower() and "blaze" not in subject.lower():
                    continue

                body = ""

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body += part.get_payload(decode=True).decode(errors="ignore")
                else:
                    body = msg.get_payload(decode=True).decode(errors="ignore")

                body_lower = body.lower()

                if username_lower not in body_lower and username_lower not in subject.lower():
                    continue

                match = re.search(r"\b[A-Z0-9]{6}\b", body)
                if match:
                    code = match.group()
                    logger.info(f"Verification code found for {username}: {code}")
                    return code

        time.sleep(5)

    return None