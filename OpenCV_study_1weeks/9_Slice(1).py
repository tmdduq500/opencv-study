#이미지를 처리할 때 객체를 탐지하거나 검출하는 영역을 명확하게 관심 영역

"""
OpenCV의 이미지는 이미지는 numpy 배열 형식과 동일
src 이미지에 src[높이(행), 너비(열)]로 관심 영역을 설정
리스트(List)나 배열(Array)의 특정 영역을 자르는 방식과 동일
이미지를 자르거나 복사할 때, dst = src의 형태로 사용할 경우, 얕은 복사(shallow copy)가 되어 원본도 영향
그러므로, *.copy()를 이용해 깊은 복사(deep copy)를 진행
"""
import cv2

src = cv2.imread("D:\Python\Image/apple.jpg", cv2.IMREAD_COLOR)
dst = src[100:600, 200:700].copy()

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()