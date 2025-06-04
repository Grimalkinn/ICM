from math import pi, sin
print('--------------------------------------------\n')
TOLERANCE = 1.0e-17
degrees = float(input("Enter an angle in degrees: "))
x = degrees * pi / 180
factor = 2
sine = 0.0
term = x
xSquared = x * x
count=1
while abs(term) > TOLERANCE:
    sine += term
    term = -term * xSquared / (factor * (factor + 1))
    factor += 2
    count+=1
# end while
print("""
Angle in radians = %g, angle in degrees = %.2f
   Python's value of sin(%.2f) = %.15f
Approximate value of sin(%.2f) = %.15f
Number of terms = %d""" % (x,  degrees, degrees, sin(x),
                           degrees, sine, count))
