# integerInput1.py
def getInt():
    number = input('Enter an integer: ').strip()
    if number != '':
        number = eval(number, {}, {})
        if type(number) is int:
            print('%d is an integer.' % number)
        else:
            print(number, 'is not an integer!')
    else:
        print('Missing input!')
getInt()
