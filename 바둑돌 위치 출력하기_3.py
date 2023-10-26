u = [[0] * 19 for _ in range(19)]
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    u[a - 1][b - 1] = 1

for i in range(19):
    for j in range(19):
        u[i][j] = str(u[i][j])

for i in range(19):
    u[i] = ' '.join(u[i])
    print(u[i])

