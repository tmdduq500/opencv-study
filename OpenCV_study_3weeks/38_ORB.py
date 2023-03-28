# ORB(Oriented FAST and rotated BRIEF) 알고리즘=FAST(Features from Accelerated Segment Test) 알고리즘, BRIEF(Binary Robust Independent Elementary Features) 알고리즘, 해리스 코너 알고리즘을 결합한 알고리즘

# FAST(Features from Accelerated Segment Test) 알고리즘
"""
로스텐(Rosten)과 드리먼드(Drummond)가 제안한 피처 검출기 알고리즘
픽셀 P와 픽셀 주변의 작은 원 위에 있는 픽셀의 집합을 비교하는 방식
픽셀 P의 주변 픽셀에 임곗값을 적용해 어두운 픽셀, 밝은 픽셀, 유사한 픽셀로 분류해 원 위의 픽셀이 연속적으로 어둡거나 밝아야 하며 이 연속성이 절반 이상이 돼야 합니다.
이 조건을 만족하는 경우 해당 픽셀은 우수한 특징점으로 볼 수 있다
"""

# BRIEF 알고리즘
"""
칼론더(Calonder) 연구진이 개발해 칼론더 피처라고도 불립니다
특징점(Key Point)을 검출하는 알고리즘이 아닌 검출된 특징점에 대한 기술자(Descriptor)를 생성하는 데 사용
[기술자(Descriptor)-서로 다른 이미지에서 특징점(Key Point)이 어떤 연관성을 가졌는지 구분하게 하는 역할]
특징점 주변 영역의 픽셀을 다른 픽셀과 비교해 어느 부분이 더 밝은지를 찾아 이진 형식으로 저장
가우시안 커널을 사용해 이미지를 컨벌루션 처리, 피처 중심 주변의 가우스 분포를 통해 첫 번째 지점과 두 번째 지점을 계산해 모든 픽셀을 한 쌍으로 생성
즉, 두 개의 픽셀을 하나의 그룹으로 묶는 방식
"""

# ORB 알고리즘
"""
FAST 알고리즘을 사용해 특징점을 검출
FAST 알고리즘은 코너뿐만 아니라 가장자리에도 반응하는 문제점-해리스 코너 검출 알고리즘을 적용해 최상위 특징점만 추출
이 과정에서 이미지 피라미드를 구성해 스케일 공간 검색을 수행
이후 스케일 크기에 따라 피처 주변 박스 안의 강도 분포에 대해 X축과 Y축을 기준, 1차 모멘트를 계산
1차 모멘트는 그레이디언트의 방향을 제공-피처의 방향을 지정할 수 있다.
방향이 지정되면 해당 방향에 대해 피처 벡터를 계산할 수 있으며, 피처는 회전 불변성을 갖고 있으며 방향 정보를 포함
하나의 ORB 피처를 가져와 피처 주변의 박스에서 1차 모멘트와 방위 벡터를 계산
피처의 중심에서 모멘트가 가리키는 위치까지 벡터를 피처 방향으로 부여. ORB의 기술자는 BRIEF 기술자에 없는 방향 정보를 갖고 있습니다.
ORB 알고리즘은 SIFT(Scale-Invariant Feature Trasnform) 알고리즘과 SURF(Speeded-Up Robust Features) 알고리즘 을 대체하기 위해 OpenCV Labs에서 개발.속도 또한 더 빨라졌다.
"""

import cv2
import numpy as np

# ORB 알고리즘-그레이스케일 이미지를 사용
src = cv2.imread("D:\Python\Image/apple_books.jpg")
#src = cv2.resize(src,dsize=(960,635))
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

target = cv2.imread("D:\Python\Image/apple.jpg", cv2.IMREAD_GRAYSCALE)
#target = cv2.resize(target, dsize=(376,362))

#ORB 클래스(cv2.ORB_create)로 ORB 객체를 생성
# cv2.ORB_create(최대 피처 수, 스케일 계수, 피라미드 레벨, 엣지 임곗값, 시작 피라미드 레벨, 비교점, 점수 방식, 패치 크기, FAST 임곗값)
orb = cv2.ORB_create(
    nfeatures=40000,
    scaleFactor=1.2,
    nlevels=8,
    edgeThreshold=31,
    firstLevel=0,
    WTA_K=2,
    scoreType=cv2.ORB_HARRIS_SCORE,
    patchSize=31,
    fastThreshold=20,
)
"""
최대 피처 수-ORB 객체가 한 번에 검출하고자 하는 특징점의 개수

스케일 계수-이미지 피라미드를 설정.(인수를 2로 지정할 경우, 이미지 크기가 절반이 되는 고전적인 이미지 피라미드를 의미)
    스케일 계수를 너무 크게 지정-특징점의 매칭 확률을 떨어뜨립니다. 반대로 스케일 계수를 적게 지정-더 많은 피라미드 레벨을 구성해야 하므로 연산 속도가 느려집니다.
피라미드 레벨-이미지 피라미드의 레벨 수를 나타냅니다.
엣지 임곗값-이미지 테두리에서 발생하는 특징점을 무시하기 위한 경계의 크기
시작 피라미드 레벨-원본 이미지를 넣을 피라미드의 레벨을 의미
비교점-BRIEF 기술자가 구성하는 비교 비트
    이 매개변수에는 2(1비트), 3(2비트), 4(2비트)의 값만 지정해 비교할 수 있습니다.
    (2를 지정할 경우 이진 형식(0, 1)을 사용하며, 3의 값을 사용할 경우 3자 간 비교 결과로 (0, 1, 2)를 사용한다. 4의 값을 사용할 경우 4자 간 비교 결과로 (0, 1, 2, 3)을 사용)
점수 방식-피처의 순위를 매기는 데 사용, 해리스 코너(cv2.ORB_HARRIS_SCORE) 방식과 FAST(cv2.ORB_FAST_SCORE) 방식을 사용
패치 크기-방향성을 갖는 BFIEF 기술자가 사용하는 개별 피처의 패치 크기
    엣지 임곗값 매개변수와 상호작용,패치 크기의 값을 변경한다면 엣지 임곗값이 패치 크기의 값보다 커야 합니다.
FAST 임곗값-FAST 검출기에서 사용되는 임곗값을 의미
"""

# 특징점 및 기술자 계산 메서드(orb.detectAndCompute)로 특징점 및 기술자를 계산
# 특징점, 기술자 = orb.detectAndCompute(입력 이미지, 마스크)을 의미
"""
특징점-좌표(pt), 지름(size), 각도(angle), 응답(response), 옥타브(octave), 클래스 ID(class_id)를 포함
좌표-특징점의 위치를 알려주며, 지름은 특징점의 주변 영역을 의미
각도-특징점의 방향(-1일 경우 방향이 없음)
응답-피처가 존재할 확률로 해석, 옥타브는 특징점을 추출한 피라미드의 스케일을 의미
클래스 ID-특징점에 대한 저장공간을 생성할 때 객체를 구분하기 위한 클러스터링한 객체 ID를 
기술자-각 특징점을 설명하기 위한 2차원 배열로 표현. 이 배열은 두 특징점이 같은지 판단할 때 사용
"""
kp1, des1 = orb.detectAndCompute(gray, None)
kp2, des2 = orb.detectAndCompute(target, None)

# 전수 조사 매칭(Brute force matching)을 활용해 객체를 인식하거나 추적
# cv2.BFMatcher=(거리 측정법, 교차 검사)을 의미
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
"""
거리 측정법-질의 기술자(Query Descriptors)와 훈련 기술자(Train Descriptors)를 비교할 때 사용되는 거리 계산 측정법을 지정.
    질의(Query)와 훈련(Train)이라는 용어로 인해 마치 추론 모델을 만드는 것처럼 착각할 수 있습니다.
        훈련-객체로 인식된 이미지를 탐지할 수 있도록 사전(Dictionary)이라는 공간에 포함하는 과정
        질의-객체를 탐지할 이미지를 뜻, 훈련은 질의 공간에서 검출할 요소를 의미
교차 검사-훈련된 집합에서 질의 집합이 가장 가까운 이웃이며, 질의 집합에서 훈련된 집합이 가장 가까운 이웃이면 서로 매칭
"""

# 매치 함수(orb.match)로 최적의 매칭을 검출
# bf.detectAndCompute(기술자1, 기술자2)을 의미
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
"""
질의 기술자(queryDescriptors) / 훈련 기술자(trainDescriptors)를 사용해 최적의 매칭을 찾습니다.
기술자 공간에서 작동하는 마스크(mask)의 행-질의 기술자의 행과 대응 / 열-내부 사전 이미지(훈련 기술자)와 대응
반환값으로 DMatch(Dictionary Match) 객체를 반환, 4개의 멤버를 갖고 있습니다.

DMatch 객체-질의 색인(queryIdx), 훈련 색인(trainIdx), 이미지 색인(imgIdx), 거리(distance)로 구성
    질의 색인 / 훈련 색인-두 이미지의 특징점에서 서로 매칭하기 위해 식별되는 색인 값을 의미
    이미지 색인-이미지와 사전 사이에서 매칭된 경우 훈련에 사용된 이미지를 구별하는 색인값을 의미
    거리-각 특징점 간 유클리드 거리 또는 매칭의 품질을 의미. 거리 값이 낮을수록 매칭이 정확
    그러므로, 정렬 함수(sorted)로 거리 값이 낮은 순으로 정렬
"""
# 반복문을 통해, 우수한 상위 100개에 대해서만 표시
for i in matches[:100]:
    idx = i.queryIdx
    x1, y1 = kp1[idx].pt
    cv2.circle(src, (int(x1), int(y1)), 3, (255, 0, 0), 3)

cv2.imshow("src", src)
cv2.waitKey()