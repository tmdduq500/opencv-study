# K-최근접 이웃 알고리즘(K-Nearest Neighbor Algorithm, KNN)
# 지도 학습에 사용할 수 있는 가장 간단한 분류 알고리즘 중 하나, 회귀 분석, 분류에서 사용
# 새로운 데이터가 입력되었을 때 기존의 데이터와 가장 가까운 k개 데이터의 정보로 새로운 데이터를 예측하는 방법
# 새로운 데이터 주변에 분포해 있는 이웃 데이터의 성질을 토대로 판단

# K-최근접 이웃 알고리즘-새로운 데이터가 입력되었을 때 가장 가까운 K개를 비교하여 가장 거리가 가까운 개수가 많은 클래스로 분류

import cv2
import numpy as np



def loadTrainData(image_path, label_path):
    with open(image_path, "rb") as image_data:
        images = np.frombuffer(image_data.read(), dtype=np.uint8, offset=16)
    with open(label_path, "rb") as label_data:
        labels = np.frombuffer(label_data.read(), dtype=np.uint8, offset=8)
    return images.reshape(-1, 784), labels


train_x, train_y = loadTrainData(
    "./fashion-mnist/train-images-idx3-ubyte",
    "./fashion-mnist/train-labels-idx1-ubyte"
)
test_x, test_y = loadTrainData(
    "./fashion-mnist/t10k-images-idx3-ubyte",
    "./fashion-mnist/t10k-labels-idx1-ubyte"
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

knn = cv2.ml.KNearest_create()
retval = knn.train(train_x.astype(np.float32), cv2.ml.ROW_SAMPLE, train_y.astype(np.int32))

count = 500
retval, results, neighborResponses, dist = knn.findNearest(
    test_x[:count].astype(np.float32), k=7
)

matches = results.astype(np.uint8) == test_y[:count][:, None]
print(np.count_nonzero(matches) / count * 100)

for idx, result in enumerate(results):
    print("Index : {}".format(idx))
    print("예측값 : {}".format(label_dict[int(result)]))
    print("실제값 : {}".format(label_dict[test_y[idx]]))
    cv2.imshow("images", test_x[idx].reshape(28, 28, 1))
    cv2.waitKey()