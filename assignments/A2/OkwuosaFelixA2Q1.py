# OkwuosaFelixA2Q1.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 2 Question 1
# Author: Felix Okwuosa
# Version: yyyy/mm/dd
#
# Purpose: reads a given list and removes duplicate data
#
# var1 - the use / meaning of each variable in the program

from time import ctime
print('\n----------------------------------------------------\n')


e1 = 0
e2 = 0
e3 = 0
e4 = 0

inital = []
final = []

def grabList():
    # length = int(input("Enter the length of the list: ")) # 4
    # for i in range(1,length):
    #     inital.append(int(input(f"Enter element {i}:")))
    
    # debug 
    length = 4
    element1 = 12
    element2 = 2.4
    element3 = 'a'
    element4 = 2.4
    inital.append(element1)
    inital.append(element2)
    inital.append(element3)
    inital.append(element4)
    return inital

    


def listSearch(arr):
    pass

def delDump():
    pass

def main():
    delDump(listSearch(grabList()))

main()

print(f"The final list is: {final}") #The final list is: [12,a]
print(f"The element {element1} occurs {e1} time at {p1}.") #The element 12 occurs 1 time at 0.
print(f"The element {element2} occurs {e2} times at {p21},{p22} => it is removed") #The element 2.4 occurs 2 times at 1,3 =>
print(f"The element {element3} occurs {e3} time at {p3}.") #The element a occurs 1 time at 2.

print("""
Programmed by Felix Okwuosa
Date: %s
End of processing.
""" % ctime())
