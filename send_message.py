#!{{pythonpath}}
import config
from telegram import Bot
import sys


def send_message(chat_id, mensaje):
    bot = Bot(config.telegram_token)
    bot.send_message(chat_id, ' '.join(mensaje))


if __name__ == '__main__':
    args = sys.argv
    if config.chat_id is None:
        send_message(args[1], args[2:])
    else:
        send_message(config.chat_id, args[1:])
