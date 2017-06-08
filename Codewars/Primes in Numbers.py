from math import sqrt
def primeFactors(n):
    print(n)
    results = []
    final = {}
    endgame = []
    x = n

    print(sqrt(n))
    for i in range(2, int(sqrt(n+1))):
        while x % i == 0:
            x //= i
            if i in final:
                final[i] += 1
            else:
                final[i] = 1
    if x != 1:
        final[x] = 1

    if final == {}:
        return('(' + str(n) + ')')
    else:
        for k, v in sorted(final.items()):
            if v == 1:
                endgame += ['(' + str(k) + ')']
            else:
                endgame += ['(' + str(k) + '**' + str(v) + ')']
    print(''.join(endgame))

primeFactors(933555431)
