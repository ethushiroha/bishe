import math
import operator

import cv2
import numpy as np


class MyLogistic:
    def __init__(self, x=0, t=0):
        self.x = x
        self.t = t

    def __calc__(self, x0):
        return (self.t * math.asin(4 * x0 * (1 - x0))) % 1

    def get_list(self, x, t, start, ends) -> list:
        result_list = []
        self.t = t
        for i in range(ends):
            x = self.__calc__(x)
            result_list.append(x)
        return result_list[start:]

    def get_list_by_range(self, x, t, start, ends, rang):
        result_list = self.get_list(x, t, start, ends)
        tmp_list = np.array(result_list) * rang
        result_list = np.array(tmp_list, dtype=int)
        return result_list


class Spread:

    @staticmethod
    def __spread__(src_list: list, spread_list: list) -> list:
        result_list = src_list
        for i in range(len(src_list)):
            for j in range(len(src_list[0])):
                left = 0
                top = 0
                if i != 0:
                    top = result_list[i - 1][j]
                if j != 0:
                    left = result_list[i][j - 1]
                result_list[i][j] = result_list[i][j] + top + left + spread_list[i][j]
        return result_list

    @staticmethod
    def spread(src_list: list, spread_list: list) -> list:
        return Spread.__spread__(src_list, spread_list)


class Displace:

    @staticmethod
    def __displace__(src_list: list, sort_list: list) -> list:
        sum_list = np.array(sort_list).sum(axis=1)
        result_list = []
        index_list = [i for i in range(len(sum_list))]
        sum_dict = dict(zip(index_list, sum_list))
        sorted_sum_dict = dict(sorted(sum_dict.items(), key=operator.itemgetter(1), reverse=True))
        keys = sorted_sum_dict.keys()
        for key in keys:
            result_list.append(src_list[key])
        return result_list

    @staticmethod
    def __displace_col__(src_list: list, sort_list: list) -> list:
        src_array = np.array(src_list).T.tolist()
        sort_array = np.array(sort_list).T.tolist()
        return np.array(Displace.__displace__(src_array, sort_array)).T.tolist()

    @staticmethod
    def __displace_row__(src_list: list, sort_list: list) -> list:
        return Displace.__displace__(src_list, sort_list)

    @staticmethod
    def displace(src_list: list, sort_list: list) -> list:
        result_list = Displace.__displace_row__(src_list, sort_list)
        return Displace.__displace_col__(result_list, sort_list)

    @staticmethod
    def __fix_row__(encrypt_list: list, sort_list: list) -> list:
        return Displace.__fix__(encrypt_list, sort_list)

    @staticmethod
    def __fix_col__(encrypt_list: list, sort_list: list) -> list:
        src_array = np.array(encrypt_list).T.tolist()
        sort_array = np.array(sort_list).T.tolist()
        return np.array(Displace.__fix__(src_array, sort_array)).T.tolist()

    @staticmethod
    def __fix__(encrypt_list: list, sort_list: list) -> list:
        sum_list = np.array(sort_list).sum(axis=1)
        result_list = [i for i in range(len(sum_list))]
        index_list = [i for i in range(len(sum_list))]
        sum_dict = dict(zip(index_list, sum_list))
        sorted_sum_dict = dict(sorted(sum_dict.items(), key=operator.itemgetter(1), reverse=True))
        keys = list(sorted_sum_dict.keys())
        for i in range(len(keys)):
            result_list[keys[i]] = encrypt_list[i]
        return result_list

    @staticmethod
    def fix(encrypt_list: list, sort_list: list) -> list:
        result_list = Displace.__fix_col__(encrypt_list, sort_list)
        return Displace.__fix_row__(result_list, sort_list)


class Xor:

    @staticmethod
    def xor(src_list: list, xor_list: list) -> list:
        src_array = np.array(src_list, dtype=int)
        xor_array = np.array(xor_list, dtype=int)
        return np.bitwise_xor(src_array, xor_array).tolist()


class Key:
    def __init__(self, x, t, r):
        self.x = x
        self.t = t
        self.r = r


class ImgCrypto:

    @staticmethod
    def generate(k1: Key, k2: Key, k3: Key, H, W):
        logistic = MyLogistic()
        start1 = k1.r
        ends1 = start1 + H * W
        # HW * 1
        sort_list = logistic.get_list(k1.x, k1.t, start1, ends1)
        sort_list = np.array(sort_list).reshape((W, H)).tolist()

        start2 = k2.r
        ends2 = start2 + H * W
        # W * H
        xor_list = logistic.get_list_by_range(k2.x, k2.t, start2, ends2, 255)
        xor_list = np.array(xor_list).reshape((W, H)).tolist()

        start3 = k3.r
        ends3 = start3 + H * W
        spread_list = logistic.get_list_by_range(k3.x, k3.t, start3, ends3, 255)
        spread_list = np.array(spread_list).reshape((W, H)).tolist()

        return sort_list, xor_list, spread_list

    @staticmethod
    def encrypt(src_list: list, sort_list: list, xor_list: list, spread_list: list) -> list:
        sorted_list = Displace.displace(src_list, sort_list)
        xored_list = Xor.xor(sorted_list, xor_list)
        return xored_list

    @staticmethod
    def decrypt(encrypt_list: list, sort_list: list, xor_list: list, spread_list: list) -> list:
        xored_list = Xor.xor(encrypt_list, xor_list)
        src_list = Displace.fix(xored_list, sort_list)
        return src_list

    @staticmethod
    def write(name: str, array: list):
        array = np.array(array)
        cv2.imwrite(name, array)


def main():
    k1 = Key(0.5, 13, 1000)
    k2 = Key(0.4, 26, 2000)
    k3 = Key(0.45, 31, 3000)
    img = cv2.imread("img.png", cv2.IMREAD_GRAYSCALE)
    width, height = img.shape

    sort_list, xor_list, spread_list = ImgCrypto.generate(k1, k2, k3, height, width)

    src_list = img.tolist()
    encryted_list = ImgCrypto.encrypt(src_list, sort_list, xor_list, spread_list)
    ImgCrypto.write("img2.png", encryted_list)

    decrypt_list = ImgCrypto.decrypt(encryted_list, sort_list, xor_list, spread_list)
    ImgCrypto.write("img3.png", decrypt_list)


def test():
    src_list = [[80, 63, 76], [29, 15, 153], [243, 128, 64]]
    sorted_list = [[43, 67, 98], [64, 47, 167], [247, 24, 16]]
    result = Displace.displace(src_list, sorted_list)
    print(result)
    print(Displace.fix(result, sorted_list))


if __name__ == '__main__':
    main()
    # test()
