# %%
############################################################
# 예측값 yn과 실제값(데이터) yn을 비교하는 구조이다.
# 1. yn^ - yn
# 2. 공식을 활용
############################################################
#import module

import pandas as pd
import numpy as np
import matplotlib.pyplot as mt

w0 = 1
w1 = 1
a = 0.001

############################################################
#definiton funtion

def preDraw(x, y, w0, w1, dataAmount=1, a = 0.001): # 그래프 생성 필수 요소 리턴
    array = []
    for i in range(10001):
        w0, w1, MSR_ = gredientFunc(x, y, w0, w1, dataAmount, a) # w[t] -> w[t+1]
        if i % 10 == 0 and i <= 3000: # w0, w1 변화 리스트
            array.append([w0, w1, MSR_])
    array = np.array(array) # numpy형식 array 변경
    return array[:, 0], array[:, 1], array[:, 2], w0, w1 # w0 -> array, w1 -> array, MSR - > array, w0, w1 | 리턴


def inputVal(): # 가중치 w0, w1, 학습률 a
    w0 = float(input("weight1: "))
    w1 = float(input("weight2: "))
    a = float(input("learning rate: "))
    return w0, w1, a


def gredientFunc(x, y, weight0, weight1, dataAmount=1, a=0.1):  # 평균제곱오차의 편미분 * 학습률 -> 이전 가중치 반영
    deviation = (weight0 * x + weight1) - y  # 예측값 - 실제값
    MSR_ = (deviation**2).sum() / (dataAmount) # MSR
    w0Result = weight0 -2*a*sum(x*deviation)/(dataAmount)   # 학습률 * 음수 편미분 -> 반영
    w1Result = weight1 -2*a*sum(deviation)/(dataAmount)  
    return round(w0Result, 4), round(w1Result, 4), round(MSR_, 4)  # float, 4


# 사용x, 평균제곱오차
def costFunc(x, y, weight0, weight1, dataAmount=1):  # 손실함수 | (예측값 - 실제값)**2
    temp = (weight0 * x + weight1) - y  # 예측값 - 실제값
    MSR = (temp ** 2).sum()  # 평균제곱오차의 sum
    total = MSR / (dataAmount)
    return round(total, 4)  # float, 4


############################################################
# start

try:
    data = pd.read_csv('linear_regression_data01.csv', delimiter=",", names=['age', 'tall'])
except:
    data = pd.read_csv('/config/workspace/PROject/TUK_machine_learning/week2/linear_regression_data01.csv', delimiter=",", names=['age', 'tall'])

dataX = data["age"].to_numpy(); dataY = data["tall"].to_numpy() # pandas에서 age파트를 numpy 형식으로 변환하여 dataX에 저장한다.
dataXAmount = dataX.size; dataYAmount = dataY.size

# preDraw -> w0, w1, w0List, w1List
mt.figure(figsize=(10,4))
mt.subplots_adjust(wspace = 0.3)

mt.subplot(1,2,1) # 데이터, 경사하강 선형회귀 그래프
mt.xlabel('Age')
mt.ylabel('Tall') 
w0, w1, a = inputVal() # w0, w1, a 입력
mt.plot(dataX, dataY, 'ro', markersize = 3, label = 'data') # 데이터 그래프
mt.plot(dataX, w0*dataX+w1, 'r--', label = 'pre_data') # 초기 직선 그래프
w0List, w1List, MSR_, w0, w1 = preDraw(dataX, dataY, w0, w1, dataXAmount, a)
mt.plot(dataX, w0*dataX+w1, 'k--', label = 'Linear Regression') # 선형회귀 그래프
for i in range(dataXAmount):
    mt.plot(dataX, w0List[i]*dataX+w1List[i], 'g--') # 변화 그래프
mt.legend()

mt.subplot(1,2,2) # 가중치 변화 그래프
mt.xlabel('Count / 100')
mt.ylabel('Weight1, Weight2')
mt.plot(range(w0List.size), w0List, 'b--', label = 'weight1') # w0
mt.plot(range(w1List.size), w1List, 'r--', label = 'weight2') # w1
mt.plot(range(MSR_.size-1), MSR_[1:], 'g--', label = 'MSR') # MSR
mt.legend()

print(w0, w1, MSR_[-1])

mt.show() # 창 표시

# Done
# %%