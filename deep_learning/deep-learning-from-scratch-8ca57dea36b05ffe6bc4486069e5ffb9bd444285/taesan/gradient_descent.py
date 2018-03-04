import numpy as np
from function_2 import function_2
from numerical_gradient import numerical_gradient

def gradient_descent(f, init_x, lr, step_num):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x

init_x = np.array([-3.0, 4.0])
step_num = 100
lr = 0.1
print(gradient_descent(function_2, init_x, lr, step_num))
