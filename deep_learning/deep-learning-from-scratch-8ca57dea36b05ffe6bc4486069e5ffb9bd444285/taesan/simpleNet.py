import numpy as np
import sys, os
sys.path.append(os.pardir)
from numerical_gradient import numerical_gradient
from MSE import mean_squared_error as mse
from common.functions import softmax
from common.functions import cross_entropy_error as cce

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cce(y, t)

        return loss

net = simpleNet()
print(net.W)
x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)
np.argmax(p)
t = np.array([0, 0, 1])
print(net.loss(x, t))

def f(W):
    return net.loss(x, t)

dW = numerical_gradient(f, net.W)
print(dW)
