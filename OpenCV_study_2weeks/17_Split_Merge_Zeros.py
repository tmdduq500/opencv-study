import cv2
import numpy as np

src = cv2.imread("D:\Python\Image/hamburger.jpg", cv2.IMREAD_REDUCED_COLOR_2)

b, g, r = cv2.split(src)

height, width, channel = src.shape

zero = np.zeros((height, width, 1), dtype=np.uint8)

bgz = cv2.merge((b, g, zero))
bzr = cv2.merge((b,zero,r))
zgr = cv2.merge((zero,g,r))

cv2.imshow("zero", zero)
cv2.imshow("zero(red)", bgz)
cv2.imshow("zero(green)", bzr)
cv2.imshow("zero(blue)", zgr)
cv2.waitKey()
cv2.destroyAllWindows()
