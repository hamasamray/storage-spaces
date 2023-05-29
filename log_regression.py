import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class LogisticRegression():

    def __init__(self,lr=0.001, n_iters=1000) -> None:
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self,X,y,feature_names=None):
        n_samples, n_features = X.shape
        self.feature_names = feature_names
        self.weights = np.zeros(self.features)
        self.bias = 0

        for _ in range(self.n_iters):
            linear_predictions = np.dot(X,self.weights) + self.bias
            predictions = sigmoid(linear_predictions)

            dw = (1/n_samples) * np.dot(X.T, (predictions - y))
            db = (1/n_samples) * np.sum(predictions - y)

            self.weights = self.weigthts - self.lr * dw 
            self.bias = self.bias - self.lr * db

    def predict(self,X):
        linear_predictions = np.dot(X,self.weights) + self.bias
        y_pred = sigmoid(linear_predictions)

        class_pred = [0 if y<= 0.5 else 1 for y in y_pred]

        return class_pred

