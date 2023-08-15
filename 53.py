def sumOfDigits(n):
    if n>=1:
        return n%10+sumOfDigits(n//10)
    else:
        return 0

if __name__ == '__main__':
    print(sumOfDigits(47253))
    print(sumOfDigits(643))
