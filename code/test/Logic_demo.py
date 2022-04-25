import matplotlib.pyplot as plt
import numpy
import math


def func(x0, u):
    try:
        x = (math.asin(u * x0 * (1 - x0)) * 7) % 1
        return x
    except Exception as e:
        print(x0, u)
        print(e)
        exit(-1)


def main():
    x_list = []
    u_list = []
    x0 = 0.5
    times = 5000

    for u in range(0, 401):
        u = u / 100
        x = func(x0, u)
        for i in range(times):
            x = func(x, u)
            x_list.append(x)

        u = [u] * times
        u_list.extend(u)

    x = numpy.array(u_list)
    y = numpy.array(x_list)

    plt.scatter(x, y, s=0.01, alpha=0.4, label="Logistic")
    plt.ylim((0, 1.05))
    plt.xlim((1.0, 4.05))
    plt.show()


if __name__ == "__main__":
    main()
