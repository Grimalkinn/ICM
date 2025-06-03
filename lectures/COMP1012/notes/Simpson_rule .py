from time import ctime
from math import sqrt, pi

def  getPosNumber(prompt):
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
                        print(number, 'is not a positive number')
                else:
                    print(number, 'is not an integer!')
        else:
            print('Missing input!')
    return number


def f(rSquared, x): # for a circle
    return sqrt(rSquared-min(x**2, rSquared))

def simpsonCircle(a, b, intervals):
    # a - the first x value, must be a real number
    # b - the last x value, must be a real number
    # intervals - the number of intervals, must be an even number
    # rSquared - the square of the radius of the circle
    # h – the width of equally spaced intervals
    # firstSum – the first sum in Simpson's rule
    # secondSum – the second sum in Simpson's rule
    # i – a general purpose index
    rSquared = b*b
    h = (b - a) / intervals
    firstSum = 0.
    for i in range(1, intervals//2 + 1):
        firstSum += f(rSquared, a + (2*i - 1)*h)
    secondSum = 0.
    for i in range(1, intervals//2):
        secondSum += f(rSquared, a + 2*i*h)
    area = h/3. * (f(rSquared, a) + 4 * firstSum + 2 * secondSum +
           f(rSquared, b))
    return area * 4  # area was for 1/4 of a circle
    
    

def main():
    print('\n' + '-' * 80)
    print('\nEnter 0 at any prompt to terminate the program.')
    while True:
        intervals = int(getPosNumber('Enter the number of intervals (even > 0): '))
        while (intervals % 2 != 0):
            print('The number of intervals, %d, must be even!' % intervals)
            intervals = int(getPosNumber(
                            'Enter the number of intervals (even > 0): '))
        if intervals == 0:
            break
        radius = float(getPosNumber('Enter the radius of the circle in cm: '))
        if radius == 0.0:
            break
        area = simpsonCircle(0.0, radius, intervals)
        actual = pi * radius * radius
        error = abs(actual - area)
        print('\nArea is from x=%.2f to x=%.2f' % (0.0, radius))
        print('Approximate area of circle is %.14e cm^2' % (area))
        print('     Actual area of circle is %.14e cm^2' % actual)
        print('Error in the approximation is %e cm^2' % error)

main()
