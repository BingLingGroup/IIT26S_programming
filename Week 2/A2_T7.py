print("Program starting.")
Fahrenheit = float(input("Insert fahrenheits: "))
Celcius = (Fahrenheit - 32) / 1.8
print("{fahrenheit:.1f}°F is {celcius:.1f}°C".format(
    fahrenheit=Fahrenheit, celcius=Celcius))
print("Program ending.")
