# 윤곽선(컨투어)를 검출하는 주된 요소-하얀색의 객체를 검출
# 그러므로 배경은 검은색이며 검출하려는 물체는 하얀색의 성질을 띄게끔 변형
# 이진화 처리 후, 반전시켜 검출하려는 물체를 하얀색의 성질을 띄도록 변환

import cv2

src = cv2.imread("D:\Python\Image/contour.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)

# cv2.findContours()를 이용하여 이진화 이미지에서 윤곽선(컨투어)를 검색
contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
"""
cv2.findContours(이진화 이미지, 검색 방법, 근사화 방법)을 의미
반환값으로 윤곽선, 계층 구조를 반환
윤곽선은 Numpy 구조의 배열로 검출된 윤곽선의 지점들이 담겨있습니다.
계층 구조는 윤곽선의 계층 구조를 의미. 각 윤곽선에 해당하는 속성 정보들이 담겨있습니다.
"""

for i in range(len(contours)):
    # cv2.drawContours()을 이용하여 검출된 윤곽선을 그립니다.
    cv2.drawContours(src, [contours[i]], 0, (0, 0, 255), 2)
    """
    cv2.drawContours(이미지, [윤곽선], 윤곽선 인덱스, (B, G, R), 두께, 선형 타입)을 의미
    윤곽선은 검출된 윤곽선들이 저장된 Numpy 배열
    윤곽선 인덱스는 검출된 윤곽선 배열에서 몇 번째 인덱스의 윤곽선을 그릴지를 의미
    """
    
    cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    print(i, hierarchy[0][i])
    cv2.imshow("src", src)
    cv2.waitKey(0)

cv2.destroyAllWindows()