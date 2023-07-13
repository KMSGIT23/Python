low, high=map(int, input().split())
temp=0
while temp != -999:
    temp=int(input())
    if temp <= high and temp >= low:
        print('Nothing to report')
    else:
        print('Alert!')
        break
