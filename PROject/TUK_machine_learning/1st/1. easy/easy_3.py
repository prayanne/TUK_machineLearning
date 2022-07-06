############################################################
# N입력받고, 최종값 사용된 정수의 개수 출력
############################################################

number = input("정수 정수 정수의 형태로 수를 입력하세요: ")

numberList = number.split(' ')

total = int(numberList[0]) * int(numberList[1]) * int(numberList[2])
totalList = str(total)

printList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(totalList)):
    if totalList[i] == "0": printList[0] += 1
    if totalList[i] == "1": printList[1] += 1
    if totalList[i] == "2": printList[2] += 1
    if totalList[i] == "3": printList[3] += 1
    if totalList[i] == "4": printList[4] += 1
    if totalList[i] == "5": printList[5] += 1
    if totalList[i] == "6": printList[6] += 1
    if totalList[i] == "7": printList[7] += 1
    if totalList[i] == "8": printList[8] += 1
    if totalList[i] == "9": printList[9] += 1

for i in range(10):
    print(printList[i])
#done