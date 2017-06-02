"""Using enumerate with only pulling the position
   if capital would have been better """


def capitals(word):
    print(word)
    pos = 0
    l = []
    for i in word:
        if i.isupper():
            l.append(pos)
        pos += 1
    print(l)
