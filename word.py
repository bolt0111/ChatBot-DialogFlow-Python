class WordTranslation:
    def __init__(self, name, translation):
        self.name = name
        self.translation = translation


class WordDefinition:
    def __init__(self, name, origin, phonetic, definitions):
        self.name = name
        self.origin = origin
        self.phonetic = phonetic
        self.definitions = definitions


class WordMeaning:
    def __init__(self, meaning_type, definition, example, synonyms):
        self.type = meaning_type
        self.definition = definition
        self.example = example
        self.synonyms = synonyms
