def wordSearch(words, lettergrid):
    for word in words:
        found = False
        row = 0
        while row < len(lettergrid) and not found:
            column = 0
            while column < len(lettergrid[row]) and not found:
                wordchar = 0
                if word[wordchar] == lettergrid[row][column]:
                    #Horizontal left to right
                    columncopy = column
                    while not found:
                        if wordchar >= len(word):
                            found = True
                            break
                        elif columncopy > len(lettergrid[row]):
                            wordchar = 0
                            break
                        if word[wordchar] == lettergrid[row][columncopy]:
                            columncopy += 1
                            wordchar += 1
                        else:
                            wordchar = 0
                            break
                    columncopy = None
                    #Vertical top to bottom
                    rowcopy = row
                    while not found:
                        if wordchar >= len(word):
                            found = True
                            break
                        elif rowcopy > len(lettergrid):
                            wordchar = 0
                            break
                        if word[wordchar] == lettergrid[rowcopy][column]:
                            rowcopy += 1
                            wordchar += 1
                        else:
                            wordchar = 0
                            break
                    rowcopy = None
                    #Diagonal top to bottom right
                    rowcopy = row
                    columncopy = column
                    while not found:
                        if wordchar >= len(word):
                            found = True
                            break
                        elif rowcopy > len(lettergrid) or columncopy > len(lettergrid[row]):
                            wordchar = 0
                            break
                        if word[wordchar] == lettergrid[rowcopy][columncopy]:
                            rowcopy += 1
                            columncopy += 1
                            wordchar += 1
                        else:
                            wordchar = 0
                            break
                    rowcopy = None
                    columncopy = None
                    #Horizontal right to left
                    columncopy = column
                    while not found:
                        if wordchar >= len(word):
                            found = True
                            break
                        elif columncopy < 0:
                            wordchar = 0
                            break
                        if word[wordchar] == lettergrid[row][columncopy]:
                            columncopy -= 1
                            wordchar += 1
                        else:
                            wordchar = 0
                            break
                    columncopy = None
                    #Vertical bottom to top
                    rowcopy = row
                    while not found:
                        if wordchar >= len(word):
                            found = True
                            break
                        elif rowcopy < 0:
                            wordchar = 0
                            break
                        if word[wordchar] == lettergrid[rowcopy][column]:
                            rowcopy -= 1
                            wordchar += 1
                        else:
                            wordchar = 0
                            break
                    rowcopy = None
                    #Diagonal top to bottom left
                    rowcopy = row
                    columncopy = column
                    while not found:
                        if wordchar >= len(word):
                            found = True
                            break
                        elif rowcopy > len(lettergrid) or columncopy < 0:
                            wordchar = 0
                            break
                        if word[wordchar] == lettergrid[rowcopy][columncopy]:
                            rowcopy += 1
                            columncopy -= 1
                            wordchar += 1
                        else:
                            wordchar = 0
                            break
                    rowcopy = None
                    columncopy = None
                    #Diagonal bottom to top right
                    rowcopy = row
                    columncopy = column
                    while not found:
                        if wordchar >= len(word):
                            found = True
                            break
                        elif rowcopy < 0 or columncopy > len(lettergrid[row]):
                            wordchar = 0
                            break
                        if word[wordchar] == lettergrid[rowcopy][columncopy]:
                            rowcopy -= 1
                            columncopy += 1
                            wordchar += 1
                        else:
                            wordchar = 0
                            break
                    rowcopy = None
                    columncopy = None
                    #Diagonal bottom to top left
                    rowcopy = row
                    columncopy = column
                    while not found:
                        if wordchar >= len(word):
                            found = True
                            break
                        elif rowcopy < 0 or columncopy < 0:
                            wordchar = 0
                            break
                        if word[wordchar] == lettergrid[rowcopy][columncopy]:
                            rowcopy -= 1
                            columncopy -= 1
                            wordchar += 1
                        else:
                            wordchar = 0
                            break
                    rowcopy = None
                    columncopy = None
                    if found:
                        words[word] = [row, column]
                column += 1
            row += 1
    print("rows dealt with")
    return words

if __name__ == "__main__":
    words = {'much': False}
    wordsearch = [["h", "c", "u", "m"], ["o", "d", "o", "g"], ["w", "t", "h", "e"], ["i", "n", "x", "z"], ["s", "w", "i", "n"], ["t", "h", "a", "t"]]
    print(wordSearch(words, wordsearch))
