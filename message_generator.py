from emoji import emojize


class Sticker:
    start = "CAACAgIAAxkBAAJgm160BuSWPFMPVMTqEfEBUlyyXmxXAAK4AAMw1J0R92WGDc8M6xUZBA"
    error = "CAACAgIAAxkBAAJgyF60QXVbKI-P1OazlkXJGNzKA1uCAALSAAMw1J0RgmKBtdzOYJcZBA"


class Emoji:
    zap = emojize(":zap:", use_aliases=True)
    smile = emojize(":relaxed:", use_aliases=True)
    sad = emojize(':pensive:', use_aliases=True)
    confused = emojize(':face_with_monocle:', use_aliases=True)


class Message:
    hello = "Hey! This is Baya Bot, let's learn English " + Emoji.smile
    error = "Oh well ... Something went wrong " + Emoji.sad
    unknown_answer = "Oh well, I missed what you said. What was that? " + Emoji.confused


def message_help(commands):
    help_text = "The following commands are available: \n\n"
    for key in commands:
        help_text += "/" + key + ": " + commands[key] + "\n"
    return help_text
