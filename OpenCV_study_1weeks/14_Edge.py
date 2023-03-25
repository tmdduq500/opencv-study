import cv2

src = cv2.imread("D:\Python\Image/forest.jpg", cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3,)
sobel2 =cv2.Sobel(gray, cv2.CV_8U, 0, 1, 3,)
sobel_1 = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3,delta=128)
sobel2_1 =cv2.Sobel(gray, cv2.CV_8U, 0, 1, 3,delta=128)

# laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=1)
# laplacian2 = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)
# laplacian3 = cv2.Laplacian(gray, cv2.CV_8U, ksize=15)



# canny = cv2.Canny(src, 0, 100)
# canny2 = cv2.Canny(src, 150, 255)
# canny3 = cv2.Canny(src, 0, 255)

cv2.imshow("sobel", sobel)
cv2.imshow("sobel2", sobel2)
cv2.imshow("sobel_1", sobel_1)
cv2.imshow("sobel2_1", sobel2_1)

# cv2.imshow("laplacian", laplacian)
# cv2.imshow("laplacian2", laplacian2)
# cv2.imshow("laplacian3", laplacian3)


# cv2.imshow("canny", canny)
# cv2.imshow("canny2", canny2)
# cv2.imshow("canny3", canny3)

cv2.waitKey()
cv2.destroyAllWindows()


