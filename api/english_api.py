import random

import requests

import message_generator
from api.word import WordTranslation, WordMeaning, WordDefinition


def __load_words():
    word_list = []
    response = requests.get('https://www.randomlists.com/data/vocabulary-words.json')
    if response.status_code != 200:
        raise Exception('Can not load words due to error {}'.format(response.status_code))
    for word in response.json()['data']:
        word_list.append(WordTranslation(word['name'], word['detail']))
    return word_list


def __parse_word_meaning(meaning):
    meanings = []
    keys = ['noun', 'exclamation', 'transitive verb', 'adjective', 'verb', 'preposition', 'conjunction', 'adverb']
    for key in keys:
        meaning_key = meaning.get(key)
        if meaning_key is not None:
            meaning_noun = meaning_key[0]
            meanings.append(WordMeaning(key,
                                        meaning_noun.get('definition', None),
                                        meaning_noun.get('example', None),
                                        meaning_noun.get('synonyms', None)))
    return meanings


def __parse_word_definition(word):
    response = requests.get('https://api.dictionaryapi.dev/api/v1/entries/en/' + word)
    if response.status_code != 200:
        raise Exception('Can not load words due to error: {}'.format(response.json().get('message')))
    data = response.json()[0]
    return WordDefinition(data['word'],
                          data.get('phonetic', None),
                          data.get('origin', None),
                          __parse_word_meaning(data['meaning']))


def __parse_synonyms(synonyms):
    if synonyms is not None:
        return "*Synonyms:* " + ' / '.join(synonyms) + "\n"
    else:
        return ""


def __parse_information(definition_name, definition):
    if definition is not None:
        return definition_name + " " + definition + "\n"
    else:
        return ""


def parse_word_definition(message):
    word = __parse_word_definition(message)
    word_definition = __parse_information(message_generator.Emoji.zap, "*" + word.name + "*") + "\n" + \
                      __parse_information("[", word.origin + "]") + "\n" + \
                      __parse_information("**", word.phonetic + "**") + "\n\n"

    for definition in word.definitions:
        word_definition = word_definition + \
                          __parse_information(message_generator.Emoji.check, definition.type) + \
                          __parse_information("*Meaning:*", definition.definition) + \
                          __parse_information("*Example:*", definition.example) + \
                          __parse_synonyms(definition.synonyms) + "\n"
    return word_definition


word_dictionary = __load_words()


def get_random_words(number):
    random_numbers = random.sample(word_dictionary, number)
    result = ""
    for word in random_numbers:
        result = result + message_generator.Emoji.zap + word.name + "\n" + word.translation + "\n\n"
    return result
