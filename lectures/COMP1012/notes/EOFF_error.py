from time import ctime
largest = 2**31-1       # compute largest integer value
smallest = -2**31         # compute smallest integer value
count = 0
total = 0.               # force total to be a float
loop = True  # continue looping until loop becomes false
while loop:
    try:
        num = input('Enter a number: ')
    except EOFError:  # handle end of file error
        loop = False
    else:  # no error, do this
        try:
            num = eval(num, {}, {})
        except:  #  handle error
            print('Invalid input!')
        else:  # no error, do this
            print ('%8.2f' % num)
            total += num
            count += 1
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num
average = total / count

print(average)
