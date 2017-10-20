
import numpy as np
import matplotlib.pyplot as plt
 
def estimate_coef (x, y):
    n = np.size(x)
    mx, my = np.mean(x), np.mean(y)
    SSxy = np.sum(y*x - n*my*mx)
    SSxx = np.sum(x*x - n*mx*mx)
    b1 = SSxy / SSxx
    b0 = my - b1*mx
    return(b0, b1)
 
def plot_regression_line(x, y, b):

    plt.scatter(x, y, color = "m",marker = "s", s = 30)
    y_pred = b[0] + b[1]*x
    plt.plot(x, y_pred, color = "r")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
 
def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.empty((10))
    i = 0
    while(i<10):
        y[i] = input()
        i = i + 1
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    plot_regression_line(x, y, b)
 
if __name__ == "__main__":
    main()
"""
Spyder Editor

This is a temporary script file.
"""


