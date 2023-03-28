# 리매핑(Remapping)-입력 이미지에 기하학적인 변형을 적용하는 방법
# 이미지에 변환 행렬 연산을 적용하는 것이 아닌, 비선형 변환을 적용할 수 있습니다.
# 픽셀들의 좌표를 임의의 특정 좌표로 옮겨 이미지를 변경하는 작업을 의미

import cv2
import numpy as np

src = cv2.imread("D:\Python\Image/buildings.jpg")
src = cv2.resize(src,dsize=(640,480))
height, width = src.shape[:2]

# 색인 배열 생성 함수(np.indices)을 활용-원본 이미지 크기와 동일한 색인 배열을 생성
# np.indices((높이, 너비), 정밀도)를 의미
map2, map1 = np.indices((height, width), dtype=np.float32)
"""
Y축 좌표 색인 행렬, X축 좌표 색인 행렬을 반환
이동되는 좌표의 값은 정수형이 아닌, 실수형
"""

# map1과 map2에 임의의 삼각 함수를 적용하여 행렬의 형태를 변경
# map1과 map2는 매핑될 좌표의 값을 의미
# 해당 행렬의 값을 변경하면 최종 반환 이미지의 형태가 달라집니다.
map1 = map1 + width / 100 * np.sin(map1)
map2 = map2 + height / 100 * np.cos(map2)

# 리매핑 함수(cv2.remap)을 활용-원본 이미지에 리매핑을 적용
# cv2.remap(원본 이미지, X축 좌표 색인 행렬, Y축 좌표 색인 행렬, 보간법, 외삽법, 외삽 색상)
dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC)
"""
원본 이미지의 픽셀 배열을 X축 좌표 색인 행렬,Y축 좌표 색인 행렬의 값을 적용-픽셀들을 이동
색인 행렬의 값-정수 좌표가 아니므로, 보간법과 외삽법을 적용
"""
cv2.imshow("dst", dst)
cv2.waitKey()