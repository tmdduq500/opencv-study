import numpy as np
import cv2

src = cv2.imread("D:\Python\Image/pencils1.jpg")
src = cv2.resize(src,dsize=(300,200))

number = np.ones_like(src) * 127

"""
최댓값(max), 최솟값(min), 절댓값 차이(absdiff), 비교(compare) 등으로 연산이 가능
최댓값 함수는 두 이미지의 요소별 최댓값을 계산 / 최솟값 함수는 두 이미지의 요소별 최솟값을 계산
최댓값 함수,최솟값 함수-정밀도에 따라 요소의 최댓값과 최솟값이 있으며, 최댓값을 넘어가거나 최솟값보다 낮아질 수 없습니다.
절댓값 차이 함수-두 이미지의 요소별 절댓값 차이를 계산
덧셈 함수,뺄셈 함수-두 배열의 요소를 서로 뺄셈했을 때 음수가 발생하면 0을 반환, 절댓값 차이 함수는 이 값을 절댓값으로 변경해서 양수 형태로 반환
비교 함수-요소별 두 이미지의 요소별 비교 연산을 수행
비교 결과-True-요소의 값을 255로 변경 / False-요소의 값을 0으로 변경
"""
_max = cv2.max(src, number)
_min = cv2.min(src, number)
_abs = cv2.absdiff(src, number)
compare = cv2.compare(src, number, cv2.CMP_GT)

src = np.concatenate((src, src, src, src), axis = 1)
number = np.concatenate((number, number, number, number), axis = 1)
dst = np.concatenate((_max, _min, _abs, compare), axis = 1)

dst = np.concatenate((src, number, dst), axis = 0)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()