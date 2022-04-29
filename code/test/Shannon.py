import matplotlib.pyplot as plt
import numpy as np


class Logistic:
    def __init__(self, u):
        self.u = u

    def __calc_logistic(self, x):
        # return self.u * np.sin(np.pi * x) / 4
        return self.u * x * (1 - x)
        # return (self.u * np.arcsin(4 * x * (1 - x))) % 1

    def __calc_Shannon(self, y_list: list, times: int):
        result = 0
        for value in y_list:
            Px = value / times
            result += Px * np.log2(Px)
        return -1 * result

    def calc_Shannon(self, times):
        y_list = []
        x0 = 0.5
        x_values = []
        x = self.__calc_logistic(x0)
        for i in range(times):
            x = self.__calc_logistic(x)
            c = int(x * 1000) / 1000.0
            if c in x_values:
                index = x_values.index(c)
                y_list[index] += 1
            else:
                y_list.append(1)
                x_values.append(c)

        return self.__calc_Shannon(y_list, times)

    @staticmethod
    def draw(times=2000):
        x_list = []
        y_list = []
        for u in np.arange(0, 4, 0.01):
            if u == 0:
                continue
            logistic = Logistic(u)
            shannon = logistic.calc_Shannon(times)
            x_list.append(u)
            y_list.append(shannon)
        return x_list, y_list


class Sine:
    def __init__(self, u):
        self.u = u

    def __calc_logistic(self, x):
        return self.u * np.sin(np.pi * x) / 4
        # return self.u * x * (1 - x)
        # return (self.u * np.arcsin(4 * x * (1 - x))) % 1

    def __calc_Shannon(self, y_list: list, times: int):
        result = 0
        for value in y_list:
            Px = value / times
            result += Px * np.log2(Px)
        return -1 * result

    def calc_Shannon(self, times):
        y_list = []
        x0 = 0.5
        x_values = []
        x = self.__calc_logistic(x0)
        for i in range(times):
            x = self.__calc_logistic(x)
            c = int(x * 1000) / 1000.0
            if c in x_values:
                index = x_values.index(c)
                y_list[index] += 1
            else:
                y_list.append(1)
                x_values.append(c)

        return self.__calc_Shannon(y_list, times)

    @staticmethod
    def draw(times=2000):
        x_list = []
        y_list = []
        for u in np.arange(0, 4, 0.01):
            if u == 0:
                continue
            logistic = Sine(u)
            shannon = logistic.calc_Shannon(times)
            x_list.append(u)
            y_list.append(shannon)
        return x_list, y_list


class OLACS:
    def __init__(self, u):
        self.u = u

    def __calc_logistic(self, x):
        # return self.u * np.sin(np.pi * x) / 4
        # return self.u * x * (1 - x)
        return (self.u * np.arcsin(4 * x * (1 - x))) % 1

    def __calc_Shannon(self, y_list: list, times: int):
        result = 0
        for value in y_list:
            Px = value / times
            result += Px * np.log2(Px)
        return -1 * result

    def calc_Shannon(self, times):
        y_list = []
        x0 = 0.5
        x_values = []
        x = self.__calc_logistic(x0)
        for i in range(times):
            x = self.__calc_logistic(x)
            c = int(x * 1000) / 1000.0
            if c in x_values:
                index = x_values.index(c)
                y_list[index] += 1
            else:
                y_list.append(1)
                x_values.append(c)

        return self.__calc_Shannon(y_list, times)

    @staticmethod
    def draw(times=2000):
        x_list = []
        y_list = []
        for u in np.arange(0, 10, 0.1):
            if u == 0:
                continue
            logistic = OLACS(u)
            shannon = logistic.calc_Shannon(times)
            x_list.append(u)
            y_list.append(shannon)
        return x_list, y_list


def main():
    plt.title("Shannon")
    x_list, y_list = Logistic.draw()
    plt.plot(x_list, y_list, color='red', label='logistic')
    print(1)
    x_list, y_list = Sine.draw()
    plt.plot(x_list, y_list, color='blue', label='Sine')
    print(2)
    x_list, y_list = OLACS.draw()
    plt.plot(x_list, y_list, color='green', label="OLACS")
    print(3)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
