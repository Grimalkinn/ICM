from numpy.random import uniform  # MonteCircle.py
from numpy import sum, pi

r = float(input('Enter the radius of the circle: '))
if r > 0:
    points = int(input('Enter the number of points: '))
    if points > 0:
        xCoords = uniform(-r, r, points)
        yCoords = uniform(-r, r, points)
        inCircle = xCoords*xCoords + yCoords*yCoords <= r*r
        probability = sum(inCircle) / points
        area = probability * 4. * r * r
        actualArea = pi * r * r
        error = abs(area - actualArea)
        print('The probability of a point being in the circle is %.4f'
               % probability)
        print('The approximate area of the circle is %.15f' % area)
        print('     The actual area of the circle is %.15f' 
               % actualArea)
        print('    The error in the approximation is % e' % error)
    else:
        print('The number of points must be greater than zero!')
else:
    print('The radius of the circle must be greater than zero!')

