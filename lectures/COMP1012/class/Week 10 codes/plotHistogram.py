# plotHistogram.py
import numpy as np
import matplotlib.pyplot as plt

count = 500
while True:
    rands = np.random.randint(1, 101, count)
    print('%d random numbers in histogram.' % count)
    myTitle = 'Frequency vs Value for ' + str(count) + ' values.'
    plt.hist(rands, bins=500)           
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.title(myTitle)
    plt.savefig('PlotHistogram.png')
    plt.show()

    data = input(
        "Press return to continue (any key to quit): ").strip()
    if data != '':
        break
    count += 100



    data = input(
        "Press return to continue (any key to quit): ").strip()
    if data != '':
        break
    count += 100