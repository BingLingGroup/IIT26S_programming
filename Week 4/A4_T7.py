print("Program starting.\n")

print("Check multiplicative persistence.")
value_str = input("Insert an integer: ")
value_int = int(value_str)
count = 0

while len(value_str) > 1:
    value_int = 1
    for c in value_str[:-1]:
        value_int = value_int * int(c)
        print("{c} * ".format(c=c), end="")
    value_int = value_int * int(value_str[-1])
    print("{c} = {result}".format(c=value_str[-1], result=value_int))
    value_str = str(value_int)
    count = count + 1

print("No more steps.\n")
print("This program took {count} step(s)".format(count=count))

print("\nProgram ending.")
