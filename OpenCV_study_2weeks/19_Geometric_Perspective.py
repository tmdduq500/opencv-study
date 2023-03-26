# 기하학적 변환(Geometric Transform)
# 이미지를 인위적으로 확대, 축소, 위치 변경, 회전, 왜곡하는 등 이미지의 형태를 변환하는 것을 의미
# 픽셀 좌푯값의 위치를 재배치하는 과정

# 아핀 변환(Affine Transformation)/원근 변환(Perspective Transformation)
# 아핀 변환(Affine Transformation)-2×3 행렬을 사용, 행렬 곱셈에 벡터 합을 활용해 표현할 수 있는 변환을 의미
# 아핀 변환은 정확하게는 3×3 행렬 형태. 행렬의 세 번째 행이 [0, 1, 1] 값을 가져 OpenCV에서는 표현하지 않음.
# 원근 변환(Perspective Transformation)- 3×3 행렬을 사용, 호모그래피(Homography)로 모델링할 수 있는 변환을 의미

import cv2
import numpy as np

src = cv2.imread("D:\Python\Image/jellybean.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

# 원근 변환(Perspective Transformation)-네 점을 사용하여 픽셀을 재매핑
"""
매핑에 사용할 변환 전 원본 이미지의 픽셀 좌표(srcPoint)과 변환 후 결과 이미지의 픽셀 좌표(dstPoint)를 선언
변환 전 원본 이미지의 픽셀 좌표가 변환 후 결과 이미지의 픽셀로 매핑되어 이미지가 변형
예제의 좌표의 순서는 좌상, 우상, 우하, 좌하 순서입니다. numpy.array 형태로 선언, 좌표의 순서는 원본 순서와 결과 순서가 동일해야함
만약, 순서가 동일하지 않다면 비틀린(twist) 형태로 이미지가 표현
"""
srcPoint = np.array([[300, 200], [400, 200], [500, 500], [200, 500]], dtype=np.float32)
dstPoint = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)
# 원근 맵 행렬 생성 함수(cv2.GetPerspectiveTransform)- 매핑 좌표에 대한 원근 맵 행렬을 생성
# M = cv2.GetPerspectiveTransform(src, dst)
# 변환 전 네 개의 픽셀 좌표(src)과 변환 후 네 개의 픽셀 좌표(dst)을 기반으로 원근 맵 행렬(M)을 생성

dst = cv2.warpPerspective(src, matrix, (width, height)) 
# 원근 변환 함수(cv2.warpPerspective)원근 맵 행렬에 대한 기하학적 변환을 수행
# dst = cv2.warpPerspective(src, M, dsize, dst, flags, borderMode, borderValue)
# 입력 이미지(src)에 원근 맵 행렬(M)을 적용, 출력 이미지 크기(dsize)로 변형해서 출력 이미지(dst)를 반환
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()