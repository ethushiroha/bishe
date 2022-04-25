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
        print("func2\n")
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


def Step1(M, N) -> set:
    tmp_times = key.r1 + key.r2
    times = M * N + tmp_times
    x_list = ChaosMap(key.x0, key.p, times)[tmp_times:]
    y_list = []
    # y_list = ChaosMap(key.y0, key.q, times)[tmp_times:]
    return x_list, y_list
    

def Pic2Arr():
    pic = cv2.imread("test.jfif", 0)
    print(f"pic.shape ==> {pic.shape}\n")
    return pic

def main():
    pic = Pic2Arr()
    M, N = pic.shape

    x_list, y_list = Step1(M, N)
    print(f"x_list ==> {x_list}\n")
    print(f"y_list ==> {y_list}\n")


if __name__ == "__main__":
    main()
