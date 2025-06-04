# passwords1.py
from random import randint, seed  # added seed

def main():
    length = int(input('Enter the length of ' +
                       'the passwords (> 7): '))
    if length > 7:
        seed(4)  # added call to seed
        numPasswords = int(input('Enter the ' +
                       'number of passwords: '))
        print('Random passwords of length %d:'
               % length)
        for passwords in range(numPasswords):
            print(randomPassword(length))
    else:
        print('The length of the passwords must' +
              ' be > 7!')

def randomChar(lowerBound, upperBound):
    return chr(randint(ord(lowerBound),
                       ord(upperBound)))

randomUppercase = lambda : randomChar('A', 'Z')
randomLowercase = lambda : randomChar('a', 'z')

def randomLetter():
    return (randomLowercase() if randint(0, 1)
            == 0 else randomUppercase())

def randomPassword(length):
    password = randomUppercase()
    for i in range(length-1):
        password+=randomLetter()
    return password

main()