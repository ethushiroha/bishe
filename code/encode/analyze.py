import cv2
import matplotlib.pyplot as plt


def plot(x_line: list, y_line: list):
    plt.bar(x_line, y_line)
    plt.show()


class Img_statistics:
    def __init__(self, name):
        self.img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)

    def counts_pixel(self):
        pixel_list = [0 for i in range(256)]
        for row in self.img:
            for col in row:
                pixel_list[col] += 1
        return pixel_list

    def draw(self):
        x_list = [i for i in range(256)]
        y_list = self.counts_pixel()
        plot(x_list, y_list)


def main():
    img = Img_statistics("/Users/admin/Documents/bishe/code/encode/img.png")
    img.draw()


if __name__ == '__main__':
    main()
