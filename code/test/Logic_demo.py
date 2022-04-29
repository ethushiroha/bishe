import math

import matplotlib.pyplot as plt
import numpy
import numpy as np


def func(x0, t):
    try:
        x = (math.asin(4 * x0 * (1 - x0)) * t) % 1
        return x
    except Exception as e:
        print(x0, t)
        print(e)
        exit(-1)


def main():
    x_list = []
    u_list = []
    x0 = 0.5
    times = 5000

    for t in np.arange(1, 20, 0.1):
        x = func(x0, t)
        for i in range(times):
            x = func(x, t)
            x_list.append(x)

        t = [t] * times
        u_list.extend(t)

    x = numpy.array(u_list)
    y = numpy.array(x_list)

    plt.scatter(x, y, s=0.01, alpha=0.4, label="Logistic")
    plt.ylim((0, 1.05))
    plt.xlim((1.0, 20.0))
    plt.show()


if __name__ == "__main__":
    main()
