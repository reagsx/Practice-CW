def find_nb(m):

    ''' m is total volume of building, building is a
    pyramid with n^3 base reducing by n-1
    and 1 cubic unit at the top '''

    if m == 1:
        return 1
    else:
        find_nb(m-1)

find_nb(4183059834009)
