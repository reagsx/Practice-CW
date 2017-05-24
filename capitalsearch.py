def capitals(word):
    print (word)
    pos = 0
    l = []
    for i in word:
        if i.isupper():
            l.append(pos)
        pos += 1
    print(l)

capitals('DiLdOzEr')
