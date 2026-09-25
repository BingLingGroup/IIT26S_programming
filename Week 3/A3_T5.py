print("Program starting.")

print("""\nOptions:
1 - Celsius to Fahrenheit
2 - Fahrenheit to Celsius
0 - Exit""")
choice = int(input("Your choice: "))

if choice == 1:
    Celsius = float(input("Insert the amount of Celsius: "))
    print("{Celsius} °C equals to {Fahrenheit} °F".format(
        Celsius=round(Celsius, 1), Fahrenheit=round(Celsius * 1.8 + 32, 1)))
elif choice == 2:
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    print("{Fahrenheit} °F equals to {Celsius} °C".format(
        Celsius=round((Fahrenheit - 32) / 1.8, 1), Fahrenheit=round(Fahrenheit, 1)))
elif not choice == 0:
    print("Unknown option.")
else:
    print("Exiting...")

print("\nProgram ending.")
