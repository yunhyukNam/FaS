# 11. 아래의 문자열의 길이를 구하기
def Num11():
    string = "dhsmfdms11dnfj20dlfvktmqkrwltn0319" # 오늘은 11월 20일 파스 박지수0319
    str_len = len(string)
    
    print(str_len)

# 12. print 함수를 사용하여 아래와 같이 출력하기 : apple;orange;banana;lemon
def Num12():
    print("apple;orange;banana;lemon")

# 13. 화면에 * 기호 100개 표시
def Num13():
    for i in range(0, 100):
        print("*", end="")

# 14. 문자열 "30"을 각각 정수형, 실수형, 복소수형, 문자형으로 변환하기
def Num14():
    a = "30"
    
    print("%d" %(int(a)))
    print("%f" %(float(a)))
    print(a)
    

# 15. 다음 문자열 "Niceman"에서 "man" 문자열만 추출하기
def Num15():
    a = "Niceman"
    
    for i in range(0, len(a)):
        p_str = a[i]
        
        if i >= 4:
            print(p_str, end="")

# 16. 다음 문자열을 거꾸로 출력해보기 : "Strawberry"
def Num16():
    a = "Strawberry"
    
    print(a[::-1])

# 17. 다음 문자열에서 '-'를 제거 후 출력하기 : "010-4023-5394"
def Num17():
    a = "010-4023-5394"
    
    print(a.replace("-", ""))

# 18. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하기 : "http://naver.com"
def Num18():
    a = "http://naver.com"
    
    print(a.replace("http://",""))

# 19. 다음 문자열을 모두 대문자, 소문자로 각각 출력하기 : "NiceMan"
def Num19():
    a = "NiceMan"
    
    print(a.upper())
    print(a.lower())

# 20. 다음 문자열을 슬라이싱을 이용해 "cde"만 출력하기 : "abcdefghijklmn"
def Num20():
    a = "abcdefghijklmn"
    
    print(a[2:5])

# 21. 다음 리스트에서 "Apple" 항목만 삭제하기 : ["Banana", "Apple", "Orange"]
def Num21():
    a = ["Banana", "Apple", "Orange"]
    a.remove("Apple")
    
    print(a)

# 22. 다음 튜플을 리스트로 변환하기 : (1, 2, 3, 4)
def Num22():
    a = (1, 2, 3, 4)
    
    print(list(a))

# 23. 다음 항목을 딕셔너리(dict)로 선언하기 : <성인 - 100000, 청소년 - 70000, 아동 - 30000>
def Num23():
    a = {"성인" : 100000, "청소년" : 70000, "아동" : 30000}
    a["소아"] = 0
    
    print(a.keys())
    print(a.values())


# 24. 23번의 항목에서 선언한 dict 항목에 <소아 - 0> 항목 추가하기

# 25. 23번에서 선언한 딕셔너리에서 key 항목만 출력하기

# 26. 23번에서 선언한 딕셔너리에서 value 항목만 출력하기

if __name__ == "__main__":
    Num22()