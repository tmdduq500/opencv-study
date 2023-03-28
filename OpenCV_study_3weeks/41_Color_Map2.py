# 순람표는 Numpy를 활용해 다음과 같이 생성
import cv2
import numpy as np

userColor_8UC1 = np.linspace(0, 255, num=256, endpoint=True, retstep=False, dtype=np.uint8).reshape(256, 1)
userColor_8UC3 = np.linspace(0, 255, num=256 * 3, endpoint=True, retstep=False, dtype=np.uint8).reshape(256, 1, 3)


src = cv2.imread("D:\Python\Image/beach.jpg")
src = cv2.resize(src,dsize=(860,576))

#색상 맵 플래그 사용
dst = cv2.applyColorMap(src, cv2.COLORMAP_PINK)

# 사용자 정의 색상 맵(userColor)적용
# dst = cv2.applyColorMap(src, userColor_8UC3)


cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()






