# 리매핑(Remapping)-입력 이미지에 기하학적인 변형을 적용하는 방법
# 이미지에 변환 행렬 연산을 적용하는 것이 아닌, 비선형 변환을 적용할 수 있습니다.
# 픽셀들의 좌표를 임의의 특정 좌표로 옮겨 이미지를 변경하는 작업을 의미

import cv2
import numpy as np

src = cv2.imread("buildings.jpg")
height, width = src.shape[:2]
map2, map1 = np.indices((height, width), dtype=np.float32)

map1 = map1 + width / 100 * np.sin(map1)
map2 = map2 + height / 100 * np.cos(map2)

dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC)
cv2.imshow("dst", dst)
cv2.waitKey()