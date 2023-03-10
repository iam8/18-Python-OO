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

    >>> finder = WordFinder("./words.txt")
    235886 words read.

    >>> finder.print_num_words()
    235886 words read.

    >>> finder.random() in finder.words
    True

    >>> finder.random() in finder.words
    True

    >>> finder.random() in finder.words
    True

    >>> finder
    WordFinder(dict_path='./words.txt')
    """

    def __init__(self, dict_path):
        """
        Create a new WordFinder and report number of words read from the file at the given
        dictionary file path.
        """

        self.dict_path = dict_path
        self.words = self.read_file()

        self.print_num_words()

    def __repr__(self):
        """
        Return string representation of WordFinder instance.
        """

        return f"WordFinder(dict_path='{self.dict_path}')"

    def read_file(self):
        """
        Read the dictionary file and create a list that contains all the words from that file.
        """

        with open(self.dict_path, "rt") as file:
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


class SpecialWordFinder(WordFinder):
    """
    Extends WordFinder class.

    Blank lines or commented-out lines in the given file of words will be ignored.

    >>> spec_finder = SpecialWordFinder("./words_special.txt")
    7 words read.

    >>> spec_finder.print_num_words()
    7 words read.

    >>> spec_finder.random() in spec_finder.words
    True

    """

    def read_file(self):
        """
        Read the dictionary file and create a list that contains all the words from that file.

        Blank lines or commented-out lines in the dictionary file (lines that begin with a #) will
        not be included in the SpecialWordFinder.
        """

        with open(self.dict_path, "rt") as file:
            return [line.strip() for line in file
                    if line.strip() and not line.strip().startswith("#")]
