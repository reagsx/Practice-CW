import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    x = [l for l in string.ascii_lowercase]
    for i in lettersGuessed:
        if i in x:
            x.remove(i)
    return ' '.join(x)




lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
