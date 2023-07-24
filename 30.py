y, m, d=tuple(map(int, input().split()))
print("%02d/%02d/%04d"%(m, d, y))
em=(m, d) in [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (1, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
ey = m==12 and d==31
if em:
    if ey:
        y+=1
        m=1
        d=1
    else:
        m+=1
        d=1
else:
    d+=1
print("%02d/%02d/%04d"%(m, d, y))
