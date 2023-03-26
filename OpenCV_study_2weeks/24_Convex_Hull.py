# 윤곽선(points, contours)의 경계면을 둘러싸는 다각형을 구하는 알고리즘
# 반환되는 결과는 윤곽선 검출 결과와 동일한 형식
# 스크랜스키(Sklansky) 알고리즘을 이용해 입력된 좌표들의 볼록한 외곽을 찾습니다

# 스크랜스키(Sklansky) 알고리즘
"""
경계 사각형의 정점(Vertex)을 검출
경계면을 둘러싸는 다각형은 경계 사각형 내부에 포함, 해당 정점을 볼록점으로 사용
영역 내부에도 다양한 윤곽점들이 존재,여기서 볼록 껍질을 이루는 볼록점들을 선별해서 선택
"""

import cv2

src = cv2.imread("D:\Python\Image/convex.jpg")
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in contours:

    # cv2.convexHull()를 활용해 윤곽선에서 블록 껍질을 검출
    hull = cv2.convexHull(i, clockwise=True)    # cv2.convexHull(윤곽선, 방향)을 의미
    """
    윤곽선은 윤곽선 검출 함수에서 반환되는 구조를 사용
    방향은 검출된 볼록 껍질의 볼록점들의 인덱스 순서를 의미
    
    윤곽선 구조-윤곽선 검출 함수의 반환값과 형태가 동일하면, 임의의 배열에서도 검출이 가능
    방향이 True-시계 방향, False-반시계 방향으로 정렬
    """
    # 블록 껍질 함수는 단일 형태에서만 검출이 가능
    # 그러므로, 반복문을 활용, 단일 형태의 윤곽선 구조에서 블록 껍질을 검출  
    cv2.drawContours(dst, [hull], 0, (0, 0, 255), 2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()