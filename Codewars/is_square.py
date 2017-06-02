import math


def is_square(n):
        return True if n > 0 and math.sqrt(n).is_integer() else False
