############################################################
# 키와 몸무게 (x, y) n명의 집단
# 더 큰 덩치 n명, 자신 n+1등
# 리스트 n개 에서, 비교상태(x1, y1)가 True, True or False, False의 조합을 배열하고, 나머지는 동등수로 사이에 집어넣기
############################################################
import copy


def insertCount(count):
    global infoList
    i = 0
    while True:
        try:
            preInsert = input("Insert Result: ")
            infoInput = list(map(int, preInsert.split()))
            weight, height = infoInput
        except:
            print("\nYou input {}.\nInteger only.".format(preInsert))
            quit()

        for n in range(2):
            if weight > 10 and weight < 200 and height > 10 and height < 200:
                infoList[i].append(infoInput[n])
        i += 1
        if i == count:
            break

def compareWeight(count):
    global infoList
    global compareWeightList

    temp = []
    for i in range(count):
    temp.attend([i][0])
    temp.sort()
    for i in range(count - 1):
        while infoList[i] < infoList[i + 1]:

def compareHeight(count):
    global compareHeightList


def compareBoth():


############################################################

preCount = ""
peapleCount = 0

infoList = []
compareWeightList = []
compareHeightList = []

try:
    preCount = input("How many people are U have?: ")
    peapleCount = int(preCount)

except:
    print("\nYou input {}.\nInteger only.".format(preCount))
    quit()

infoList = [list() for i in range(peapleCount)]
compareWeightList = [list() for i in range(peapleCount)]
compareHeightList = [list() for i in range(peapleCount)]

insertCount(peapleCount)
compareWeight(peapleCount)
compareHeight(peapleCount)
compareBoth(peapleCount)


#Done