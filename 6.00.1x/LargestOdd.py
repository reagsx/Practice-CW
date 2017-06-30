def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # Your code here
    num_dic = {}
    odd_num = []

    for i in L:
        if i not in num_dic:
            num_dic[i] = 1
        else:
            num_dic[i] += 1

    for k, v in num_dic.items():
        if v % 2 == 0:
            pass
        else:
            odd_num.append(k)
    if odd_num == []:
        return None
    else:
        return(max(odd_num))



print(largest_odd_times([3,4,5,3,4,5,6,7,3,2,4,5,6,7]))
