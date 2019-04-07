# Fyysikkokillan fuksimatrikkeli 2019 pistebot

Aalto yliopiston Fyysikkokillan fuksimatrikkeli 2019 korttipelin pisteytys telegrambotti

## Vaatimukset
* Python 2.7.2+
* Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)
```
$ pip install python-telegram-bot
```

## Asennus
* Luo botti ja ansaitse API-avain [@BotFather](http://t.me/BotFather)
* Tallenna API-avain ENV-muuttujaksi
```
$ export TGPISTE_TOKEN=”ApiAvainTähän”
```

## Käynnistys
```
$ screen -S pistebot
$ python pistebot.py
```


## Suuret kiitokset
* Matrikkelitoimikunta 2019
* Fyysikkokillan kahvikone
* [kvantti-telegram-bot-example](https://github.com/EinariTuukkanen/kvantti-telegram-bot-example)
