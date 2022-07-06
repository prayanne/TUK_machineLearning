############################################################
# OX quiz counter
# 연속된 정답들은 각각 n, n+1, n+2의 점수를 갖는다.
############################################################

def quizResultApd(count):
    global quizResultList
    quizResultInput = ""
    i = 0
    while True:
        quizResult = input("Insert Result: ")
        resultLen = len(quizResult)
        if resultLen > 0 and resultLen < 80:
            i += 1
            quizResultInput += quizResult + " "
            if i == count:
                quizResultList = quizResultInput.split()
                break

############################################################

preCount = ""
quizCount = 0
quizResultList = []
quizCountChk = 0
score = 0
scoreList = []
scoreSum = 0
scoreSumList = []
error = ""

try:
    preCount = input("How many quiz are U have?: ")
    quizCount = int(preCount)

except:
    print("\nYou input {}.\nInteger only.".format(preCount))
    quit()



quizResultApd(quizCount)

scoreList = [list() for i in range(quizCount)]
scoreSumList = [list() for i in range(quizCount)]

for i in range(quizCount):
    for n in quizResultList[i]:
        for m in n:
            if m == "O" or m == "o":
                score += 1
                scoreList[i].append(score)
            elif m == "X" or m == "x":
                score = 0
                scoreList[i].append(score)
            else:
                error = "Incorrect input"
                break
    score = 0
    quizCountChk += 1

for i in range(quizCount):
    for n in scoreList[i]:
        scoreSum += n
    scoreSumList[i] = scoreSum
    scoreSum = 0

if error == "":
    print(*scoreSumList, sep = '\n')

elif not error == "":
        print("{} error!\nPlz input again.".format(error))
        quit()

#Done