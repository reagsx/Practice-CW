''' find the longest palindrome in the substrings of a given string '''


def longest_palindrome(s):
    pally = []
    length = len(s)
    # if nothing is given return 0
    if length == 0:
        return 0
    # break down the string into substrings
    subs = [s[i:x+1] for i in range(length) for x in range(i, length)]
    # iterate through the strings and look for palindromes
    for d in subs:
        if d == d[::-1]:
            pally.append(d)
    # return the length of the longest palindrome
    return len(max(pally, key=len))
