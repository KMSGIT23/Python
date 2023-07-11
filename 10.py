a = int(input())
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print("%d 년은 윤년입니다" % a)
        else:
            print("%d 년은 평년입니다" % a)
    else:
        print("%d 년은 윤년입니다" % a)
else:
    print("%d 년은 평년입니다" % a)
