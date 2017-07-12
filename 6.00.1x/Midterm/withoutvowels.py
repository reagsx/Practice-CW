def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    voweless_string = ''
    for i in s:
        if i not in vowels:
            voweless_string += i
    print(voweless_string)

print_without_vowels('My family goes to the market on sunday.')
