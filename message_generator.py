import random

from emoji import emojize

import eng_api

word_dictionary = eng_api.load_words()


class Sticker:
    start = "CAACAgIAAxkBAAJgm160BuSWPFMPVMTqEfEBUlyyXmxXAAK4AAMw1J0R92WGDc8M6xUZBA"


class Emoji:
    zap = emojize(":zap:", use_aliases=True)
    smile = emojize(":relaxed:", use_aliases=True)


def random_words(number):
    random_numbers = random.sample(word_dictionary, number)
    result = ""
    for word in random_numbers:
        result = result + Emoji.zap + word.name + "\n" + word.definition + "\n\n"
    return result


def hello_message():
    return "Hey! This is Baya Bot, let's learn English " + Emoji.smile
