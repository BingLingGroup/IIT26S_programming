print("Program starting.\n")

start_value = int(input("Insert starting value: "))
end_value = int(input("Insert stopping value: ")) + 1

print("\nStarting while-loop:")
i = 1
output_list = []
while i < end_value:
    output_list.append("{value}".format(value=i))
    i = i + 1

print(" ".join(output_list))
print("\nProgram ending.")
