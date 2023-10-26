n=int(input())
a=[0 for _ in range(23)]
data=list(map(int, input().split()))

for i in data:
    if i in data:
        a[i-1]+=1

for i in range(len(a)):
    a[i]=str(a[i])

a.reverse()
a=' '.join(a)
print(a)
