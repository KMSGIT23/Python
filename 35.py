dice1=(1,2,3,4,5,6)
dice2=(2,3,5,7,11,13)
plus=set()

for i in range(len(dice1)):
    for j in range(len(dice2)):
        plus.add(dice1[i]+dice2[j])
        
print(plus)
