s = 'azcbobobegghakl'

winner = 'n'
for l in [s[i:x+1] for i in range(len(s)) for x in range(i, len(s))]:
    if l == (''.join(sorted(l))):
        if len(l) > len(winner):
            winner = l
print(winner)
