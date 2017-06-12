def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        print(aStr)
        return False
    if len(aStr) == 1:
        print(aStr)
        return char == aStr
    if char == aStr[len(aStr) // 2]:
        print(aStr)
        return True
    elif char < aStr[len(aStr) // 2]:
        print(aStr)
        return isIn(char, aStr[:len(aStr) // 2])
    else:
        print(aStr)
        return isIn(char, aStr[len(aStr) // 2 + 1:])

print(isIn('w', 'cdhklmnnsuxyzz'))
