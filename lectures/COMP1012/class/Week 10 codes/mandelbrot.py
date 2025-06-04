import numpy as np
import matplotlib.pyplot as plt
from time import ctime


def mandelbrot(realPart, imagPart, imgSize, iterations, xOffset):
    img = np.zeros((imgSize,imgSize),int)
    deltaX = realPart / img.shape[1] * 2.
    deltaY = imagPart / img.shape[0] * 2.
    
    INFINITY = 16.0
    
    y = -imagPart
    # row number is along the y (imaginary) axis
    for row in range(img.shape[0]):
        x = -realPart - xOffset
        # column number is along the x (real) axis
        for column in range(img.shape[1]):
            # do the work
            a, b = x, y
            n = 0
            while n < iterations:
                aa, bb = a*a, b*b
                a, b = aa - bb + x, 2.0 * a * b + y
                if aa + bb > INFINITY:
                    break
                n += 1
            if n < iterations:
                img[row, column] = n
            x += deltaX
        y += deltaY
    drawMandelbrot(img)
def displayTerminationMessage():
    print('''
Programmed by Stew Dent.
Date: %s
End of Processing.''' % ctime())


def drawMandelbrot(img):
    # img - the 2-D array holding the image to 
    #       display
    plt.figure()
    plt.imshow(img, interpolation='nearest') 
    plt.title('Mandelbrot')
    plt.xlabel('Real Axis')
    plt.ylabel('Imaginary Axis')
    plt.tick_params(axis='both', which='both',bottom='off', top='off',labelbottom='off', labelleft='off')
    plt.savefig('mandelbrot.png')
    plt.show()

def main():    
    # realPart - real part of the intial complex number
    # imagPart - imaginary part of the initial complex number
    # imgSize - the size of the square grid for the image
    # iterations - the number of iterations before giving up
    imgSize = int(input("Enter the size of the grid: "))
    realPart = float(input('Enter the maximum real part:'))
    imagPart = float(input('Enter the maximum imaginary art: '))
    xOffset = float(input('Enter the x offet: '))
    iterations = int(input('Enter the number of iterations: '))
    mandelbrot(realPart, imagPart, imgSize, iterations,xOffset)
    displayTerminationMessage()

main()