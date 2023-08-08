com=["게맛살", "구멍", "글라이더", "대롱", "더치페이", "롱다리", "리본", "멍게", "박쥐", "본네트", "빨대", "살구", "양심", "이빨", "이자", "자율", "주기", "쥐구멍", "차박", "트라이앵글"]
print("컴퓨터 : <시작>끝말잇기를 하자. 내가 먼저 말할게. 기차")
l={"기차", }
jj=['냥', '녀', '뇨', '니', '라', '락', '란', '래', '량', '려', '렷', '로', '론', '뢰', '료', '루', '류', '륜', '리']
dd=['양', '여', '요', '이', '나', '낙', '난', '내', '양', '여', '엿', '노', '논', '뇌', '요', '누', '유', '윤', '이']
n=input("플레이어 : ")
a=list(n)    
if a[0] != '차':
    print("글자가 안 이어져. 내가 이겼다!<끝>")
else:
    while True:
        found_word=None
        
        for word in com:
            if word[0] == a[-1]:
                found_word = word
                break

        for i in range(len(jj)):
            if a[-1]==jj[i]:
                a[-1]=dd[i]
                for word in com:
                    if word[0] == a[-1]:
                        found_word = word
                        break
                
        if found_word is None:
            print("컴퓨터 : 모르겠다. 내가 졌어.<끝>")
            break
        
        print("컴퓨터 :", found_word)
        
        com.remove(found_word)
        
        n=input("플레이어 : ")
        a=list(n)
        c=list(found_word)
        if a[0] != c[-1]:
            print("컴퓨터 : 글자가 안 이어져. 내가 이겼다!<끝>")
            break

        if n in l:
            print("컴퓨터 : 아까 했던 말이야. 내가 이겼어!<끝>")
            break
        else:
            l.add(n)
