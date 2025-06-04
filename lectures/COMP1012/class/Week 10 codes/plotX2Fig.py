# plotX2Fig.py
import numpy as np
import matplotlib.pyplot as plt

def plotCurve(x, y):
    plt.figure()
    plt.plot(x, y)  # create the plot
    plt.savefig('PlotX2.eps') # postscript
    plt.savefig('PlotX2.png') # png file
    plt.show()      # display the plot

def main():
    xCoords = np.arange(-5., 5.1, .1)
    yCoords = xCoords**2
    plotCurve(xCoords, yCoords)

main()
