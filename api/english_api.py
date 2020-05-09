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
    keys = ['noun', 'exclamation', 'transitive verb']
    for key in keys:
        meaning_key = meaning.get(key)
        if meaning_key is not None:
            meaning_noun = meaning_key[0]
            meanings.append(WordMeaning("noun",
                                        meaning_noun.get('definition', ''),
                                        meaning_noun.get('example', ''),
                                        meaning_noun.get('synonyms', [])))
    return meanings


def __parse_word_definition(word):
    response = requests.get('https://api.dictionaryapi.dev/api/v1/entries/en/' + word)
    if response.status_code != 200:
        raise Exception('Can not load words due to error {}'.format(response.status_code))
    data = response.json()[0]
    return WordDefinition(data['word'],
                          data.get('phonetic', ''),
                          data.get('origin', ''),
                          __parse_word_meaning(data['meaning']))


def parse_word_definition(message):
    word = __parse_word_definition(message)
    word_definition = word.name + "\n" + word.origin + "\n" + word.phonetic + "\n"
    for definition in word.definitions:
        word_definition = word_definition + \
                          definition.type + "\n" + \
                          definition.definition + "\n" + \
                          definition.example + "\n" + \
                          ' '.join(definition.synonyms) + "\n\n"
    return word_definition


word_dictionary = __load_words()


def get_random_words(number):
    random_numbers = random.sample(word_dictionary, number)
    result = ""
    for word in random_numbers:
        result = result + message_generator.Emoji.zap + word.name + "\n" + word.translation + "\n\n"
    return result
