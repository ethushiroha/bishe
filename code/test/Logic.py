import matplotlib.pyplot as plt
import numpy


def main():
    x_list = []
    u_list = []
    x0 = 0.5
    times = 2000

    for u in range(0, 401):
        u = u / 100
        x = u * x0 * (1-x0)
        for i in range(times):
            x = u * x * (1 - x)
            x_list.append(x)
        
        u = [u] * times
        u_list.extend(u)
    
    x = numpy.array(u_list)
    y = numpy.array(x_list)

    plt.scatter(x, y, s=0.02, alpha=0.4, label="Logistic")
    plt.ylim((0, 1.05))
    plt.xlim((3.0, 4.05))
    plt.show()


if __name__ == "__main__":
    main()
