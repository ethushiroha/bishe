import math

import matplotlib.pyplot as plt
import numpy as np


def plot(x_line: list, y_line: list):
    plt.plot(x_line, y_line)
    plt.show()


class Logistic_lyapunov:

    def __init__(self, u):
        self.u = u

    def __calc_logistic_lyapunov(self, x):
        return math.log(abs(self.u * (1 - 2 * x)))

    def __calc_logistic(self, x):
        return self.u * x * (1 - x)

    def __calc(self, x0, n: int):
        sum = 0
        x = self.__calc_logistic(x0)
        for i in range(n):
            x = self.__calc_logistic(x)
            sum += self.__calc_logistic(x)
        return sum / n

    @staticmethod
    def draw(x0, n: 2000):
        x_line = []
        y_line = []
        for u in np.arange(0, 4, 0.001):
            logistic = Logistic_lyapunov(u)
            y_line.append(logistic.__calc(x0, n))
            x_line.append(u)

        plot(x_line, y_line)


def main():
    Logistic_lyapunov.draw(0.5, 2000)


if __name__ == '__main__':
    main()
