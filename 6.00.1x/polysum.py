import math


def polysum(n, s):

    """ A regular polygon has 'n' number of sides.Each side has
    length 's'. This function returns the sum of the area and perimeter
    squared. """

    perimeter = s * n
    area = (.25*n*s**2) / (math.tan(math.pi/n))
    return round(area + perimeter**2, 4)
