import matplotlib.pyplot as plt
import numpy
import numpy as np


def logistic(u, x):
    return u * x * (1 - x)


def draw_logistic():
    x_list = []
    u_list = []
    x0 = 0.5
    times = 2000

    for u in range(0, 401):
        u = u / 100
        x = logistic(u, x0)
        for i in range(times):
            x = logistic(u, x)
            x_list.append(x)

        u = [u] * times
        u_list.extend(u)

    x = numpy.array(u_list)
    y = numpy.array(x_list)

    plt.scatter(x, y, s=0.02, alpha=0.4, label="Logistic")
    plt.xlabel("u")
    plt.ylabel("x value")
    plt.title("logistic map")
    plt.ylim((0, 1.05))
    plt.xlim((0.0, 4.05))
    plt.show()


def sine(u, x):
    return u * np.sin(np.pi * x) / 4


def draw_sine():
    x_list = []
    u_list = []
    x0 = 0.5
    times = 2000

    for u in range(0, 401):
        u = u / 100
        x = sine(u, x0)
        for i in range(times):
            x = sine(u, x)
            x_list.append(x)

        u = [u] * times
        u_list.extend(u)

    x = numpy.array(u_list)
    y = numpy.array(x_list)

    plt.scatter(x, y, s=0.02, alpha=0.4, label="Sine map")
    plt.xlabel("u")
    plt.ylabel("x value")
    plt.title("sine map")
    plt.ylim((0, 1.05))
    plt.xlim((0.0, 4.05))
    plt.show()


def main():
    # draw_logistic()
    draw_sine()


if __name__ == "__main__":
    main()
