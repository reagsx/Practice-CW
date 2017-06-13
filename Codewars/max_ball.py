def max_ball(v0):
    v = (v0 * 1000) / 60 / 60
    t = 0
    saved = 0

    while True:
        h = v * t - (.5 * 9.81 * t * t)
        if h >= saved:
            saved = h
        else:
            break
        t += .1
    return(int(round((t-.1)*10))))



max_ball(15)
