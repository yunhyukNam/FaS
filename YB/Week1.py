def prob1():
   korean = 80
   english = 75
   math = 55
   
   print(f"홍길동씨의 국어 점수 : {korean}")
   print(f"홍길동씨의 영어 점수 : {english}")
   print(f"홍길동씨의 수학 점수 : {math}")
   
   sum = korean + english + math
   ever = sum / 3
   
   print("홍길동씨의 평균 점수 : %.1f" %ever)
   
def prob2():
    n_num = 13
    
    if ((n_num % 2) == 0):
        print("13은 짝수입니다.")
    else:
        print("13은 홀수입니다.")
   
def prob3():
    reg_num = "881120-1068234"
    
    hong_year = reg_num[:2]
    hong_month = reg_num[2:4]
    hong_day = reg_num[4:6]
    
    print(f"홍길동씨의 생년은 {hong_year}년이고, 생월은 {hong_month}월, 생일은 {hong_day}일입니다.")
    
    
def prob4():
    reg_num = "881120-1068234"
    
    sort_idx = reg_num.index("-")
    hong_sex = int(reg_num[sort_idx + 1])
    
    if hong_sex == 1:
        print("홍길동씨는 남자입니다.")
    elif hong_sex == 2:
        print("홍길동씨는 여자입니다.")
    else:
        print("홍길동씨는 ???입니다.")
    
def prob5():
    some_str = "a:b:c:d"
    print(f"replace 전 문자열 : {some_str}")
    
    replace_str = some_str.replace(":", "#")
    print(f"replace 후 문자열 : {replace_str}")
    
    
def prob6():
    list6 = [1, 3, 5, 4, 2]
    
    new_list = sorted(list6, reverse=True)
    print(new_list)
    
def prob7():
    list7 = ["Life", "is", "too", "short"]
    
    new_str = " ".join(list7)
    print(f"합쳐진 문자열 : {new_str}")
    
def prob8():
    tuple8 = (1, 2, 3)
    new_tuple = tuple8 + (4,)
    
    print(f"튜플 값 추가 : {new_tuple}")
    

def prob9():
    a = {'A':90, 'B':80, 'C':70}
    
    value = a.pop('B')
    
    print(f"B의 값 : {value}")
    
    
def prob10():
    a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
    
    new_a = list(set(a))
    print(new_a)

if __name__ == "__main__":
    prob_num = int(input("문제 번호 : "))
    
    if prob_num == 1:
        prob1()
    elif prob_num == 2:
        prob2()
    elif prob_num == 3:
        prob3()
    elif prob_num == 4:
        prob4()
    elif prob_num == 5:
        prob5()
    elif prob_num == 6:
        prob6()
    elif prob_num == 7:
        prob7()
    elif prob_num == 8:
        prob8()
    elif prob_num == 9:
        prob9()
    elif prob_num == 10:
        prob10()
    else:
        print("문제 번호를 제대로 입력해주십시오.")