print("Program starting.")
Fahrenheit = float(input("Insert fahrenheits: "))
Celcius = (Fahrenheit - 32) / 1.8
print("{fahrenheit}°F is {celcius}°C".format(
    fahrenheit=round(Fahrenheit, 1), celcius=round(Celcius, 1)))
print("Program ending.")
