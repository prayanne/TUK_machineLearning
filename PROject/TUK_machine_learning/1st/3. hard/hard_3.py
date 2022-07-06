# -*- coding: utf-8 -*- 
############################################################
# N장의 카드, M장에 가장 가깝게
# M - (N1 N2 N3의 합)에서 가장 0에 가까운 합을 구하면 됨.
############################################################

sumList = []
listNum = []
numSum = [] # 22.06.29 주석추가 | 근접한 수를 저장하는 리스트. 1. 근접지수 == 0 | 2. 근접지수 == i or -i


def cardSum(cutLine): # 22.06.29 주석추가 | 리스트 업 함수, 1. m값 근접 지수들의 리스트 2. 중복x, 3장을 뽑는 모든 경우들의 리스트
    for i in range(len(cardList)-2):
        i += 1
        for n in range(len(cardList)):
            n += 1
            if n <= i:
                continue
            else:
                for m in range(len(cardList)):
                    m += 1
                    if m <= n:
                        continue
                    else:
                         sumList.append(cutLine - (cardList[i-1] + cardList[n-1] + cardList[m-1])) # 22.06.29 주석추가 | m값에 근접한 정도를 나타내는 지수, 절댓값(지수)가 0에 가까울수록 가까운 수.
                         listNum.append([i-1, n-1, m-1]) # 22.06.29 주석추가 | n장의 카드 중에서, 중복없이 3장을 뽑는 모든 경우를 리스트에 저장.

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

#Done