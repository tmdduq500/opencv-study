#역상(Reverse Image)은 영상이나 이미지를 반전 된 색상으로 변환하기 위해서 사용

"""
픽셀 단위마다 비트 연산(Bitwise Operation)을 적용하는데, 그중 NOT 연산을 적용

NOT 연산은 각 자릿수의 값을 반대로 바꾸는 연산
"""

import cv2

src = cv2.imread("D:\Python\Image/whitebutterfly.jpg", cv2.IMREAD_COLOR)
#NOT 연산 함수(cv2.bitwise_not)로 이미지에 NOT 연산을 적용

"""
dst = cv2.bitwise_not(src, mask)는 입력 이미지(src), 마스크(mask)로 출력 이미지(dst)을 생성

마스크는 NOT 연산을 적용할 특정 영역을 의미합니다. 마스크 배열이 포함되어 있다면, 해당 영역만 반전 연산을 적용
"""
#Tip : not 연산 이외에도 and, or, xor 연산이 존재
dst = cv2.bitwise_not(src)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()