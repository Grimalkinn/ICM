# OkwuosaFelixA1Q3.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 1 Question 3
# Author: Felix Okwuosa
# Version: yyyy/mm/dd
#
# Purpose: compute the ratio of two numbers and output the decimal number in a speceified decimal position
#
# var1 - the use / meaning of each variable in the program

from time import ctime

print('\n----------------------------------------------------\n')

value = 0
answer = 0
count = 0

nume = int(input("Enter the numerator: 93"))
deno = int(input("Enter the denominator: 26"))
index = int(input("Enter the position of the decimal digit that you want: 3"))


answer = nume / deno
output = list(str(answer))

# decimals = []
# deci = ['3','.','5','7','6','9']

for i in range(len(output)):
    if output[i] == ".":
        for j in range(index):
            if j == index-1:
                value = output[j+i+1]


print(f"The answer of the division is: {answer:.8f}\n")
print(f"{value} is placed in position {index} after decimal point\n") 

print("""
Programmed by Felix Okwuosa
Date: %s
End of processing.
""" % ctime())
