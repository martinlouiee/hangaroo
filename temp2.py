def getGuessedWord(secretWord, lettersGuessed):
    getGuessedWord = ''
    for x in secretWord:
        if x in lettersGuessed:
            getGuessedWord += x
        else:
            getGuessedWord += ' _ '
    return getGuessedWord