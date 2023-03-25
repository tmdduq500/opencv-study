import cv2

#이미지 입력 함수(cv2.imread)를 통해 원본 이미지로 사용할 src를 선언하고 로컬 경로에서 이미지 파일을 읽어 옴
src = cv2.imread("D:\Python\Image/glass.jpg", cv2.IMREAD_COLOR)

#대칭 함수(cv2.flip)로 이미지를 대칭
#dst = cv2.flip(src, flipCode)는 원본 이미지(src)에 대칭 축(flipCode)을 기준으로 대칭한 출력 이미지(dst)를 반환

"""
flipCode < 0은 XY 축 대칭(상하좌우 대칭)을 적용
flipCode = 0은 X 축 대칭(상하 대칭)을 적용
flipCode > 0은 Y 축 대칭(좌우 대칭)을 적용
"""
dst = cv2.flip(src, 0)

#이미지 표시 함수(cv2.imshow)와 키 입력 대기 함수(cv2.waitkey)로 윈도우 창에 이미지를 띄울 수 있음
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()