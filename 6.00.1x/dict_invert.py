def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    dinv = {}
    for k, v in d.items():
        print(k, v)
        if v not in dinv:
            dinv[v] = [k]
        else:
            dinv[v].append(k)
    for i in dinv.values():
        i.sort()
    return dinv


dict_invert({6: 30, 2: 30, 8: 54, 1: 10, 2: 20, 3: 30, 4: 30})
dict_invert({4:True, 2:True, 0:True})
