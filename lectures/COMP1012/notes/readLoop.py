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


def displayList(heading, theList):
    print('\n%s' % heading)
    for element in theList:
        print(element)
    print('There are %d elements in the list.' %
          len(theList))

def displayTerminationMessage():
    print('''
Programmed by Stew Dent.
Date: %s
End of processing.''' % ctime())

def main():
    numbers = []
    number = getInteger("Enter an integer: ")
    while number != '':
        numbers.append(number)
        number = getInteger("Enter an integer: ")
    displayList(
         'The elements in the list of numbers are:',
          numbers)
    displayTerminationMessage()

main()

