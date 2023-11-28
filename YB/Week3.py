# --------- 추가적인 과제 (복습용) ------------

# 7. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하기 (if문 사용)
def Num7():
    test_dict = {"봄": "딸기", "여름": "토마토", "가을": "사과", "겨울": "귤"}

    for i in test_dict.keys():
        if i == "가을":
            print(test_dict[i])

# 8. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하기 (if문 사용)
def Num8():
    test_dict = {"봄": "딸기", "여름": "토마토", "가을": "사과", "겨울": "귤"}

    for j in test_dict.values():
        if j == "사과":
            b = True
            break
        else:
            b = False

    print(b)

# 9. 다음 점수 구간에 맞게 학점을 출력하기 : (0~20 - E / 21~40 - D / 41~60 - C / 61~80 - B / 81~100 - A) (if문 사용)
def Num9():
    score = int(input("Input your score : "))
    
    if (0 <= score and score <= 20):
        print("E")
    elif (20 < score and score <= 40):
        print("D")
    elif (40 < score and score <= 60):
        print("C")
    elif (60 < score and score <= 80):
        print("B")
    elif (80 < score and score <= 100):
        print("A")
    else:
        exit(1)

# 10. 다음 3개의 숫자 중 가장 큰 수를 출력하기 : 12, 6, 8 (if문 사용)
def Num10():
    num = [12, 6, 8]
    bigNum = 0
    i = 0
    while(True):
        if (i < 2):
            if (bigNum <= num[i]):
                bigNum = num[i]
            elif (bigNum >= num[i + 1]):
                bigNum = bigNum
            else:
                break
        else:
            break
        
        i += 1
    
    print(bigNum)

# 11. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남/여를 판별하기 (if문 사용)
def Num11():
    Number = "123456-1524521"
    gender = int(Number[7:8])
        
    if (gender == 1):
        print("Male")
    elif (gender == 2):
        print("Female")
    

# 12. 다음 리스트 중에서 '정' 글자를 제외하고 출력하기 (while문 또는 for문 사용)
def Num12():
    Num12_list = ["갑", "을", "병", "정"]
    i = 0
    
    while True:
        if (i == 3):
            break
        else:
            print(Num12_list[i])
        
        i += 1

# 13. 1부터 100까지 자연수 중 '홀수'만 한 줄로 출력하기 (while문 또는 for문 사용)
def Num13():
    for i in range(1, 100):
        if i % 2 == 0:
            continue
        else:
            print(i, end=" ")

# 14. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하기 (while문 또는 for문 사용)
def Num14():
    Num14_list = ["nice", "study", "python", "anaconda", "!"]
    
    for i in Num14_list:
        if (len(i) >= 5):
            print(i)

# 15. 아래 리스트 항목 중에서 소문자만 출력하기 (while문 또는 for문 사용)
def Num15():
    Num15_list = ["A", "b", "c", "D", "e", "F", "G", "h"]
    
    for j in Num15_list:
        if (ord(j) <= 122 and ord(j) >= 97):
            print(j)

# 16. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하기 (while문 또는 for문 사용)
def Num16():
    Num16_list = ["A", "b", "c", "D", "e", "F", "G", "h"]
    
    for k in Num16_list:
        if (65 <= ord(k) and ord(k) <= 90):
            print(k)

if __name__ == "__main__":
    Num16()