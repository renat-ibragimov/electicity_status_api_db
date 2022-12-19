import requests
import time

import config
from status_checker import StatusChecker


def send_to_channel():
    while True:
        checker = StatusChecker()
        if checker.status_checker():
            requests.post(
                f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage",
                data={"chat_id": config.CHANNEL_ID,
                      "text": checker.status_checker()})
        time.sleep(59)


if __name__ == '__main__':
    send_to_channel()

