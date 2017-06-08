
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


def readInt(val=''):
    while True:
        n = input("value {}: ".format(val))
        try:
            n = int(n)
            return n
        except ValueError:
            print("Non numeric input - please try again!")
