import struct

import numpy as np


def OLACS(x):
    return (107 * np.arcsin(4 * x * (1 - x))) % 1


def main():
    f = open("a.bin", "wb+")
    x0 = 0.5
    x = OLACS(x0)
    result_list = []
    # for i in range(1000000):
    #     x = OLACS(x)
    for i in range(1000000):
        x = OLACS(x)
        result_list.append(x)

    result_list = np.array(result_list)
    mean = np.mean(result_list)
    i = 0
    tmp = 0
    count = 0
    for i in range(len(result_list)):
        tmp = tmp * 2 + (result_list[i] >= mean)
        if i % 8 == 0:
            count += 1
            tmp = struct.pack("B", tmp)
            f.write(tmp)
            tmp = 0

    print(count)
    f.close()


if __name__ == '__main__':
    main()
    print("fin")
