#readline


def main():
    infile = open('data1.txt', 'r')
    print('The data in the file is:')
    data = infile.readline()
    while data:
        print(data, end='')
        data = infile.readline()
    infile.close()
    
main()
