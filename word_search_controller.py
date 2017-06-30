import word_search_model as model

class Logic(object):
    """Class representing the word search solver controller.

    Attributes:
        grid: List of lists representing the word search grid.
        words_to_find: Dictionary with key representing a word to be found in
            word search grid and value representing the location of the word's
            first character.
    """

    def __init__(self):
        """Constructor for Logic object."""
        self.grid = None
        self.words_to_find = None

    def set_grid(self, grid):
        """Setter for grid attribute.

        Args:
            grid: List of lists representing the word search grid.
        """
        self.grid = grid

    def set_words_to_find(self, words_to_find):
        """Setter for words_to_find attribute.

        Args:
            words_to_find: Dictionary with key representing a word to be found
                in word search grid and value representing the location of the
                word's first character.
        """
        self.words_to_find = words_to_find

    def solve(self):
        """Call word search solver model to solve word search."""
        print("logic is calling model") # For debugging purposes
        result = model.solve(self.grid, self.words_to_find)
        print(result) # For debugging purposes
        return result
