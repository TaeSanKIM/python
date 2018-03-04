import numpy as np
from function_2 import function_2

def numerical_gradient_1d(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]

        x[idx] = float(tmp_val) + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad

def numerical_gradient(f, x):
    if x.ndim == 1:
        return numerical_gradient_1d(f, X)
    else:
        grad = np.zeros_like(x)

        for idx, X in enumerate(x):
            grad[idx] = numerical_gradient_1d(f, X)

        return grad
