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
    np.sum(np.power(args,(2/3)))
    pass


updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('pisteet +args', piste_lasku))
updater.start_polling()
updater.idle()
