from uzwords import words
from difflib import Match, get_close_matches


def checkWord(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    avilable = False

    if word in matches:
        avilable = True
        matches = word
    elif
    return {'avilable': avilable, 'matches': matches}

if __name__ == '__main__':
    print(checkWord('ҳато'))
    print(checkWord('хато'))
    print(checkWord('тариҳ'))

print(get_close_matches('тарих', words))

# print(len(words))
# print(words[0])
# print(words[-1])
# print(words[7777])
# print(words[13213])