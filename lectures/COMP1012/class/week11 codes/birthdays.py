# birthdays.py

from random import randint
import numpy as np
from math import ceil

birthday = lambda days : randint(1, days)
def sameBirthday(days):
    birthdays = np.zeros((days), bool)
    count = 0
    while True:
        day = birthday(days)-1
        count += 1
        if birthdays[day]:
            break
        else:
            birthdays[day] = True
    return count

def main():
    days = 365
    count = 0
    samples = 10000
    for i in range(samples):
        count += sameBirthday(days)
    people = ceil(count/samples)        # Round a number upward to its nearest integer
    print('The number of people required to '+
          'have the same birthday is %d.'
          % people)

main()
