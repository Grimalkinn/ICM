def main():
    infile = open('data1.txt', 'r')
    print ('The data in the file is:')
    data = infile.read()
    print(data)
    total=0
    print(data.split())
    countint=0
    countfloat=0
    countstr=0
    for i in data.split():
        print(i)
        try:
            a=eval(i)
        except:
            countstr+=1
        else:
            if type(a)==int:
                countint+=1
            elif type(a)==float:
                countfloat+=1
                
    print("int: ", countint)
    print("float: ",countfloat)
    print("string: ", countstr)
main()

#count the number of integer and float that you have in
#your file
#hint: use eval function