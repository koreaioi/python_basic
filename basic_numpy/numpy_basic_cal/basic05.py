import numpy as np

array1 = np.arange(16).reshape(4,4)
print(array1)
array2 = array1 < 10
print(array2)

array1[array2] = 100
print(array1)
# array2 에서 참이 되는 값들을 100으로 바꾼다. True => 100
# 이미지 처리에서 어떤색상이 너무 밝으면 그 색상만 바꾸는게 가능
# ex 색이 250 이상인건 200으로 줄인다든지

array3 = np.arange(240, 256).reshape(4,4)
print(array3)

array4 = array3 > 250
array3[array4] = 200

print(array3)