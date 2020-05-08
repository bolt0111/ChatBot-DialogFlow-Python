import random

from emoji import emojize

import eng_api

word_dictionary = eng_api.load_words()


class Sticker:
    start = "CAACAgIAAxkBAAJgm160BuSWPFMPVMTqEfEBUlyyXmxXAAK4AAMw1J0R92WGDc8M6xUZBA"
    error = "CAACAgIAAxkBAAJgyF60QXVbKI-P1OazlkXJGNzKA1uCAALSAAMw1J0RgmKBtdzOYJcZBA"


class Emoji:
    zap = emojize(":zap:", use_aliases=True)
    smile = emojize(":relaxed:", use_aliases=True)


def random_words(number):
    random_numbers = random.sample(word_dictionary, number)
    result = ""
    for word in random_numbers:
        result = result + Emoji.zap + word.name + "\n" + word.translation + "\n\n"
    return result


def hello_message():
    return "Hey! This is Baya Bot, let's learn English " + Emoji.smile


def error_message():
    return "Oh well ... Something went wrong"


def message_help(commands):
    help_text = "The following commands are available: \n\n"
    for key in commands:
        help_text += "/" + key + ": " + commands[key] + "\n"
    return help_text


def parse_word_definition(message):
    word = eng_api.get_word_definition(message)
    word_definition = word.name + "\n" + word.origin + "\n" + word.phonetic + "\n"
    for definition in word.definitions:
        word_definition = word_definition + \
                          definition.type + "\n" + \
                          definition.definition + "\n" + \
                          definition.example + "\n" + \
                          ' '.join(definition.synonyms) + "\n\n"
    return word_definition
