# rollDiceProbability2.py
import numpy as np
import matplotlib.pyplot as plt

rollDie = lambda numRolls: np.random.randint(1, 7, numRolls)
rollDice = lambda numRolls: rollDie(numRolls) + rollDie(numRolls)
    
def main():
    numRolls = int(input('Enter the number of times to roll '+\
                         'the die (> 0): '))
    if numRolls > 0:
        rolls = rollDice(numRolls)
        plt.hist(rolls, bins=11)
        plt.title('Distribution of sums of rolling a pair ' +\
                  'of dice.')
        plt.xlabel('Sum of a pair of dice.')
        plt.ylabel('Frequency.')
        plt.savefig('DiceDistro.png')
        plt.show()
    else:
        print(numRolls, ' is not greater than zero!')
    
main()
