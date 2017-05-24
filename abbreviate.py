import re

how_does_re_work = re.compile(r'(?:(\w+)(\W+)?)')
def abbreviate(s):
    final = [] 
    
    for i, cheese in re.findall(how_does_re_work, s):
        if len(i) > 3:
            final.append(i[0] + str(len(i)-2) + i[-1])
        else:
            final.append(i)
        final.append(cheese)
        
    print (final)
    return ''.join(final)