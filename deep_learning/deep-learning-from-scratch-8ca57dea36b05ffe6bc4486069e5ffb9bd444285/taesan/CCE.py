import numpy as np

def cross_entopy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    delta = 1e-7
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + delta)) / batch_size

def main():
    t = np.array([[0, 1, 0],[1, 0, 0]])
    y = np.array([[0.1, 0.05, 0.8], [0.9, 0.1, 0]])
    print(cross_entopy_error(y, t))
    print(y.shape)

if __name__ == "__main__":
    main()
