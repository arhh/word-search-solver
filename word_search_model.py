def match_horizontal(word, row, column, grid):
    """Horizontally match a word's characters with those in the word search.

    Args:
        word: A string representing the word to match.
        row: An integer representing the row containing some subset of
            characters in word.
        column: An integer representing the column currently being pointed
            to.

    Returns:
        A boolean representing whether or not a complete match has been
        made beginning at the row and column passed as arguments.
    """
    word_index = 0 # Indexes the current word
    match_success = True
    # Begin left to right match:
    while word_index < len(word) and match_success == True:
        character_to_match = word[word_index]
        # If the character being pointed to in the grid matches the character being pointed to in the word to match:
        if column < len(grid[0]) and character_to_match == grid[row][column]:
            word_index += 1
            column += 1
        else:
            match_success = False

    # Begin right to left match:
    if match_success == False:
        column -= word_index # Decrement column to equal initial value when match_horizontal was called
        word_index = 0
        match_success = True
        while word_index < len(word) and match_success == True:
            character_to_match = word[word_index]
            # If the character being pointed to in the grid matches the character being pointed to in the word to match:
            if column >= 0 and character_to_match == grid[row][column]:
                word_index += 1
                column -= 1
            else:
                match_success = False

    return match_success


def match_vertical(word, row, column, grid):
    """Vertically match a word's characters with those in the word search.

    Args:
        word: A string representing the word to match.
        row: An integer representing the row containing some subset of
            characters in word.
        column: An integer representing the column currently being pointed
            to.

    Returns:
        A boolean representing whether or not a complete match has been
        made beginning at the row and column passed as arguments.
    """
    word_index = 0 # Indexes the current word
    match_success = True
    # Begin top to bottom match:
    while word_index < len(word) and match_success == True:
        character_to_match = word[word_index]
        # If the character being pointed to in the grid matches the character being pointed to in the word to match:
        if row < len(grid) and character_to_match == grid[row][column]:
            word_index += 1
            row += 1
        else:
            match_success = False

    # Begin bottom to top match:
    if match_success == False:
        row -= word_index # Decrement row to equal initial value when match_vertical was called
        word_index = 0
        match_success = True
        while word_index < len(word) and match_success == True:
            character_to_match = word[word_index]
            # If the character being pointed to in the grid matches the character being pointed to in the word to match:
            if row >= 0 and character_to_match == grid[row][column]:
                word_index += 1
                row -= 1
            else:
                match_success = False

    return match_success


def match_diagonal_left_right(word, row, column, grid):
    """Diagonally match a word's characters with those in the word search.

    Diagonally match a word's characters with those in the word search going
    from top-left to bottom-right or bottom-right to top-left.

    Args:
        word: A string representing the word to match.
        row: An integer representing the row containing some subset of
            characters in word.
        column: An integer representing the column currently being pointed
            to.

    Returns:
        A boolean representing whether or not a complete match has been
        made beginning at the row and column passed as arguments.
    """
    word_index = 0 # Indexes the current word
    match_success = True
    # Begin top-left to bottom-right match:
    while word_index < len(word) and match_success == True:
        character_to_match = word[word_index]
        # If the character being pointed to in the grid matches the character being pointed to in the word to match:
        if column < len(grid[0]) and row < len(grid) and character_to_match == grid[row][column]:
            word_index += 1
            column += 1
            row += 1
        else:
            match_success = False

    # Begin bottom-right to top-left match:
    if match_success == False:
        column -= word_index # Decrement column to equal initial value when match_diagonal was called
        row -= word_index # Decrement row to equal initial value when match_diagonal was called
        word_index = 0
        match_success = True
        while word_index < len(word) and match_success == True:
            character_to_match = word[word_index]
            # If the character being pointed to in the grid matches the character being pointed to in the word to match:
            if column >= 0 and row >= 0 and character_to_match == grid[row][column]:
                word_index += 1
                column -= 1
                row -= 1
            else:
                match_success = False

    return match_success


def match_diagonal_right_left(word, row, column, grid):
    """Diagonally match a word's characters with those in the word search.

    Diagonally match a word's characters with those in the word search going
    from top-right to bottom-left or bottom-left to top-right.

    Args:
        word: A string representing the word to match.
        row: An integer representing the row containing some subset of
            characters in word.
        column: An integer representing the column currently being pointed
            to.

    Returns:
        A boolean representing whether or not a complete match has been
        made beginning at the row and column passed as arguments.
    """
    word_index = 0 # Indexes the current word
    match_success = True
    # Begin top-right to bottom-left match:
    while word_index < len(word) and match_success == True:
        character_to_match = word[word_index]
        # If the character being pointed to in the grid matches the character being pointed to in the word to match:
        if column >= 0 and row < len(grid) and character_to_match == grid[row][column]:
            word_index += 1
            column -= 1
            row += 1
        else:
            match_success = False

    # Begin bottom-left to top-right match:
    if match_success == False:
        column += word_index # Decrement column to equal initial value when match_diagonal was called
        row -= word_index # Decrement row to equal initial value when match_diagonal was called
        word_index = 0
        match_success = True
        while word_index < len(word) and match_success == True:
            character_to_match = word[word_index]
            # If the character being pointed to in the grid matches the character being pointed to in the word to match:
            if column < len(grid[0]) and row >= 0 and character_to_match == grid[row][column]:
                word_index += 1
                column += 1
                row -= 1
            else:
                match_success = False

    return match_success


match_algorithms = [match_horizontal, match_vertical, match_diagonal_left_right, match_diagonal_right_left]

def solve(grid, words_to_find):
    """Solve word search.

    Solve word search by producing the location of the first letter for each
    word in the word search grid.

    Args:
        grid: A list of lists representing a word search grid.
        words_to_find: A dictionary with the key representing the word to
            be found in grid and value representing location of beginning
            of word in grid.

    Returns:
        A dictionary with the key representing the word to be found in
        grid and value representing location of beginning of word in
        grid.
    """
    for word in words_to_find: # Go through each word in the list of words to match
        row = 0 # Points to row in grid when searching
        column = 0 # Points to column in grid when searching
        is_matched = False
        while row < len(grid) and is_matched == False:
            character_to_match = word[0] # Assign first character of current word
            # Move to start of next row if at end of current row:
            if column >= len(grid[0]):
                column = 0
                row += 1
                continue
            # If the character being pointed to in the grid matches the character being pointed to in the word to match:
            elif character_to_match == grid[row][column]:
                for algorithm in match_algorithms:
                    is_matched = algorithm(word, row, column, grid)
                    if is_matched == True:
                        words_to_find[word] = (row, column)
                        break
            column += 1

    return words_to_find


if __name__ == "__main__":
    # The test grid here is a list of strings rather than a list of lists as described in the doc string.
    grid = ["ttowarddvbnay", "eadhbvreeyows", "ooeohawestrka", "ksyawedisetor", "wanyenabvahib", "wgkhsaroeagad", "ashtrdbbohcro", "cweuearotkito", "wawovwuawelnv", "wwbseaoawewsd", "gahprwrlfrrbb", "sywwudyterods", "tsaedaehabofr"]
    words_to_find = {"above": False, "ahead": False, "away": False, "backward": False, "behind": False, "below": False, "down": False, "east": False, "forward": False, "left": False, "north": False, "reverse": False, "right": False, "sideways": False, "skyward": False, "south": False, "toward": False, "up": False, "west": False}
    print(solve(grid, words_to_find))
