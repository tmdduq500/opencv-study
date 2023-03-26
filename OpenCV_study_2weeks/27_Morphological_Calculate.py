# 열림(Opening)
"""
팽창 연산자와 침식 연산자의 조합, 침식 연산을 적용한 다음, 팽창 연산을 적용

열림 연산을 적용-침식 연산으로 인해 밝은 영역이 줄어들고 어두운 영역이 늘어납니다.
줄어든 영역을 다시 복구하기 위해 팽창 연산을 적용하면 반대로 어두운 영역이 줄어들고 밝은 영역이 늘어납니다.
이로 인해 스펙클(speckle)이 사라지면서 발생한 객체의 크기 감소를 원래대로 복구
"""

# 닫힘(Closing)
"""
팽창 연산자와 침식 연산자의 조합, 열림과 반대로 팽창 연산을 적용한 다음, 침식 연산을 적용
닫힘 연산-팽창 연산으로 인해 어두운 영역이 줄어들고 밝은 영역이 늘어납니다.
늘어난 영역을 다시 복구하기 위해 침식 연산을 적용하면 밝은 영역이 줄어들고 어두운 영역이 늘어납니다.
그로 인해 객체 내부의 홀(holes)이 사라지면서 발생한 크기 증가를 원래대로 복구
"""

# 그레이디언트(Gradient)
"""
팽창 연산자와 침식 연산자의 조합
열림 연산이나 닫힘 연산과 달리 입력 이미지에 각각 팽창 연산과 침식 연산을 적용하고 감산을 진행
입력 이미지와 비교했을 때 팽창 연산은 밝은 영역이 더 크며, 반대로 침식 연산은 밝은 영역이 더 작습니다.
각각의 결과를 감산한다면 입력 이미지에 객체의 가장자리가 반환
그레이디언트는 밝은 영역의 가장자리를 분리하며 그레이스케일 이미지가 가장 급격하게 변하는 곳에서 가장 높은 결과를 반환
"""

# 탑햇(TopHat)
"""
입력 이미지(src)와 열림(Opening)의 조합
그레이디언트 연산과 비슷하게 입력 이미지에 열림 연산을 적용한 이미지를 감산
열림 연산이 적용된 이미지는 스펙클이 사라지고 객체의 크기가 보존된 결과
이 결과를 입력 이미지에서 감산한다면 밝은 영역이 분리되어 사라졌던 스펙클이나 작은 부분들이 표시
즉, 입력 이미지의 객체들이 제외되고 국소적으로 밝았던 부분들이 분리
 탑햇 연산은 열림 연산에서 사라질 요소들을 표시
"""

# 블랙햇(BlackHat)
"""
입력 이미지(src)와 닫힘(Closing)의 조합
탑햇 연산과 비슷하게 닫힘 연산을 적용한 이미지에 입력 이미지를 감산
닫힘 연산이 적용된 이미지는 객체 내부의 홀이 사라지고 객체의 크기가 보존된 결과
이 결과에 입력 이미지를 감산한다면 어두운 영역이 채워져 사라졌던 홀 등이 표시
즉, 입력 이미지의 객체들이 제외되고 국소적으로 어두웠던 홀들이 분리
Tip : 블랙햇 연산은 닫힘 연산에서 사라질 요소들을 표시
"""

# 히트미스(HitMiss)
"""
히트미스 연산-단일 채널 이미지에서 활용, 주로 이진화 이미지에 적용
히트미스 연산-이미지의 전경이나 배경 픽셀의 특정 패턴을 찾는 데 사용하는 이진 형태학으로서 구조 요소의 형태에 큰 영향을 받습니다.
히트미스 연산의 커널-기존 컨벌루션 커널과 다른 역할
내부 요소의 값은 0 또는 1의 값만 의미가 있습니다.
커널 내부의 0은 해당 픽셀을 고려하지 않는다는 의미, 1은 해당 요소를 유지하겠다는 의미
이 특성 덕분에 히트미스 연산을 모서리(Corner)를 검출하는 데 활용
"""

import numpy as np
import cv2

src = cv2.imread("D:\Python\Image/office.jpg")
# src = cv2.resize(a, dsize=(600,400))

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9,9))

# 생성된 구조 요소(kernel)를 활용해 모폴로지 변환을 적용
# 모폴로지 함수(cv2.morphologyEx)로 모폴로지 연산을 진행
dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel, iterations=9)
"""
cv2.morphologyEx(원본 배열, 연산 방법, 구조 요소, 고정점, 반복 횟수, 테두리 외삽법, 테두리 색상)로 모폴로지 연산을 진행
연산 방법에 따라, 모폴로지 연산 결과가 달라집니다. 예제의 연산 방법은 열림 연산
연산 방법에는 기존 팽창 함수(cv2.dilate)와 침식 함수(cv2.erode)도 포함
"""

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()