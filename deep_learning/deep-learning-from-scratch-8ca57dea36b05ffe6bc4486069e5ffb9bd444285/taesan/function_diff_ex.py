import numpy as np
import matplotlib.pylab as plt
from numerical_diff import numerical_diff as diff

def function_1(x):
    return 0.01*x**2 + 0.1*x
x = np.arange(0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()
print(diff(function_1, 5))
print(diff(function_1, 10))
