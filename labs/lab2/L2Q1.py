

dollar = 0
quarter = 0
dime = 0
nickel = 0
penny = 0
count = 0

amount = float(input("Enter number of pennies: "))
ogAmount = amount

while amount > 5:
    if amount > 100:
        dollar += 1
        amount -= 100
    elif amount > 25:
        quarter += 1
        amount -= 25
    elif amount > 10:
        dime += 1
        amount -= 10
    elif amount > 5:
        amount -= 5
        nickel += 1

penny = int(amount)

print(f"{ogAmount} pennies is equivalent to: \n")
