"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
        reads words from a file and allows to randomly pick one
    """
    def __init__(self, file_name):
        """creates the wordFinder, takes in a filepath for a txt document of words, tells how many words in document"""
        word_file = open(file_name, "r")
        self.words=[]
        self.words = self.parseFile(word_file)

        file_len = len(self.words)

        print(f"{file_len} words read")

    def parseFile(self, word_file):
        """parses the file into an array of words"""
        words = []
        for line in word_file:
            #use rstrip to remove the linebreak
            words.append(line.strip())
        word_file.close()

        return words

    def random(self):
        """returns a random word from the file"""
        ind = random.randint(0,len(self.words)-1)
        return self.words[ind]


class SpecialWordFinder(WordFinder):
    """
        a class that reads words from a file and allows to randomly pick one
        works with files that have blank lines and comments, does not return blank lines or comment lines
    """

    def parseFile(self, word_file):
        """parses the file into an array of words"""
        words = []
        for line in word_file:
            #removes comments and blanklines
            if not line.startswith("#") and line.strip()!="":
                words.append(line.strip())
        word_file.close()

        return words
