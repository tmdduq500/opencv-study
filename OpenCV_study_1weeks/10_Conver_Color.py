#색상 공간 변환(Convert Color)은 본래의 색상 공간에서 다른 색상 공간으로 변환할 때 사용
#색상 공간 변환 함수는 데이터 타입을 같게 유지하고 채널을 변환

"""
채널의 수가 감소하게 되어 이미지 내부의 데이터는 설정한 색상 공간과 일치하는 값으로 변환되며, 데이터 값이 변경되거나 채널 순서가 변경될 수 있음
"""

import cv2

#색상 공간 변환 함수(cv2.cvtcolor)

"""
dst = cv2.cvtcolor(src, code, dstCn)는 입력 이미지(src), 색상 변환 코드(code), 출력 채널(dstCn)으로 출력 이미지(dst)을 생성

색상 변환 코드는 원본 이미지 색상 공간2결과 이미지 색상 공간을 의미

원본 이미지 색상 공간은 원본 이미지와 일치

출력 채널은 출력 이미지에 필요한 채널의 수를 설정
"""

#Tip : BGR은 RGB 색상 채널을 의미합니다. (Byte 역순)
#Tip : 출력 채널은 기본값을 사용하여 자동으로 채널의 수를 결정
src = cv2.imread("D:\Python\Image/crow.jpg", cv2.IMREAD_COLOR)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()