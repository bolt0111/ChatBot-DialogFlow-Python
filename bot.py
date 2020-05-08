import time

import schedule
import telebot
from telebot import apihelper

import message_generator
import security

bot = telebot.TeleBot(security.TOKEN)
apihelper.proxy = {'https': security.PROXY}

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


@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    try:
        schedule.every().day.at('12:00').do(subscribe_message, message)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print("subscribing error: " + str(e) + "\n")


@bot.message_handler(commands=['unsubscribe'])
def unsubscribe():
    try:
        schedule.cancel_job(subscribe_message)
    except Exception as e:
        print("unsubscribe error: " + str(e) + "\n")


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, message_generator.message_help(commands))


@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_text(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
        bot.send_message(message.chat.id, message_generator.parse_word_definition(message.text.lower()))
    except Exception as e:
        print("Error with getting word definition: " + str(e))
        bot.send_message(message.chat.id, message_generator.error_message())
        bot.send_sticker(message.chat.id, message_generator.Sticker.error)


def subscribe_message(message):
    number_words = 5
    bot.send_message(message.chat.id, message_generator.random_words(number_words))


bot.polling()
