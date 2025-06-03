def getInt():
    number = input('Enter an integer: ').strip()
    if number != '':
        try:
            number = eval(number, {}, {})
        except:  # handle the error
            print('Invalid input!')
        else:    # no error, do this
            if type(number) is int:
                print('%d is an integer.' % number)
            else:
                print(number, 'is not an integer!')
    else:
        print('Missing input!')

getInt()
