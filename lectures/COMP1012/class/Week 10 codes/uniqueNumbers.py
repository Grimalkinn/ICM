import numpy as np
import matplotlib.pyplot as plt
from time import ctime

def getInteger(prompt):
    while True:
        number = input(prompt).strip()
        if number != '':
            try:
                number = eval(number, {}, {})
            except:
                print(number, 'is not valid!')
            else:
                if type(number) is int:
                    break
                else:
                    print(number, 'is not an integer!')
        else:
            break
    return number


def displaySequence(heading, theSequence):
    print('\n%s' % heading)
    for element in theSequence:
        print(element)
    print('There are %d elements in the sequence.' %
          len(theSequence))

def displayTerminationMessage():
    print('''
Programmed by Stew Dent.
Date: %s
End of processing.''' % ctime())


def main():
    listOfNumbers = []
    setOfNumbers = set()
    number = getInteger("Enter an integer: ")
    while number != '':
        listOfNumbers.append(number)
        setOfNumbers.add(number)
        number = getInteger("Enter an integer: ")
    displaySequence(
         'The elements in the list of numbers are:',
          listOfNumbers)
    displaySequence(
         'The elements in the set of numbers are:',
         setOfNumbers)
    displayTerminationMessage()

main()



