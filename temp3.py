import string
def getAvailableLetters(lettersGuessed):
    getAvailableLetters = string.ascii_lowercase
    y =''
    for x in getAvailableLetters:
        if x in lettersGuessed:
            pass
        else:
            y += x
    return y