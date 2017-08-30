def genPrimes():
    pn = 2
    while True:
        next = pn + 1
        for i in range(1, pn):
            if pn % i == 0:
                pass
            else:
                yield pn

doobie=genPrimes()
doobie.next()
