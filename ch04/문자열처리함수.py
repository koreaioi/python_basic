python = "Python is Amazing"
print(python.lower()) # 소문자로
print(python.upper()) # 대문자로
print(python[0].isupper()) # 0번째 인덱스가 대문자인가? -> true or false
print(len(python)) #길이
print(python.replace("Python" , "Java"))

index = python.index("n")
print(index) # 맨 처음 나온 인덱스를 기준으로 출력
index = python.index("n", index + 1) #기존 n의 위치에 + 1 한 인덱스부터 탐색시작
print(index)

print(python.find("Java")) # 맨 처음 나온 인덱스를 기준으로 출력, 없으면 -1
# print(python.index("Java")) # 없으면 오류가 난다.

print(python.count("n")) # 해당 문자가 나온 회수

# 소문자, 대문자, 대문자인지 소문자인지 확인, 길이, 인덱스 출력, find함수, count