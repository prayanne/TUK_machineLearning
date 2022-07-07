#%%
############################################################
# 예측값 yn과 실제값(데이터) yn을 비교하는 구조이다.
# 1. yn^ - yn
# 2. 공식을 활용
############################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as mt
import math

############################################################

def costFunc(x, y, weight0, weight1, dataAmount = 1): # 손실함수, 평균제곱오차 | 예측값과 실제값이 얼마나 차이나는지 보여주는 함수이다. 손실함수를 통해 평균제곱오차를 도출한다.
 # 예측값 - 실제값 | 데이터1 즉, xn에서 예측값 y, 실제값 y를 비교한다. | 차이를 제곱하여 추합해, 데이터 개수로 나누고, 평균을 구한다. | 차이나는 정도를 평균으로 나타낸 것으로 이를 근거로 가중치를 변화한다.
    temp = (weight0 * x + weight1) - y # 예측값 - 실제값 | numpy array로 구성한다.
    arrSum = (temp**2).sum() # 
    
    total = arrSum / (dataAmount) # 평균 | dataAmount는 함수 요소로 받아온다.
    return round(total, 4) # float, 소수점 5자리에서 반올림

def gredientFunc(x, y, weight0, weight1, dataAmount = 1, a = 0.1): # 손실함수, 평균제곱오차 | 예측값과 실제값이 얼마나 차이나는지 보여주는 함수이다. 손실함수를 통해 평균제곱오차를 도출한다.
 # 예측값 - 실제값 | 데이터1 즉, xn에서 예측값 y, 실제값 y를 비교한다. | 차이를 제곱하여 추합해, 데이터 개수로 나누고, 평균을 구한다. | 차이나는 정도를 평균으로 나타낸 것으로 이를 근거로 가중치를 변화한다.

    global w0
    global w1
    
    temp = (weight0 * x + weight1) - y # 예측값 - 실제값 | numpy array로 구성한다.
    w0Sum = (x*temp).sum() # 
    w1Sum = (temp).sum() # 
    w0Result = -2 * a * w0Sum / (dataAmount) # 평균제곱오차의 2차원 그래프의 편미분값들(w0, w1)과 학습률을 곱한다. | 이후, 이를 w0, w1에서 빼게 된다. | w0[t+1] = w0[t] - 2a*2/n * x(평균오차) 이므로, 기울기의 
    w1Result = -2 * a * w1Sum / (dataAmount)
    
    w0 += w0Result
    w1 += w1Result
    
    return round(w0, 4), round(w1, 4) # float, 소수점 5자리에서 반올림

def drawMatplt():
    # mt.show()
    while 1:
        print(gredientFunc(dataX, dataY, w0, w1, dataXAmount, a))
############################################################

data = pd.read_csv('/config/workspace/PROject/TUK_machine_learning/week2/linear_regression_data01.csv', delimiter=",", names =['age', 'name'])

dataX = data["age"].to_numpy()
dataXAmount = dataX.size
dataY = data["name"].to_numpy()
dataYAmount = dataY.size

w0 = float(input("weight1: ")) # 데이터1 가중치
w1 = float(input("weight2: ")) # 데이터2 가중치

a = float(input("leaning rate: ")) # 학습률, Learning Rate

# print(costFunc(dataX, dataY, w0, w1, dataXAmount)) # age, name, weight0, weight1 | numpy array

for i in range(20000):
    
    # mt.plot(x, )
    
    print(costFunc(dataX, dataY, w0, w1, dataXAmount), end=' - ') # age, name, weight0, weight1 | numpy array
    print(gredientFunc(dataX, dataY, w0, w1, dataXAmount, a))
    
mt.plot(dataX, dataY, 'ro')
mt.show()
#Done
# %%
