#Montcarlo2

from numpy.random import uniform
import numpy as np

def montePyramid(length, width, height, points):
    # xCoords - correspond to the length of the pyramid
    # yCoords - correspond to the width of the pyramid
    # zCoords - correspond to the height of the pyramid
    xCoords = uniform(0., length, points)
    yCoords = uniform(0., width, points)
    zCoords = uniform(0., height, points)
    factor = (height - zCoords) / height
    # np.all works like and for arrays
    """The numpy.all() function returns True when all the
    elements of ndarray passed to the first parameter are True and returns False otherwise."""
    xInPyramid = np.all([0 <= xCoords, xCoords <= length *
                 factor], axis = 0)
    yInPyramid = np.all([0 <= yCoords, yCoords <= width *
	             factor], axis = 0)
    inPyramid = np.all([xInPyramid, yInPyramid], axis=0)
    probability = np.sum(inPyramid) / points
    volume = probability * length * width * height
    return print(probability, volume)


montePyramid(8,3,5,300)