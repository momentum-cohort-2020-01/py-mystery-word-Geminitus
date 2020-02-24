import string
from random import randint

easy_words = []
medium_words = []
hard_words = []


def get_words(file):
    with open(file) as file:
        word_lines = ' '.join(file.readlines())
        l_word_lines = word_lines.lower()
        words = l_word_lines.split(' ')
        for word in words:
            if len(word) >= 4 or len(word) <= 6:
                easy_words.append(word)
            if len(word) > 6 or len(word) <= 8:
                medium_words.append(word)
            if len(word) > 8:
                hard_words.append(word)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the words in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        get_words(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
easy_words = [w.replace('\n', '') for w in easy_words]
medium_words = [w.replace('\n', '') for w in medium_words]
hard_words = [w.replace('\n', '') for w in hard_words]


class Game:
    def __init__(self, difficulty, name):
        self.difficulty = difficulty
        self.name = name

    def play(difficulty):
        if difficulty == 'easy':
            index_of_rand_word = randint(0, len(easy_words))


class Player:
    def __init__(self, name):
        self.name = name


class Word:
    def __init__(self):
