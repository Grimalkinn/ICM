from pprint import pprint

#import pprint

tempC = [-20 + temp * 5 for temp in range(9)]
tempF = [9/5. * temp + 32 for temp in tempC]
#print(tempC)
#print(tempF)


table1=[[tC,tF]for tC,tF in zip(tempC,tempF)]
pprint(table1[:6:2])

table1[1]=99
pprint(table1)
#print(table1[:6])

'''print("celcius\tfahrenheit")

for celcius, fahrenheit in table1:
    
    print("%6.2f\t%6.2f"%(celcius, fahrenheit))'''

