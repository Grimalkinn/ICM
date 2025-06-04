# plotX2X3sub.py
"""The tight_layout() function in pyplot module of 
                            matplotlib library is used to automatically 
                            adjust subplot parameters to give specified padding."""
import numpy as np
import matplotlib.pyplot as plt

def plotSubPlots(x, y2, y3):
    plt.figure()
    plt.subplot(2, 2, 1)
    plt.plot(x, y2, 'r-', x, y3, 'b-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['x^2', 'x^3'], loc='lower right')
    plt.title('Top Plot')

    plt.subplot(2, 2, 2)
    plt.plot(x, y2, 'm--', x, y3, 'c+')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['x^2', 'x^3'], loc='best')
    plt.title('Bottom Plot')
    plt.subplot(2, 2, 3)
    plt.plot(x, y2, 'm--', x, y3, 'c+')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['x^2', 'x^3'], loc='best')
    plt.title('Bottom Plot')
    plt.subplot(2, 2, 4)
    plt.plot(x, y2, 'm--', x, y3, 'c+')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['x^2', 'x^3'], loc='best')
    plt.title('Bottom Plot')
    plt.tight_layout()  
    plt.savefig('PlotX2X3.png') # png file
    plt.show()      # display the plot

x = np.arange(-5., 5.1, .1)
y2 = x**2
y3 = x**3
plotSubPlots(x, y2, y3)
