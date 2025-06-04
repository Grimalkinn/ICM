# plotX2Decorate.py
import numpy as np
import matplotlib.pyplot as plt

def plotCurve(x,y):
    plt.figure()
    plt.plot(x, y)  # create the plot
    plt.xlabel('x(t)')
    plt.ylabel('y(t)')
    plt.axis([-6., 6., -1, 30]) # rarely used
    plt.legend(['x^2'])  # legend is a list of strings
    plt.title('COMP1012:  f(x)=x^2')
    plt.savefig('PlotX2Dec.png') # png file
    plt.show()      # display the plot

x = np.arange(-5., 5.1, .1)
y = x**2
plotCurve(x,y)
