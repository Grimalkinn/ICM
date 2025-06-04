#readAverage1

def main():
    infile = open('data1.txt', 'r')
    lines = infile.readlines()
    infile.close()
    
    total=0
    for line in lines:
        print(line,end='')
        total=total+ float(line)
    print("The average is: ", total/len(lines))

    
main()

#C:\\Users\\ababa\\Documents\\Abolfazl\\Instructor\\ICM\\COMP courses ICM\COMP 1012\\week12\\