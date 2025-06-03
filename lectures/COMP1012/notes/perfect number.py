from time import ctime
from math import sqrt

def getPosInt(prompt):
    # prompt - the prompt to display to the user for input
    # number - the number entered by the user
    while True:
        number = input(prompt).strip()
        if number != '':
            try:
                number = eval(number, {}, {})
            except:
                print('Invalid input!')
            else:
                if type(number) is int:
                    if number > 0:
                        break
                    else:
                        print(number, 'is not a positive integer!')
                else:
                    print(number, 'is not an integer!')
        else:
            break
    return number


def findDivisors(number):  # find divisors of number
    divisors = []
    for divisor in range(1, int(sqrt(number))+1):
        if number % divisor == 0:
            divisors.append(divisor)
            divisors.append(number//divisor)
        # if
    # for
    divisors.sort()  # sort into ascending order
    return divisors
# findDivisors


def displayDivisors(divisors):# display the divisors
    for divisor in divisors:
        print(divisor)
    # for
# displayDivisors


def perfectNumber(divisors): # is this a perfect number?
    if sum(divisors[:-1]) == divisors[-1]:
        print(divisors[-1], 'is a perfect number!')
# perfectNumber

def main(): # get input from user and process it
    print('\n------------------------------------------')
    number = getPosInt('Enter a positive number (Enter to quit): ')
    while type(number) is int:
        print('The divisors for %d are:' % number)
        divisors = findDivisors(number)
        displayDivisors(divisors)
        perfectNumber(divisors)
        number = getPosInt(
                       'Enter a positive number (Enter to quit): ')
    print("""
Programmed by Stew Dent.
Date: %s.
End of processing.""" % ctime())

main()

