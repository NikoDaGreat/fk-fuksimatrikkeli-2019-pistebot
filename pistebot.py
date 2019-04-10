# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler
import os
import time
import numpy as np

# API-avain
token = os.environ['TGPISTE_TOKEN']

def start(bot, update):
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id,
                    'Tervetuloa Fyysikkokillan fuksimatrikkelin 2019 korttipelinpisteytysapubottihimmeliin! Aloita komennolla /help ')


def help(bot, update):
    chat_id = update.message.chat.id
    bot.send_photo(chat_id, photo=open('kaava.jpg', 'rb'))
    bot.sendMessage(chat_id,
                    'Voit laskea pisteet komennolla "/pisteet x_1 x_2 ... x_n", missä x_n on korttien määrä jokaisessa ryhmässäsi.\nJos jostain ryhmästä ei ole yhtään korttia, ei tarvitse merkitä 0.\n\nPisteet lasketaan kuvan kaavalla. Botin lähdekoodi löytyy osoitteesta https://github.com/NikoDaGreat/fk-fuksimatrikkeli-2019-pistebot')

def piste_lasku(bot, update, args):
    chat_id = update.message.chat.id

    try:
        vector = list(map(int, args))
        points = np.sum(np.power(vector,(2/3)))
        teksti = 'Pisteet ovat ' + str(points)
        bot.sendMessage(chat_id, text=teksti)
        # tallennetaan UNIX-time ja pistemäärä
        pisteLog = open('pisteLog.txt', 'a+')
        pisteLog.write(str(time.time()) + '\t' + str(points) + '\n')
        pisteLog.close()

    except Exception as e:
        bot.sendMessage(chat_id, 'Pisteet annettiin väärässä muodossa. Kirjoita /help tai kokeile uudestaan!')
        print(str(e))


updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('pisteet', piste_lasku, pass_args=True))
updater.start_polling()
updater.idle()
