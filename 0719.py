# 약수 중 소수가 4개인 수 찾기
'''li=[608, 808, 614, 322, 402, 287, 627, 326, 928, 418, 458, 808, 797, 646, 995, 945, 591, 472, 466, 905, 135, 378, 700, 787, 700, 582, 514, 703, 251, 484, 790, 642, 455, 829, 539, 906, 363, 529, 150, 220, 545, 424, 381, 703, 896, 902, 561, 309, 690, 277, 529, 122, 242, 807, 416, 764, 336, 677, 597, 197, 847, 556, 204, 617, 376, 904, 975, 762, 634, 452, 837, 993, 736, 620, 377, 588, 285, 789, 184, 943, 208, 273, 751, 136, 498, 207, 809, 444, 417, 219, 951, 914, 462, 637, 296, 199, 967, 556, 270, 976, 851, 847, 955, 364, 118, 291, 898, 276, 327, 996, 862, 494, 723, 981, 922, 527, 369, 232, 801, 240, 196, 804, 249, 491, 761, 979, 571, 798, 225, 849, 889, 503, 104, 395, 855, 459, 464, 638, 591, 963, 391, 800, 464, 935, 880, 616, 882, 972, 626, 438, 812, 978, 826, 263, 390, 899, 471, 177, 340, 532, 862, 616, 141, 402, 200, 449, 371, 864, 380, 583, 137, 915, 597, 391, 700, 865, 648, 479, 539, 638, 167, 521, 381, 740, 128, 434, 415, 169, 588, 345, 293, 301, 198, 884, 852, 661, 864, 809, 271, 367, 742, 316, 730, 649, 447, 725, 293, 687, 675, 399, 906, 104, 160, 904, 903, 459, 748, 983, 462, 563, 131, 368, 137, 987, 388, 912, 796, 628, 275, 899, 775, 254, 682, 946, 130, 719, 161, 294, 705, 435, 448, 900, 415, 670, 928, 423, 114, 228, 615, 135, 667, 995, 751, 252, 603, 105, 900, 186, 681, 553, 223, 586, 710, 974, 529, 630, 818, 142, 469, 826, 444, 922, 738, 375, 301, 892, 447, 418, 354, 980, 945, 841, 390, 111, 131, 110, 190, 710, 802, 906, 746, 507, 395, 864, 444, 244, 943, 953, 193, 585]
for i in li:                    #i== 하나하나 대상 
    lii=[]                      #li == i 의 약수
    liii=[]
    for j in range(1,i+1):      #li 요소에 접근할 j 
        if i%j==0:
            lii.append(j)       #lii 에 약수를 넣는다
    sosu=0
    for k in lii:               #li 의 약수 하나하나에 접근할 k 
        s=0
        for l in range(1,k+1):  #li의 약수의 약수를 구한다
            if k%l==0:
                s+=1   
        if s==2:
            sosu+=1 
    if sosu==4:
        print(i)
'''

#break, continue

'''for i in [1,2,3]:
    if i ==2:
        break   #2에 접근할때 반복문 탈출! 
    print(i)    #1만 나온다

#1. break 는 반복문 안에서만 사용가능!
#2. break 는 제일 가 까운 반복문 하나만 빠져나간다!
#3. N이 소수인지 판별 가능

n=int(input())
for i in range(2,n):
    if n%i==0:
        break
else:
    print("d")



for i in [1,2,3,4]:
    for j in [1,2,3]:
        if j ==2:           #j에서 2를 만나면 가까운 반복문 1개만 빠져나감.
            break
        print(i,j)



for i in range(1,11):
    if i%2==0:
        print("ㅉ")
else:
    print("ㅎ")
print()

#for ~ else : 반복이 완전히 돌아갔다. else 종속문장 실행
#             반복이 중간에 끊기면 esle 실행

for i in range(1,11):
    if i%2==0:
        print("ㅉ")
        break
else:
    print("ㅎ")
'''

#continue
# 다음 코드 실행
'''
for i in range(1,11):
    if i<6:                 # i 가 6보다 작은건 패스하고 다음 코드 실행
        continue
    print(i)'''




# While문!
'''
for : 반복횟수 명확
while: 반복 불명확(게임, GUI 프로그램)
'''
'''for i in range(1,11):
    print(i)
print("="*30)


i =1 
while i<11:
    print(i)
    i+=1'''

#while 로 구구단.
'''k=2
while k<10:
    i=0
    while i < 9:
        i+=1
        print(i)
        print(k,"X",i,"=",k*i)
    k+=1
'''

# while True!!
'''
while True:
    kor = int(input("국어점수:"))
    if 0<=kor<=100:
        break

'''
'''while True:
    ans = input("python 존잼 ㅇㅈ? (yes/no)")
    if ans=="yes":
        print("ㅇㅇㅈ")
        break
'''

'''
while True:
    a=int(input())
    if a==0:
        break'''
'''li=[]
while True:
    a=int(input())
    if a==0:
        print(sum(li)/len(li))
        break
    li.append(a)'''

#문자열.isnumeric()
#> 문자열이 숫자로만 구성이 되어있으면 True
#> 아니면 False

#함수가 bool 값 반환하면 if 문이랑 찰떡
#함수가 list 반환 for 문이랑 찰떡

'''li=[]
while True:
    a=int(input())
    if a==0:
        print(sum(li)/len(li))
        break
    li.append(a)'''
'''


li=[]
while True:
    kor = input("국어점수: ")
    if kor.isnumeric():
        kor=int(kor)
        li.append(kor)
    else:
        if kor=="q":
            if li:
                print(sum(li)/len(li))
                break
            else:
                print("뭐라도 입력하세요")
        else:
            print("숫자입력하세요")'''

'''
Q. 종료시까지 점수를 입력받는 프로그램을 사용자가 사용할 수 있도록 작성해주세요. 

요구명세서 

1) 숫자가 입력되었을 경우
    1-1) 0에서 100까지 입력되었을 경우
    1-2) 그외 범위가 입력되었을 경우
2) 문자가 입력되었을 경우
    2-1) 종료시그널(q) 이 입력되었을 경우
       2-1-1) 입력된 숫자가 있을 경우
       2-1-2) 입력된 숫자가 없을 경우
    2-2) 그외 입력이 들어올 경우

'''        
'''li=[]
while True:
    kor = input("국어점수를 입력하세요: ")
    if kor.isnumeric():
        kor=int(kor)           #1         
        if 0<=kor<=100:         #1-1
            li.append(kor)
        else:
            print("0부터 100까지의 점수를 입력하세요.")               #1-2
    else:                       #2  
        if kor=="q":       #2-1
            if li:
                print(sum(li)/len(li))            #2-1-1
            else:               #2-1-2
                print("점수를 입력하세요.")
                break
        else:                   #2-2
            print("점수를 입력하세요.")
'''
'''
1-1) 리스트에 담는다
1-2) 올바른 범위를 입력하라고 안내해준다.
2-1-1) 평균을 출력하고 종료를 해준다.
2-1-2) 입력된 값이 없다고 안내해준다.
2-2) 숫자입력하라고 안내해준다.'''



'''
1. 숫자가 입력됐을 경우
    1-1 돈이 충분할 경우
        1-1-1 콜라, 사이다, 커피 더하고 종료
            1-1-1-1 종료버튼이 눌렸을 경우
            1-1-1-2 종료버튼이 아닌 다른 버튼이 눌렸을 경우
    1-2 돈이 부족할 경우
2. 음수가 입력됐을 경우
3. 문자가 입력됐을 경우



'''
# print("-"*4,"MENU","-"*4,
# '''
# 1. 콜라 / 300
# 2. 사이다 / 300
# 3. 커피 / 200
# 4. 돈 넣기
# 5. 잔돈 반환
# ''',
# "-"*4,"MENU","-"*4)

'''
1. 돈 넣기
    1-1 2번으로 이동(돈 넣기(4)를 입력할때까지 반복
2. 메뉴 선택
    2-1 돈이 충분하면 3으로 이동
    2-2 돈이 부족하면 안내
3. 잔돈반환
    3-1 잔돈이 있으면 반환하고 종료
    3-2 잔돈이 없으면 종료
4. 종료
'''
