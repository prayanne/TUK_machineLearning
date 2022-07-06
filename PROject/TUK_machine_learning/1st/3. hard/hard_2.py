############################################################
# 별 1 - n - 1
############################################################

repeat = int(input("Insert Number: "))
n = 0
i = 0
while 1:
    n += 1
    i = 0
    if n - 1 >= repeat: break
    for i in range(n):
        print("*", end='')
    print("")

n -= 1

while 1:
    n -= 1
    i = 0
    if n <= 0: break
    for i in range(n):
        print("*", end='')
    print("")
#Done