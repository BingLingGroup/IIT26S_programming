print("Program starting.\n")

start_value = int(input("Insert starting value: "))
end_value = int(input("Insert stopping value: ")) + 1

print("\nStarting for-loop:")
output_list = []
for i in range(start_value, end_value):
    output_list.append("{value}".format(value=i))

print(" ".join(output_list))
print("\nProgram ending.")
