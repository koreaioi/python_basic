# 집합(set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python을 모두  할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java를 하거나 python을 할 수 있는 개발자, 둘 중 하나)
print(java | python)
print(java.union(python))

# 차집합 (java를 할 수는 있으나 python을 할 수 없는 개발자
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)