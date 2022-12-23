import pytz

import datetime
import time

# noinspection PyUnresolvedReferences
from telethon import TelegramClient, events, sync

import config
from db_worker import DBWorker
from tg_bot import TGBot


def last_status():
    with DBWorker() as w:
        return w.get_status()


def save_status(new_status):
    with DBWorker() as w:
        w.insert_status(new_status)


def local_time():
    local = pytz.timezone('Europe/Kyiv').fromutc(datetime.datetime.utcnow())
    return datetime.datetime.strftime(local, "%H:%M:%S %d-%m-%Y")


def check_alert_status():
    client = TelegramClient('electricity_status_bot',
                            config.TG_API_ID, config.TG_API_HASH)
    client.start()

    while True:
        last_post = client.get_messages(config.SOURCE_CHANNEL_NAME, limit=1)
        for msg in last_post:
            status = msg.message.split(" ")[-1]
            if status == config.ALERT_ON \
                    and last_status() != config.ALERT_ON:
                TGBot(
                    f'\U0001F534 Повітряна тривога!\n{local_time()}')
                save_status(config.ALERT_ON)
            if status == config.ALERT_OFF \
                    and last_status() != config.ALERT_OFF:
                TGBot(
                    f'\U0001F7E2 Відбій повітрянної тривоги!\n{local_time()}')
                save_status(config.ALERT_OFF)
        time.sleep(60)


if __name__ == "__main__":
    check_alert_status()
