# 픽셀 접근-이미지 배열에서 특정 좌표에 대한 값을 받아오거나, 변경할 때 사용
# OpenCV의 Mat 클래스-Numpy 배열을 사용-문자열, 리스트, 튜플 등에 사용되는 슬라이싱을 동일하게 사용 가능

import cv2
import numpy as np

# 회색 그라데이션 이미지인 gray를 선언
# 그라데이션 이미지는 등간격(numpy.linspace)을 활용해 구현
# 등간격 배열을 생성-이미지 배열이 아니므로, 차원 변경(numpy.reshape) 함수를 활용해 단일 채널 이미지로 변경
gray = np.linspace(0, 255, num=90000, endpoint=True, retstep=False, dtype=np.uint8).reshape(300, 300, 1) #300×300×1 크기 이미지를 생성-num은 90000
color = np.zeros((300, 300, 3), np.uint8)

color[0:150, :, 0] = gray[0:150, :, 0]
color[:, 150:300, 2] = gray[:, 150:300, 0]

x, y, c = 200, 100, 0
access_gray = gray[y, x, c]
access_color_blue = color[y, x, c]
access_color = color[y, x]

print(access_gray)
print(access_color_blue)
print(access_color)

cv2.imshow("gray", gray)
cv2.imshow("color", color)
cv2.waitKey(0)
cv2.destroyAllWindows()