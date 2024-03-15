import numpy as np
#최대, 최소, 합계, 평균 구하기
array = np.arange(16).reshape(4,4)

print("최댓 값: ", np.max(array))
print("최소 값: ", np.min(array))
print("합계: ", np.sum(array))
print("평균 값: ",np.mean(array))

print(array)

# 열 또는 행 기준으로 합계, 평균 구하기
print("행 기준 합계", np.sum(array ,axis=0)) #axis를 0 하면 열을 기준으로 더함
print("행 기준 합계", np.sum(array ,axis=1)) #axis를 1 하면 행을 기준으로 더함
