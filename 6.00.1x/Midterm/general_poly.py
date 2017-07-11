def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def structure(x):
        d = 0
        n = len(L) - 1
        for i in range(len(L)):
            d += L[i]*x**n
            n -= 1
        return d
    return structure

print(general_poly([1, 2, 3, 4])(10))
