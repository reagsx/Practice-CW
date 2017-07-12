def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    tri_nums = [0]

    for i in range(1, k+1):
        if k >= tri_nums[-1]:
            t = sum(range(i+1))
            if t not in tri_nums:
                tri_nums.append(t)
        else:
            break
    if k in tri_nums:
        return True
    else:
        return False
