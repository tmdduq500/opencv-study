import cv2
src = cv2.imread("D:\Python\Image/hamburger.jpg", cv2.IMREAD_REDUCED_COLOR_2)

b, g, r = cv2.split(src)

# b = src[:, :, 0]
# g = src[:, :, 1]  #numpy 형식 채널 분리
# r = src[:, :, 2]
 
inverse = cv2.merge((r, g, b)) 

cv2.imshow("b(numpy)", b)
cv2.imshow("g(numpy)", g)
cv2.imshow("r(numpy)", r)
cv2.imshow("inverse(numpy)", inverse)
cv2.waitKey()
cv2.destroyAllWindows()
