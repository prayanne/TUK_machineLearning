############################################################
# 1번째 - 테스트 케이스 개수 C
# 2번째 - 1 <= N <= 1000의 정수 이후, 점수의 나열
# 평균을 내고, 넘는 사람들의 비율 출력
############################################################
average = []
overStudentList = []
error = ""
############################################################

def studentCount(list):
    data = list.split(" ")
    count = int(data[0])
    if count != int(len(data)) - 1:
        return False
    else:
        if count <= 1000 and count >= 1:
            return True

def scoreAvailable(list):
    total = 0
    data = list.split(" ")
    for count in range(len(data) - 1):
        score = int(data[count + 1])
        if score > 100 or score < 0:
            return False
        total += score
    average.append(round(total / int(data[0]), 3))
    return True

def overAver(list, count):
    try:
        i = 0
        data = list.split(" ")
        student = int(data[0])
        over = 0
        for i in range(student):
            if average[count] < int(data[i + 1]):
                over += 1
        overStudentList.append(round(over / student * 100, 3))
        return True
    except:
        return False

############################################################

c = int(input("테스트 케이스의 개수를 입력하세요: "))

i = 0
for i in range(c):
    student = input("학생 수, 점수의 집합을 입력하세요: ")
    if studentCount(student) is not True:
        print("Student Count error")
        error = "studentCntErr"
        break
    if scoreAvailable(student) is not True:
        print("Score Average error")
        error = "scoreAverErr"
        break
    if overAver(student, i) is not True:
        print("Over Score error")
        error = "OverScrErr"
        break
    i += 1

if error == "studentCntErr" or error == "scoreAverErr" or error == "OverScrErr":
    print(f"Error message: {error} \nTry again")
else:
    for count in range(c):
        print(f"{overStudentList[count]}%", end=' ')
    #Done