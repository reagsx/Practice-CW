def find_children(dancing_brigade):
    '''iterate over letters, find capitals, match lowercase'''
    return sorted(dancing_brigade, key = lambda v: (v.upper(), v[0].islower()))




find_children("xXfuUuuF")
