#plz use the provided csv file
#or remove the top text
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
    with open('wine.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        year = np.empty((27))
        price = np.empty((27))
        wrain = np.empty((27))
        agst = np.empty((27))
        hrain = np.empty((27))
        age = np.empty((27))
        fpop = np.empty((27))
        i=0
        for row in readCSV:
            y = row[0]
            p = row[1]
            w = row[2]
            a = row[3]
            h = row[4]
            g = row[5]
            f = row[6]

            year[i]=y
            price[i]=p
            wrain[i]=w
            agst[i]=a
            hrain[i]=h
            age[i]=g
            fpop[i]=f
            i= i+1
    
    b = estimate_coef(year,price)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    plot_regression_line(year,price, b)
    
    b = estimate_coef(wrain,price)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    plot_regression_line(wrain,price, b)
    
    b = estimate_coef(agst,price)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    plot_regression_line(agst,price, b)
    
    b = estimate_coef(hrain,price)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    plot_regression_line(hrain,price, b)
    
    b = estimate_coef(age,price)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    plot_regression_line(age,price, b)
    
    b = estimate_coef(fpop,price)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    plot_regression_line(fpop,price, b)
    
    
 
if __name__ == "__main__":
    main()
"""
Spyder Editor

This is a temporary script file.
"""


