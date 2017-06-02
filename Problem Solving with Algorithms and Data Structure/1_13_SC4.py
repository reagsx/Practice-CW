from fractions import gcd

# Removed to use built in function
# def gcd(m, n):
#    while m % n != 0:
#        oldm = m
#        oldn = n
#        m = oldn
#        n = oldm % oldn
#    return n


class Fraction:
    def __init__(self, top, bottom):
        if not isinstance(top, int):
            NumError = ValueError(
                "{} is not a valid choice! Use an integer silly goose!", top
            )
            raise NumError
        if not isinstance(bottom, int):
            NumError = ValueError(
                "{} is not a valid choice! Use an integer slick willy!", bottom
            )
        if top > 0 and bottom > 0:
            top = abs(top)
            bottom = abs(bottom)
        elif bottom < 0:
            top = - top
            bottom = abs(bottom)

        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + \
                    self.den*otherfraction.num
        newden = self.den * otherfraction.den

        # common = gcd(newnum, newden)

        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.num*otherfraction.den - \
                    self.den*otherfraction.num
        newden = self.den * otherfraction.den

        # common = gcd(newnum, newden)

        return Fraction(newnum, newden)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den

        # common = gcd(newnum, newden)

        return Fraction(newnum, newden)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.den

        # common = gcd(newnum, newden)

        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def _getNum(self):
        return self.num

    def getDen(self):
        return self.den


x = Fraction(1, -2)
y = Fraction(2, 3)
print(x + y)
print(x == y)
print(x > y)
print(x * y)
print(x / y)
print(x < y)
