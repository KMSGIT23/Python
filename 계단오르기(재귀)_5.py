n = int(input())
a = [0]
m = [0 for row in range(301)]
for i in range(n):
    a.append(int(input()))

def s(n):
    if n <= 0:
        return 0
    if m[n] != 0:
        return m[n]
        
    if n == 1:
        m[n] = a[1]
        return m[n]
    elif n == 2:
        m[n] = a[2] + a[1]
        return m[n]
    else:
        o1 = s(n - 3) + a[n - 1] + a[n]
        o2 = s(n - 2) + a[n]
        m[n] = max(o1, o2)
        return m[n]

print(s(n))
