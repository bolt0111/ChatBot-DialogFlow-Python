import requests

from word import WordTranslation, WordDefinition, WordMeaning


def load_words():
    word_list = []
    response = requests.get('https://www.randomlists.com/data/vocabulary-words.json')
    if response.status_code != 200:
        raise Exception('Can not load words due to error {}'.format(response.status_code))
    for word in response.json()['data']:
        word_list.append(WordTranslation(word['name'], word['detail']))
    return word_list


def get_word_meaning(meaning):
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


def get_word_definition(word):
    response = requests.get('https://api.dictionaryapi.dev/api/v1/entries/en/' + word)
    if response.status_code != 200:
        raise Exception('Can not load words due to error {}'.format(response.status_code))
    data = response.json()[0]
    return WordDefinition(data['word'],
                          data.get('phonetic', ''),
                          data.get('origin', ''),
                          get_word_meaning(data['meaning']))
