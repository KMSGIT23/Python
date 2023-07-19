#4.2-1
def sumOfDigits(num):
    num=list(str(num))
    for i in range(len(num)):
        num[i]=int(num[i])
    return sum(num)

if __name__=="__main__":
    num=int(input())
    result=sumOfDigits(num)
    print(result)
