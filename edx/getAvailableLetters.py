import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letterSet = set(string.ascii_lowercase)
    guessedSet = set(lettersGuessed)
    remainSet = letterSet.difference(guessedSet)
    remainList = list(remainSet)
    remainList.sort()
    return "".join(remainList)

print(getAvailableLetters(['g', 'a', 'l']))
