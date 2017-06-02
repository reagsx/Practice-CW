def sum_array(arr):
    if arr is None or len(arr) <= 1:  # check if there is enough numbers
        return 0
    else:
        arr.remove(min(arr))  # remove min
        arr.remove(max(arr))  # remove max
        return sum(arr)
