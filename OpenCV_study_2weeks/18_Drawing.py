# 도형 그리기-선형 타입(Line Types)/비트 시프트(Bit Shift)

#선형 타입(Line Types)
#브레젠험 알고리즘(Bresenham's algorithm)/안티 에일리어싱(Anti-Aliasing)
"""
선은 점들의 연속으로 이뤄진 형태, 두 점 사이의 직선을 그린다면 시작점과 도착점 사이에 연속한 점을 두게 되어 직선을 그리게 됩니다
일반적으로 직선의 방정식을 사용한다면 두 점 사이에 있는 모든 좌표를 알 수 있습니다.
하지만 이 방식은 실수 형태로 소수점이 발생
이미지는 래스터 형식의 사각형 격자 구조로 이뤄진 행렬, 점의 좌표는 모두 정수의 값으로 이뤄져 있습니다
"""

# 브레젠험 알고리즘(Bresenham's algorithm)
# 실수 연산을 하지 않고 정수 연산으로만 선을 그릴 수 있도록 개발된 알고리즘
# 4 연결 방식-선분에 픽셀을 할당할 때 다음에 할당될 위치로 오른쪽, 왼쪽, 위쪽, 아래쪽 영역만 고려
# 8 연결 방식-대각선 방향까지 추가돼 총 여덟 개의 위치를 고려

# 안티 에일리어싱(Anti-Aliasing)
# 영상 신호의 결함을 없애기 위한 기법으로서 이미지나 객체의 가장자리 부분에서 발생하는 계단 현상을 없애고 계단을 부드럽게 보이도록 하는 방식
# 가우스 필터링을 사용하며, 넓은 선의 경우 항상 끝이 둥글게 그려집니다.

# 비트 시프트(Bit Shift)
# 소수점 이하의 값이 포함된 실숫값 좌표로도 도형 그리기 함수를 사용
# 서브 픽셀(sub pixel) 정렬을 지원해서 소수점 이하 자릿수를 표현
# 소수점은 도형 그리기 함수에서 표현할 수 없으므로 비트 시프트의 값으로 지정

import cv2
import numpy as np

src = np.zeros((600, 800, 3), dtype=np.uint8)

src = cv2.line(src, (100, 100), (600, 100), (0, 0, 255), 3, cv2.LINE_AA)    #직선 그리기 함수(cv2.line)
"""
dst = cv2.line(src, pt1, pt2, color, thickness, lineType, shift)
입력 이미지(src)에 시작 좌표(pt1)부터 도착 좌표(pt2)를 지나는 특정 색상(color)과 두께(thickness)의 직선을 그림
추가로 선형 타입(lineType), 비트 시프트(shift)를 설정
"""

src = cv2.circle(src, (200, 200), 50, (0, 255, 0), cv2.FILLED, cv2.LINE_4)  #원 그리기 함수(cv2.circle)
"""
dst = cv2.circle(src, center, radius, color, thickness, lineType, shift)
입력 이미지(src)에 중심점(center)으로부터 반지름(radius)크기의 특정 색상(color)과 두께(thickness)의 원을 그림
추가로 선형 타입(lineType), 비트 시프트(shift)를 설정할 수 있음
만약, 내부가 채워진 원을 그리는 경우, 두께에 cv2.FILLED을 사용해 내부를 채울 수 있음
"""

src = cv2.rectangle(src, (300, 200), (500, 300), (255, 0, 0), 5, cv2.LINE_8)   #사각형 그리기 함수(cv2.rectangle)
"""
dst = cv2.circle(src, center, radius, color, thickness, lineType, shift)
입력 이미지(src)에 중심점(center)으로부터 반지름(radius)크기의 특정 색상(color)과 두께(thickness)의 원을 그림
추가로 선형 타입(lineType), 비트 시프트(shift)를 설정할 수 있음
만약, 내부가 채워진 원을 그리는 경우, 두께에 cv2.FILLED을 사용,내부를 채울 수 있음
"""
src = cv2.ellipse(src, (650, 300), (100, 150), 0, 90, 180, (255, 255, 0), 2)    #호 그리기 함수(cv2.ellipse)
"""
dst = cv2.ellipse(src, center, axes, angle, startAngle, endAngle, color, thickness, lineType, shift)
입력 이미지(src)에 중심점(center)으로부터 장축과 단축(axes) 크기를 갖는 특정 색상(color)과 두께(thickness)의 호를 그림.
각도(angle)는 장축이 기울어진 각도를 의미, 시작 각도(startAngle)와 도착 각도(endAngle)를 설정해 호의 형태를 구성
"""
pts1 = np.array([[100, 350], [300, 350], [200, 400]])
pts2 = np.array([[100, 500], [300, 500], [200, 550]])

# poly 함수를 사용하는 경우, numpy 형태로 저장된 위치 좌표들이 필요
# n개의 점이 저장된 경우, n 각형을 그릴 수 있습니다.
src = cv2.polylines(src, [pts1], True, (0, 255, 255), 2)    #내부가 채워지지 않은 다각형 그리기 함수(cv2.polylines)
"""
dst = cv2.ellipse(src, pts, isClosed, color, thickness, lineType, shift)
입력 이미지(src)에 선들의 묶음(pts) 이뤄진 N개의 내부가 채워지지 않은 다각형을 그림
닫힘 여부(isClosed)를 설정해 처음 좌표와 마지막 좌표의 연결 여부를 설정, 설정한 색상(color)과 두께(thickness)의 다각형이 그려짐
"""
src = cv2.fillPoly(src, [pts2], (125, 125, 255), cv2.LINE_AA) #내부가 채워진 다각형 그리기 함수(cv2.fillPoly)
"""
dst = cv2.ellipse(src, pts, color, thickness, lineType, shift, offset)
입력 이미지(src)에 선들의 묶음(pts) 이뤄진 N개의 내부가 채워지지 않은 다각형을 그림
설정한 색상(color)과 두께(thickness)의 다각형이 그려짐
추가로 선형 타입(lineType), 비트 시프트(shift), 오프셋(offset)을 설정할 수 있음
오프셋은 좌표를 (x, y)만큼 이동시켜 표시
"""

src = cv2.putText(src, "osy&hsm", (350, 550), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3) #문자 그리기 함수(cv2.putText)
"""
dst = cv2.putText(src, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
입력 이미지(src)에 문자열(text)을 텍스트 박스의 좌측 상단 모서리(org)를 기준으로 문자가 그려짐
설정한 글꼴(fontFace)과 글자 크기(fontScale), 색상(color)과 두께(thickness)의 다각형이 그려짐
추가로 선형 타입(lineType), 기준 좌표(bottomLeftOrigin)를 설정할 수 있음
기준 좌표는 텍스트 박스 좌측 상단 모서리가 아닌 텍스트 박스 좌측 하단 모서리를 사용할 경우 기준 좌표에 true를 지정
"""
cv2.imshow("src", src)
cv2.waitKey()
cv2.destroyAllWindows()