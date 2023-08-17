#1
def compound_interest_amount_withoutN(p, r, t):
    P=p*((1+r)**t)
    return P

if __name__=='__main__':
    print(compound_interest_amount_withoutN(3600000, 0.058, 2))
    print(compound_interest_amount_withoutN(10000000, 0.05/12, 12))

#2
def compound_interest_amount(p, r, t, n):
    P=p*((1+r/n)**(n*t))
    return P

if __name__=='__main__':
    print(compound_interest_amount(1500000, 0.043, 6, 4))
    print(compound_interest_amount(1500000, 0.043, 6, 1/2))
    print(compound_interest_amount(3600000, 0.058, 2, 1))
