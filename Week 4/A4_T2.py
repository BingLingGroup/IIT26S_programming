print("Program starting.\n")

start_value = int(input("Insert starting value: "))
end_value = int(input("Insert stopping value: ")) + 1

print("\nStarting for-loop:")
if start_value < end_value:
    print(start_value, end="")
for i in range(start_value + 1, end_value):
    print(" {value}".format(value=i), end="")

print("\n\nProgram ending.")
