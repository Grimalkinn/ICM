sales = []
sales.append(['Bob', 1500., 840., 1750.])
sales.append(['Pat', 450., 900.])
sales.append(['Fred', 990., 550, 275., 1200.])
sales.append(['Jane', 1330., 1075., 1100.])

for person in sales:
    print('Sales for', person[0], '->', end=' ')
    total = 0.
    for amount in person[1:]:
        print('$%.2f ' % amount, end=' ')
        total += amount
    print('Total: $%.2f\n' % total)
