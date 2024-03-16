import numpy as np

# 단일 객체 저장 및 불러오기
array = np.arange(0,10)
np.save('save.npy', array) # 넘파이 객체를 save.npy 라는 파일로 저장

# 넘파일 파일 불러오기
result = np.load('save.npy')
print(result)

# 복수 객체 저장 및 불러오기
array1 = np.arange(10)
array2 = np.arange(10, 20)
np.savez('saved.npz', array1=array1 , array2=array2)

data = np.load('saved.npz')
result1 = data['array1'] #key value 중 key를 넣어서 저장
result2 = data['array2']

print(result1)
print(result2)