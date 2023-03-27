# 템플릿 매칭-원본 이미지에서 템플릿 이미지와 일치하는 영역을 찾는 알고리즘
# 원본 이미지 위에 템플릿 이미지를 놓고 조금씩 이동하며 이미지 끝에 도달할 때 까지 비교해 찾음
# 템플릿 이미지와 동일하거나, 가장 유사한 영역을 원본 이미지에서 검출

import cv2

# 탬플릿 매칭은 그레이스케일 이미지를 사용, cv2.IMREAD_GRAYSCALE를 적용
src = cv2.imread("D:\Python\Image/poketmons.jpg", cv2.IMREAD_GRAYSCALE)
# src = cv2.resize(src,dsize=(800,600))
templit = cv2.imread("D:\Python\Image/poketmon.jpg", cv2.IMREAD_GRAYSCALE)
# templit = cv2.resize(templit, dsize=(300,200))
dst = cv2.imread("D:\Python\Image/poketmons.jpg")
# dst = cv2.resize(dst, dsize=(800,600))

# 템플릿 매칭 함수(cv2.matchTemplate)로 템플릿 매칭을 적용
result = cv2.matchTemplate(src, templit, cv2.TM_SQDIFF_NORMED)
# cv2.matchTemplate(원본 이미지, 템플릿 이미지, 템플릿 매칭 플래그)을 의미합니다.
"""
원본 이미지, 템플릿 이미지-8비트의 단일 채널 이미지를 사용
템플릿 매칭 플래그-템플릿 매칭에 사용할 연산 방법을 설정
"""
# 결괏값(dst)은 32비트의 단일 채널 이미지로 반환
"""
또한, 배열의 크기는 W - w + 1, H - h + 1의 크기
(W, H)는 원본 이미지의 크기, (w, h)는 템플릿 이미지의 크기
결괏값이 위와 같은 크기를 갖는 이유는 원본 이미지에서 템플릿 이미지를 일일히 비교하기 때문
"""

# 결괏값(dst)에서 가장 유사한 부분을 찾기 위해 최소/최대 위치 함수(cv2.minMaxLoc)로 검출값을 찾습니다.
"""
최소/최대 위치 함수-최소 포인터, 최대 포인터, 최소 지점, 최대 지점을 반환
검출 위치의 좌측 상단 모서리 좌표-최소 지점(minLoc)이나 최대 지점(maxLoc)에 위치
이미지 크기는 템플릿 이미지와 동일
"""
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
x, y = minLoc
h, w = templit.shape

dst = cv2.rectangle(dst, (x, y), (x +  w, y + h) , (0, 0, 255), 1)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


