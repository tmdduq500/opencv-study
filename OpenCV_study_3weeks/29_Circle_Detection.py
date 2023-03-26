# 허프 원 변환(Hough Circle Transform) 알고리즘을 활용
"""
3차원 누산 평면으로 검출
각 차원은 원의 중심점 x, 원의 중심점 y, 원의 반경 r을 활용해 누산 평면을 구성
누산 평면은 2차원 공간(x, y)에서 3차원 공간(a, b, r)으로 변환
허프 원 변환의 동작 방식은 이미지에서 가장자리를 검출
OpenCV 원 검출 함수-2단계 허프 변환(Two stage Hough Transform) 방법을 활용,원을 검출
"""

import cv2
import numpy as np

src = cv2.imread("D:\Python\Image/colorball.jpg")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# cv2.HoughCircles(검출 이미지, 검출 방법, 해상도 비율, 최소 거리, 캐니 엣지 임곗값, 중심 임곗값, 최소 반지름, 최대 반지름)이용, 원 검출을 진행
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1 = 250, param2 = 10, minRadius = 80, maxRadius = 120)
"""
검출 방법은 항상 2단계 허프 변환 방법(21HT, 그레이디언트) 사용
해상도 비율-원의 중심을 검출하는 데 사용되는 누산 평면의 해상도를 의미
인수를 1로 지정- 입력한 이미지와 동일한 해상도를 가집니다 / 인수를 2로 지정- 누산 평면의 해상도가 절반으로 줄어 입력 이미지의 크기와 반비례
최소 거리-일차적으로 검출된 원과 원 사이의 최소 거리. 이 값은 원이 여러 개 검출되는 것을 줄이는 역할
캐니 엣지 임곗값-허프 변환에서 자체적으로 캐니 엣지를 적용, 이때 사용되는 상위 임곗값을 의미
하위 임곗값-자동으로 할당, 상위 임곗값의 절반에 해당하는 값을 사용
중심 임곗값-그레이디언트 방법에 적용된 중심 히스토그램(누산 평면)에 대한 임곗값.값이 낮을 경우 더 많은 원이 검출
최소 반지름,최대 반지름-검출될 원의 반지름 범위. 0을 입력-검출할 수 있는 반지름에 제한 조건을 두지 않습니다.
최소 반지름,최대 반지름에 각각 0을 입력-반지름을 고려하지 않고 검출, 최대 반지름에 음수를 입력- 검출된 원의 중심만 반환
"""
#반환된 circles 값들을 반올림하고 2^16개의 양수로 표현
circles = np.uint16(np.around(circles))

# 검출을 통해 반환되는 circles 변수는 (1, N, 3)차원 형태
"""
내부 차원의 요소로는 검출된 중심점(x, y)과 반지름(r)이 저장
반복문을 활용해 circles 배열에서 중심점과 반지름을 반환
검출된 정보는 소수점을 포함. 원 그리기 함수는 소수점이 포함되어도 사용할 수 있으므로, 형변환을 진행하지 않습니다.
원 그리기 함수를 활용해 (x, y, r)의 원을 표시
"""
for i in circles[0]:

    cv2.circle(dst, (i[0], i[1]), i[2], (255, 255, 255), 5)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()