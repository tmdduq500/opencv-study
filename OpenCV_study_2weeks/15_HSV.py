import cv2
src = cv2.imread("D:\Python\Image/Jellybean.jpg", cv2.IMREAD_REDUCED_COLOR_2)
#색상 공간 변환 함수(cv2.cvtcolor)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

#각각의 채널로 분리하기 위해서 채널 분리 함수(cv2.split)를 적용
#색상(Hue), 채도(Saturation), 명도(Value)를 나타낸 값으로 분리
h, s, v = cv2.split(hsv)
cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)
cv2.waitKey()
cv2.destroyAllWindows()
