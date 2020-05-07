import telebot
from telebot import apihelper

import eng_api

bot = telebot.TeleBot("1225997731:AAEVtBib-Ho4vMof1-CE5NuK-SqXaKLKgoI")
apihelper.proxy = {'https': 'socks5h://416062411:fgq4hlS6@orbtl.s5.opennetwork.cc:999'}
eng_api.load_words()
number_words = 5


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, eng_api.random_words(number_words))


bot.polling()
