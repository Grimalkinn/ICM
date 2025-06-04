# rollDieProbability2.py

from random import randint

def rollDie():
    return randint(1, 6)
    
def main():
    rolls = [0] * 6
    numRolls = int(input('Enter the number of times to '+\
                         'roll the die (> 0): '))
    if numRolls > 0:
        for i in range(numRolls):
            rolls[rollDie()-1] += 1
        for roll in range(6):
            probability = rolls[roll] / numRolls
            print('roll: %d, probability: %.3f'\
                   % (roll+1, probability))
    else:
        print(numRolls, ' is not greater than zero!')

main()
