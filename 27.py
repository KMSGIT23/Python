#4.2.2-1
score=[0, 0, 2, 4, 7, 7, 9, 11, 11, 13, 18, 20]

stem_leaf=[[], [], []]

for s in score:
    d, m=divmod(s, 10)
    stem_leaf[d].append(m)

#4.2.2-2
score=[0, 0, 2, 4, 7, 7, 9, 11, 11, 13, 18, 20]

stem_leaf=[[], [], []]

for s in score:
    d, m=divmod(s, 10)
    stem_leaf[d].append(m)

i=0
while i<3:
    print(str(i)+":",stem_leaf[i])
    i+=1
