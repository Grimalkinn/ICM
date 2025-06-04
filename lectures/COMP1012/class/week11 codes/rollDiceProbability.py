# rollDiceProbability.py

from random import randint

rollDie = lambda : randint(1, 6)

rollDice = lambda : rollDie() + rollDie()
    
def main():
    rolls = [0] * 11
    numRolls = int(input('Enter the number of times '+'to roll the die (> 0): '))
    if numRolls > 0:
        for i in range(numRolls):
            rolls[rollDice()-2] += 1
        for roll in range(11):
            probability = rolls[roll] / numRolls
            print('roll: %2d, probability: %.3f' \
                   % (roll+2, probability))
    else:
        print(numRolls, ' is not greater than zero!')

main()
