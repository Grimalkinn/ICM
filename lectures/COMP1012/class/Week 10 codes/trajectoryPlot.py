# trajectoryPlot.py
from time import ctime
from math import pi, cos, tan
from numpy.lib.scimath import sqrt
import numpy as np
import matplotlib.pyplot as plt

def trajectory(v0, y0, theta, intervals):
    theta = theta * pi / 180  # convert to radians
    G = 9.81        # m/s**2
    a = -G / (2 * v0**2 * cos(theta)**2)
    b = tan(theta)
    c = y0       
    distance = (-b - sqrt(b*b - 4*a*c)) / (2 * a)
    #root2 = (-b + sqrt(b*b - 4*a*c)) / (2 * a)
    xValues = np.linspace(0., distance, intervals+1)
    yValues = (a * xValues + b) * xValues + c
    return (xValues, yValues)


def plotTrajectory(xValues, yValues):
    plt.figure()
    plt.plot(xValues, yValues, 'y-')
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.title('Projectile Trajectory')
    plt.legend(['ax^2+bx+c'])
    plt.savefig('trajectory.png')
    plt.show()

print('\n' + '-'* 80)
intervals = 100

while True:
  try:
    v0 = float(input("Enter the initial velocity: "))
    y0 = float(input('Enter the initial height: '))
    theta = float(input('Enter the launch angle: '))
    break
  except:
    print('Invalid data, try again!')


# display the values of the variables
print("""
v0        = %.1f m/s
y0        = %.1f m
theta     = %d degrees
intervals = %d
""" % (v0, y0, theta, intervals))

xValues, yValues = trajectory(v0, y0, theta, \
                              intervals)
plotTrajectory(xValues, yValues)

print("""
Programmed by Stew Dent.
Date: %s.
End of processing.""" % ctime())
