import matplotlib.pyplot as plt
import numpy as np


def plot(x_line: list, y_line: list):
    plt.plot(x_line, y_line)
    line_min = min(x_line)
    line_max = max(x_line)
    plt.hlines(line_min, line_max, 0.5, colors='r', linestyles="dashed")
    plt.show()


class Sine_lyapunov:
    def __init__(self, u):
        self.u = u

    def __calc_sine(self, x):
        return self.u * np.sin(np.pi * x) / 4

    def __calc_sine_lyapunov(self, x):
        return np.log(abs(np.pi * self.u * np.cos(np.pi * x) / 4))

    def __calc(self, x0, n: int):
        sum = 0
        x = self.__calc_sine(x0)
        for i in range(n):
            x = self.__calc_sine(x)
            sum += self.__calc_sine_lyapunov(x)
        return sum / n

    @staticmethod
    def draw(x0, n=2000):
        x_line = []
        y_line = []
        for u in np.arange(0, 4, 0.001):
            if u == 0:
                continue
            sine = Sine_lyapunov(u)
            y_line.append(sine.__calc(x0, n))
            x_line.append(u)

        plot(x_line, y_line)


class Logistic_lyapunov:
    def __init__(self, u):
        self.u = u

    def __calc_logistic_lyapunov(self, x):
        return np.log(abs(self.u * (1 - 2 * x)))

    def __calc_logistic(self, x):
        return self.u * x * (1 - x)

    def __calc(self, x0, n: int):
        sum = 0
        x = self.__calc_logistic(x0)
        for i in range(n):
            x = self.__calc_logistic(x)
            sum += self.__calc_logistic_lyapunov(x)
        return sum / n

    @staticmethod
    def draw(x0, n: 2000):
        x_line = []
        y_line = []
        for u in np.arange(0, 4, 0.001):
            if u == 0:
                continue
            logistic = Logistic_lyapunov(u)
            y_line.append(logistic.__calc(x0, n))
            x_line.append(u)

        plot(x_line, y_line)


class My_logistic_lyapunov:
    def __init__(self, t):
        self.t = t

    def __calc_my_logistic(self, x):
        return np.arcsin(4 * (1 - x) * x) * self.t % 1

    def __calc_my_logistic_lyapunov(self, x):
        tmp = (self.t * 4 * (1 - 2 * x)) / (np.sqrt(1 - 16 * x * x * (1 - x) * (1 - x)))
        return np.log(abs(tmp))

    def __calc(self, x0, n):
        sum = 0
        x = self.__calc_my_logistic(x0)
        for i in range(n):
            x = self.__calc_my_logistic(x)
            sum += self.__calc_my_logistic_lyapunov(x)
        return sum / n

    @staticmethod
    def draw(x0, n: 2000):
        x_line = []
        y_line = []
        for t in np.arange(0, 64):
            if t == 0:
                continue
            my_logistic = My_logistic_lyapunov(t)
            y_line.append(my_logistic.__calc(x0, n))
            x_line.append(t)

        plot(x_line, y_line)


def main():
    # Logistic_lyapunov.draw(0.5, 2000)
    Sine_lyapunov.draw(0.5, 2000)
    # My_logistic_lyapunov.draw(0.5, 2000)
    print(1)


if __name__ == '__main__':
    main()
