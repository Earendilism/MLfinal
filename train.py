import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def logistic_regression(x, w, b):
    z = np.dot(x, w) + b
    return sigmoid(z)

def loss(y, y_hat):
    return -np.sum(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))

def gradient(x, y, w, b):
    y_hat = logistic_regression(x, w, b)
    dw = np.dot(x.T, (y_hat - y))
    db = np.sum(y_hat - y)
    return dw, db

def train(x, y, w, b, learning_rate, epochs):
    for epoch in range(epochs):
        dw, db = gradient(x, y, w, b)
        w = w - learning_rate * dw
        b = b - learning_rate * db
    return w, b

def predict(x, w, b):
    y_hat = logistic_regression(x, w, b)
    y_hat = np.round(y_hat)
    return y_hat

if __name__ == "__main__":
    x = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 1])
    w = np.zeros(2)
    b = 0
    learning_rate = 0.01
    epochs = 100
    w, b = train(x, y, w, b, learning_rate, epochs)
    print("w:", w)
    print("b:", b)
    y_hat = predict(x, w, b)
    print("y_hat:", y_hat)
