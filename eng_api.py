import random

import requests

word_dictionary = {}


def load_words():
    response = requests.get('https://www.randomlists.com/data/vocabulary-words.json')
    if response.status_code != 200:
        raise Exception('Can not load words due to error {}'.format(response.status_code))
    for todo_item in response.json()['data']:
        word_dictionary[todo_item['name']] = todo_item['detail']


def random_words(number):
    random_numbers = random.sample(word_dictionary.keys(), number)
    result = ""
    for key in random_numbers:
        result = result + key + "\n" + word_dictionary.get(key) + "\n\n"
    return result
