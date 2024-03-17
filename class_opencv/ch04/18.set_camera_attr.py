import cv2

def zoom_bar(value):
    global vfile
    vfile.set(cv2.CAP_PROP_ZOOM, value)


def focus_bar(value):
    global vfile
    vfile.set(cv2.CAP_PROP_FOCUS,value)


movie_file = "move_file.avi"
vfile = cv2.VideoCapture(movie_file)
if not vfile.isOpened() : raise Exception("비디오 연결 실패!")

#윈도우 이름 지정
window = "Change Camera Properties"
cv2.namedWindow(window)
# zoom, focus 트랙바 생성
cv2.createTrackbar('zoom', window, 0, 40, zoom_bar)
cv2.createTrackbar('focus', window, 0, 40, focus_bar)

while True:
    ret, frame = vfile.read()
    if not ret : break;
    if cv2.waitKey(30) >= 0 :break; #30ms 대기후 다음 프레임 넘어가거나 입력값이오면 break

    cv2.imshow(window, frame)



vfile.release()