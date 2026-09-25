print("Program starting.")
print("Insert two integers.")
int_1 = int(input("Insert first integer: "))
int_2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")

if int_1 > int_2:
    print("First integer is greater.\n")
elif int_1 == int_2:
    print("Integers are the same.\n")
else:
    print("Second integer is greater.\n")

print("Adding integers together")
sum = int_1 + int_2
print("{int_1} + {int_2} = {sum}\n".format(int_1=int_1, int_2=int_2, sum=sum))

print("Checking the parity of the sum...")
if sum % 2:
    print("Sum is Odd.")
else:
    print("Sum is even.")

print("Program ending.")
