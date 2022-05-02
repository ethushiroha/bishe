import matplotlib.pyplot as plt
import numpy as np


def OLACS(t, x):
    # return t * x * (1 - x)
    return (t * np.arcsin(4 * (1 - x) * x)) % 1


def main():
    x0 = 0.5
    times = 1000
    x_list = []
    y_list = []
    for t in np.arange(0, 4, 0.01):
        if t == 0:
            continue
        x = OLACS(t, x0)
        for i in range(times):
            x = OLACS(t, x)
            x_list.append(t)
            y_list.append(x)
    print(1)
    plt.scatter(x_list, y_list, s=0.01, alpha=0.4)
    plt.ylim((0, 1.05))
    plt.xlim((1.0, 4.05))
    plt.show()


if __name__ == '__main__':
    main()
