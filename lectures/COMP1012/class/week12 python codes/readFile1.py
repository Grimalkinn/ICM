def main():
    infile = open('data1.txt', 'r')
    print ('The data in the file is:')
    data = infile.read()
    print(data)
    total=0
    print(data.split())
    for i in data.split():
        total+=float(i)
    print(total/len(data.split()))
    
    print(len(data.split()))
main()

#count the number of integer and float that you have in
#your file
#hint: use eval function