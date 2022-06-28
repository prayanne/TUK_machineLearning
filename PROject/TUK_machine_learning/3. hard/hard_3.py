############################################################
# N장의 카드, M장에 가장 가깝게
# M - (N1 N2 N3의 합)에서 가장 0에 가까운 합을 구하면 됨.
############################################################

sumList = []
listNum = []
numSum = []
sSum =[]

def cardSum(num, cutLine):
    for i in range(num - 2):
        i += 1
        for n in range(num):
            n += 1
            if n <= i:
                continue
            else:
                for m in range(num):
                    m += 1
                    if m <= n:
                        continue
                    else:
                         sumList.append(cutLine - (i + n + m))
                         listNum.append([i, n, m])
nCard = int(input("카드 수: "))
mCard = int(input("목표 수: "))

cardSum(nCard, mCard)

i = 0
while 1:
    if i in sumList:
        if i == 0:
            numSum.append(mCard)
            break
        numSum.append(mCard + i)
        break
    i += 1
    if i > (nCard - 1) * 3: break
n = 0
while 1:
    if n in sumList:
        if n == 0:
            numSum.append(mCard)
            break
        numSum.append(mCard - n)
        break
    n -= 1
    if -n > (nCard-1)*3: break

print(numSum, sumList, listNum)