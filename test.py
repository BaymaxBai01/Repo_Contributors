import numpy as np
from math import sqrt
from collections import Counter

# 在sklearn中，对于数据的拟合,创建模型，是放在fit方法中

class Knn:
    def __init__(self, n_neighbor=3):
        self.X_train = None
        self.y_train = None
        self.n_neighbor = n_neighbor

    def fit(self, X_train, y_train):
        #  给定x_train和y_train，得到训练模型
        assert X_train.shape[0] == len(y_train)
        self.X_train = X_train
        self.y_train = y_train
        return self

    def predict(self, X):
        # 对于给定的待预测数据，返回预测结果
        assert self.X_train is not None
        assert self.y_train is not None
        assert self.X_train.shape[1] == X.shape[0]
        # distance = []  # 保存和其他所有点的距离
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        # 给定一个样本，求出一个结果
        distance = [sqrt(np.sum((x_train - x) ** 2)) for x_train in self.X_train]
        nearest = np.argsort(distance)
        nearest = [i for i in nearest[:self.n_neighbor]]
        top_K = [i for i in self.y_train[nearest]]
        votes = Counter(top_K)
        y_predict = votes.most_common(1)[0][0]
        return y_predict

    def __repr__(self):
        return "KnnClassifier(n_neighbor=3)"