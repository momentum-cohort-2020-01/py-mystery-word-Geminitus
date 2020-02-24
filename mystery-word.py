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
        words = [w.replace('\n', '') for w in words]
        for word in words:
            if len(word) >= 4 and len(word) <= 6:
                easy_words.append(word)
            if len(word) > 6 and len(word) <= 8:
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


class Game:
    def __init__(self, difficulty, name):
        self.difficulty = difficulty
        self.name = name
        self.guesses = 0

    def play(self):
        if self.difficulty == 'easy':
            index_of_rand_word = randint(0, len(easy_words))
            rand_word = easy_words[index_of_rand_word]
            print(rand_word)
            choice = input(
                f'Press any letter to guess at the {len(rand_word)} letters long word: ')
            display_word = ''
            while display_word is not rand_word:
                if choice in rand_word:
                    rand_word.count(choice)
                    display_word = ''
                    while len(display_word) < len(rand_word):
                        if rand_word.index(choice) == len(display_word):
                            display_word += choice
                        else:
                            display_word += "_"
                    choice = input(
                        f'{display_word} is the Mystery Word so far. Press another key to make another guess. ')
                else:
                    self.guesses += 1
                    print(
                        "The letter you have chosen is not a part of the Mystery Word.")
        if self.difficulty == 'medium':
            index_of_rand_word = randint(0, len(medium_words))
            rand_word = medium_words[index_of_rand_word]
            choice = input(
                f'Press any letter to guess at the {len(rand_word)} letters long word')
            if choice in rand_word:
                print()
            else:
                print("The letter you have chosen is not a part of the Mystery Word.")
        if self.difficulty == 'hard':
            index_of_rand_word = randint(0, len(hard_words))
            rand_word = hard_words[index_of_rand_word]
            choice = input(
                f'Press any letter to guess at the {len(rand_word)} letters long word')
            if choice in rand_word:
                print()
            else:
                print("The letter you have chosen is not a part of the Mystery Word.")


new_game = Game('easy', 'Austin')
new_game.play()
