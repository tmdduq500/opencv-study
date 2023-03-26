# 영상이나 이미지에서 코너를 검출하는 알고리즘
# 코너-트래킹(Tracking) 하기 좋은 지점(특징)
# 꼭짓점은 트래킹하기 좋은 지점

import cv2

src = cv2.imread("D:\Python\Image/coffee.jpg")
src=cv2.resize(src, dsize=(800,600))
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

# cv2.goodFeaturesToTrack()를 활용해 윤곽선들의 이미지에서 코너를 검출
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03)
"""
cv2.goodFeaturesToTrack(입력 이미지, 코너 최댓값, 코너 품질, 최소 거리, 마스크, 블록 크기, 해리스 코너 검출기 유/무, 해리스 코너 계수)을 의미

입력 이미지-8비트 또는 32비트의 단일 채널 이미지를 사용
코너 최댓값-검출할 최대 코너의 수를 제한합니다. 코너 최댓값보다 낮은 개수만 반환
코너 품질-반환할 코너의 최소 품질을 설정합니다. 코너 품질은 0.0 ~ 1.0 사이의 값으로 할당, 일반적으로 0.01 ~ 0.10 사이의 값을 사용
최소 거리-검출된 코너들의 최소 근접 거리, 설정된 최소 거리 이상의 값만 검출
마스크-입력 이미지와 같은 차원을 사용하며, 마스크 요솟값이 0인 곳은 코너로 계산하지 않음
블록 크기-코너를 계산할 때, 고려하는 코너 주변 영역의 크기를 의미
해리스 코너 검출기 유/무-해리스 코너 검출 방법 사용 여부를 설정
해리스 코너 계수-해리스 알고리즘을 사용할 때 할당하며 해리스 대각합의 감도 계수를 의미
"""
for i in corners:
    x,y=i[0]
    cv2.circle(dst, (int(x),int(y)), 3, (0, 0, 255), 2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()