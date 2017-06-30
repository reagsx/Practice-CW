def longest_consec(strarr, k):

    print(max([''.join(x) for x in [strarr[i:i+k] for i in range(len(strarr))]]
          , key=len) if len(strarr) > 0 and len(strarr) > k and k >= 0
          else '')


longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)



def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""

    return(max([''.join(x) for x in [strarr[i:i+k] for i in range(len(strarr))]], key=len))
