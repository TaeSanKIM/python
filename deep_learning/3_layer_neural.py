import numpy as np
import sigmoid_function as sg

x = np.array([1.0, 0.5])
w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])
a1 = np.dot(x, w1) + b1
print(a1)
z1 = sg.sigmoid(a1)
print(z1)

w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.4, 0.6]])
b2 = np.array([0.1, 0.2])
a2 = np.dot(z1, w2)
z2 = sg.sigmoid(a2)
print(z2)
