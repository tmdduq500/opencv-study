#이미지 확대와 축소는 이미지 피라미드(Image pyramid)를 활용해 이미지의 크기를 원하는 단계까지 샘플링하는 작업
"""
원본 이미지에서 크기를 확대하는 것을 업 샘플링이라 하며 하위 단계의 이미지를 생성

원본 이미지에서 크기를 축소하는 것을 다운 샘플링이라 하며, 상위 단계의 이미지를 생성 
"""
#이미지 피라미드 종류 2개
#가우시안 피라미드(Gaussian Pyramid)
#라플라시안 피라미드(Laplacian pyramid)
import cv2

src = cv2.imread("D:\Python\Image/fruits.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

#이미지 확대 함수(cv2.pyrUp)
"""
dst = cv2.pyrUp(src, dstSize, borderType)는 입력 이미지(src), 출력 이미지 크기(dstSize), 테두리 외삽법(borderType)으로 출력 이미지(dst)을 생성
출력 이미지 크기(dstSize)는 매우 세밀한 크기 조정을 필요로 할때 사용
테두리 외삽법(borderType)은 이미지를 확대하거나 축소할 경우, 이미지 영역 밖의 픽셀은 추정해 값을 할당
"""
dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)
#이미지 축소 함수(cv2.pyrUp), 이미지 확대 함수(cv2.pyrUp과 이하 동일)
dst2 = cv2.pyrDown(src)

"""
이미지 확대 함수는 BORDER_DEFAULT의 픽셀 외삽법만 사용 가능
이미지 축소 함수는 BORDER_CONSTANT의 픽셀 외삽법을 제외한 나머지 플래그만 사용
"""

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()