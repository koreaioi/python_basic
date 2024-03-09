# 사전 Dictionary == key:value 형태
# key의 중복을 허용하지 않는다. 중괄호를 사용한다. {}

# 딕셔너리 출력시 사전명[key값] 하면 value가 나온다
cabinet = {3 : "유재석", 100 : "김태호"}
# print(cabinet[3])
# print(cabinet[100])
#
# print(cabinet.get(3))
#
# # 캐비넷에 5라는 키값이 없어서 line 12에서 오류가 나 프로그램이 종료된다.
# print(cabinet[5])
#
# # 캐비넷에 키값이 없을 때 get을 사용하면 None을 반환
# print(cabinet.get(5))
# # 캐비넷에 키값이 없을 때 get을 사용해 None일 경우 두번째 매개인자를 출력
# print(cabinet.get(5), "사용 가능")

# 포함 확인
# print(3 in cabinet)
# print(5 in cabinet)

cabinet = {"A-3" : "유재석" , "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님 수정 및 추가
print(cabinet)
cabinet["A-3"] = "김종국" # 김종국으로 대체됨
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"] # 키가 "A-3" 인 한 쌍 제거
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

