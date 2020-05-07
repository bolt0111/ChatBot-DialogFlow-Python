import requests

from model.WordTranslation import Word


def load_words():
    word_list = []
    response = requests.get('https://www.randomlists.com/data/vocabulary-words.json')
    if response.status_code != 200:
        raise Exception('Can not load words due to error {}'.format(response.status_code))
    for word in response.json()['data']:
        word_list.append(Word(word['name'], word['detail']))
    return word_list


def get_word_definition(word):
    response = requests.get('')
