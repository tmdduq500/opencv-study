import numpy as np
import cv2

src = cv2.imread("D:\Python\Image/analysis.jpg")
# 크기 조절
src = cv2.resize(src,dsize=(300,200))
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 논리곱(bitwise_and), 논리합(bitwise_or), 배타적 논리합(bitwise_xor), 부정(bitwise_not) 등으로 연산

# 논리곱 함수-두 이미지의 요소별 논리곱을 계산
# 연산 이미지1과 연산 이미지2의 값을 비트 단위로 파악, 해당 비트에 대해 AND 연산을 진행
_and = cv2.bitwise_and(gray, binary)

# 논리합 함수-두 이미지의 요소별 논리합을 계산
# 연산 이미지1과 연산 이미지2의 값을 비트 단위로 파악, 해당 비트에 대해 OR 연산을 진행
_or = cv2.bitwise_or(gray, binary)

# 배타적 논리합 함수-두 이미지의 요소별 배타적 논리합을 계산
# 연산 이미지1과 연산 이미지2의 값을 비트 단위로 파악, 해당 비트에 대해 XOR 연산을 진행합니다.
_xor = cv2.bitwise_xor(gray, binary)

# 부정 함수-두 이미지의 요소별 논리합을 계산
# 연산 이미지1의 값을 비트 단위로 파악, 해당 비트에 대해 NOT 연산을 진행
_not = cv2.bitwise_not(gray)
_not2 = cv2.bitwise_not(binary)


src = np.concatenate((np.zeros_like(gray), gray, binary, _not2), axis = 1)
dst = np.concatenate((_and, _or, _xor, _not), axis = 1)
dst = np.concatenate((src, dst), axis = 0)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()