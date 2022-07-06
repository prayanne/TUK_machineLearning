# a = 4 # 상수 
# b = 5
# print(f"{a} {b}")
# print("{} {}".format(a,b))

# def func(split=' '):
#     pass

# func('_')

# 3개중 1개
# a b => b c


# # 포인터 X => 전부 주소
# a,b,c,d,e = map(str, [1,2,3,4,5])
# print(a,b,c,d,e)
# a = list(map(str, [1,2,3,4,5]))
# print(a)

# [0] * 100
# a = []
# for i in range(100):
#     a.append(0)

# a = [0 for i in range(10)]    
# totalList = '123456789'
# for s in totalList:
#     a[int(s)] += 1
# print(a)

"""
python -> c 
if(조건 <= 0False, !0 True)
    
True
"""
    
# if True:
#     pass

# if hour>=0 and hour <=23:
#     break

# for i in range(5):
#     # 0 ~ 4
#     print(""*0+"*"*0)

# average = []
# overStudentList = []
# error = ""

# API 실무 => 규격화
# return {
#     "error" : "message",
#     "status": True
#     "data" : {
#         {
#             "id":"",
#             "userName": "",
#             "data": ""
#         },
#         {
#             "id":"",
#             "userName": "",
#             "data": ""
#         },
#         {
#             "id":"",
#             "userName": "",
#             "data": ""
#         }
#     }
# }


# def studentCount(list):
#     data = list.split(" ") # 1번
#     count = int(data[0])   # 2번
#     if count != int(len(data)) - 1:
#         return False
#     else:
#         if count <= 1000 and count >= 1:
#             return True

# def scoreAvailable(list):
#     total = 0
#     data = list.split(" ") # 3번
#     for count in range(len(data) - 1): # 4번
#         score = int(data[count + 1])
#         if score > 100 or score < 0:
#             return False
#         total += score
#     average.append(round(total / int(data[0]), 3))
#     return True

# def overAver(list, count):
#     try:
#         i = 0
#         data = list.split(" ")
#         student = int(data[0])
#         over = 0
#         for i in range(student):
#             if average[count] < int(data[i + 1]):
#                 over += 1
#         overStudentList.append(round(over / student * 100, 3))
#         return True
#     except:
#         return False

# ############################################################

# c = int(input("테스트 케이스의 개수를 입력하세요: "))

# i = 0
# for i in range(c):
#     student = input("학생 수, 점수의 집합을 입력하세요: ")
#     result = studentCount(student)

#     if studentCount(student) is not True:
#         print("Student Count error")
#         error = "studentCntErr"
#         break
#     if scoreAvailable(student) is not True:
#         print("Score Average error")
#         error = "scoreAverErr"
#         break
#     if overAver(student, i) is not True:
#         print("Over Score error")
#         error = "OverScrErr"
#         break
#     i += 1

# if error == "studentCntErr" or error == "scoreAverErr" or error == "OverScrErr":
#     print(f"Error message: {error} \nTry again")
# else:
#     for count in range(c):
#         print(f"{overStudentList[count]}%", end=' ')
    #Done
    
# =======================================================================================
    
############################################################
# 두자리 루틴, 첫 수 - 루틴 - 첫 수의 반복횟수 n을 구한다.
############################################################

# return 방식 1개로 통일
# def over10(num):
#     numList = num
#     if int(numList) < 10: return "under10" # 22.06.29 | 10 < n < 100에서 0 < n < 100로 조건을 변경했다. 분기 추가
#     total = int(numList[0]) + int(numList[1])
#     if total >= 10: return "True"
#     else: return "False"

# def plusNum(num):
#     numList0 = num
#     result = over10(num)
#     if over10(num) == "True": # over10(num)
#         numPlus0 = str(int(numList0[0]) + int(numList0[1]))[1]
#         total =  numList0[1] + numPlus0
#     elif over10(num) == "False": # not over10(num)
#         total = numList0[1] + str(int(numList0[0]) + int(numList0[1]))
#     elif over10(num) == "under10": total = str(int(numList0)) + str(int(numList0)) # 22.06.29 | 0 < n < 100로 조건 변경. | 앞 문자 "0"을 int로 제거후, str으로 변환한다.
#     return total

# ############################################################

# fstNum = input("수를 입력하시오: ")

# saveNum = fstNum
# repeat = 1
# error = ""

# while 1:
#     if 0 > int(fstNum) or int(fstNum) > 100:
#         error = "10"
#         break
#     saveNum = plusNum(saveNum)
#     if int(fstNum) == int(saveNum):  break
#     repeat += 1


# if error == "10":
#     print(f"Error message: {error} \nTry again")

# else: print(repeat)
#Done


sumList = []
listNum = []
numSum = [] # 22.06.29 주석추가 | 근접한 수를 저장하는 리스트. 1. 근접지수 == 0 | 2. 근접지수 == i or -i

result = 0

import math
def cardSum(cutLine): # 22.06.29 주석추가 | 리스트 업 함수, 1. m값 근접 지수들의 리스트 2. 중복x, 3장을 뽑는 모든 경우들의 리스트
    # n^3
    min = math.INT_MAX
    for i in range(len(cardList)-2):
        # i += 1 
        for n in range(i+1, len(cardList) - 1):
            # n += 1
            ## if n <= i:
            ##     continue
            #else:
                for m in range(n+1, len(cardList)):
                    # m += 1
                    ## if m <= n:
                    ##     continue
                    #else:
                         temp = cutLine - (cardList[i-1] + cardList[n-1] + cardList[m-1])
                         # if temp <= cutLine tmpe >max:
                         
                         if temp >=0 and temp <min:
                             min = temp
                             result = cardList[i-1] + cardList[n-1] + cardList[m-1]
                         sumList.append(cutLine - (cardList[i-1] + cardList[n-1] + cardList[m-1])) # 22.06.29 주석추가 | m값에 근접한 정도를 나타내는 지수, 절댓값(지수)가 0에 가까울수록 가까운 수.
                        #  listNum.append([i-1, n-1, m-1]) # 22.06.29 주석추가 | n장의 카드 중에서, 중복없이 3장을 뽑는 모든 경우를 리스트에 저장.

############################################################

condition = input("입력: ") # 22.06.29 | 예제처럼, [수 | 수] 의 형식으로 지원하게 변경.

nCard = int(condition.split(" ")[0]) # 22.06.29 | 변경된 형식에 맞추어 nCard, mCard에 각각 split, 이후 계산은 동일하므로, int 옵션을 추가.
mCard = int(condition.split(" ")[1])

cardList = list(map(int, input("카드s 입력: ").split(" "))) # 22.06.29 | 카드들을 입력받음. 박세연님의 map() 함수를 활용함.

if nCard is not len(cardList): # 22.06.29 주석 추가 | 카드수 매칭
    print("CardList len error")
    quit()
for i in range(len(cardList)): # 22.06.29 주석추가 | 카드의 수 크기 제한
    if cardList[i] <= 0 or cardList[i] > 100000:
        print("CardList range error")
        quit()

cardSum(mCard) # 22.06.29 주석추가 | 리스트 업 함수.

# 22.06.29 주석추가 | 근접 지수 중, 양수, 음수를 나누어 가장 절대값이 낮은
i = 0
while 1:
    if i in sumList:
        if i == 0:
            numSum.append(mCard)
            break
        numSum.append(mCard - i)
        break
    i += 1
    if i > 300000: break
n = 0
while 1:
    if n in sumList:
        if n == 0:
            numSum.append(mCard)
            break
        numSum.append(mCard - n)
        break
    n -= 1
    if -n > 300000: break

# 22.06.29 기능 추가 | len이 2인 numSum에서 근접 지수를 계산해, 1. 근접 정도가 같은 수들, 2. 더 근접한 수를 출력하게 함.
# len(numSum) == 1
if i == 0 and n == 0: # 22.06.29 주석추가 | 근접 지수 == 0
    print(numSum[0])
elif len(numSum) == 1: # 22.06.29 주석추가 | 근접 지수가 양수, 혹은 음수만 존재할 때, numSum은 1개의 요소만 존재함.
    print(numSum[0])
# len(numSum) == 2
else:
    if mCard - numSum[0] < -(mCard - numSum[1]):
        print(numSum[0])
    elif mCard - numSum[0] > -(mCard - numSum[1]):
        print(numSum[1])
    elif mCard - numSum[0] == -(mCard - numSum[1]): # 22.06.29 주석추가 | 근접 지수의 절대 값이 똑같은 경우를 분기함.
        print(numSum[0], numSum[1])

#print(numSum, sumList, listNum)

    """
    1. 돌아가는거
    2. 예외처리
    3. 가독성
    
    """