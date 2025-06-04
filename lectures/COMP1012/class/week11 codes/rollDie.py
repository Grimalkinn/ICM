# rollDie.py

from random import random

def rollDie():
    return int(random() * 6) + 1
    
print('The number rolled is', rollDie())


rollDie()