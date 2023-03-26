# 모폴로지 변환(Perspective Transformation)-영상이나 이미지를 형태학적 관점에서 접근하는 기법
# 주로 영상 내 픽셀값 대체에 사용-노이즈 제거, 요소 결합 및 분리, 강도 피크 검출 등에 이용
# 집합의 포함 관계, 이동(translation), 대칭(reflection), 여집합(complement), 차집합(difference) 등의 성질을 사용
# 팽창(dilation) / 침식(erosion) -이미지와 커널의 컨벌루션 연산

# 팽창(dilation)-노이즈 제거 후 줄어든 크기를 복구하고자 할 때 주로 사용
"""
커널 영역 안에 존재하는 모든 픽셀의 값을 커널 내부의 극댓값(local maximum)으로 대체
구조 요소(element)를 활용, 이웃한 픽셀들을 최대 픽셀값으로 대체
팽창 연산을 적용-어두운 영역이 줄어들고 밝은 영역이 늘어납니다.
커널의 크기나 반복 횟수에 따라 밝은 영역이 늘어나 스펙클(speckle)이 커지며 객체 내부의 홀(holes)이 사라집니다.
"""

# 침식(Erosion)-노이즈 제거에 주로 사용
"""
커널 영역 안에 존재하는 모든 픽셀의 값을 커널 내부의 극솟값(local minimum)으로 대체
즉, 구조 요소(element)를 활용, 이웃한 픽셀을 최소 픽셀값으로 대체
침식 연산을 적용-밝은 영역이 줄어들고 어두운 영역이 늘어납니다.
커널의 크기나 반복 횟수에 따라 어두운 영역이 늘어나 스펙클(speckle)이 사라지며, 객체 내부의 홀(holes)이 커집니다.
"""

import numpy as np
import cv2

a = cv2.imread("D:\Python\Image/zebra.jpg")
src=cv2.resize(a,dsize=(600,400))

# cv2.getStructuringElement()를 활용해 구조요소를 생성
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5)) # cv2.getStructuringElement(커널의 형태, 커널의 크기, 중심점)로 구조 요소 생성
"""
커널의 형태는 직사각형(Rect), 십자가(Cross), 타원(Ellipse)
커널의 크기-구조 요소의 크기를 의미. 이때, 커널의 크기가 너무 작다면 커널의 형태는 영향을 받지 않습니다.
고정점-커널의 중심 위치. 필수 매개변수가 아니며, 설정하지 않을 경우 사용되는 함수에서 값이 결정
"""
# 생성된 구조 요소를 활용해 모폴로지 변환을 적용
# 팽창 연산의 경우 밝은 영역이 커지며, 침식 연산의 경우 어두운 영역이 커집니다.

# cv2.dilate(원본 배열, 구조 요소, 고정점, 반복 횟수, 테두리 외삽법, 테두리 색상)로 팽창 연산을 진행
dilate = cv2.dilate(src, kernel, anchor=(-1, -1), iterations=5) # 팽창 함수(cv2.dilate)

# cv2.erode(원본 배열, 구조 요소, 고정점, 반복 횟수, 테두리 외삽법, 테두리 색상)로 침식 연산을 진행
erode = cv2.erode(src, kernel, anchor=(-1, -1), iterations=5)   # 침식 함수(cv2.erode)

# 연결 함수(np.concatenate)로 원본 이미지, 팽창 결과, 침식 결과를 하나의 이미지로 연결
dst = np.concatenate((src, dilate, erode), axis=1)  # np.concatenate(연결할 이미지 배열들, 축 방향)로 이미지를 연결
"""
axis=0으로 사용할 경우, 세로 방향으로 연결
수평 연결 함수(cv2.hconcat) / 수직 연결 함수(cv2.vconcat)`로도 이미지를 연결
"""
cv2.imshow('src',src)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)
cv2.destroyAllWindows()