# 점진성 확률적 허프 변환(Progressive Probabilistic Hough Transform)
"""
또 다른 허프 변환 함수를 사용해 직선을 검출
앞선 알고리즘은 모든 점에 대해 직선의 방정식을 세워 계산하기 때문에 비교적 많은 시간이 소모
기본적으로 점진성 확률적 허프 변환 알고리즘은 앞선 알고리즘을 최적화한 방식
모든 점을 대상으로 직선의 방정식을 세우는 것이 아닌, 임의의 점 일부만 누적해서 계산
일부의 점만 사용하기 때문에 확률적
그러므로, 정확도가 높은 입력 이미지에 대해 검출에 드는 시간이 대폭 줄어듭니다.
또한 시작점과 끝점을 반환하므로 더 간편하게 활용
"""

import numpy as np
import cv2

src = cv2.imread("D:\Python\Image/road.jpg")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 5000, 1500, apertureSize = 5, L2gradient = True)

# cv2.HoughLinesP(검출 이미지, 거리, 각도, 임곗값, 최소 선 길이, 최대 선 간격)를 이용하여 직선 검출을 진행
lines = cv2.HoughLinesP(canny, 0.8, np.pi / 180, 90, minLineLength = 10, maxLineGap = 100)
"""
검출 이미지, 거리, 각도, 임곗값은 앞선 허프 변환 알고리즘 함수와 동일한 의미
최소 선 길이는 검출된 직선이 가져야 하는 최소한의 선 길이를 의미. 이 값보다 낮은 경우 직선으로 간주하지 않습니다.
최대 선 간격은 검출된 직선들 사이의 최대 허용 간격을 의미. 이 값보다 간격이 좁은 경우 직선으로 간주하지 않습니다.
"""

"""
검출을 통해 반환되는 lines 변수는 (N, 1, 4)차원 형태를 갖습니다.
마지막 차원에서 x1, y1, x2, y2의 순서로 시작점과 끝점을 표시
별도의 계산 없이 선 그리기 함수를 활용해 (x1, y1) ~ (x2, y2)의 위치를 표시
"""
for i in lines:
    cv2.line(dst, (int(i[0][0]), int(i[0][1])), (int(i[0][2]), int(i[0][3])), (0, 0, 255), 2)


cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()