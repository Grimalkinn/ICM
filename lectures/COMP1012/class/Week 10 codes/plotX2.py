# plotX2.py
import matplotlib.pyplot as plt
import numpy as np

def plotCurve(xCoords,yCoords):
    plt.figure()  # create a figure to hold the plot
    plt.plot(xCoords, yCoords)  # create the plot
    plt.show()      # display the plot

def main():
    xCoords = np.arange(-5., 5.1, .1)
    yCoords = xCoords**2
    plotCurve(xCoords, yCoords)

main()
