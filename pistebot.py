# -*- coding: utf-8 -*-
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import os
import numpy as np

# API-avain
token = os.environ['TGPISTE_TOKEN']

def start(bot, update):
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id,
                    'Tervetuloa Fyysikkokillan fuksimatrikkelin 2019 korttipelinpisteytysapubottihimmeliin.')


def piste_lasku(bot, update, args):
    chat_id = update.message.chat.id

    try:
        vector = list(map(int, args))
        points = np.sum(np.power(vector,(2/3)))
        teksti = 'Pisteet ovat ' + str(points)
        bot.sendMessage(chat_id, text=teksti )

    except Exception as e:
        bot.sendMessage(chat_id, 'Pisteet annettiin väärässä muodossa. Kokeile uudestaan!')
        print(str(e))


updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('pisteet', piste_lasku, pass_args=True))
updater.start_polling()
updater.idle()
