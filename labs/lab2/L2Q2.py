
count = 0
rem = 0
while True:
    kilogram = 0
    
    pounds = int(input("Enter the integer number of pounds (<0 to quit): "))
    count = pounds
    if count == -1:
        break
    ounces = float(input("Enter the number of ounces as a real number: "))
    
    amountP = float(pounds)
    amountO = float(ounces)

    # pounds to kilograms
    while amountP > 2.2046:
        # if amountP >= 2.2046:
        kilogram += 1.0
        amountP = amountP - 2.2046

    while amountO > 35.2736:
        # if amountO >= 35.2736:
        kilogram += 1.0
        amountO = amountO - 35.2736
    
    rem += amountO
    rem += amountP

    print(f"The number of kilograms for {pounds} pounds and {ounces} ounces is {float(kilogram )}\n") 

    
