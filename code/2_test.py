import matplotlib.pyplot as plt
import numpy
import cv2

class key:
    p = 0.3
    x0 = 0.4
    q = 0.2
    y0 = 0.4
    r1 = 120
    r2 = 165
    r3 = 77
    r4 = 219

def ChaosMap0(x, p):
    y = x
    if 0 < y < p:
        print("func1\n")
        y = y / p
    elif p <= y < 0.5:
        print("func\n")
        y = (y - p) / (0.5 - p)
    elif 0.5 <= y < 1:
        print("func3\n")
        ChaosMap0(1 - y, p)
    return y

def ChaosMap(x0, p, times: int) -> list:
    y = x0
    x_list = []
    for i in range(times):     
        y = ChaosMap0(y, p)
        x_list.append(y)

    return x_list    
