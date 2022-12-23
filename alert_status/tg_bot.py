import requests

import config


class TGBot:
    def __init__(self, message: str):
        self.message = message
        self.send_msg()

    def send_msg(self):
        requests.post(
            f"https://api.telegram.org/bot{config.PRIMORSKII_COURT_BOT_TOKEN}/"
            f"sendMessage",
            data={"chat_id": config.PRIMORSKII_COURT_CHANNEL_ID,
                  "text": self.message})
