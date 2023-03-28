# 색상 맵(Color Map)-입력 이미지에 순람표(Lookup table) 구조로 이루어진 데이터를 적용
# 주로 데이터를 시각화하기 위해 사용, 색상의 분포표로 데이터를 쉽게 확인할 수 있다
# 픽셀값이 1:1로 매칭- 선형 구조나 비선형 구조로도 데이터를 매핑해 표현할 수 있다

import cv2

src = cv2.imread("D:\Python\Image/beach.jpg")
src = cv2.resize(src,dsize=(860,576))

# 색상 맵 적용 함수(cv2.applyColorMap)를 활용-원본 이미지에 특정 색상 맵 배열이 적용된 이미지를 생성
dst = cv2.applyColorMap(src, cv2.COLORMAP_OCEAN)
# dst = cv2.applyColorMap(src, colormap)
# 입력 이미지(src)에 색상 맵(colormap)을 적용한 결과 이미지(dst)를 반환
# 색상 맵 적용 함수-색상 맵 플래그가 아닌, 사용자 정의 색상 맵(userColor)을 활용해 이미지를 적용
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

