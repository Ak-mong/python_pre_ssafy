score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]

stem_leaf = [[],[],[]]

for s in score:
    d,m = divmod(s,10)
    stem_leaf[d].append(m)

print(stem_leaf)
print(stem_leaf[0])
print()
print('0:',stem_leaf[0])
print('1:',stem_leaf[1])
print('2:',stem_leaf[2])
print()
for s in range(len(stem_leaf)):
    print(f'{s}: {stem_leaf[s]}')
