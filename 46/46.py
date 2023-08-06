import random

#코드를 실행할 때 아래의 파일을 저장하여 알맞은 경로를 open()에 입력
food=open('food.txt').read().split()
color=open('color.txt').read().split()

f=random.choice(food)
c=random.choice(color)

print(c, f)
