jumin = "001104-1234567"

# 필요한 만큼 문자열을 자르기 = 슬라이싱

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전 (0,1 번째 인덱스)
print("월 : " +jumin[2:4]) # 2 부터 4 직전
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:]) # 맨뒤 인덱스 생략 가능
print("뒤 7자리 : " + jumin[-7:]) #뒤에서 7번째 ~ 끝까지
