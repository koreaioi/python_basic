# 튜플
# 리스트에 비해 내용 변경 or 추가가 불가능 하지만 리스트보다 속도가 빠르다.
# () 소괄호 사용

menu = ("돈까스", "치즈까스")
print(menu[0], menu[1])

#menu.add("생선까스") <- 오류 (수정, 추가 불가)

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국",20,"코딩")
