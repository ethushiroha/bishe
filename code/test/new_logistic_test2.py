# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math

# 初值敏感性

u = 4
t = 13


def func(x):
    return (math.asin(u * x * (1 - x)) * t) % 1


def main():
    times = 10
    x1_0 = 0.5
    x2_0 = 0.5000001

    x1 = func(x1_0)
    x2 = func(x2_0)
    for i in range(times):
        x1 = func(x1)
        x2 = func(x2)
        if i % 1 == 0:
            print(x1, x2)


if __name__ == "__main__":
    main()
