tempC = (-40, -30, -20, -10, 0, 10, 20, 30, 40)
tempF = []
print("Celsius\tFahrenheit")
for i in tempC:
    
    fahrenheit=(9/5)*i+32
    tempF.append(fahrenheit)
    print("%.2f\t\t%.2f"%(i,fahrenheit))


