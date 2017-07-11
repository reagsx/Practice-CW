def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    print(sorted(L2, key=lambda e: (isinstance(e, (float, int)), e)) != \
                sorted(L1, key=lambda e: (isinstance(e, (float, int)), e)))

    if (len(L1) != len(L2)) or (
            sorted(L2, key=lambda e: (isinstance(e, (float, int)), e)) !=
            sorted(L1, key=lambda e: (isinstance(e, (float, int)), e))):
        return False

    elif L1 == [] and L2 == []:
        return ('None', 'None', 'None')

    else:
        mostfrequent = max(set(L1), key=L1.count)
        timesappeared = L1.count(mostfrequent)
        ftype = type(mostfrequent)
        return(mostfrequent, timesappeared, ftype)


print(is_list_permutation(['a', 'a', 'b'], ['a', 'b']))
print(is_list_permutation([1, 'b', 1, 'c', 'c', 1], ['c', 1, 'b', 1, 1, 'c']))
print(is_list_permutation([], []))
print(is_list_permutation([0, 4, 8, 3, 0, 2, 2, 1, 4, 7, 8, 3, 7, 0, 0], [3, 4, 0, 3, 8, 0, 2, 0, 7, 2, 0, 3, 7, 2, 1]))
print(is_list_permutation([1, 2, 1], [2, 1, 2]))
