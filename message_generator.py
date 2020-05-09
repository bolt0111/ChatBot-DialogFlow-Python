from emoji import emojize


class Sticker:
    start = "CAACAgIAAxkBAAJlvV62spvcM24UodEoOMaOBqm3VQ2JAAIMAAPLm8wYVeUb04BjW2wZBA"
    error = "CAACAgIAAxkBAAJlv162srQ4pKVlw_GTpi2LWHi7udoHAAILAAPLm8wYHXFmgN4_n68ZBA"
    smile = "CAACAgIAAxkBAAJlwV62ss5B_1oEs4p6WJ6AVkquBP0hAAIKAAPLm8wYZd7Zi1a78BwZBA"


class Emoji:
    zap = emojize(":zap:", use_aliases=True)
    smile = emojize(":relaxed:", use_aliases=True)
    sad = emojize(':pensive:', use_aliases=True)
    confused = emojize(':face_with_monocle:', use_aliases=True)
    check = emojize(":white_check_mark:", use_aliases=True)


class Message:
    hello = "Hey! This is Baya Bot, let's learn English " + Emoji.smile
    error = "Oh well ... Something went wrong " + Emoji.sad
    unknown_answer = "Oh well, I missed what you said. What was that? " + Emoji.confused


def message_help(commands):
    help_text = "The following commands are available: \n\n"
    for key in commands:
        help_text += "/" + key + ": " + commands[key] + "\n"
    return help_text
