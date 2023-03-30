# K-최근접 이웃 알고리즘(K-Nearest Neighbor Algorithm, KNN)
# 지도 학습에 사용할 수 있는 가장 간단한 분류 알고리즘 중 하나, 회귀 분석, 분류에서 사용
# 새로운 데이터가 입력되었을 때 기존의 데이터와 가장 가까운 k개 데이터의 정보로 새로운 데이터를 예측하는 방법
# 새로운 데이터 주변에 분포해 있는 이웃 데이터의 성질을 토대로 판단

# K-최근접 이웃 알고리즘-새로운 데이터가 입력되었을 때 가장 가까운 K개를 비교하여 가장 거리가 가까운 개수가 많은 클래스로 분류

import cv2
import numpy as np


# Fashion-MNIST은 기존의 MNIST 데이터 세트를 대신해 사용할 수 있게 제공되는 패션 데이터 세트
def loadTrainData(image_path, label_path):
    with open(image_path, "rb") as image_data:
        images = np.frombuffer(image_data.read(), dtype=np.uint8, offset=16)
    with open(label_path, "rb") as label_data:
        labels = np.frombuffer(label_data.read(), dtype=np.uint8, offset=8)
    return images.reshape(-1, 784), labels


train_x, train_y = loadTrainData(
    "./OpenCV_study_3weeks/fashion-mnist/train-images-idx3-ubyte",
    "./OpenCV_study_3weeks/fashion-mnist/train-labels-idx1-ubyte"
)
test_x, test_y = loadTrainData(
    "./OpenCV_study_3weeks/fashion-mnist/t10k-images-idx3-ubyte",
    "./OpenCV_study_3weeks/fashion-mnist/t10k-labels-idx1-ubyte"
)



label_dict = {
    0: "T-shirt/top",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle boot",
}

# K-최근접 이웃 알고리즘 클래스(cv2.ml.KNearest_create)로 knn 인스턴스를 생성
knn = cv2.ml.KNearest_create()

# K-최근접 이웃 알고리즘 훈련 메서드(knn.train)로 훈련을 진행
retval = knn.train(train_x.astype(np.float32), cv2.ml.ROW_SAMPLE, train_y.astype(np.int32))
# retval = knn.train(samples, layout, responses)-훈련 데이터(samples)에서 어떠한 배치 형태(layout)로 구성되어 있는지 확인해 라벨(responses)과 매핑
"""
훈련 데이터(samples)-CV_32F(float) 형식을 사용하며, 라벨(responses)은 CV_32F(flaot) 형식 또는 CV_32S(int) 형식을 사용합니다.
배치 형태(layout)-두 가지의 플래그만 존재합니다
    훈련 데이터의 데이터가 행(ROW_SAMPLE) / 열(COL_SAMPLE)로 구성되어 있는지 설정
반환되는 결과(retval)-학습이 정상적으로 진행되었으면 참 값을 반환하고, 학습에 실패했다면 거짓 값을 반환
"""

# K-최근접 이웃 알고리즘 이웃 예측 메서드(knn.findNearest)로 훈련 모델에 대한 예측(predict)을 진행
count = 500
retval, results, neighborResponses, dist = knn.findNearest(
    test_x[:count].astype(np.float32), k=7
)
# retval, results, neighborResponses, dist = knn.findNearest(samples, k)는 테스트 데이터(samples)에 대해 최근접 이웃 개수(k)에 대한 예측값을 반환

"""
반환값(retval)-첫 번째 테스트 데이터에 대한 예측 결과를 반환하며, 결괏값(results)은 테스트 데이터에 대한 모든 예측 결과를 반환

결괏값(results)-(N, 1)의 크기를 가지며 (CV_32F) 형식으로 반환

이웃 응답값(neighborResponses)과 거리(dist)-예측 결과를 분석하기 위해 사용된 최근접 이웃의 클래스 정보와 거리(L2-Norm)를 반환
    이웃 응답값(neighborResponses)과 거리(dist)-(N, k) 크기를 가지며 CV_32F 형식으로 반환
테스트 데이터-간략하게 500개만 사용해 평가
    데이터 타입의 기본값을 np.uint8로 사용했으므로 예측 메서드의 테스트 데이터 형식 을 np.float32로 변경
    예측이 완료된 후 비교 연산을 진행할 때, test_y를 전치 행렬로 변경해야하므로, test_y에 [:, None] 구문을 추가
[:, None] 구문-배열에 열 벡터를 생성해 test_y를 전치 행렬로 변경할 수 있다.
"""

matches = results.astype(np.uint8) == test_y[:count][:, None]
print(np.count_nonzero(matches) / count * 100)

for idx, result in enumerate(results):
    print("Index : {}".format(idx))
    print("예측값 : {}".format(label_dict[int(result)]))
    print("실제값 : {}".format(label_dict[test_y[idx]]))
    cv2.imshow("images", test_x[idx].reshape(28, 28, 1))
    cv2.waitKey()