from time import ctime

def getBoolean(prompt):
    # prompt - the prompt to display to the user
    # data   - the input from the user
    # result - the return value: True if user enters yes and
    #          False if user enters no
    while True:
        data = input(prompt).strip()
        data = data[0]
        if data == 'y' or data == 'Y':
            result = True
            break
        elif data == 'n' or data == 'N':
            result = False
            break
        else:
            print(data, 'is not a valid response!')
    return result


def getValidInt(prompt, minX):
    while True:
         number = input(prompt).strip()
         if number != '':
            try:
                number = eval(number, {}, {})
            except:  # handle the error
                print('Invalid input!')
            else:    # no error, do this
                if type(number) is int:
                    
                    if number % 2 == 1:
                        if number >= minX:
                            break
                        else:
                            print('%d is not greater than %d!' %
                                 (number, minX-1))
                    else:
                        print('%d is not odd!' % number)
                else:
                    print(number, 'is not an integer!')
         else:
            print('Missing input!')
    return number



def drawX(size):
    """ size of x
    Draw an X in size by size grid.
    size - the size of the grid
    """
    # indices - the valid row and column indicies
    # row     - the current column index
    # column  - the current column index
    
    indices = range(size)
    for row in indices:
        for column in indices:
            if row == column or row + column == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()  # for next print to start on a new line

def main():
    """
    The main function. """
    # prompt    - the prompt to dispay to the user
    # minX      - the minimum size of an X to draw
    # playAgain - prompt for playAgain question
    # drawAnX   - true if another X is to be drawn
    print('\n' + '-' * 80)
    prompt = 'Enter the size of the X (odd integer > 2): '
    playAgain = 'Draw another X? (Y/N): '
    minX = 3
    drawAnX = True
    while drawAnX:
        drawX(getValidInt(prompt, minX))
        drawAnX = getBoolean(playAgain)
    print("""
Programmed by Stew Dent.
Date: %s.
End of processing.""" % ctime())

main()