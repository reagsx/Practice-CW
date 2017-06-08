def f(n):
    x = 0
    if type(n) == int and n > 0:
        for i in range(n+1):
            x += i
    else:
        None
    print(x)

f('flo')
