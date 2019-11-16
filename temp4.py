def isWordGuessed(secretWord,lettersGuessed):
    for x in secretWord:
        if x not in lettersGuessed:
            return False
        else:
            return True
def getGuessedWord(secretWord, lettersGuessed):
    getGuessedWord = ''
    for x in secretWord:
        if x in lettersGuessed:
            getGuessedWord += x
        else:
            getGuessedWord += ' _ '
    return getGuessedWord
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
def Hangaroo(secretWord):
    print ("Welcome to Hangaroo!")
    print ("you are challenged to guess for the secret word!")
    lettersGuessed=[]
    mistakesMade=0
    while (secretWord != lettersGuessed):
        if secretWord != getGuessedWord(secretWord, lettersGuessed):
            print ("Available letters:", getAvailableLetters(lettersGuessed))
            print (getGuessedWord (secretWord, lettersGuessed))
            print ("Mistakes Made = ", mistakesMade)
            w = input("Input your guess: ")
            wInLowerCase = w.lower()
            
            if wInLowerCase not in secretWord and wInLowerCase not in lettersGuessed:
                print("Your guess is not in the secret word! Try again")
                mistakesMade+=1
            elif wInLowerCase not in secretWord and wInLowerCase in lettersGuessed:
                print ("You've already made that guess! Try again")
            elif wInLowerCase in secretWord and wInLowerCase in lettersGuessed:
                print ("You've already made that guess! Try again")
            else:
                lettersGuessed.append(wInLowerCase)
                print ("NICE GUESS!")
            lettersGuessed.append(wInLowerCase)
        else:
            print ("Congratulations you have successfully guessed the secret word!")
            print ("The secret word is :", getGuessedWord(secretWord, lettersGuessed))
            print ("Mistakes made = ",mistakesMade)
            break