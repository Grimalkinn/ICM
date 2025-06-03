# OkwuosaFelixA1Q2.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 1 Question 2
# Author: Felix Okwuosa
# Version: yyyy/mm/dd
#
# Purpose: compute the approximate values of: (1+x)ex, where x > 0
#
# var1 - the use / meaning of each variable in the program

from time import ctime

print('\n----------------------------------------------------\n')

value = approx = terms = 0

# deci = int(input("Enter the number of decimal places: 60"))
# x = int(input("Enter the value of x: 2"))
deci = 60
x = 2

# Add terms to the sum of the series as long as the value of the current term is greater than 0.
# Count the number of terms in the series.
# Your program must input the value of the number of decimal places and the value of x. Both
# of these must be integers. There must NOT be any floats in the summation of the series!
# Compute the value of (1+x)ex using Python's exp function and display the value to 14
# decimal places using exponential format.
# Display the approximate value of (1+x)ex, which is the sum of the series, so that it looks like
# a real number (contains a decimal point). Display the number of terms in the series as an
# integer using the appropriate format code.


print(f"Python's values of (3)e^2 is: \n{value}\n")
print(f"The approximate value of (3)e^2 is: \n{approx}\n") # 2.21671682967919e+01
print(f"The number of terms in the series is \n{terms}\n") # 22.167168296791943735039113077372809954641688103715564213501952

print("""
Programmed by Felix Okwuosa
Date: %s
End of processing.
""" % ctime())
