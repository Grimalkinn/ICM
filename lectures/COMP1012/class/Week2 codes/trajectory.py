from time import ctime
from math import pi, cos, tan
print('------------------------------------------------------------\n')
G = 9.81       # m/s**2
v0 = float(input('Enter the inital velocity in m/s: '))
y0 = float(input('Enter the initial height in m: '))
theta = float(input('Enter the initial angle in degrees: '))
x = float(input('Enter the distance x in m: '))
# display the values of the variables
print("""
gravity = %.2f m/s^2
v0      = %.1f m/s
y0      = %.1f m
theta   = %g degrees
x       = %.1f m
""" % (G, v0, y0, theta, x))
theta = theta * pi / 180  # convert theta to radians
# calculate the vertical position of the ball and display the result
y = x * tan(theta) - 1 / (2 * v0**2) * G * x**2 / cos(theta)**2 + y0
print('The position of the ball is (%.2f,%.4f)' % (x, y))
print("""
Programmed by Stew Dent.
Date: %s.
End of processing.""" % ctime())
