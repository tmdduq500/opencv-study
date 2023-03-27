import cv2

def onChange(pos):
    pass

src = cv2.imread("D:\Python\Image/cherryblossom.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_2)


# 트랙 바를 윈도우 창에 부착하기 위해선, 미리 윈도우 창에 생성된 상태여야 합니다.
# cv2.namedWindow("윈도우 창 제목")을 사용해 윈도우 창을 생성(윈도우 창 제목은 변수와 같은 기능)
cv2.namedWindow("Trackbar Windows")

# cv2.createTrackbar("트랙 바 이름", "윈도우 창 제목", 최솟값, 최댓값, 콜백 함수)을 사용해 트랙 바를 생성
cv2.createTrackbar("threshold", "Trackbar Windows", 0, 255, lambda x:x)
cv2.createTrackbar("maxValue", "Trackbar Windows", 0, 255, lambda x:x)
"""
트랙 바 이름-트랙 바의 명칭, 윈도우 창 제목과 같이 변수와 비슷한 역할
윈도우 창 제목-트랙 바를 부착할 윈도우 창을 의미
최솟값,최댓값-트랙 바를 조절할 때 사용할 최소/최대 값을 의미
콜백 함수-트랙 바의 바를 조절할 때 위치한 값을 전달
onChange 함수의 pos-현재 발생한 트랙 바 값을 반환
특별한 이벤트를 처리하지 않는다면, 함수의 반환값에 pass나 return를 사용하거나 lambda 함수로 아무 작업을 하지 않음
"""

# cv2.setTrackbarPos("트랙 바 이름", "윈도우 창 제목", 설정값)을 사용해 트랙 바의 값을 설정
cv2.setTrackbarPos("threshold", "Trackbar Windows", 127)
cv2.setTrackbarPos("maxValue", "Trackbar Windows", 255)
"""
트랙 바 이름, 윈도우 창 제목-앞서 설명한 역할과 동일
설정값-초기에 할당된 값이나, 특정 조건 등을 만족했을 때 강제로 할당할 값을 설정
"""

# cv2.waitKey(1)은 1ms마다, 키보드 이벤트를 감지
# ord('q')는 문자 q를 아스키 코드 값으로 변경
while cv2.waitKey(1) != ord('q'):

    # cv2.getTrackbarPos("트랙 바 이름", "윈도우 창 제목")을 사용해 트랙 바의 값을 받아옵니다.
    thresh = cv2.getTrackbarPos("threshold", "Trackbar Windows")
    maxval = cv2.getTrackbarPos("maxValue", "Trackbar Windows")

    _, binary = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)

    cv2.imshow("Trackbar Windows", binary)

cv2.destroyAllWindows()
