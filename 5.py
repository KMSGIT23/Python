a=int(input())
if a >=1997:
    print('Z세대입니다')
elif a<=1996 and 1980<a:
    print('밀레니얼 세대입니다')
elif 1980>=a and 1964<a:
    print('X세대입니다')
elif 1964>=a and 1945<a:
    print('베이비붐 세대입니다')
elif 1945>=a and 1925<a:
    print('침묵 세대입니다')
else:
    print('가장 위대한 세대입니다')
