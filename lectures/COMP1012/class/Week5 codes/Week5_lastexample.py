from time import ctime

def threeNplus1(number):
    result = [number]
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        result.append(number)
    return result

def displayList(theList, number):
    print('\nThe 3N+1 sequence for %d follows:' % number)
    for index, element in enumerate(theList):
        if index % 6 == 0 and index != 0:
            print()
        print('%10d' % (element), end = ' ')

def main():
    print('-------------------------------------------------------\n')
    number = int(input('Enter a positive integer: '))
    if number > 0:
        displayList(threeNplus1(number), number)
    else:
        print('Number must be greater than zero!')
    print("""
\nProgrammed by Stew Dent.
Date: %s.
End of processing.""" % ctime())

main()
