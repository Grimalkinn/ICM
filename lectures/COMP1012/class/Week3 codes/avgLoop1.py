numbers = [1, 2, 3, 4, 5, 6]
total = 0
index = 0
print("The numbers are:")
while index < len(numbers):
    number = numbers[index]
    print(number)
    total += number
    index += 1
# while

print("The average is %g" % (total //
                             len(numbers)))

