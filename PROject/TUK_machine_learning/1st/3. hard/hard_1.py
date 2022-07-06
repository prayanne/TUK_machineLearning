############################################################
# 두자리 루틴, 첫 수 - 루틴 - 첫 수의 반복횟수 n을 구한다.
############################################################

def over10(num):
    numList = num
    if int(numList) < 10: return "under10" # 22.06.29 | 10 < n < 100에서 0 < n < 100로 조건을 변경했다. 분기 추가
    total = int(numList[0]) + int(numList[1])
    if total >= 10: return True
    else: return False

def plusNum(num):
    numList0 = num

    if over10(num) is True:
        numPlus0 = str(int(numList0[0]) + int(numList0[1]))[1]
        total =  numList0[1] + numPlus0
    elif over10(num) is False:
        total = numList0[1] + str(int(numList0[0]) + int(numList0[1]))
    elif over10(num) == "under10": total = str(int(numList0)) + str(int(numList0)) # 22.06.29 | 0 < n < 100로 조건 변경. | 앞 문자 "0"을 int로 제거후, str으로 변환한다.
    return total

############################################################

fstNum = input("수를 입력하시오: ")

saveNum = fstNum
repeat = 1
error = ""

while 1:
    if 0 > int(fstNum) or int(fstNum) > 100:
        error = "10"
        break
    saveNum = plusNum(saveNum)
    if int(fstNum) == int(saveNum):  break
    repeat += 1


if error == "10":
    print(f"Error message: {error} \nTry again")

else: print(repeat)
#Done