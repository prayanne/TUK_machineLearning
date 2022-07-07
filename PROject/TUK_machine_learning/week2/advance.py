# %%
############################################################
# 예측값 yn과 실제값(데이터) yn을 비교하는 구조이다.
# 1. yn^ - yn
# 2. 공식을 활용
############################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as mt


############################################################

def preDraw(x, y, dataAmount=1): # 그래프 생성에 필요한 요소를 리턴하는 함수이다. | 요소: [데이터1, 데이터2, 데이터 수량]
    w0, w1, a = inputVal() # w0, w1, a에 값을 입력한다.
    array = [] # 가중치 [w0, w1]를 150개 마다 추가받는 배열
    for i in range(30001): # 30001번 반복한다.
        w0, w1 = gredientFunc(x, y, w0, w1, dataAmount, a) # 편미분 * 학습률을 반영하는 함수
        if i % 150 == 0 and i < 6001: # 150개 마다 array에 [w0, w1]를 추가한다.
            array.append([w0, w1])
    array = np.array(array) # array를 numpy형식 array로 변경한다. |
    return array[:, 0], array[:, 1], w0, w1 # w0-array, w1-array, w0, w1 | 리턴


def inputVal(): # 가중치 w0, w1, 학습률 a를 입력받고, 리턴한다.

    w0 = float(input("weight1: "))  # 데이터1 가중치
    w1 = float(input("weight2: "))  # 데이터2 가중치
    a = float(input("learning rate: "))  # 학습률, Learning Rate
    return w0, w1, a


def gredientFunc(x, y, weight0, weight1, dataAmount=1, a=0.1):  # 평균제곱오차의 편미분구하고, 학습률을 곱해, 이전 가중치에 반영하는 함수

    temp = (weight0 * x + weight1) - y  # 예측값 - 실제값 | numpy array로 구성한다.
    w0Sum = (x * temp).sum()  # error*실제값,x를 행렬곱한 후, sum한다.
    w1Sum = (temp).sum()  # 평균오차만 sum한다.
    w0Result = weight0 -2 * a * w0Sum / (dataAmount)  # 평균제곱오차의 2차원 그래프의 편미분값들(w0, w1)과 학습률을 곱한다. | 이후, 이를 w0, w1에서 빼게 된다. | w0[t+1] = w0[t] - 2a*2/n * x(평균오차) 이므로, 기울기가 극소값에 빠지게 진행한다. 목표는 최솟값에 도달하는 것이다.
    w1Result = weight1 -2 * a * w1Sum / (dataAmount)  # 학습률에 도출된 음수 편미분값을 반영한다.
    return round(w0Result, 4), round(w1Result, 4)  # float, 소수점 5자리에서 반올림


# 사용x 함수, 평균제곱오차를 리턴한다.
def costFunc(x, y, weight0, weight1,dataAmount=1):  # 손실함수, 평균제곱오차 | 예측값과 실제값이 얼마나 차이나는지 보여주는 함수이다. 손실함수를 통해 평균제곱오차를 도출한다.
    # 예측값 - 실제값 | 데이터1 즉, xn에서 예측값 y, 실제값 y를 비교한다. | 차이를 제곱하여 추합해, 데이터 개수로 나누고, 평균을 구한다. | 차이나는 정도를 평균으로 나타낸 것으로 이를 근거로 가중치를 변화한다.
    temp = (weight0 * x + weight1) - y  # 예측값 - 실제값 | numpy array로 구성한다.
    arrSum = (temp ** 2).sum()  # 평균제곱오차의 sum

    total = arrSum / (dataAmount)  # 평균 | dataAmount는 함수 요소로 받아온다.
    return round(total, 4)  # float, 소수점 5자리에서 반올림


############################################################
# start

data = pd.read_csv('linear_regression_data01.csv', delimiter=",", names=['age', 'tall']) # csv파일 data에 pandas series로 저장한다.

dataX = data["age"].to_numpy() # pandas에서 age파트를 numpy 형식으로 변환하여 dataX에 저장한다.
dataXAmount = dataX.size # age파트의 수를 추출한다.
dataY = data["tall"].to_numpy() # 이하 동문, dataY에 저장한다.
dataYAmount = dataY.size # 이하 동문, dataYAmount에 저장한다.

# 가중치 w0, w1
# 학습률 learning rate - a를 설정
w0 = 1
w1 = 1
a = 0.001

# preDraw에서 함수를 대거 불러와, 가중치 w0, w1와 가중치의 집합 w0List, w1List를 리턴한다.
mt.figure(figsize=(10,4)) # figure1의 창 크기를 조정한다.
mt.subplots_adjust(wspace = 0.3) # 그래프간 가로 간격 조정한다.

mt.subplot(1,2,1) # 데이터, 경사하강 선형회귀 그래프
w0List, w1List, w0, w1 = preDraw(dataX, dataY, dataXAmount) # 첫번째 값 입력, 근접한 가중치 추출, 가중치와 가중치 리스트 리턴.
mt.xlabel('Age') # x, y축에 이름을 지정한다.
mt.ylabel('Tall') 
mt.plot(dataX, dataY, 'ro', markersize = 3, label = 'data') # 데이터 그래프
mt.plot(dataX, w0*dataX+w1, 'k--', label = 'Linear Regression') # 선형회귀 그래프
mt.legend() # subplot0, 그래프들의 라벨

mt.subplot(1,2,2) # 가중치 변화 그래프
mt.plot(range(w0List.size), w0List, 'b--', label = 'weight1') # 반복횟수에 맞춰 변화하는 가중치0을 시각화한다.
mt.plot(range(w1List.size), w1List, 'r--', label = 'weight2') # 이하 동문, 가중치1
mt.xlabel('Count / 150') # x, y축에 이름을 지정한다.
mt.ylabel('Weight1, Weight2') # 이하 동문
mt.legend() # subplot0, 그래프들의 라벨

print(w0, w1)

mt.show() # 창 표시

# Done
 # %%