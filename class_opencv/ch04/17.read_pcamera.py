import cv2

movie_file = "move_file.avi" # 미리 비디오 파일 이름 지정

vfile = cv2.VideoCapture(movie_file) # 카메라에 연결
if not vfile.isOpened(): raise Exception("카메라 연결 실패")

while True:
    ret, frame = vfile.read() # 한 프레임씩 읽기?
    if not ret : break; # 값이 없으면 취소
    # 30ms단위로 프레임을 바꾼다. -> 1000ms / 30 -> 33프레임이 나온다.
    # 키 값이 입력되면 break 한다. 키값이 입력 안되면 다음 라인으로 넘어감
    if cv2.waitKey(30) >= 0 : break
    cv2.imshow(movie_file, frame)

# 다른 방식

# if vfile.isOpened():
#     while True:
#         vret, vframe = vfile.read()
#         if vret: #값이 있으면
#             cv2.imshow(movie_file, vframe)
#             cv2.waitKey(25) #40프레임 (1000ms / 25ms)
#         else:
#             break;