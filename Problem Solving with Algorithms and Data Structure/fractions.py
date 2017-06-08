from frac_utilities import gcd


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

    def __repr__(self):
        return '%s(%r)' % (self.__class__, self.__str__())

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other):
        newnum = self.num*other.den + \
                    self.den*other.num
        newden = self.den * other.den

        # common = gcd(newnum, newden)

        return Fraction(newnum, newden)

# this is evidently called when __add__ doesn't know what is going on
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            other = Fraction(other, 1)
            return self.__add__(other)

# __iadd__ for fractions
    def __iadd__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.__add__(other)

    def __sub__(self, other):
        newnum = self.num*other.den - \
                    self.den*other.num
        newden = self.den * other.den

        # common = gcd(newnum, newden)

        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        # common = gcd(newnum, newden)

        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.den

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

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


def readFraction():
    n = readInt('numerator')
    d = readInt('denominator')
    return Fraction(n, d)
