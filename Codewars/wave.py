def wave(word):
    collection = []
    if word == ' ':
        return ''
    for i in range(len(word)):
        x = []
        for l, k in enumerate(word):
            if l == i:
                x.append(k.upper())
            else:
                x.append(k)
            v = str(x)
        if v.islower() is False:
            collection.append(str(''.join(x)))
    return collection


wave('asdfasdfasd  asdfasdf awef aw waefaw fwea')
