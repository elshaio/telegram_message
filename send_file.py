#!{{pythonpath}}
import config
from telegram import Bot
import sys


def send_file(chat_id, archivo):
    bot = Bot(config.telegram_token)
    bot.send_document(chat_id=chat_id, document=open(archivo[0], 'rb'))


if __name__ == '__main__':
    args = sys.argv
    if config.chat_id is None:
        send_file(args[1], args[2:])
    else:
        send_file(config.chat_id, args[1:])
