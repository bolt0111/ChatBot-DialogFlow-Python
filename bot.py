import time

import schedule
import telebot
from telebot import apihelper

import api.dialogflow_api as dialog_flow
import api.english_api as english_api
import message_generator
import security

bot = telebot.TeleBot(security.TOKEN)
apihelper.proxy = {'https': security.PROXY}

commands = {  # command description used in the "help" command
    'start': 'Start learning English',
    'help': 'Information about the available commands',
    'translate': 'Get word meaning and full information',
    'subscribe': 'Start learning English by 5 words everyday',
    'unsubscribe': 'Stop sending 5 words'
}


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_sticker(message.chat.id, message_generator.Sticker.start)
    bot.send_message(message.chat.id, message_generator.Message.hello)
    command_help(message)


@bot.message_handler(commands=['subscribe'])
def command_subscribe(message):
    try:
        schedule.every().day.at('12:00').do(subscribe_message, message)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print("subscribing error: " + str(e) + "\n")


@bot.message_handler(commands=['unsubscribe'])
def command_unsubscribe():
    try:
        schedule.cancel_job(subscribe_message)
    except Exception as e:
        print("unsubscribe error: " + str(e) + "\n")


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, message_generator.message_help(commands))


@bot.message_handler(commands=['translate'])
def command_translate(message):
    bot.register_next_step_handler_by_chat_id(message.chat.id, callback=command_translate_word)


def command_translate_word(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
        bot.send_message(message.chat.id, english_api.parse_word_definition(message.text.lower()))
    except Exception as e:
        print("Error with getting word definition: " + str(e))
        bot.send_message(message.chat.id, message_generator.Message.error)
        bot.send_sticker(message.chat.id, message_generator.Sticker.error)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_message(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
        bot.send_message(message.chat.id, dialog_flow.call_small_talk(message.text.lower()))
    except Exception as e:
        print("Error with getting answer from small talk: " + str(e))
        bot.send_message(message.chat.id, message_generator.Message.unknown_answer)
        bot.send_sticker(message.chat.id, message_generator.Sticker.error)


def subscribe_message(message):
    number_words = 5
    bot.send_message(message.chat.id, english_api.get_random_words(number_words))


bot.polling()
