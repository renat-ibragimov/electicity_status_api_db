import time

import telebot

import config
from db_worker import DBWorker
from status_checker import StatusChecker

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    with DBWorker() as worker:
        last_known_status = worker.get_status()
        if last_known_status:
            bot.send_message(message.chat.id, f'{last_known_status[1]} з '
                                              f'{last_known_status[2]}')
    while True:
        checker = StatusChecker()
        if checker.status_checker():
            bot.send_message(message.chat.id, checker.status_checker())
        time.sleep(2)


bot.polling(none_stop=True, interval=0)
