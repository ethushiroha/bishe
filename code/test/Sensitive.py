import matplotlib.pyplot as plt
import numpy as np


def OLACS(x):
    t = 26
    return (t * np.arcsin(4 * x * (1 - x))) % 1


def draw(times: int = 60):
    x0 = 0.4
    x1 = 0.40000001
    x0_list = []
    x1_list = []
    y0_list = []
    y1_list = []

    for i in range(times):
        x0_list.append(i)
        x1_list.append(i)
        y0_list.append(x0)
        y1_list.append(x1)
        x0 = OLACS(x0)
        x1 = OLACS(x1)
        # print(x0, x1)

    plt.plot(x0_list, y0_list, color='red', label="x0=0.4")
    plt.plot(x1_list, y1_list, color='blue', label="x0=0.40000001")
    plt.xlabel("times")
    plt.ylabel("x value")
    plt.title("Iterative curve")
    plt.legend()
    plt.show()


def main():
    draw()


if __name__ == '__main__':
    main()
