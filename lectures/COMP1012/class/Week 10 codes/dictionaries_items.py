capitals = {'Manitoba' : 'Winnipeg', 'Saskatchewan' : 'Regina', 'Alberta' : 'Edmonton',
'British Columbia' : 'Victoria'}

keys=list(capitals.keys())

values=list(capitals.values())


print(capitals.items())


for keys,values in capitals.items():
    
    print(keys,values)