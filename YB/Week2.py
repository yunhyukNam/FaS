def prob2():
    hap = 0
    i = 0
    
    while (i < 1000):
        if (i % 3 == 0):
            if (i > 1000):
                break
            else:
                hap += i
                i += 1
            
        else:
            i += 1
            continue
    
    print(f"1부터 1000까지의 수들 중 3의 배수를 모두 더한 값 : {hap}")

def prob3():
    i, j = 0, 0

    while i <= 5:
        j = 0
        
        while j <= 5:
            if(j < i):
                print('*', end ='')
            j += 1
        i += 1
        print()
        

def prob4():
    i = 1
    
    while i <= 100:
        print(i)
        i += 1
        
        
def prob5():
    score = [ 70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    
    st = 0
    st_cnt = 0
    
    for i in range(0, len(score)):
        st += score[i]
        st_cnt = i
        
        i += 1
        
    st = st / st_cnt
    print("학생들의 평균 점수는 %.1f점입니다." %st)


def prob6():
    numbers = [ 1, 2, 3, 4, 5]
    result = []
    
    for i in numbers:
        if i % 2 == 1:
            result.append(i+2)
            
    print(result)

if __name__ == "__main__":
    prob_num = int(input("문제 번호를 입력하세요. : "))
    
    if prob_num == 1:
        print("python이 출력된다.")
        
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
        
    else:
        print("문제 번호를 맞게 입력해주십시오.")