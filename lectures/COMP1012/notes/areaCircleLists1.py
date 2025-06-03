from time import ctime
from math import sqrt, pi

def getPosNum(prompt):
    while True:
        number = input(prompt).strip()
        if number != '':
            try:
                number = eval(number, {}, {})
            except:
                print('Invalid input!')
            else:
                if type(number) is int or type(number) is float:
                    if number >= 0:
                        break
                    else:
                        print(number, 'is not a positive number!')
                else:
                    print(number, 'is not an number!')
        else:
            print('Missing input!')
    return number

def fxCircle(radius, xCoords):
    rSquared = radius * radius
    return [sqrt(rSquared-min(x**2, rSquared))
            for x in xCoords]

def areaCircle(fx, radius, intervals):
    xCoords = [i * radius/intervals for i in
               range(intervals+1)]
    yCoords = fx(radius, xCoords)
    area = 0.
    for i in range(intervals):
        area += yCoords[i] + yCoords[i+1]
    #area = 4. * area / 2 * deltaX
    area *= 2 * radius/intervals
    return area

def main():
    print('\n' + '-' * 80)
    print('\nEnter 0 at any prompt to terminate the program.')
    while True:
        radius = float(getPosNum(
                 'Enter the radius in cm (>0): '))
        if radius == 0.0:
            break
        intervals = int(getPosNum(
                'Enter the number of intervals (>0): '))
        if intervals == 0:
            break
        area = areaCircle(fxCircle, radius, intervals)
        actual = pi * radius * radius
        error = abs(actual - area)
        print("""
Approximate area of circle is %.14e cm^2
     Actual area of circle is %.14e cm^2
     The error in the area is %e cm^2""" % (area, actual, error))

main()
