"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
        reads words from a file

        >>> wf = WordFinder("testWords.txt")
        3 words read
    
    """
    def __init__(self, file_name):
        """creates the wordFinder, takes in a filepath for a txt document of words, tells how many words in document"""
        word_file = open(file_name, "r")

        self.words = []

        for line in word_file:
            #use rstrip to remove the linebreak
            self.words.append(line.strip())

        word_file.close()
        file_len = len(self.words)

        print(f"{file_len} words read")

    def random(self):
        """returns a random word from the file"""
        ind = random.randint(0,len(self.words)-1)
        print(self.words[ind])
        return self.words[ind]

