# OkwuosaFelixA1Q1.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 1 Question 1
# Author: Felix Okwuosa
# Version: yyyy/mm/dd
#
# Purpose:  compute the GCD of two numbers
#
# var1 - the use / meaning of each variable in the program

from time import ctime

print('\n----------------------------------------------------\n')

gcd = 0 # store value of gcd
lcm = 0 # store value of lcm

first = int(input("Enter the first integer number: ")) # get first number from user
second = int(input("Enter the second integer number: ")) # get second number from user
# first = 5
# second = 2

if type(first) == type(0.0):
    print("A float value is entered which is not acceptable")
else:
    #  First compute the remainder of dividing the larger number by the smaller
    #  number
    # • Next, replace the larger number with the smaller number and the smaller
    #  number with the remainder.
    # • Repeat this process until the smaller number is 0. The GCD is the last 
    # value of the larger number.

    if first > second:
        small = second
        large = first
    else:
        small = first
        large = second


    temp = large # store value of large
    loop = True # loop condition
    while loop:
        if (large % first == 0) and (large % second == 0):
            lcm = large
            loop = False
        else:
            large += 1
    large = temp


    while small <= 0:
        # rem = large / small # strore the remainder
        rem = small % large # store the remainder
        temp = large
        large = small
        small = rem
    gcd = large

    print(f"The Greatest Common Divider is: {gcd}")  # 1
    print(f"The Larger Common Multiplier is: {lcm}") # 10

print("""
Programmed by Felix Okwuosa
Date: %s
End of processing.
""" % ctime())