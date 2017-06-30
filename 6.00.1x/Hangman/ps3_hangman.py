# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import string
import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    x = [w for w in secretWord]
    y = x[:]
    for i in x:
        if i in lettersGuessed:
            while i in y:
                y.remove(i)
    if y == []:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    x = [w for w in secretWord]
    y = []
    for i in x:
        if i in lettersGuessed:
            y.append(i)
        else:
            y.append(' _')

    return(''.join(y))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    x = [l for l in string.ascii_lowercase]
    for i in lettersGuessed:
        if i in x:
            x.remove(i)
    return ' '.join(x)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long')

    guesses = 8
    lettersGuessed = []
    secWordlist = [x for x in secretWord]

    while guesses > 0 and isWordGuessed(secretWord, lettersGuessed) is False:
        print('-----------')
        print('You have', str(guesses), 'guesses left')
        print('Available Letters:', getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        lowercaseGuess = guess.lower()

        if lowercaseGuess not in lettersGuessed:
            lettersGuessed.append(lowercaseGuess)
            if lowercaseGuess in secWordlist:
                print('Good Guess:',
                      getGuessedWord(secretWord, lettersGuessed))
            else:
                print('OOPS! That letter is not in my word:',
                      getGuessedWord(secretWord, lettersGuessed))
                guesses -= 1
        elif lowercaseGuess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
    if isWordGuessed(secretWord, lettersGuessed) is True:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ', secretWord, '.', sep='')








# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
