from math import exp

n=int(input("Enter the number of terms: "))

term=1
count= 1
ee=1
while count<=n:
    
    term=term/count
    ee+=term
    count+=1
    
print("Actual value of e: ", exp(1), "approximated value", ee)
    