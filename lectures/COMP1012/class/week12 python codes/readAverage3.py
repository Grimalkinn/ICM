#readAverage3



def main():
    infile = open('data1.txt', 'r')
    numbers = [float(line) for line in infile]
    infile.close()
    
    average = sum(numbers) / len(numbers)
    print('\nThe average is', average)

main()
