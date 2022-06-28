############################################################
#시, 분을 입력받음, 0:45 이전은 23으로 넘김, 45 이전 이후로 분기를 나누고, 0:45에서 한번 더 분기할 것
############################################################

while 1:
    hour = int(input("시를 입력하세요: "))
    if hour >= 24 or hour < 0:
        continue
    else:
        break

while 1:
    minute = int(input("분을 입력하세요: "))
    if minute >= 60 or minute < 0:
        continue
    else:
        break



#조건문으로 45 이전, 이후 분기, 45 이전 분기에서 0:45 한번 더 분기

if minute < 45:
    if hour == 0:
        print(f"23:{15 + minute}")
    else:
        print(f"{hour-1}:{15 + minute}")
else:
    print(f"{hour}:{minute-45}")
#Done