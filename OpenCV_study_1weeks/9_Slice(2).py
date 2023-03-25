"""
dst 이미지를 생성할 때, dst = src.copy()가 아닌 dst = src로 적용한다면 깊은 복사가 적용되지 않음

얕은 복사로 이미지를 복사할 경우, dst 이미지와 src 이미지는 동일한 결과로 반환
"""

import cv2

src = cv2.imread("D:\Python\Image/apple.jpg", cv2.IMREAD_COLOR)

"""
roi 이미지를 생성하여 src[높이(행), 너비(열)]로 관심 영역을 설정

이후, dst[높이(행), 너비(열)] = roi를 이용하여 dst 이미지에 해당 영역을 붙여넣을 수 있음

잘라낸 이미지와 붙여넣을 이미지의 크기가 다르다면 이미지를 붙여넣을 수 없음


"""
dst = src.copy() 
roi = src[100:500, 200:600]
dst[0:400, 0:400] = roi

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()