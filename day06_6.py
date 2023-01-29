# 문제 1 : 머신러닝을 사용해서 300명이 방문했을때 판매량을 예측해보세요

import sklearn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


dt = pd.read_csv('kyobo.csv', encoding='cp949')
print(dt.head())

x = dt.iloc[:,:-1].values
y = dt.iloc[:,-1].values
print(x)
print(y)

machine_s = LinearRegression()
machine_s.fit(x,y)

y_pred = machine_s.predict(x)
print('AI 예측값:',machine_s.predict([[300]]))


plt.scatter(x,y,color='green')
plt.plot(x,y_pred,color='red')
plt.title('sales volume')
plt.xlabel('Unique Visitor')
plt.ylabel('sales volume')
plt.show()