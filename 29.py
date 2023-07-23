n = int(input())
L = []
i=2
while i <= n:
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    else:
        L.append(i)
    i += 1

print(L)
