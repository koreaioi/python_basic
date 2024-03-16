import numpy as np

# 균일한 간격으로 데이터 생성
array = np.linspace(0,10,5) #개수는 다섯개 인데 0~10을 5개의 균일한 간격으로 할당
print(array)

# 난수의 재연 (실행 마다 결과 동일 seed?)
np.random.seed(7)
print(np.random.randint(0,10,(2,3)))

# Numpy 배열 객체의 복사
array1 = np.arange(0,10)
array2 = array1 # 참조하게 됨
array3 = array1.copy() # 얕은 복사
array2[0] = 99
print(array1)
print(array1)
array3[0] = 0
print(array3)

# 중복된 원소 제거
array = np.array([1,1,2,2,3,3,4,4,4,5,])
print(np.unique(array))