from time import ctime 
print('---------------------------------------------------\n')
celsius = float(input(
          'Enter the first celsius temperature: '))
stop = float(input(
       'Enter the last celsius temperature: '))
step = float(input(
       'Enter the difference between temperatures: '))

print("Celsius\tFahrenheit")  # display a heading

while celsius <= stop:
    fahrenheit = (9/5)*celsius + 32
    print("%7.2f\t%10.2f" % (celsius, fahrenheit))
    celsius += step

print("""
Programmed by Stew Dent.
Date: %s.
End of processing.""" % ctime())
