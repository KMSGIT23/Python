import random

file='ko_en.txt'

with open(file, 'r') as f:
    lines=f.readlines()

d=dict()

e=lambda x: 65<=ord(x)<=90 or 97<=ord(x)<=122

for l in f.splitlines():
    i=0
    while not e(l[i]):
        i+=1
    else:
        ko, en=l[:i - 1], l[i:]
        d[ko]=en

o=list(d.keys())

while True:
    k=random.choice(o)
    c=d[k]
    print('Write the following sentence in English.')
    print(f"{k}\n")
    ans=input('your answer: ') ; print('\n')

    if ans==c:
        print("result: Correct!\n") ; print("-"*80)
    else:
        print("result: Not correct!")
        print(f'right answer: {c}\n') ; print("-"*80)
