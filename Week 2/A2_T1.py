print("Program starting.")
name = input("What is your name: ")
first_float = float(input("Enter a floating point number: "))
second_float = float(input("Enter second floating point number: "))
print("John you gave numbers {first} and {second}".format(
    first=first_float, second=second_float))
print("Multiplying first and second number will result in product {product}".format(
    product=round(first_float * second_float, 2)))
print("Program ending.")
