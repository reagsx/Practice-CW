# Playing with Digits


def dig_pow(n, p):
    # your code
    count = 0
    v = []
    pw = []
    x = [int(i) for i in str(n)]
    for i in x:
        v.append(i ** (p + count))
        pw.append(p + count)
        count += 1
    k = sum(v)/n

    if sum(v) % n == 0:
        return k
    else:
        return -1
