def getInt(prompt):
    while True:
        number = input(prompt).strip()
        if number != '':
            try:
                number = eval(number, {},{})
            except:  # handle the error
                print('Invalid input!')
            else:    # no error, do this
                if type(number) is int:
                    break
                else:
                    print(number, 'is not an integer!')
        else:
            print('Missing input!')
    return number

print(getInt('Enter an integer: '))
