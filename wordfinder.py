# Ioana A Mititean
# 12/19/22
# 18.8: Python OOP Exercise

"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """
    Class to find random words from a given dictionary.

    dict_path (str): path to a 'dictionary' file on disk. The file must contain words, with one
    word per line.

    """

    def __init__(self, dict_path):
        self.dict_path = dict_path
        self.words = self.read_file()

        self.print_num_words()

    def read_file(self):
        """
        Read the dictionary file and create a list that contains all the words from that file.
        """

        with open(self.dict_path) as file:
            return [word.strip() for word in file]

    def print_num_words(self):
        """
        Print a message showing the total number of words read in from the dictionary file.
        """

        print(f"{len(self.words)} words read.")

    def random(self):
        """
        Return a random word from the dictionary file.
        """

        return choice(self.words)



