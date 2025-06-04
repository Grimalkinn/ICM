from time import ctime

def main():
    infile = open('data1.txt', 'r') # 'r' means read
    for line in infile:
        print(line, end='')
    infile.close()
    
    print("""\n
Programmed by Stew Dent.
Date: %s.
End of processing.""" % ctime())

main()
