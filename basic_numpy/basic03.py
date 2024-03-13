import numpy as np

# 배열 나누기
array = np.arange(8).reshape(2,4)
#array를 인덱스 [2] 를 기준으로 axis=1(열)을 축으로 나눈다)
left, right = np.split(array, [2] , axis =1)

print(left.shape)  #(2,2) 출력
print(right.shape) #(2,2) 출력
print(array)
print(left)
print(right)

