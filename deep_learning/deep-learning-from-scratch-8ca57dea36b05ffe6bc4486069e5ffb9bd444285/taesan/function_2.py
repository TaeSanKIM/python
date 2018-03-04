from numerical_diff import numerical_diff as diff
import numpy as np

def function_2(x):
    return np.sum(x**2)

def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

print(diff(function_tmp1, 3.0))
print(diff(function_tmp2, 4.0))
