from math import pi, cos, tan
G = 9.81        # m/s**2
v0 = 5.0        # m/s
y0 = 1          # m
theta = 60      # degrees
x = 0.          # m
heights = []    # m
distances = []  # m

# display the values of the variables
print("""
gravity = %.2f m/s^2
v0      = %.1f m/s
y0      = %.1f m
theta   = %d degrees
x       = %.1f m
""" % (G, v0, y0, theta, x))

theta = theta * pi / 180  # convert theta to radians
# calculate the vertical position of the ball
# and display the result
y = y0
while y >= 0:
    heights.append(y)
    distances.append(x)
    x += .1
    y = x * tan(theta) - 1 / (2 * v0**2) * G *x**2 / cos(theta)**2 + y0
# while

i= 0
while i< len(heights):
    print("%.1f\t%.6f" % (distances[i],
                          heights[i]))
    i += 1
# while
