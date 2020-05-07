import telebot
from telebot import apihelper

import message_generator

bot = telebot.TeleBot("1225997731:AAEVtBib-Ho4vMof1-CE5NuK-SqXaKLKgoI")
apihelper.proxy = {'https': 'socks5h://416062411:fgq4hlS6@orbtl.s5.opennetwork.cc:999'}
number_words = 5


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_sticker(message.chat.id, message_generator.Sticker.start)
    bot.send_message(message.chat.id, message_generator.hello_message())


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, message_generator.random_words(number_words))


bot.polling()
