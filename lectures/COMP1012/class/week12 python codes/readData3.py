from time import ctime

def main():
    infile = open('data1.txt', 'r')
    lines = [line for line in infile]
    infile.close()
    print(lines)
    a=[]
    for line in lines:
        print(line.strip())  
        a.append(line)

    print("""\n
Programmed by Stew Dent.
Date: %s.
End of processing.""" % ctime())

main()
