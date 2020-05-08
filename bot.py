import telebot
from telebot import apihelper

import message_generator

bot = telebot.TeleBot("1225997731:AAEVtBib-Ho4vMof1-CE5NuK-SqXaKLKgoI")
apihelper.proxy = {'https': 'socks5h://416062411:fgq4hlS6@orbtl.s5.opennetwork.cc:999'}

commands = {  # command description used in the "help" command
    'start': 'Start learning English',
    'help': 'Information about the available commands',
    'subscribe': 'Start learning English by 5 words everyday',
    'unsubscribe': 'Stop sending 5 words'
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_sticker(message.chat.id, message_generator.Sticker.start)
    bot.send_message(message.chat.id, message_generator.hello_message())
    command_help(message)


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, message_generator.message_help(commands))


@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_text(message):
    number_words = 5
    try:
        if message.text == '-':
            bot.send_message(message.chat.id, message_generator.random_words(number_words))
        else:
            bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
            bot.send_message(message.chat.id, message_generator.parse_word_definition(message.text.lower()))
    except Exception:
        bot.send_message(message.chat.id, message_generator.error_message())
        bot.send_sticker(message.chat.id, message_generator.Sticker.error)


bot.polling()
