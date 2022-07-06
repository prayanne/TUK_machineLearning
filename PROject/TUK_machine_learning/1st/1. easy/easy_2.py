############################################################
# N, N 입력받고, 4분면 판단
############################################################

number = input("정수 정수의 형태로 수를 입력하세요: ")

numberList = number.split(' ')

if int(numberList[0]) > 0:
    if int(numberList[1]) > 0:
        print(1)
    else:
        print(4)
else:
    if int(numberList[1]) > 0:
        print(2)
    else:
        print(3)
#done