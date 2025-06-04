
from time import ctime

def displayTerminationMessage():
	print('''
Programmed by Stew Dent.
Date: %s
End of processing.''' % ctime())

def displayFrequencies(frequencies):
	print('\n%10s %10s' % ('Number', 'Frequency'))
	for number in frequencies:
		print('%10d %10d' % (number, frequencies[number]))

def displaySortedFrequencies(frequencies):
	sortedKeys = sorted(frequencies.keys())
	print('\n%10s %10s' % ('Number', 'Frequency'))
	for key in sortedKeys :
		print('%10d %10d' % (key, frequencies[key]))


def main():
    frequencies = {}
    
    data=input("Enter an integer: ").strip()
    while data:
        number = int(data)
        if number in frequencies:
            frequencies[number] += 1
        else:
            frequencies[number] = 1
        data=input("Enter an integer: ").strip()
    displayFrequencies(frequencies)
    displaySortedFrequencies(frequencies)
    displayTerminationMessage()
    
main()
