import random
import re


def hole_in_sentence(string):
    # Returns an with a random word replaced by ____, and the missing word, as a dict
    string_list = re.findall("\w*", string)
    words = []
    for word in string_list:
        if len(word) > 3:
            words.append(word)
    word_to_replace = random.sample(words, 1)[0]
    holed_sentence = string.replace(word_to_replace, '______')
    response = {'quote': holed_sentence, 'missing_word': word_to_replace}
    return response


print(hole_in_sentence("Le ciel sait que l'on saigne, sous nos cagoules"))
