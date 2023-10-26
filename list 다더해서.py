def stack(a, sum):
    if len(a) == 0:
        return sum
    sum += a.pop()
    return stack(a, sum)

if __name__=="__main__":
    a = list(map(int, input().split()))
    sum = 0
    print(stack(a, sum))
