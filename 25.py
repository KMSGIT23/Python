#문제 1
def palindrome(x):
    x=x.lower()
    d=x[::-1]
    return x==d


#문제 2
def palindrome(x):
    x=x.lower()
    d=x[::-1]
    return x==d


#문제 3
def palindrome(x):
    x=x.lower()
    x=x.replace(' ', '')
    d=x[::-1]
    return x==d
