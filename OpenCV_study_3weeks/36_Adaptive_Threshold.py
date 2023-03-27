# 적응형 이진화 알고리즘-입력 이미지에 따라 임곗값이 스스로 다른 값을 할당할 수 있도록 구성된 이진화 알고리즘

import cv2

src = cv2.imread("D:\Python\Image/tree.jpg")
src = cv2.resize(src,dsize=(600,400))
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)


# 적응형 이진화 함수(cv2.adaptiveThreshold)로 그레이스케일 이미지를 이진화를 적용
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)
# cv2.adaptiveThreshold(입력 이미지, 최댓값, 적응형 이진화 플래그, 임곗값 형식, 블록 크기, 감산값)을 의미
"""
입력 이미지-8비트의 단일 채널 이미지를 사용
최댓값, 임곗값 형식-기존 이진화 함수와 동일한 역할
적응형 이진화 플래그-블록 크기 내의 연산 방법을 의미
"""
"""
플래그-두 종류 / 연산 방법-세 가지
평균 가중치, 가우시안 가중치, 혼합(평균 가중치와 가우시안 가중치를 OR 연산해 사용)
"""
# 그냥 이진화 함수 사용
# ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# cv2.imshow("dst", dst)

cv2.imshow("binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()



