import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \
load_mnist(normalize=True, one_hot_label=True)

train_size = x_train.shape[0]
batch_size = 10
batch_mark = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mark]
t_batch = t_train[batch_mark]
print(x_batch)
print(t_batch)

batch_size = 2
t = np.array([0, 6])
y = np.array([[0.1, 0, 0.6, 0, 0.1, 0.1, 0, 0.2, 0], [0.1, 0, 0, 0, 0.1, 0, 0.8, 0, 0]])
print(y[np.arange(batch_size), t])
