import numpy as np

array = np.random.randint(1,10, 4).reshape(2,2)
print(array)
result_array = array * 10 #벡터 * 스칼라 여서 각각 10이 곱해진다
print(result_array)

