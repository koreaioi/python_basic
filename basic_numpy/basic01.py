import numpy as np

# 0 부터 3 까지의 배열 만들기
#array = np.arange(n) # 0 ~ n 까지 값 배열에 넣기 (1 차원)
array1 = np.arange(4)
print(array1)

# shape(4,4) 만큼의 크기(2 차원)에 zero로 초기화하고 그 자료형들은 각각 실수(float)형이다.
array2 = np.zeros((4,4), dtype = float)
print(array2)

# shape(3,3) 만큼의 크기(2차원)에 one로 초기화하고 그 자료형들은 각각 문자형(str)이다.
array3 = np.ones((3,3), dtype = str)
print(array3)

# 0 부터 9까지 랜덤하게 초기화 된 배열 만들기
#np.random.randint(x, y, 배열 크기) #숫자는 x ~ y-1 사이의 정수(int)
array4 = np.random.randint(0,10, (3,3))
print(array4)

# 통계적 사용
# 평균이 0이고, 표준 편차가 1인 표준 정규를 띄는 배열 = 표준 정규분표
array5 = np.random.normal(0,1,(3,3))
print(array5)

