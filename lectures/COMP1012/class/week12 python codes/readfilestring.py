#readfilestring

from time import ctime

def main():
    infile = open('data1.txt', 'r')
    lines = infile.readlines()
    infile.close()

    print(lines)
    for line in lines:
        print(line, end='')
    
    print("""\n
Programmed by Stew Dent.
Date: %s.
End of processing.""" % ctime())

main()

