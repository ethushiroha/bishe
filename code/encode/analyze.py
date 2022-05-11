import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr


def plot(x_line: list, y_line: list):
    plt.bar(x_line, y_line)
    plt.show()


class Img_statistics:
    def __init__(self, name):
        self.img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)

    def __counts_pixel(self):
        pixel_list = [0 for i in range(256)]
        for row in self.img:
            for col in row:
                pixel_list[col] += 1
        return pixel_list

    # == hist
    def draw(self):
        x_list = [i for i in range(256)]
        y_list = self.__counts_pixel()
        img: np.ndarray = self.img
        img = img.reshape((1, self.img.shape[0] * self.img.shape[1]))
        plt.hist(img[0], bins=255)
        plt.xlabel("pixel")
        plt.ylabel("frequency")
        print(1)
        plt.show()
        # plot(x_list, y_list)

    def draw2(self):
        x_list = [i for i in range(256)]
        y_list = self.__counts_pixel()
        plot(x_list, y_list)


class Img_Cov:
    def __init__(self, name1: str, name2: str):
        self.img1 = cv2.imread(name1, cv2.IMREAD_GRAYSCALE)
        self.img2 = cv2.imread(name2, cv2.IMREAD_GRAYSCALE)

    def __calc(self):
        hist1 = cv2.calcHist([self.img1], [0], None, [256], [0.0, 255.0])
        hist2 = cv2.calcHist([self.img2], [0], None, [256], [0.0, 255.0])


class Corr:
    def __init__(self, name: str):
        self.img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)

    def get_next(self, height, width, reverse=False):
        x_line = []
        y_line = []
        img = self.img
        if reverse:
            img = img.T
        for i in range(height):
            for j in range(width):
                if j == width - 1:
                    continue
                x_line.append(img[i][j])
                y_line.append(img[i][j + 1])
        return x_line, y_line

    def get_horizontal(self):
        width, height = self.img.shape
        return self.get_next(height, width, reverse=False)

    def get_vertical(self):
        width, height = self.img.shape
        return self.get_next(height, width, reverse=True)

    def draw(self):
        x_line, y_line = self.get_vertical()
        print(calc_r(x_line, y_line))
        print()
        print(pearsonr(x_line, y_line))
        plt.xlabel("raw pixel")
        plt.ylabel("adjacent pixels")
        plt.scatter(x_line, y_line, s=1)
        plt.show()


def calc_r(x_list: list, y_list: list):
    EX = np.mean(x_list)
    EY = np.mean(y_list)
    length = len(x_list)
    sum = 0
    for i in range(length):
        sum += (x_list[i] - EX) * (y_list[i] - EY)
    cov = sum / length

    DX = np.var(x_list)
    DY = np.var(y_list)
    return cov / (np.sqrt(DX) * np.sqrt(DY))


def main():
    # img_name = "/Users/admin/Documents/bishe/code/encode/img.png"
    img_name = "/Users/admin/Documents/bishe/code/encode/encrypted.png"
    # img = Img_statistics("/Users/admin/Documents/bishe/code/encode/img2.png")
    # img.draw()
    img = Corr(img_name)
    img.draw()
    # img = Img_statistics(img_name)
    # img.draw()


def test():
    img1 = cv2.imread("/Users/admin/Documents/bishe/code/encode/encrypted.png", cv2.IMREAD_GRAYSCALE)
    hist1 = cv2.calcHist([img1], [0], None, [255], [0.0, 255.0])
    x_line = [i for i in range(255)]
    plot(x_line, hist1)


if __name__ == '__main__':
    main()
    # test()
