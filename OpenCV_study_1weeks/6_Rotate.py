import cv2

#이미지 입력 함수(cv2.imread)를 통해 원본 이미지로 사용할 src를 선언하고 로컬 경로에서 이미지 파일을 읽어 옴
src = cv2.imread("D:\Python\Image/ara.jpg", cv2.IMREAD_COLOR)

#height, width, channel = src.shape를 이용하여 해당 이미지의 높이, 너비, 채널의 값을 저장
#높이와 너비를 이용하여 회전 중심점을 설정
height, width, channel = src.shape

#2×3 회전 행렬 생성 함수(cv2.getRotationMatrix2D)
"""
matrix = cv2.getRotationMatrix2D(center, angle, scale)는 중심점(center), 각도(angle), 비율(scale)로 매핑 변환 행렬(matrix)을 생성
중심점(center)은 튜플(Tuple) 형태로 사용하며 회전의 기준점을 설정합니다.
각도(angle)는 중심점을 기준으로 회전할 각도를 설정
비율(scale)은 이미지의 확대 및 축소 비율을 설정
"""
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

#아핀 변환 함수(cv2.warpAffine)로 회전 변환을 계산
"""
dst = cv2.warpAffine(src, M, dsize)는 원본 이미지(src)에 M(아핀 맵 행렬)을 적용하고 출력 이미지 크기(dsize)로 변형해서 출력 이미지(dst)를 반환
아핀 맵 행렬(M)은 회전 행렬 생성 함수에서 반환된 매핑 변환 행렬을 사용
출력 이미지 크기(dsize)는 튜플(Tuple) 형태로 사용하며 출력 이미지의 너비와 높이를 의미
아핀 맵 행렬에 따라 회전된 이미지를 반환
"""
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()