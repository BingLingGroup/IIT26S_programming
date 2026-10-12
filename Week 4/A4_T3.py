print("Program starting.\n")

start_value = int(input("Insert starting value: "))
end_value = int(input("Insert stopping value: ")) + 1

print("\nStarting while-loop:")
i = 1
if start_value < end_value:
    print(start_value, end="")
while i < end_value:
    print(" {value}".format(value=i), end="")
    i = i + 1

print("\n\nProgram ending.")
