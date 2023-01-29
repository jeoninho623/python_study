# pip install scikit-learn
# 머신러닝 모듈
import sklearn
# 그래프 모듈
import matplotlib.pyplot as plt
# 수학/과학 계산 모듈
import numpy as np
# 다차원 데이터 모듈
import pandas as pd
from sklearn.linear_model import LinearRegression
print(sklearn.__version__)

'''
머신러닝 : 데이터(정제) -> 기계학습 -> 예측결과 -> 머신러닝별 비교 후 선정
'''
# 데이터를 가져온다
원본데이터 = pd.read_csv('sample2.csv', encoding='cp949')
print(원본데이터.head())                # 잘 가져왔는지 상위 5개만 보기

# x(원인), y(결과)
X = 원본데이터.iloc[:,:-1].values
Y = 원본데이터.iloc[:,-1].values
print(X)
print(Y)
# 기본
선형기계학습 = LinearRegression()
# fit을 사용하면 기계학습을 한다 (모델생성)
선형기계학습.fit(X,Y)                  

# 학습한 내용을 바탕으로 예측을 해
y_pred = 선형기계학습.predict(X)
print('예측한 y값\n',y_pred)


print('AI 예측값:', 선형기계학습.predict([[4.5]]))
print('AI 예측값:', 선형기계학습.predict([[6.5],[15]]))

# 출력
plt.scatter(X,Y, color='green')                 # 원본데이터는 점으로 그려줘
plt.plot(X, y_pred, color='red')                # 예측데이터는 선으로 그려줘
plt.title('corrsion rate per hours')            # 제목 정해줘
plt.xlabel('hours')                             # x축 제목 정해줘
plt.ylabel('corrsion rate')                     # y축 제목 정해줘
plt.show()                                      # 보여줘