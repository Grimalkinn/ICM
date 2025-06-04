# plotX2X3.py
import numpy as np
import matplotlib.pyplot as plt
def plotCurves(x,y2,y3,y4,y5):
    plt.figure()
    plt.plot(x, y2, 'r',linewidth=1)  # red solid line
    plt.plot(x, y3, 'b') # blue solid line
    plt.plot(x, y4, 'g') # blue solid line
    plt.plot(x, y5, 'y') # blue solid line


    plt.xlabel('time(s)')
    plt.ylabel('Voltage(v)')
    plt.legend(['x^2','x^3','x^4','x^5'], loc='best')
    plt.title('the plot of final exam')
    plt.savefig('PlotX2.png') # png file
    plt.figure()
    
    plt.show()      # display the plot
x = np.arange(-5., 5.1, .1)
y2 = x**2
y3 = x**3
y4=x**4
y5=x**5

plotCurves(x,y2,y3,y4,y5)

# plot x^4 and x^5 along with the above plot