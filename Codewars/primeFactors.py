""" It currently cannot complete fast enough, I think if the
prime number section is slowing it down with large numbers
it causes the whole thing to time out and it does not complete """


def primeFactors(n):
    results = []
    final = {}
    stupid = []
    # gets the list we'll be dividing by
    for i in range(2, n+1):
        if n % i == 0:
            fac = i
            for x in range(2, n+1):
                if ((fac % x) == 0) and (fac == x):
                    if x in results:
                        results.append(x)
                    else:
                        results.append(x)
                elif ((fac % x) == 0) or (fac < x):
                    break
# Use the list we made to start seeing how many times we can divide,
# and build a dictionary that keeps track
    for o in results:
        v = n
        while v % o == 0:
            v /= o
            if o in final:
                final[o] += 1
            else:
                final[o] = 1
# Somehow print in the correct format
    for k, v in final.items():
        if v == 1:
            stupid += ['(' + str(k) + ')']
        else:
            stupid += ['(' + str(k) + '**' + str(v) + ')']
    print(''.join(stupid))


primeFactors(7775460)
