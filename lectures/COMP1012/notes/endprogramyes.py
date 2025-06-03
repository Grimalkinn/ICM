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
getBoolean("enter a number")