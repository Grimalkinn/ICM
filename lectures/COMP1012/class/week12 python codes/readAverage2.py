#readAverage2

def main():
    infile = open('data1.txt', 'r')
    lines = infile.readlines()
    infile.close()
    
    a = [float(line) for line in lines]
    print(a)
    total=sum(a)
    print('\nThe average is', total / len(lines))

main()
