# differentBirthdays.py

from random import randint
import numpy as np

birthday = lambda days : randint(1, days)

def differentBirthdays(people, days):
    birthdays = np.zeros((days), bool)
    for i in range(people):
        day = birthday(days)-1
        if not birthdays[day]:
            birthdays[day] = True
    # sum(birthdays) counts the number
    # of occurrences of True in the
    # array.
    return sum(birthdays)

def main():
    days = 365
    people = 365
    count = 0
    samples = 10000
    for i in range(samples):
        count += differentBirthdays(people,
                 days)
    different = count//samples
    print((people, different))

main()
