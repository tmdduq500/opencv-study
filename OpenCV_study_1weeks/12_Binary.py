#이진화(Binary)는 어느 지점을 기준으로 값이 높거나 낮은 픽셀의 값을 대상으로 특정 연산을 수행할 때 사용

import cv2

src = cv2.imread("D:\Python\Image/geese.jpg", cv2.IMREAD_COLOR)


gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

#이진화 함수(cv2.threshold)로 그레이스케일 이미지에 이진화를 적용
"""
retval, dst = cv2.threshold(src, thresh, maxval, type)는 
입력 이미지(src)를 임곗값 형식(type)에 따라 임곗값(thresh)과 최댓값(maxval)을 활용하여 설정 임곗값(retval)과 결과 이미지(dst)를 반환

입력 이미지는 단일 채널 이미지(그레이스케일)을 입력해 사용

임곗값 형식은 임곗값을 초과한 값은 최댓값으로 변경, 임곗값 이하의 값은 0으로 바꾸는 등의 연산 적용

설정 임곗값은 일반적으로 임곗값과 동일, 임곗값을 대신 계산해주는 알고리즘인 Otsu나 Triangle를 사용하면, 임곗값을 알 수 있음
"""
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()