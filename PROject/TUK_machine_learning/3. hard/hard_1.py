############################################################
# 두자리 루틴, 첫 수 - 루틴 - 첫 수의 반복횟수 n을 구한다.
############################################################

def over10(num):
    numList = num
    total = int(numList[0]) + int(numList[1])
    if total >= 10: return True
    else: return False

def plusNum(num):
    numList0 = num

    if over10(num) is True:
        numPlus0 = str(int(numList0[0]) + int(numList0[1]))[1]
        total =  numList0[1] + numPlus0
    elif over10(num) is False:
        total = num[1] + str(int(numList0[0]) + int(numList0[1]))
    return total

############################################################

fstNum = input("수를 입력하시오: ")

saveNum = fstNum
repeat = 1
error = ""

while 1:
    if 10 > int(fstNum) or int(fstNum) > 100:
        error = "10"
        break
    saveNum = plusNum(saveNum)
    if fstNum == saveNum:  break
    repeat += 1


if error == "10":
    print(f"Error message: {error} \nTry again")

else: print(repeat)
#Done