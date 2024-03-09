# 리스트 []

# 지하철 칸 별로 10명, 20명, 30명
#
# subway1 = 10
# subway2 = 20
# subway3 = 30
#
# subway = [10,20,30]
# print(subway)
#
# subway  = ["유재석", "조세호", "박명수"]
# print(subway)
#
# # 리스트를 활용하기
# # 조세호씨가 몇 번째 칸에 타고 있는가? - 인덱스는 0번째 부터 시작
# print(subway.index("조세호"))
#
# # 하하씨가 다음 정류장에서 버스 탑승!
# subway.append("하하")
# print(subway)
#
# # append는 맨 뒤에 추가 하므로 중간에 추가하는 방법은 없을까?
# # 정형돈씨를 유재석 - 조세호 사이에 태워보기
# subway.insert(1, "정형돈")
# print(subway)
#
# # 버스에 있는 사람을 한 명씩 뒤에서 꺼냄
# # print(subway.pop())
# # print(subway)
# #
# # print(subway.pop())
# # print(subway)
# #
# # print(subway.pop())
# # print(subway)
#
# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)
#
# # 순서 뒤집기 기능 반대로 정렬
# num_list.reverse()
# print(num_list)
#
# # 리스트의 값 지우기
# num_list.clear()
# print(num_list)

# 리스트는 다양한 자료형과 함께 사용 가능
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20,True]
print(mix_list)

# 리스트 학장
num_list.extend(mix_list)
print(num_list)


