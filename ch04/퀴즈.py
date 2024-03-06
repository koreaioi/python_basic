"""
Quiz) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙 1 : http:// 부분은 제외 => naver.com
규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 개수  + "!" 로 구성
                    (nav)          (5)          (1)          (!)
예) 생성된 비밀번호 : nav51!
"""

# 규칙 1
url = "http://naver.com"
my_str = url.replace("http://","")

# 규칙 2
index = my_str.index(".")
my_str = my_str[0:index]
#print(my_str)

# 규칙 3
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
#print(password)

print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))