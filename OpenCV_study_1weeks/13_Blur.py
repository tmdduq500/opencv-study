#흐림 효과(Blur)는 블러링(Blurring) 또는 스무딩(Smoothing)이라 불리며, 노이즈를 줄이거나 외부 영향을 최소화하는 데 사용 
#단순히 이미지를 흐리게 만드는 것뿐만 아니라 노이즈를 제거해서 연산 시 계산을 빠르고 정확하게 수행하는 데 도움

import cv2

src = cv2.imread("D:\Python\Image/apple.jpg", cv2.IMREAD_REDUCED_COLOR_4)

#단순 흐림 효과 함수(cv2.blur)
"""
단순 흐림 효과는 각 픽셀에 대해 커널을 적용해 모든 픽셀의 단순 평균을 구하는 연산

dst = cv2.blur(src, ksize, anchor, borderType)는 
입력 이미지(src)를 커널 크기(ksize), 고정점(anchor), 테두리 외삽법(borderType)으로 흐림 효과를 적용한 결과 이미지(dst)를 반환
"""

#커널(kernel)은 이미지에서 (x, y)의 픽셀과 해당 픽셀 주변을 포함한 작은 크기의 공간

#고정점(Anchor Point)은 커널을 통해 컨벌루션된 값을 할당한 지점
#컨벌루션(Convolution)이란 새로운 픽셀을 만들어 내기 위해 커널 크기의 화소 값을 이용해 어떤 시스템을 통과해 계산하는 것을 의미

#테두리 외삽법(Border Extrapolation)은 컨벌루션을 적용할 때, 이미지 가장자리 부분의 처리 방식
dst1 = cv2.blur(src, (3, 3), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
dst2 = cv2.blur(src, (9,9 ), (-1, -1), borderType=cv2.BORDER_DEFAULT)
dst3 = cv2.blur(src,(15,15), (-1,-1), borderType=cv2.BORDER_DEFAULT)

#cv2.imshow("src",src)
cv2.imshow("dst", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

