def multiplication_table(row, col):

    return [[x * i for x in range(1, row+1)] for i in range(1, col+1)]


multiplication_table(3,3)
