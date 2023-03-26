# 직선 검출 알고리즘은 허프 변환(Hough Transform)을 활용해 직선을 검출
# 허프 변환(Hough Transform)-이미지에서 직선을 찾는 가장 보편적인 알고리즘
"""
이미지에서 선과 같은 단순한 형태를 빠르게 검출할 수 있으며, 직선을 찾아 이미지나 영상을 보정하거나 복원
허프 선 변환은 이미지 내의 어떤 점이라도 선 집합의 일부일 수 있다는 가정하에 직선의 방정식을 이용해 직선을 검출
"""

import numpy as np
import cv2

# 이미지에서 직선을 검출하기 위해서, 전처리 작업을 진행
src = cv2.imread("D:\Python\Image/road.jpg")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 5000, 1500, apertureSize = 5, L2gradient = True)

# cv2.HoughLines(검출 이미지, 거리, 각도, 임곗값, 거리 약수, 각도 약수, 최소 각도, 최대 각도)를 이용하여 직선 검출을 진행
lines = cv2.HoughLines(canny, 0.8, np.pi / 180, 150, srn = 100, stn = 200, min_theta = 0, max_theta = np.pi)
"""
거리와 각도는 누산 평면에서 사용되는 해상도를 나타냅니다.
거리의 단위는 픽셀을 의미, 0.0 ~ 1.0의 실수 범위를 갖습니다.
각도의 단위는 라디안을 사용, 0 ~ 180의 범위를 갖습니다.

임곗값은 허프 변환 알고리즘이 직선을 결정하기 위해 만족해야 하는 누산 평면의 값을 의미

누산 평면은 각도*거리의 차원을 갖는 2차원 히스토그램으로 구성

거리 약수와 각도 약수는 거리와 각도에 대한 약수(divisor)를 의미

두 값 모두 0의 값을 인수로 활용할 경우, 표준 허프 변환이 적용, 하나 이상의 값이 0이 아니라면 멀티 스케일 허프 변환이 적용

최소 각도와 최대 각도는 검출할 각도의 범위를 설정
"""


"""
검출을 통해 반환되는 lines 변수는 (N, 1, 2)차원 형태
내부 차원의 요소로는 검출된 거리(rho)와 각도(theta)가 저장
반복문을 활용해 lines 배열에서 거리와 각도를 반환할 수 있으며
거리와 각도를 다시 직선의 방정식의 형태로 구성해야 결과 이미지 위에 표현

허프 변환 함수는 시작점과 도착점을 알려주는 함수가 아닌, 가장 직선일 가능성이 높은 거리와 각도를 검출
검출된 정보는 직선의 방정식에 더 가깝습니다.
"""
for i in lines:
    rho, theta = i[0][0], i[0][1]
    a, b = np.cos(theta), np.sin(theta)
    x0, y0 = a*rho, b*rho

    scale = src.shape[0] + src.shape[1]

    x1 = int(x0 + scale * -b)
    y1 = int(y0 + scale * a)
    x2 = int(x0 - scale * -b)
    y2 = int(y0 - scale * a)

    cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.circle(dst, (int(x0),int(y0)), 3, (255, 0, 0), 5, cv2.FILLED)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()