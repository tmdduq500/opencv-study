# K-평균 군집화 알고리즘(K-means Clustering Algorithm)-비지도 학습의 대표적인 알고리즘 중 하나
# 라벨(Label)이 달려 있지 않은 입력 데이터에 라벨을 달아줍니다.
# 임의의 K개의 중심점(Centroid)를 기준으로 최소 거리에 기반한 군집화를 진행
# 각각의 데이터는 가장 가까운 중심에 군집(Cluster)을 이루며, 같은 중심에 할당된 데이터는 하나의 군집군으로 형성

import numpy as np
import cv2

src = cv2.imread("D:\Python\Image/flower.jpg")
src = cv2.resize(src,dsize=(640,463))

# K-평균 군집화 알고리즘 함수의 입력 데이터 조건을 맞추기 위해
# reshape() 메서드와 astype() 메서드를 활용해 차원과 데이터 형식을 변경
# K-평균 군집화 알고리즘-[N, 3]의 차원 / float32의 데이터 형식을 입력 조건으로 사용
data = src.reshape(-1, 3).astype(np.float32)

# 알고리즘의 종료 기준(TermCriteria)을 설정
criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 10, 0.001)

# K-평균 군집화 알고리즘 함수(cv2.kmeans)-입력 데이터에 특정 군집 개수만큼 군집화를 진행
retval, bestLabels, centers = cv2.kmeans(data, 3, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# retval, bestLabels, centers = cv2.kmeans(data, K, bestLabels, criteria, attempts, flags, centers)
"""
입력 데이터(data)에서 K(K)개의 군집을 설정, 라벨(bestLabels)과 중심점(centers)을 찾습니다.
종료 기준(criteria)-군집화의 반복 작업의 조건을 설정, 시도(attempts)-초기에 다른 라벨을 사용해 반복 실행할 횟수를 설정
플래그(flags)-초기 중심값 위치에 대한 설정을 진행, 결괏값(retval)-이미지의 압축률을 반환
"""
centers = centers.astype(np.uint8)
"""
중심값(centers)-flaot32 형식, uint8 형식으로 변환해 Python OpenCV에서 주로 사용하는 형식으로 변경
중심값(centers)-(2, 3)의 차원을 가지며, 라벨(bestLabels)-(Width * Height, 1)의 차원을 갖습니다.
중심값(centers)에 할당된 값이 라벨(bestLabels)에 매핑할 경우, 시각화를 진행할 수 있습니다.
"""

# Numpy의 브로드캐스팅을 적용해 centers[bestLabels]를 진행. 이때 차원은 (Width * Height, 3)으로 변경
dst = centers[bestLabels].reshape(src.shape)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()