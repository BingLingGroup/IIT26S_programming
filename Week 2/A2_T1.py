print("Program starting.")
name = input("What is your name: ")
first_float = float(input("Enter a floating point number: "))
second_float = float(input("Enter second floating point number: "))
print("John you gave numbers {first:.2f} and {second:.2f}".format(
    first=first_float, second=second_float))
print("Multiplying first and second number will result in product {product:.2f}".format(
    product=first_float * second_float))
print("Program ending.")
