import WordSearch as model

class Logic(object):
    def __init__(self):
        self.wordsearch = None
        self.words = None

    def setWordSearch(self, wordsearch):
        self.wordsearch = wordsearch

    def setWords(self, words):
        self.words = words

    def solve(self):
        print("logic is calling model")
        result = model.wordSearch(self.words, self.wordsearch)
        print(result)
        return result
