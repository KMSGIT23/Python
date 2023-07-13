n=int(input("What year were you born? "))
n1=input("Are you Korean?(y/n) ")
if n1=='n':
    if 1996<n:
        print("Z세대 입니다.")
    elif 1980<n and 1997>n:
        print("밀레니얼 세대입니다.")
    elif 1964<n and 1981>n:
        print("X세대 입니다.")
    elif 1965>n and 1945<n:
        print("베이비 부머 세대입니다.")
    elif 1946>n and 1924 <n:
        print("침묵 세대입니다.")
    elif 1925>n:
        print("가장 위대한 세대입니다.")
else:
    if 1996<n:
        print("Z세대 입니다.")
    elif 1980<n and 1997>n:
        print("밀레니얼 세대입니다.")
    elif 1963<n and 1981>n:
        print("X세대 입니다.")
    elif 1964>n and 1954<n:
        print("베이비 부머 세대입니다.")
    elif 1955>n and 1924 <n:
        print("침묵 세대입니다.")
    elif 1925>n:
        print("가장 위대한 세대입니다.")
