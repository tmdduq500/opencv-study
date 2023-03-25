#OpenCV에서 이미지를 불러올 때는 확장자를 확인하는 방식이 아닌 파일 시그니처를 읽어 파일의 포맷을 분석
#파일 시그니처==파일 매직 넘버(File Magic Number)

import cv2

#이미지 입력 함수(cv2.imread)를 통해 로컬 경로의 이미지 파일을 읽어올 수 있음
#image = cv2.imread(fileName, flags)는 파일 경로(fileName)의 이미지 파일을 플래그(flags) 설정에 따라 불러옴

image = cv2.imread("D:\Python\Image/lunar.jpg", cv2.IMREAD_UNCHANGED)


#이미지 표시 함수(cv2.imshow),키 입력 대기 함수(cv2.waitkey)로 윈도우 창에 이미지를 띄울 수 있음

#height, width , channel = image.shape를 이용하여 해당 이미지의 높이, 너비, 채널의 값을 확인할 수 있습니다.
#이미지의 속성은 크기, 정밀도, 채널을 주요한 속성으로 사용

height, width,channel = image.shape
print(height, width , channel)  

cv2.imshow("Moon", image)
cv2.waitKey()
cv2.destroyAllWindows()