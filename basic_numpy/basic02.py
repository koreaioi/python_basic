import numpy as np

# Numpy 배열 합치기 -> 1차원 배열 들을 가로 축으로 합쳐서 그대로 1차원
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.concatenate([array1, array2])

print(array3.shape)
print(array3)



# Numpy 배열 형태 바꾸기
# 1차원 배열 [1,2,3,4] 를 2차원 배열 로 바꾸기 [[1,2],[3,4]]
array1 = np.array([1,2,3,4])
array2 = array1.reshape((2,2))
print(array2)

# Numpy 배열 합치기 -> 1차원 배열 들을 세로 축으로 합쳐서 그대로 2차원

array1 = np.arange(4).reshape(1,4)
array2 = np.arange(8).reshape(2,4)

print(array1)
print(array2)
#array1과 array2 세로축으로 합치기
array3 = np.concatenate([array1, array2], axis=0) #axis = 0 이 세로축으로 합치라는 뜻
print(array3)
#axis = 0 행, axis = 1 열