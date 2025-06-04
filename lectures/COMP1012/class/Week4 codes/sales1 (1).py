sales = []
sales.append(['Bob', 1500., 840., 1750.])
sales.append(['Pat', 450., 900.])
sales.append(['Fred', 990., 550, 275., 1200.])
sales.append(['Jane', 1330., 1075., 1100.])

sales1=[]
#print(sales)

for person in sales:
    print('Sales for', person[0], '->', end=' ')
    total = 0.
    '''for amount in person[1:]:
        print('$%.2f ' % amount, end=' ')
        total += amount'''
    total=sum(person[1:])
    print('Total: $%.2f\n' % total)
    sales1.append(person[0])
    sales1.append(total)


print(sales1)

print((sales1[1::2]))


sales2=[]
for index, element in enumerate(sales1):
    
    if type(element)==float:
        sales2.append((element))
print(sales1[sales1.index(max(sales1[1::2]))],end=" ")

print(max(sales2))





   
#print(max(sales1))
    


