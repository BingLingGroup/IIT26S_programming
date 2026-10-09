print("Program starting.")

value = int(input("Insert a positive integer: "))
i = 0
while value != 1:
    print("{value} -> ".format(value=value), end="")
    if value & 1:
        value = value * 3 + 1
    else:
        value = value >> 1
    i = i + 1
else:
    print("1")

print("Sequence had {count} total steps.".format(count=i))

print("\nProgram ending.")
