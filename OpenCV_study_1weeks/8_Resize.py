#이미지를 확대하는 경우에는 픽셀에 대한 보간법
#이미지를 축소하는 경우에는 픽셀에 대한 병합법이 수행

#이미지 피라미드는 2배로 확대하거나 축소하는 경우만 가능하므로, 원하는 크기로 변환하기 위해서 이미지 크기 조절 함수를 사용

"""
첫 번째 방법은 이미지의 크기를 사용자가 요구하는 절대 크기로 변경하는 방법. 즉, 임의의 크기(640×480이나 123×456 등의 이미지 크기)로 변환
두 번째 방법은 이미지의 크기를 비율에 맞게 상대 크기로 변경하는 방법. 이 경우, 입력 이미지의 크기와 비례하도록 너비와 높이가 계산
"""

import cv2

src = cv2.imread("D:\Python\Image/champagne.jpg", cv2.IMREAD_COLOR)

#이미지 크기 조절 함수(cv2.resize)
"""
dst = cv2.resize(src, dstSize, fx, fy, interpolation)는
입력 이미지(src), 절대 크기(dstSize), 상대 크기(fx, fy), 보간법(interpolation)으로 출력 이미지(dst)을 생성

절대 크기는 튜플(Tuple) 형식으로 (너비, 높이)의 값을 할당해 사용
"""

#상대 크기는 절대 크기에 (0, 0)을 할당한 다음, 상대 크기의 값을 할당해 사용
#절대 크기에 (0, 0)을 할당하는 이유로는 fx와 fy에서 계산된 크기가 dsize에 할당

dst = cv2.resize(src, dsize=(480, 480), interpolation=cv2.INTER_AREA)


#보간법은 이미지의 크기를 변경하는 경우, 변형된 이미지의 픽셀은 추정해서 값을 할당해야 합니다.
#이미지의 비율을 변경하면 존재하지 않는 영역에 새로운 픽셀값을 매핑하거나 존재하는 픽셀들을 압축해서 새로운 값을 할당
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()