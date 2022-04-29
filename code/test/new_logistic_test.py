import math

import matplotlib.pyplot as plt


# 分布均匀，密钥空间

def func(u, t, x):
    return (math.asin(u * (1 - x) * x) * t) % 1


def main():
    x0 = 0.5
    u = 4
    # t = 7
    times = 10000
    for t in range(1, 10):
        x = func(u, t, x0)
        ans_list = [0 for i in range(10)]
        x_list = [i for i in range(10)]
        for i in range(times):
            x = func(u, t, x)
            ans_list[int(x * 10)] += 1

        plt.plot(x_list, ans_list, 'o-', label='t={}'.format(str(t)))
        # min_ans = min(ans_list)
        # max_ans = max(ans_list)
        # if min_ans < 850:
        #     print(min_ans, t)
        # if max_ans > 1150:
        #     print(max_ans, t)
    plt.xlabel("x")
    plt.ylabel("k(x)")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
