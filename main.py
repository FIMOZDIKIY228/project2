from pkgutil import get_data
from turtledemo.penrose import start

import requests
import telebot
from auth_data import token
def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "выберете валюту btc, usd, kzt")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == "btc":
            try:
                url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'
                response = requests.get(url)
                data = response.json()
                btc_p = data['data']['rates']['RUB']
                bot.send_message(message.chat.id,
                                 f"BTC стоит:{btc_p} рублей"
                                 )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Что-то пошло не так"
                )

        if message.text.lower() == "usd":
            try:
                url = 'https://api.coinbase.com/v2/exchange-rates?currency=USD'
                response = requests.get(url)
                data = response.json()
                usd_p = data['data']['rates']['RUB']
                bot.send_message(message.chat.id,
                                 f"USD стоит:{usd_p} рублей"
                                 )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Что-то пошло не так"
                )

        if message.text.lower() == "kzt":
            try:
                url = 'https://api.coinbase.com/v2/exchange-rates?currency=KZT'
                response = requests.get(url)
                data = response.json()
                kzt_p = data['data']['rates']['RUB']
                bot.send_message(message.chat.id,
                                 f"KZT стоит:{kzt_p} рублей"
                                 )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Что-то пошло не так"
                )
        else: bot.send_message(
                    message.chat.id,
                    "Проверьте правильность написания команды"
                )

    bot.polling()

if __name__ == '__main__':
    telegram_bot(token)
