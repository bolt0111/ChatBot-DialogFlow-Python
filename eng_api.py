import requests


def load_words():
    word_dictionary = {}
    response = requests.get('https://www.randomlists.com/data/vocabulary-words.json')
    if response.status_code != 200:
        raise Exception('Can not load words due to error {}'.format(response.status_code))
    for todo_item in response.json()['data']:
        word_dictionary[todo_item['name']] = todo_item['detail']
    return word_dictionary
