############################################################
#첫째 줄에는 별1개, 2개, ..N개 까지 찍으며, 이는 오른쪽 정렬이다.
############################################################

star = input("별의 갯수를 입력하세요: ")
starCount = int(star)

count = 0
#반복문으로 별의 갯수만큼 칸을 만들고, 이를 오른정렬로 출력하게 한다.

done = 0
i = 0
while done < starCount:
    done += 1
    i = 0

    for i in range(starCount):

        if i < starCount - done:
            print(" ", end='')
        else:
            print("*", end='')

    print("")
#Done