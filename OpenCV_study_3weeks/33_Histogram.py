# 히스토그램이-도수 분포표 중 하나,데이터의 분포를 몇 개의 구간으로 나누고 각 구간에 속하는 데이터를 시각적으로 표현한 막대그래프
# X 축을 픽셀의 값 / Y 축을 해당 픽셀의 개수로 표현

# 히스토그램 3요소
"""
1.빈도 수(BINS): 히스토그램 그래프의 X 축 간격
    픽셀값의 범위는 0~255로 총 256개의 범위, (ex.빈도 수의 값이 8이라면 0 ~ 7, 8 ~ 15, …, 248 ~ 255의 범위로 총 32개의 막대가 생성)

2.차원 수(DIMS): 히스토그램을 분석할 이미지의 차원
    그레이스케일-단일 채널, 하나의 차원에 대해 분석 / 색상 이미지-다중 채널, 세 개 이상의 차원에 대해 분석
3.범위(RANGE): 히스토그램 그래프의 X 축 범위
    이미지에서 측정하려는 픽셀값의 범위, 특정 픽셀값 영역에 대해서만 분석하게 하는 데 사용
"""

import cv2
import numpy as np

src = cv2.imread("D:\Python\Image/road1.jpg")
src = cv2.resize(src,dsize=(800,600))
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
result = np.zeros((src.shape[0], 256), dtype=np.uint8)

# 히스토그램 계산 함수(cv2.calcHist)를 통해 분포를 계산
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
# cv2.calcHist(연산 이미지, 특정 채널, 마스크, 히스토그램 크기, 히스토그램 범위)를 이용,히스토그램을 계산
"""
특정 채널은 차원 수(DIMS)를 설정, 그레이스케일 이미지-단일 채널-0을 사용
마스크-특정 영역에 대해서만 연산할 때 사용. 해당 영역은 없으므로, None을 할당
히스토그램 크기-빈도 수(BINS)를 설정. 픽셀의 범위는 0 ~ 255 이므로, [256]을 할당
히스토그램 범위-범위(RANGE)를 설정. 예외 사항이 없으므로, 0 ~ 255의 범위를 계산하기 위해 [0, 256]을 할당
"""

# 히스토그램을 통해 연산된 결과는 정규화되지 않은 값
# 정규화 함수(cv2.normalize)를 통해 값을 변경
cv2.normalize(hist, hist, 0, result.shape[0], cv2.NORM_MINMAX)
# cv2.normalize(입력 배열, 결과 배열, alpha, beta, 정규화 기준)으로 값을 정규화
# cv2.NORM_MINMAX을 통해, 정규화 기준을 최솟값이 alpha가 되고, 최댓값이 beta가 되게 변경
# 최솟값은 0이 되며, 최댓값은 result.shape[0]

for x, y in enumerate(hist):
    cv2.line(result, (int(x), result.shape[0]), (int(x), result.shape[0] - int(y)), 255)

dst = np.concatenate((gray,result),axis=1)
dst2 = np.hstack([gray, result])

cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()