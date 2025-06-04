# allBirthdays.py

from random import randint
import numpy as np
from math import ceil

birthday = lambda days : randint(1, days)

def allBirthdays(days):
    people = 0
    count = 0  # count days with birthdays
    birthdays = np.zeros((days), bool)
    while count < days:
        day = birthday(days)-1
        people += 1
        if not birthdays[day]:
            birthdays[day] = True
            count += 1
    return people

def main():
    days = 365
    count = 0
    samples = 10000
    for i in range(samples):
        count += allBirthdays(days)
    people = ceil(count/samples)
    print((people, days))

main()

