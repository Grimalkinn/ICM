tempC = (-40, -30, -20, -10, 0, 10, 20, 30, 40)
tempF = []
print("Celsius\tFahrenheit")
i = 0
while i < len(tempC):
    tempF.append(9./5 * tempC[i] + 32)
    print("%7d\t%10d" %(tempC[i],
                          tempF[i]))
    i += 1
# while
