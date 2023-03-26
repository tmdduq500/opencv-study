import numpy as np
import cv2

src = cv2.imread("D:\Python\Image/pencils1.jpg")
src = cv2.resize(src,dsize=(300,200))

# 동일한 크기의 matrix/vector를 생성하여 1로 초기화하여 반환하는 함수
# 회색 이미지(127, 127, 127)과 검은색 이미지(2, 2, 2)
number1 = np.ones_like(src) * 127
number2 = np.ones_like(src) * 2

# cv2.Calc(연산 이미지1, 연산 이미지2)를 이용하여 이미지 연산
"""
결괏값이 0보다 작다면, 0으로 반환, 결괏값이 255보다 크다면, 255로 반환
만약, 대수적 표현(+, - 등)을 통해 연산을 진행- 오버플로우(Overflow)나 언더플로우(Underflow)가 발생
(ex.0 - 2를 진행한다면 -1이 아닌, 255값)
이미지는 uint8로, 256개의 공간(0 ~ 255)을 갖고 있습니다.
"""

# 회색 이미지로만 연산
add = cv2.add(src, number1)
sub = cv2.subtract(src, number1)
mul = cv2.multiply(src, number1)
div = cv2.divide(src, number1)

# 검정색 이미지로만 연산
add2 = cv2.add(src, number2)
sub2 = cv2.subtract(src, number2)
mul2 = cv2.multiply(src, number2)
div2 = cv2.divide(src, number2)

# 연결 함수(np.concatenate)로 이미지들을 연결
src = np.concatenate((src, src, src, src), axis = 1)
# number = np.concatenate((number1, number1, number2, number2), axis = 1)
dst = np.concatenate((add, sub, mul, div), axis = 1)
dst2 = np.concatenate((add2,sub2,mul2,div2),axis=1)
dst = np.concatenate((src, dst, dst2), axis = 0)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()